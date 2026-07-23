# Uncomplicated common cold without pneumonia or breathing red flags

Phenotype ID: `common_cold_uncomplicated_no_pneumonia_or_breathing_red_flags`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of uncomplicated common cold.
- No pneumonia, hypoxia, asthma/COPD exacerbation, severe dehydration, pregnancy/pediatric pathway, or specialist-directed plan.

## Exclusions

- Pneumonia, hypoxia, shortness of breath at rest, chest pain, asthma/COPD exacerbation, severe dehydration, immunocompromised host, pregnancy/pediatric pathway, or specialist-directed plan.

## Must-Not-Miss Diagnoses

- Pneumonia.
- Hypoxia.
- Asthma/COPD exacerbation.
- Severe dehydration.

## Primitive List

- `common_cold_uncomplicated_no_pneumonia_or_breathing_red_flags.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `common_cold_uncomplicated_no_pneumonia_or_breathing_red_flags.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: pneumonia, hypoxia, chest_pain, poor_inhaler_access, severe_dehydration, focal_lung_findings_or_infiltrate, immunocompromised, pregnancy, pediatric_pathway
- `common_cold_uncomplicated_no_pneumonia_or_breathing_red_flags.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `common_cold_uncomplicated_no_pneumonia_or_breathing_red_flags.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `common_cold_uncomplicated_no_pneumonia_or_breathing_red_flags.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `common_cold_uncomplicated_no_pneumonia_or_breathing_red_flags.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: pneumonia, hypoxia, chest_pain, poor_inhaler_access, severe_dehydration, focal_lung_findings_or_infiltrate, immunocompromised, pregnancy, pediatric_pathway
- `common_cold_uncomplicated_no_pneumonia_or_breathing_red_flags.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: pneumonia, hypoxia, chest_pain, poor_inhaler_access, severe_dehydration, focal_lung_findings_or_infiltrate, immunocompromised, pregnancy, pediatric_pathway
- `common_cold_uncomplicated_no_pneumonia_or_breathing_red_flags.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `common_cold_uncomplicated_no_pneumonia_or_breathing_red_flags.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `common_cold_uncomplicated_no_pneumonia_or_breathing_red_flags.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `common_cold_uncomplicated_no_pneumonia_or_breathing_red_flags.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: pneumonia, hypoxia, chest_pain, poor_inhaler_access, severe_dehydration, focal_lung_findings_or_infiltrate, immunocompromised, pregnancy, pediatric_pathway

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit an uncomplicated common cold.

WHAT WE FOUND:
Your clinician diagnosed a common cold and did not find pneumonia, breathing distress, or another emergency problem today.

WHAT TO DO AT HOME:
- Rest and drink fluids as tolerated.
- Use humidified air, saline spray, honey if safe for you, or other comfort measures if helpful.
- Wash your hands and avoid close contact while symptoms are contagious.

MEDICATIONS:
- Antibiotics are not needed for an uncomplicated common cold.
- Use over-the-counter medicines only if safe for you and follow the label.

RETURN TO ED IF:
- Trouble breathing, chest pain, blue lips, confusion, fainting, or worsening shortness of breath.
- Fever that is high or persistent, dehydration, or symptoms that get much worse after starting to improve.
- Concern for pneumonia, asthma/COPD flare, or symptoms not improving as expected.

FOLLOW UP:
Follow up with primary care, urgent care, or the ED if symptoms are not improving or your clinician told you to recheck.
```
