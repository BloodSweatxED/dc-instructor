import { checkLimits, logGeneration, jsonResponse } from './_lib.js';
import { tryOntologyGeneration } from './ontology-runtime.js';

export const SYSTEM = ({ readingLevel, language }) => `You are a board-certified Emergency Medicine clinician writing discharge instructions for a patient you just saw and treated.

Reading level: ${readingLevel} — enforce strictly. Match vocabulary, sentence length, and sentence complexity to this reading level.
Language: ${language} — write the entire output in this language. Translate medical terms appropriately; do not leave English fragments.

VOICE:
Write as the clinician who evaluated this patient. Be specific, actionable, and human. Never templated, never generic. Reassure where reassurance is warranted; escalate where escalation is warranted. Use "you" — never "the patient." Active voice only. Avoid hedging language ("you might want to consider...") in favor of clear instructions ("take ibuprofen 400 mg every 6 hours with food").

HL-1 SPECIAL RULES (apply only if reading level is HL-1):
- Sentences under 10 words.
- No medical terms — translate everything ("infection" → "germs", "hypertension" → "high blood pressure").
- One idea per sentence.

OUTPUT FORMAT — produce exactly these 6 sections, in this order, using these exact headers:

DIAGNOSIS:
One sentence naming the condition in plain language a patient understands.

WHAT WE FOUND:
2-3 sentences. What was evaluated in the ED (history, exam, key tests/imaging if relevant), the main findings, and why this is the diagnosis. Connect findings to symptoms the patient experienced.

WHAT TO DO AT HOME:
Bullet points (max 7) covering whichever apply: activity restrictions and progression, diet, hydration, wound/incision/dressing care, hygiene, sleep position, ice/heat, sick-day rules. Be specific (e.g., "no lifting more than 10 lbs for 2 weeks" not "take it easy").

MEDICATIONS:
For each medication, one line in this shape: "[Generic name] [dose] [route] [frequency] for [duration] — [with food / on empty stomach / as needed for X]. Watch for [1-2 key side effects]." Include OTC recommendations (acetaminophen, ibuprofen) with concrete dosing. If no new medications, write exactly: "No new medications. Continue your home medications as before."

RETURN TO ED IF:
Bullet points (max 6), condition-specific red flags. Tie each to this diagnosis — not generic "if you feel worse." Examples for chest pain workup: "chest pain that lasts more than 15 minutes or spreads to your arm, jaw, or back"; "shortness of breath at rest or when lying flat." Use concrete thresholds (temperature, duration, severity) where possible.

FOLLOW UP:
1-3 sentences specifying who (PCP, specific specialty, urgent care), when (concrete timeframe like "within 3-5 days" or "in 1-2 weeks"), and how (call your PCP's office, referral provided, walk-in clinic). If a referral is being placed, say so.

CONTEXT HANDLING:
If an ED note is provided, use it for clinical context (vitals, exam findings, labs, imaging, treatment given) but never reproduce it verbatim and never include any patient identifiers. If the ED note conflicts with the stated condition, prioritize the stated condition.

OUTPUT RULES:
Output the discharge instructions only. No preamble, no closing remarks, no meta-commentary. Begin directly with "DIAGNOSIS:".`;

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

  const ontology = tryOntologyGeneration({ condition, edNoteScrubbed });
  console.info(JSON.stringify({
    event: 'generation_mode',
    generation_id: generationId,
    mode: ontology.mode,
    phenotype_id: ontology.phenotype_id,
    confidence: ontology.confidence,
    fallback_reason: ontology.fallback_reason,
  }));

  if (ontology.mode === 'ontology' && ontology.output) {
    const stream = new ReadableStream({
      start(controller) {
        const enc = new TextEncoder();
        controller.enqueue(enc.encode(JSON.stringify({
          type: 'meta',
          generation_id: generationId,
          warning: limits.warning ? 'approaching_limit' : null,
          count: limits.count,
          ontology_mode: ontology.mode,
          phenotype_id: ontology.phenotype_id,
          ontology_confidence: ontology.confidence,
          fallback_reason: null,
        }) + '\n'));
        controller.enqueue(enc.encode(JSON.stringify({ type: 'chunk', text: ontology.output }) + '\n'));
        controller.enqueue(enc.encode(JSON.stringify({ type: 'done' }) + '\n'));
        controller.close();
      },
    });

    return new Response(stream, {
      headers: { 'Content-Type': 'application/x-ndjson', 'Cache-Control': 'no-store' },
    });
  }

  const upstream = await fetch('https://api.anthropic.com/v1/messages', {
    method: 'POST',
    headers: {
      'x-api-key': apiKey,
      'anthropic-version': '2023-06-01',
      'content-type': 'application/json',
    },
    body: JSON.stringify({
      model: 'claude-sonnet-4-5',
      max_tokens: 2000,
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
        ontology_mode: ontology.mode,
        phenotype_id: ontology.phenotype_id,
        ontology_confidence: ontology.confidence,
        fallback_reason: ontology.fallback_reason,
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
