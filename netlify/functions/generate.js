import { checkLimits, logGeneration, jsonResponse } from './_lib.js';

export const config = { path: '/api/generate' };

const SYSTEM = ({ readingLevel, language }) => `You are a clinical discharge instruction writer for Emergency Medicine.

Reading level: ${readingLevel} — enforce strictly.
Language: ${language} — write entirely in this language.

HL-1 rules: sentences under 10 words, no medical terms, use "you" not "the patient", active voice only.

Format exactly:
WHAT HAPPENED: (1-2 sentences)
WHAT TO DO AT HOME: (bullet points, max 6)
MEDICATIONS: (if relevant)
RETURN TO ED IF: (bullet points, max 5 — return precautions)
FOLLOW UP: (1-2 sentences)

If an ED note is provided as context, use it for clinical context but do not reproduce it. Do not include any patient identifiers from the note. Output instructions only. No preamble.`;

export default async (req) => {
  if (req.method !== 'POST') return jsonResponse(405, { error: 'Method not allowed' });

  const limits = await checkLimits();
  if (limits.blocked) return jsonResponse(429, { error: 'limit', reason: limits.reason });

  const apiKey = process.env.ANTHROPIC_API_KEY;
  if (!apiKey) return jsonResponse(500, { error: 'Server not configured' });

  let body;
  try { body = await req.json(); } catch { return jsonResponse(400, { error: 'Invalid JSON' }); }
  const { condition, edNoteScrubbed, readingLevel = '6th Grade', language = 'English', hasImage = false } = body || {};
  if (!condition || typeof condition !== 'string') {
    return jsonResponse(400, { error: 'condition required' });
  }

  const userMessage = edNoteScrubbed
    ? `CONDITION: ${condition}\n\nED NOTE CONTEXT (PHI redacted):\n${edNoteScrubbed}`
    : `CONDITION: ${condition}`;

  const generationId = await logGeneration({
    reading_level: readingLevel,
    language,
    condition_input: condition,
    has_image_request: hasImage,
  });

  const upstream = await fetch('https://api.anthropic.com/v1/messages', {
    method: 'POST',
    headers: {
      'x-api-key': apiKey,
      'anthropic-version': '2023-06-01',
      'content-type': 'application/json',
    },
    body: JSON.stringify({
      model: 'claude-sonnet-4-5',
      max_tokens: 1500,
      stream: true,
      system: SYSTEM({ readingLevel, language }),
      messages: [{ role: 'user', content: userMessage }],
    }),
  });

  if (!upstream.ok || !upstream.body) {
    const errText = await upstream.text().catch(() => '');
    return jsonResponse(502, { error: 'upstream', detail: errText.slice(0, 500) });
  }

  const stream = new ReadableStream({
    async start(controller) {
      const enc = new TextEncoder();
      controller.enqueue(enc.encode(JSON.stringify({
        type: 'meta',
        generation_id: generationId,
        warning: limits.warning ? 'approaching_limit' : null,
        count: limits.count,
      }) + '\n'));

      const reader = upstream.body.getReader();
      const dec = new TextDecoder();
      let buf = '';
      while (true) {
        const { value, done } = await reader.read();
        if (done) break;
        buf += dec.decode(value, { stream: true });
        const lines = buf.split('\n');
        buf = lines.pop() || '';
        for (const line of lines) {
          if (!line.startsWith('data:')) continue;
          const data = line.slice(5).trim();
          if (!data || data === '[DONE]') continue;
          try {
            const evt = JSON.parse(data);
            if (evt.type === 'content_block_delta' && evt.delta?.type === 'text_delta') {
              controller.enqueue(enc.encode(JSON.stringify({ type: 'chunk', text: evt.delta.text }) + '\n'));
            }
          } catch {}
        }
      }
      controller.enqueue(enc.encode(JSON.stringify({ type: 'done' }) + '\n'));
      controller.close();
    },
  });

  return new Response(stream, {
    headers: { 'Content-Type': 'application/x-ndjson', 'Cache-Control': 'no-store' },
  });
};
