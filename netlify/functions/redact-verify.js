import { jsonResponse, originAllowed } from './_lib.js';

const SYSTEM = `You are a HIPAA Safe Harbor verifier. The user provides text that has been pre-scrubbed of obvious identifiers (replaced with bracketed tokens like [NAME], [MRN], [DATE]). Your job: find any REMAINING PHI that the regex pass missed — particularly contextual identifiers such as:

- Specific employer names ("firefighter at Engine 14")
- Public roles tied to small geographies ("mayor of Smithtown")
- Unique medical history that could re-identify (extremely rare conditions, public injury events)
- Specific landmarks, schools, units, neighborhoods
- Relationship-based identifiers ("husband of Senator X")
- Geographic subdivisions smaller than state, except per Safe Harbor allowance for large zip codes

Return ONLY valid JSON of the form:
{"additionalRedactions":[{"text":"<exact substring>","type":"<EMPLOYER|ROLE|GEO|RELATION|RARE|OTHER>"}]}

If nothing remains to redact, return {"additionalRedactions":[]}. No prose, no preamble, JSON only.`;

export default async (req) => {
  if (req.method !== 'POST') return jsonResponse(405, { error: 'Method not allowed' });
  if (!originAllowed(req)) return jsonResponse(403, { error: 'Forbidden' });
  const apiKey = process.env.ANTHROPIC_API_KEY;
  if (!apiKey) return jsonResponse(500, { error: 'Server not configured' });

  let body;
  try { body = await req.json(); } catch { return jsonResponse(400, { error: 'Invalid JSON' }); }
  const text = (body?.text || '').toString().slice(0, 8000);
  if (!text.trim()) return jsonResponse(200, { scrubbed: '', additionalRedactions: [] });

  const r = await fetch('https://api.anthropic.com/v1/messages', {
    method: 'POST',
    headers: {
      'x-api-key': apiKey,
      'anthropic-version': '2023-06-01',
      'content-type': 'application/json',
    },
    body: JSON.stringify({
      model: 'claude-haiku-4-5-20251001',
      max_tokens: 600,
      system: SYSTEM,
      messages: [{ role: 'user', content: text }],
    }),
  });

  if (!r.ok) {
    return jsonResponse(200, { scrubbed: text, additionalRedactions: [], degraded: true });
  }

  const data = await r.json();
  const raw = data?.content?.[0]?.text || '{"additionalRedactions":[]}';
  let parsed = { additionalRedactions: [] };
  try {
    const match = raw.match(/\{[\s\S]*\}/);
    parsed = JSON.parse(match ? match[0] : raw);
  } catch {}

  let scrubbed = text;
  const applied = [];
  for (const item of parsed.additionalRedactions || []) {
    if (!item?.text || typeof item.text !== 'string') continue;
    const token = `[${(item.type || 'OTHER').toUpperCase()}]`;
    if (scrubbed.includes(item.text)) {
      scrubbed = scrubbed.split(item.text).join(token);
      applied.push({ type: item.type || 'OTHER', original: item.text });
    }
  }

  return jsonResponse(200, { scrubbed, additionalRedactions: applied });
};
