# Simple canker sore without systemic symptoms

Phenotype ID: `aphthous_ulcer_simple_no_systemic_symptoms`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of simple canker sore or aphthous ulcer.
- No fever, rash, ocular symptoms, genital ulcers, immunocompromised-host pathway, deep-space infection, or airway concern.

## Exclusions

- Fever, rash, diarrhea, headache with systemic syndrome, ocular symptoms, genital ulcers, or recurrent severe ulcers.
- Deep-space dental/neck infection, airway symptoms, dehydration, or immunocompromised host.
- Suspicion for herpes, zoster, Stevens-Johnson syndrome, or malignancy.

## Must-Not-Miss Diagnoses

- Deep-space oral infection.
- Herpes or zoster pathway.
- Stevens-Johnson syndrome.
- Oral malignancy.
- Behcet-like systemic disease.

## Primitive List

- `aphthous_ulcer_simple_no_systemic_symptoms.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `aphthous_ulcer_simple_no_systemic_symptoms.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: airway_symptoms, deep_space_swelling, dehydration_or_unable_to_drink, systemic_or_recurrent_oral_ulcer_features, genital_ulcers, ocular_symptoms, mucosal_lesions, immunocompromised
- `aphthous_ulcer_simple_no_systemic_symptoms.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `aphthous_ulcer_simple_no_systemic_symptoms.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `aphthous_ulcer_simple_no_systemic_symptoms.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `aphthous_ulcer_simple_no_systemic_symptoms.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: airway_symptoms, deep_space_swelling, dehydration_or_unable_to_drink, systemic_or_recurrent_oral_ulcer_features, genital_ulcers, ocular_symptoms, mucosal_lesions, immunocompromised
- `aphthous_ulcer_simple_no_systemic_symptoms.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: airway_symptoms, deep_space_swelling, dehydration_or_unable_to_drink, systemic_or_recurrent_oral_ulcer_features, genital_ulcers, ocular_symptoms, mucosal_lesions, immunocompromised
- `aphthous_ulcer_simple_no_systemic_symptoms.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `aphthous_ulcer_simple_no_systemic_symptoms.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `aphthous_ulcer_simple_no_systemic_symptoms.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `aphthous_ulcer_simple_no_systemic_symptoms.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: airway_symptoms, deep_space_swelling, dehydration_or_unable_to_drink, systemic_or_recurrent_oral_ulcer_features, genital_ulcers, ocular_symptoms, mucosal_lesions, immunocompromised

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit a canker sore, also called an aphthous ulcer.

WHAT WE FOUND:
Your exam was reassuring for a simple mouth sore. We did not find signs of a dangerous mouth or throat infection today.

WHAT TO DO AT HOME:
- Avoid spicy, acidic, or sharp foods if they make the sore hurt more.
- Brush gently and keep up with routine mouth care.
- Drink fluids so mouth pain does not lead to dehydration.

MEDICATIONS:
- Use over-the-counter mouth pain medicine only as directed on the label or by your clinician.
- Use acetaminophen or ibuprofen only if you can take it safely and follow the label.

RETURN TO ED IF:
- Fever, rash, eye pain, genital sores, severe swelling, or trouble swallowing.
- You cannot drink enough fluids.
- The sore lasts more than 2 weeks, gets worse, or keeps coming back.

FOLLOW UP:
Follow up with primary care, dentistry, or ENT if the sore is not improving, lasts more than 2 weeks, or recurs often.
```
