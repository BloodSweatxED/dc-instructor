# Seborrheic dermatitis or dandruff without secondary infection

Phenotype ID: `seborrheic_dermatitis_or_dandruff_no_secondary_infection`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of seborrheic dermatitis or dandruff.
- No secondary bacterial infection, eye involvement, severe diffuse rash, or immunocompromised-host pathway.

## Exclusions

- Cellulitis or secondary infection concern.
- Rash near the eye or mucosal involvement.
- Severe diffuse rash, skin peeling, systemic illness, or immunocompromised host requiring a separate pathway.

## Must-Not-Miss Diagnoses

- Cellulitis.
- Severe cutaneous adverse reaction.
- Psoriasis flare requiring a different pathway.
- Immunocompromised-host infection.

## Primitive List

- `seborrheic_dermatitis_or_dandruff_no_secondary_infection.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `seborrheic_dermatitis_or_dandruff_no_secondary_infection.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: secondary_skin_infection_concern, near_eye_or_genitals, mucosal_lesions, skin_peeling_or_sloughing, immunocompromised, systemic_illness
- `seborrheic_dermatitis_or_dandruff_no_secondary_infection.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `seborrheic_dermatitis_or_dandruff_no_secondary_infection.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `seborrheic_dermatitis_or_dandruff_no_secondary_infection.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `seborrheic_dermatitis_or_dandruff_no_secondary_infection.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: secondary_skin_infection_concern, near_eye_or_genitals, mucosal_lesions, skin_peeling_or_sloughing, immunocompromised, systemic_illness
- `seborrheic_dermatitis_or_dandruff_no_secondary_infection.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: secondary_skin_infection_concern, near_eye_or_genitals, mucosal_lesions, skin_peeling_or_sloughing, immunocompromised, systemic_illness
- `seborrheic_dermatitis_or_dandruff_no_secondary_infection.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `seborrheic_dermatitis_or_dandruff_no_secondary_infection.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `seborrheic_dermatitis_or_dandruff_no_secondary_infection.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `seborrheic_dermatitis_or_dandruff_no_secondary_infection.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: secondary_skin_infection_concern, near_eye_or_genitals, mucosal_lesions, skin_peeling_or_sloughing, immunocompromised, systemic_illness

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit seborrheic dermatitis or dandruff.

WHAT WE FOUND:
Your exam was reassuring for this common flaky skin condition. We did not find signs of a deeper infection or emergency skin problem today.

WHAT TO DO AT HOME:
- Use the shampoo, cream, or skin-care plan your clinician recommended.
- Avoid scratching or picking at irritated areas.
- Keep the area clean and avoid harsh products that make burning or itching worse.

MEDICATIONS:
- Use over-the-counter dandruff shampoo or medicated shampoo only as directed on the label or by your clinician.
- Use acetaminophen or ibuprofen only if you can take it safely and follow the label.

RETURN TO ED IF:
- Spreading redness, warmth, pus, fever, or severe pain.
- Rash near the eye, rapidly worsening swelling, or skin peeling.
- Symptoms become much worse despite the plan you were given.

FOLLOW UP:
Follow up with primary care or dermatology if symptoms are not improving with the plan you were given.
```
