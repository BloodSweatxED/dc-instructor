# Dental pain without deep-space infection

Phenotype ID: `dental_pain_no_deep_space_infection`

Status: `reviewed`

## Inclusion Criteria

- Dental pain or localized dental infection without airway, deep-space, or sepsis concern.

## Exclusions

- Ludwig angina concern.
- Deep-space infection.
- Airway symptoms.
- Immunocompromised host.

## Must-Not-Miss Diagnoses

- Deep-space neck infection.
- Ludwig angina.
- Airway compromise.
- Sepsis.

## Primitive List

- `dental_pain_no_deep_space_infection.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only | unsafe modifiers: none
- `dental_pain_no_deep_space_infection.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier | unsafe modifiers: airway_symptoms, deep_space_swelling, immunocompromised, trismus
- `dental_pain_no_deep_space_infection.home_care.home_care_1.v1` | `home_care` | audit: source_supported | unsafe modifiers: none
- `dental_pain_no_deep_space_infection.home_care.home_care_2.v1` | `home_care` | audit: source_supported | unsafe modifiers: none
- `dental_pain_no_deep_space_infection.home_care.home_care_3.v1` | `home_care` | audit: source_supported | unsafe modifiers: none
- `dental_pain_no_deep_space_infection.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier | unsafe modifiers: airway_symptoms, deep_space_swelling, immunocompromised, trismus
- `dental_pain_no_deep_space_infection.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier | unsafe modifiers: airway_symptoms, deep_space_swelling, immunocompromised, trismus
- `dental_pain_no_deep_space_infection.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only | unsafe modifiers: none
- `dental_pain_no_deep_space_infection.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only | unsafe modifiers: none
- `dental_pain_no_deep_space_infection.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only | unsafe modifiers: none
- `dental_pain_no_deep_space_infection.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier | unsafe modifiers: airway_symptoms, deep_space_swelling, immunocompromised, trismus

## Assembled Six-Section Output

```text
DIAGNOSIS:
You were treated for dental pain today.

WHAT WE FOUND:
Your exam did not show signs of a dangerous deep infection in the face, jaw, or neck today.

WHAT TO DO AT HOME:
- Keep the mouth clean with gentle brushing.
- Avoid chewing on the painful side.
- A dentist must treat the tooth problem for it to fully resolve.

MEDICATIONS:
- Take antibiotics only if they were prescribed.
- Use acetaminophen or ibuprofen only if you can take it safely and follow the label.

RETURN TO ED IF:
- Face or neck swelling, fever, trouble swallowing, drooling, voice change, or trouble breathing.
- You cannot open your mouth normally.
- Pain or swelling spreads quickly.

FOLLOW UP:
See a dentist as soon as possible.
```
