import { describe, it, expect } from 'vitest';
import { redactPHI, summarizeRedactions } from './phiRedact.js';

const types = (r) => r.redactions.map((x) => x.type);

describe('redactPHI — Safe Harbor identifiers', () => {
  it('returns empty result for empty input', () => {
    expect(redactPHI('')).toEqual({ scrubbed: '', redactions: [] });
    expect(redactPHI(null)).toEqual({ scrubbed: '', redactions: [] });
  });

  it('redacts SSN', () => {
    const r = redactPHI('SSN 123-45-6789 on file');
    expect(r.scrubbed).toBe('SSN [SSN] on file');
    expect(types(r)).toContain('SSN');
  });

  it('redacts phone numbers in common formats', () => {
    for (const phone of ['555-867-5309', '(555) 867-5309', '+1 555.867.5309']) {
      const r = redactPHI(`call ${phone} please`);
      expect(r.scrubbed).toContain('[PHONE]');
      expect(r.scrubbed).not.toContain('867');
    }
  });

  it('redacts email and URL', () => {
    const r = redactPHI('contact jdoe@example.com or https://example.com/chart');
    expect(r.scrubbed).toContain('[EMAIL]');
    expect(r.scrubbed).toContain('[URL]');
  });

  it('redacts MRN with label', () => {
    const r = redactPHI('MRN: A12345678 presented today');
    expect(r.scrubbed).toContain('[MRN]');
    expect(r.scrubbed).not.toContain('A12345678');
  });

  it('redacts dates (slash, written, ISO)', () => {
    const r = redactPHI('Seen 06/02/2026, follow-up June 15, 2026, op date 2026-05-13');
    expect(r.scrubbed).not.toMatch(/2026/);
  });

  it('redacts age over 89 but keeps younger ages', () => {
    const over = redactPHI('92 yo male');
    expect(over.scrubbed).toContain('[AGE>89]');
    const under = redactPHI('45 yo male');
    expect(under.scrubbed).toContain('45 yo');
  });

  it('redacts street addresses and zip codes', () => {
    const r = redactPHI('Lives at 123 Maple Street, Springfield 02134');
    expect(r.scrubbed).toContain('[ADDR]');
    expect(r.scrubbed).toContain('[ZIP]');
  });

  it('redacts capitalized name bigrams', () => {
    const r = redactPHI('Pt is John Smith, seen with wife');
    expect(r.scrubbed).toContain('[NAME]');
    expect(r.scrubbed).not.toContain('John Smith');
  });
});

describe('redactPHI — clinical text preserved', () => {
  it('keeps whitelisted clinical bigrams', () => {
    const text =
      'Chief Complaint: Chest Pain. Physical Exam: Vital Signs stable. ' +
      'Urgent Care follow up. Physical Therapy referral. Normal Sinus rhythm.';
    const r = redactPHI(text);
    expect(r.scrubbed).toBe(text);
    expect(r.redactions).toEqual([]);
  });

  it('keeps single-word allowlisted terms in bigrams', () => {
    const r = redactPHI('Discharge Plan reviewed with Patient Family');
    expect(r.scrubbed).toContain('Discharge Plan');
    expect(r.scrubbed).toContain('Patient Family');
  });

  it('keeps vitals and dosing numbers', () => {
    const text = 'BP 142/88, HR 96, ibuprofen 400 mg q6h, Tmax 38.2';
    const r = redactPHI(text);
    expect(r.scrubbed).toBe(text);
  });
});

describe('summarizeRedactions', () => {
  it('counts by type', () => {
    const summary = summarizeRedactions([
      { type: 'NAME', original: 'a' },
      { type: 'NAME', original: 'b' },
      { type: 'SSN', original: 'c' },
    ]);
    expect(summary).toContainEqual({ type: 'NAME', count: 2 });
    expect(summary).toContainEqual({ type: 'SSN', count: 1 });
  });
});
