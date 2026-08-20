# Dry cracked hands without infection or systemic skin disease

Phenotype ID: `dry_cracked_hands_no_infection_or_systemic_skin_disease`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of dry cracked hands or hand xerosis.
- No secondary infection, deep wound, severe cutaneous adverse reaction, immunocompromised host, or specialist-directed dermatology plan.

## Exclusions

- Secondary infection, open deep wound, severe cutaneous adverse reaction, mucosal lesions, systemic illness, immunocompromised host, diabetes with hand wound concern, or specialist-directed dermatology plan.

## Must-Not-Miss Diagnoses

- Cellulitis.
- Deep hand infection.
- Severe cutaneous adverse reaction.
- Systemic skin disease.

## Primitive List

- `dry_cracked_hands_no_infection_or_systemic_skin_disease.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `dry_cracked_hands_no_infection_or_systemic_skin_disease.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: secondary_skin_infection_concern, open_wound, severe_cutaneous_adverse_reaction, skin_peeling_or_sloughing, mucosal_lesions, systemic_illness, immunocompromised, diabetes_general_risk, specialist_directed_dermatology_plan
- `dry_cracked_hands_no_infection_or_systemic_skin_disease.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `dry_cracked_hands_no_infection_or_systemic_skin_disease.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `dry_cracked_hands_no_infection_or_systemic_skin_disease.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `dry_cracked_hands_no_infection_or_systemic_skin_disease.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: secondary_skin_infection_concern, open_wound, severe_cutaneous_adverse_reaction, skin_peeling_or_sloughing, mucosal_lesions, systemic_illness, immunocompromised, diabetes_general_risk, specialist_directed_dermatology_plan
- `dry_cracked_hands_no_infection_or_systemic_skin_disease.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: secondary_skin_infection_concern, open_wound, severe_cutaneous_adverse_reaction, skin_peeling_or_sloughing, mucosal_lesions, systemic_illness, immunocompromised, diabetes_general_risk, specialist_directed_dermatology_plan
- `dry_cracked_hands_no_infection_or_systemic_skin_disease.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `dry_cracked_hands_no_infection_or_systemic_skin_disease.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `dry_cracked_hands_no_infection_or_systemic_skin_disease.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `dry_cracked_hands_no_infection_or_systemic_skin_disease.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: secondary_skin_infection_concern, open_wound, severe_cutaneous_adverse_reaction, skin_peeling_or_sloughing, mucosal_lesions, systemic_illness, immunocompromised, diabetes_general_risk, specialist_directed_dermatology_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit dry, cracked skin on the hands.

WHAT WE FOUND:
Your clinician diagnosed dry, cracked hands. We did not find signs of spreading infection, deep wound, severe allergic reaction, or a systemic skin emergency today.

WHAT TO DO AT HOME:
- Use a gentle moisturizer often.
- Avoid harsh soaps or irritating chemicals when you can.
- Protect the hands from repeated wet work or cold exposure when possible.

MEDICATIONS:
- Use skin medicines only if prescribed or recommended.
- Do not use leftover antibiotic or steroid creams unless your clinician said they are safe.

RETURN TO ED IF:
- Spreading redness, pus, fever, red streaks, or worsening warmth.
- Skin peeling, mouth sores, target-like rash, or feeling very ill.
- Painful cracks that deepen, bleed heavily, or do not improve as expected.

FOLLOW UP:
Follow up with primary care, urgent care, dermatology, or the ED if symptoms are not improving or your clinician told you to recheck.
```
