// HIPAA Safe Harbor (45 CFR 164.514(b)) — client-side first-pass redactor.
// Returns { scrubbed, redactions }. Original strings stay client-side only.

const COMMON_MEDICAL_BIGRAM_WHITELIST = new Set([
  'Chief Complaint', 'Past Medical', 'Family History', 'Social History',
  'Review Systems', 'Physical Exam', 'Vital Signs', 'Chest Pain', 'Abdominal Pain',
  'Shortness Breath', 'Right Lower', 'Left Lower', 'Right Upper', 'Left Upper',
  'Emergency Department', 'Discharge Instructions', 'Return Precautions',
  'Mental Status', 'Heart Rate', 'Blood Pressure', 'Body Mass',
]);

const PATTERNS = [
  { type: 'SSN', re: /\b\d{3}-\d{2}-\d{4}\b/g },
  { type: 'PHONE', re: /\b(?:\+?1[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b/g },
  { type: 'EMAIL', re: /\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b/g },
  { type: 'URL', re: /\bhttps?:\/\/\S+/g },
  { type: 'DOB', re: /\b(?:DOB|D\.O\.B\.?|born)[\s:]*\d{1,2}[\/-]\d{1,2}[\/-]\d{2,4}\b/gi },
  { type: 'DATE', re: /\b\d{1,2}[\/-]\d{1,2}[\/-]\d{2,4}\b/g },
  { type: 'DATE', re: /\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)[a-z]*\s+\d{1,2},?\s+\d{4}\b/gi },
  { type: 'DATE_ISO', re: /\b\d{4}-\d{2}-\d{2}\b/g },
  { type: 'MRN', re: /\b(?:MRN|MR#|Med\s*Rec(?:ord)?#?|Patient\s*ID|Acct#?)[\s:#]*([A-Z0-9-]{5,15})\b/gi },
  { type: 'AGE>89', re: /\b(9[0-9]|1[0-9]{2})\s*(?:yo|y\/o|year[-\s]?old|years?\s*old)\b/gi },
  { type: 'ADDR', re: /\b\d{1,6}\s+[A-Z][A-Za-z]+(?:\s+[A-Z][A-Za-z]+){0,3}\s+(?:St|Street|Ave|Avenue|Rd|Road|Blvd|Boulevard|Ln|Lane|Dr|Drive|Ct|Court|Pl|Place|Way|Pkwy|Parkway)\.?\b/g },
  { type: 'ZIP', re: /\b\d{5}(?:-\d{4})?\b/g },
];

const NAME_BIGRAM = /\b([A-Z][a-z]{1,15})\s+([A-Z][a-z]{1,15})\b/g;

export function redactPHI(input) {
  if (!input) return { scrubbed: '', redactions: [] };
  let text = input;
  const redactions = [];

  // Apply pattern-based redaction
  for (const { type, re } of PATTERNS) {
    text = text.replace(re, (match) => {
      redactions.push({ type, original: match });
      return `[${type}]`;
    });
  }

  // Heuristic: capitalized name bigrams not on the medical whitelist
  text = text.replace(NAME_BIGRAM, (match, a, b) => {
    if (COMMON_MEDICAL_BIGRAM_WHITELIST.has(`${a} ${b}`)) return match;
    // Skip if both words are very common medical terms (single-word allowlist subset)
    const allowSingles = ['Patient', 'Doctor', 'Nurse', 'Admit', 'Discharge', 'Emergency', 'Hospital'];
    if (allowSingles.includes(a) || allowSingles.includes(b)) return match;
    redactions.push({ type: 'NAME', original: match });
    return '[NAME]';
  });

  return { scrubbed: text, redactions };
}

export function summarizeRedactions(redactions) {
  const counts = {};
  for (const r of redactions) counts[r.type] = (counts[r.type] || 0) + 1;
  return Object.entries(counts).map(([type, n]) => ({ type, count: n }));
}
