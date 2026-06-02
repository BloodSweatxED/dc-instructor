# Community-acquired pneumonia, outpatient

Phenotype ID: `community_acquired_pneumonia_outpatient`

Status: `draft`

## Inclusion Criteria

- Pneumonia judged stable for outpatient treatment.
- No hypoxia, sepsis, or admission need at discharge.

## Exclusions

- Hypoxia.
- Sepsis.
- Immunocompromised host.
- High-risk comorbidity or unreliable outpatient plan.

## Must-Not-Miss Diagnoses

- Sepsis.
- Pulmonary embolism mimic.
- Heart failure mimic.
- Empyema.
- Hypoxic respiratory failure.

## Primitive List

- `community_acquired_pneumonia_outpatient.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_needed, clinician_judgment_only | unsafe modifiers: none
- `community_acquired_pneumonia_outpatient.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_needed, clinician_judgment_only, unsafe_without_modifier | unsafe modifiers: hypoxia, immunocompromised, elderly_frail, sepsis, poor_follow_up
- `community_acquired_pneumonia_outpatient.home_care.home_care_1.v1` | `home_care` | audit: source_needed | unsafe modifiers: none
- `community_acquired_pneumonia_outpatient.home_care.home_care_2.v1` | `home_care` | audit: source_needed | unsafe modifiers: none
- `community_acquired_pneumonia_outpatient.home_care.home_care_3.v1` | `home_care` | audit: source_needed | unsafe modifiers: none
- `community_acquired_pneumonia_outpatient.home_care.home_care_4.v1` | `home_care` | audit: source_needed | unsafe modifiers: none
- `community_acquired_pneumonia_outpatient.medications.medication_guidance_1.v1` | `medications` | audit: source_needed, clinician_judgment_only, unsafe_without_modifier | unsafe modifiers: hypoxia, immunocompromised, elderly_frail, sepsis, poor_follow_up
- `community_acquired_pneumonia_outpatient.medications.medication_guidance_2.v1` | `medications` | audit: source_needed, clinician_judgment_only, unsafe_without_modifier | unsafe modifiers: hypoxia, immunocompromised, elderly_frail, sepsis, poor_follow_up
- `community_acquired_pneumonia_outpatient.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_needed, clinician_judgment_only | unsafe modifiers: none
- `community_acquired_pneumonia_outpatient.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_needed, clinician_judgment_only | unsafe modifiers: none
- `community_acquired_pneumonia_outpatient.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_needed, clinician_judgment_only | unsafe modifiers: none
- `community_acquired_pneumonia_outpatient.follow_up.default_follow_up.v1` | `follow_up` | audit: source_needed, clinician_judgment_only, unsafe_without_modifier | unsafe modifiers: hypoxia, immunocompromised, elderly_frail, sepsis, poor_follow_up

## Assembled Six-Section Output

```text
DIAGNOSIS:
You were treated for pneumonia.

WHAT WE FOUND:
Your ED evaluation found a lung infection that was safe to treat at home today. Your oxygen level and overall condition were reassuring enough for discharge.

WHAT TO DO AT HOME:
- Rest and increase activity slowly.
- Drink fluids if you are allowed.
- Use warm liquids or steam if they help cough or mucus.
- Avoid smoking and smoke exposure.

MEDICATIONS:
- Take antibiotics exactly as prescribed.
- Use fever or pain medicine only if you can take it safely and follow the label.

RETURN TO ED IF:
- Worse trouble breathing, blue lips, confusion, fainting, or chest pain.
- Fever or symptoms worsen after starting treatment.
- You cannot keep medicines or fluids down.

FOLLOW UP:
Follow up with primary care as instructed.
```
