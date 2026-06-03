# Phase 29 Candidate Ranking

Status: complete.

Phase 29 ranks the next phenotype candidates after the expansion gate reopened.

Recommendation: build `acute_bronchitis_no_pneumonia` next.

Why this candidate:

- Common ED discharge problem.
- Clear source support from CDC and MedlinePlus.
- Strong antibiotic-stewardship value.
- Safer static boundary than low-risk syncope, chest pain, palpitations, biliary colic, or hyperglycemia.
- Existing harvest has all six discharge sections represented.
- Main risks are visible and controllable: pneumonia miss, hypoxia, COPD/asthma overlap, immunocompromise, medication dosing, and overconfident "no pneumonia" wording.

Candidates considered:

| Candidate | Recommendation | Reason |
| --- | --- | --- |
| `acute_bronchitis_no_pneumonia` | first | Best mix of frequency, source support, and runtime boundary clarity. |
| `acute_sinusitis_supportive_care` | second | Useful, but antibiotic boundary and symptom-duration claims need tighter source work. |
| `conjunctivitis_uncomplicated` | later | Common, but contact lens, HSV, trauma, and vision-change blockers need careful source work. |
| `urticaria_no_anaphylaxis` | later | Source overlap exists, but it may duplicate allergic reaction content unless boundaries are rebuilt. |
| `migraine_improved_discharge` | later | Good ED fit, but neurologic red-flag boundary needs a stronger packet. |
| `syncope_low_risk_discharge` | defer | Too dependent on ECG, risk stratification, comorbidities, and local follow-up for static early expansion. |
| `chest_pain_low_risk_negative_ed_workup` | defer | Already retired as static ontology content. Do not reopen until a narrower reviewed phenotype is designed. |

Decision:

Proceed to a source-first planning packet for `acute_bronchitis_no_pneumonia`. Do not promote or generate patient-facing ontology text yet.
