# Phase 33 Acute Bronchitis Clinician Review

Target phenotype: `acute_bronchitis_no_pneumonia`.

Decision: approve for narrow reviewed runtime use after Phase 32 stress coverage passes.

Clinical boundary:

- Adult with clinician diagnosis or discharge impression of acute bronchitis, chest cold, or viral bronchitis.
- No pneumonia diagnosis or unresolved focal pneumonia concern.
- Oxygenation and work of breathing acceptable for discharge.
- No unstable vital signs, sepsis concern, or admission need.
- Not a COPD or asthma exacerbation pathway.
- No antibiotics prescribed for suspected bacterial infection.

Review answers:

- Keep the diagnosis line.
- Keep the `no pneumonia concern` line only because the runtime boundary requires clinician documentation that pneumonia concern was addressed.
- Keep antibiotic stewardship language, but do not give medication names, doses, schedules, or durations.
- Keep follow-up generic and clinician-instruction based.
- Do not promise exact symptom duration.
- Do not add broad `cough` as a runtime term.
- Do not use this as a fallback for unmatched respiratory complaints.

Promotion requirement: runtime cases from Phase 20, Phase 31, and Phase 32 must pass before promotion.
