# Localized impetigo without cellulitis or systemic symptoms

Phenotype ID: `localized_impetigo_no_cellulitis_or_systemic_symptoms`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of localized impetigo.
- No cellulitis, abscess, ecthyma or deep infection, eye/genital involvement, systemic illness, immunocompromised-host pathway, or outbreak/public-health-directed plan.

## Exclusions

- Cellulitis, abscess, ecthyma, deep skin infection, systemic illness, sepsis, or rapidly spreading infection.
- Eye, genital, extensive, bullous, recurrent, or immunocompromised-host disease.
- Public-health-directed outbreak plan or poor follow-up.

## Must-Not-Miss Diagnoses

- Cellulitis.
- Abscess.
- Ecthyma.
- Sepsis.

## Primitive List

- `localized_impetigo_no_cellulitis_or_systemic_symptoms.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `localized_impetigo_no_cellulitis_or_systemic_symptoms.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: secondary_skin_infection_concern, abscess_concern, ecthyma_or_deep_skin_infection, bullous_or_extensive_impetigo, near_eye_or_genitals, immunocompromised, systemic_illness, sepsis, rapid_progression, poor_follow_up
- `localized_impetigo_no_cellulitis_or_systemic_symptoms.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `localized_impetigo_no_cellulitis_or_systemic_symptoms.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `localized_impetigo_no_cellulitis_or_systemic_symptoms.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `localized_impetigo_no_cellulitis_or_systemic_symptoms.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: secondary_skin_infection_concern, abscess_concern, ecthyma_or_deep_skin_infection, bullous_or_extensive_impetigo, near_eye_or_genitals, immunocompromised, systemic_illness, sepsis, rapid_progression, poor_follow_up
- `localized_impetigo_no_cellulitis_or_systemic_symptoms.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: secondary_skin_infection_concern, abscess_concern, ecthyma_or_deep_skin_infection, bullous_or_extensive_impetigo, near_eye_or_genitals, immunocompromised, systemic_illness, sepsis, rapid_progression, poor_follow_up
- `localized_impetigo_no_cellulitis_or_systemic_symptoms.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `localized_impetigo_no_cellulitis_or_systemic_symptoms.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `localized_impetigo_no_cellulitis_or_systemic_symptoms.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `localized_impetigo_no_cellulitis_or_systemic_symptoms.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: secondary_skin_infection_concern, abscess_concern, ecthyma_or_deep_skin_infection, bullous_or_extensive_impetigo, near_eye_or_genitals, immunocompromised, systemic_illness, sepsis, rapid_progression, poor_follow_up

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit impetigo, a contagious superficial skin infection.

WHAT WE FOUND:
Your clinician diagnosed localized impetigo. We did not find spreading cellulitis, a deeper infection, or systemic illness today.

WHAT TO DO AT HOME:
- Keep sores clean and covered when possible.
- Wash your hands after touching the area.
- Avoid scratching and do not share towels, clothing, or bedding until improving.

MEDICATIONS:
- Use antibiotic ointment or pills only if prescribed and exactly as directed.
- Use acetaminophen or ibuprofen only if you can take it safely and follow the label.

RETURN TO ED IF:
- Fever, spreading redness, warmth, swelling, red streaks, severe pain, or pus.
- Sores spread quickly, involve the eye or genitals, or become deep open ulcers.
- You feel very ill or symptoms worsen despite the plan you were given.

FOLLOW UP:
Follow up with primary care, urgent care, or dermatology if symptoms are not improving with treatment or if spread continues.
```
