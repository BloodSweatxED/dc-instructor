# Low-risk chest pain after negative ED workup

Phenotype ID: `chest_pain_low_risk_negative_ed_workup`

Status: `retired`

## Inclusion Criteria

- Chest pain evaluated in ED and judged low risk for discharge.
- No active ischemia, unstable vital signs, or admission need.

## Exclusions

- Abnormal ECG or troponin requiring admission.
- Ongoing concerning pain.
- Pulmonary embolism, aortic emergency, myocarditis, or pericarditis concern.

## Must-Not-Miss Diagnoses

- Acute coronary syndrome.
- Pulmonary embolism.
- Aortic dissection.
- Pneumothorax.
- Myocarditis.

## Primitive List

- `chest_pain_low_risk_negative_ed_workup.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `chest_pain_low_risk_negative_ed_workup.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: abnormal_troponin, abnormal_ecg, ongoing_pain, syncope, known_cad_high_risk
- `chest_pain_low_risk_negative_ed_workup.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `chest_pain_low_risk_negative_ed_workup.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `chest_pain_low_risk_negative_ed_workup.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `chest_pain_low_risk_negative_ed_workup.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: abnormal_troponin, abnormal_ecg, ongoing_pain, syncope, known_cad_high_risk
- `chest_pain_low_risk_negative_ed_workup.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: abnormal_troponin, abnormal_ecg, ongoing_pain, syncope, known_cad_high_risk
- `chest_pain_low_risk_negative_ed_workup.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `chest_pain_low_risk_negative_ed_workup.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `chest_pain_low_risk_negative_ed_workup.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `chest_pain_low_risk_negative_ed_workup.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: abnormal_troponin, abnormal_ecg, ongoing_pain, syncope, known_cad_high_risk

## Assembled Six-Section Output

```text
DIAGNOSIS:
You were evaluated for chest pain today.

WHAT WE FOUND:
Your ED workup was reassuring today. No emergency cause was found, but chest pain can change after you leave.

WHAT TO DO AT HOME:
- Rest today.
- Avoid heavy activity until you know how you feel and follow your clinician's instructions.
- Keep track of symptoms if they return.

MEDICATIONS:
- Continue your home medicines unless your clinician told you to stop.
- Take any new medicine exactly as prescribed.

RETURN TO ED IF:
- Chest pain that returns, gets worse, or spreads to the arm, jaw, back, or neck.
- Shortness of breath, sweating, fainting, new weakness, or coughing blood.
- Fast or irregular heartbeat with dizziness or chest pain.

FOLLOW UP:
Follow up with primary care or cardiology as instructed.
```
