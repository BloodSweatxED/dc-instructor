# Phase 31 Acute Bronchitis Draft

Phase 31 creates `acute_bronchitis_no_pneumonia` as a narrow draft phenotype only.

Runtime may recognize the phenotype for review stress testing, but must fall back because it is not clinician-reviewed. This is intentional. Do not promote it until the primitive packet has been reviewed.

## Boundary

Include only adults with cough or chest cold symptoms when the clinician diagnosis or discharge impression is acute bronchitis, chest cold, or viral bronchitis, and the ED note supports no pneumonia concern, acceptable oxygenation, comfortable work of breathing, and safe discharge.

Block pneumonia diagnosis or infiltrate, focal lung findings, hypoxia, respiratory distress, COPD or asthma exacerbation pathway, immunocompromise, frail elderly status, hemoptysis, cardiac or pulmonary embolism chest-pain concern, sepsis, unstable vital signs, and antibiotics prescribed for suspected bacterial infection.

## Runtime Expectations

- Clean acute bronchitis matches `acute_bronchitis_no_pneumonia` but falls back with `phenotype_not_clinician_reviewed`.
- Pneumonia or infiltrate blocks.
- Hypoxia blocks.
- Respiratory distress blocks.
- COPD or asthma overlap blocks.
- Antibiotics for suspected bacterial infection blocks.
- Vague cough does not match.

## Guardrails

- Do not promote acute bronchitis yet.
- Do not add broad `cough` as a standalone term.
- Do not infer antibiotic instructions.
- Do not use acute bronchitis as a catch-all respiratory fallback.
- Do not assert lungs are clear unless clinician documentation supports it.
- Do not promise an exact symptom duration.
