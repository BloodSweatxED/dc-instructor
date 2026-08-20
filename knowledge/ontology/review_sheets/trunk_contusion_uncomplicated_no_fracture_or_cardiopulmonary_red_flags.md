# Trunk contusion without fracture or cardiopulmonary red flags

Phenotype ID: `trunk_contusion_uncomplicated_no_fracture_or_cardiopulmonary_red_flags`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of uncomplicated trunk contusion.
- No fracture concern, cardiopulmonary red flags, abdominal red flags, infection, or high-energy trauma.

## Exclusions

- Fracture or dislocation concern, chest pain, shortness of breath, abdominal pain red flags, high-energy trauma, unstable vital signs, or specialist-directed trauma plan.

## Must-Not-Miss Diagnoses

- Rib or spine fracture.
- Pneumothorax.
- Pulmonary embolism or acute coronary syndrome when chest symptoms are present.
- Intra-abdominal injury.

## Primitive List

- `trunk_contusion_uncomplicated_no_fracture_or_cardiopulmonary_red_flags.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `trunk_contusion_uncomplicated_no_fracture_or_cardiopulmonary_red_flags.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, chest_pain, cardiac_or_pe_chest_pain_concern, respiratory_distress, hypoxia, peritoneal_signs, severe_or_focal_abdominal_pain, high_energy_trauma, unstable_vital_signs, specialist_directed_orthopedic_plan
- `trunk_contusion_uncomplicated_no_fracture_or_cardiopulmonary_red_flags.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `trunk_contusion_uncomplicated_no_fracture_or_cardiopulmonary_red_flags.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `trunk_contusion_uncomplicated_no_fracture_or_cardiopulmonary_red_flags.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `trunk_contusion_uncomplicated_no_fracture_or_cardiopulmonary_red_flags.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, chest_pain, cardiac_or_pe_chest_pain_concern, respiratory_distress, hypoxia, peritoneal_signs, severe_or_focal_abdominal_pain, high_energy_trauma, unstable_vital_signs, specialist_directed_orthopedic_plan
- `trunk_contusion_uncomplicated_no_fracture_or_cardiopulmonary_red_flags.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, chest_pain, cardiac_or_pe_chest_pain_concern, respiratory_distress, hypoxia, peritoneal_signs, severe_or_focal_abdominal_pain, high_energy_trauma, unstable_vital_signs, specialist_directed_orthopedic_plan
- `trunk_contusion_uncomplicated_no_fracture_or_cardiopulmonary_red_flags.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `trunk_contusion_uncomplicated_no_fracture_or_cardiopulmonary_red_flags.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `trunk_contusion_uncomplicated_no_fracture_or_cardiopulmonary_red_flags.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `trunk_contusion_uncomplicated_no_fracture_or_cardiopulmonary_red_flags.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, chest_pain, cardiac_or_pe_chest_pain_concern, respiratory_distress, hypoxia, peritoneal_signs, severe_or_focal_abdominal_pain, high_energy_trauma, unstable_vital_signs, specialist_directed_orthopedic_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit a trunk bruise.

WHAT WE FOUND:
Your clinician diagnosed a trunk bruise. We did not find signs of fracture, dangerous chest or belly injury, infection, or poor blood flow today.

WHAT TO DO AT HOME:
- Rest the sore area as needed.
- Use ice wrapped in a cloth for short periods.
- Take deep breaths normally unless your clinician gave different instructions.

MEDICATIONS:
- Use acetaminophen or ibuprofen only if you can take it safely and follow the label.
- Use medicines only as prescribed or recommended.

RETURN TO ED IF:
- Chest pain, trouble breathing, fainting, coughing blood, or worsening belly pain.
- New numbness, weakness, severe worsening pain, or fever.
- Symptoms that worsen or do not improve as expected.

FOLLOW UP:
Follow up with primary care, urgent care, or the ED if symptoms are not improving or your clinician told you to recheck.
```
