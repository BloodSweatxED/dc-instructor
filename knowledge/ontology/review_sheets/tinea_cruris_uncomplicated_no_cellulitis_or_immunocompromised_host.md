# Uncomplicated tinea cruris without cellulitis or immunocompromised host

Phenotype ID: `tinea_cruris_uncomplicated_no_cellulitis_or_immunocompromised_host`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of uncomplicated tinea cruris or jock itch.
- No cellulitis, abscess, genital ulcer/STI pathway, immunocompromised host, extensive or recurrent fungal rash, pregnancy/pediatric pathway, or specialist-directed plan.

## Exclusions

- Cellulitis, abscess, pus, fever, systemic illness, severe pain, rapidly progressive rash, or immunocompromised host.
- Genital ulcers, STI concern, scrotal/testicular pain, pregnancy/pediatric pathway, extensive or recurrent fungal rash, or specialist-directed dermatology plan.

## Must-Not-Miss Diagnoses

- Cellulitis.
- Fournier gangrene or necrotizing infection.
- STI/genital ulcer disease.
- Testicular emergency mimic.

## Primitive List

- `tinea_cruris_uncomplicated_no_cellulitis_or_immunocompromised_host.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `tinea_cruris_uncomplicated_no_cellulitis_or_immunocompromised_host.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: secondary_skin_infection_concern, abscess_or_boils_or_carbuncle, rapid_progression, systemic_illness, immunocompromised, near_eye_or_genitals, genital_ulcers, sti_or_genital_pathway, scrotal_or_testicular_pain, extensive_or_recurrent_fungal_rash, pregnancy, pediatric_pathway, specialist_directed_dermatology_plan
- `tinea_cruris_uncomplicated_no_cellulitis_or_immunocompromised_host.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `tinea_cruris_uncomplicated_no_cellulitis_or_immunocompromised_host.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `tinea_cruris_uncomplicated_no_cellulitis_or_immunocompromised_host.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `tinea_cruris_uncomplicated_no_cellulitis_or_immunocompromised_host.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: secondary_skin_infection_concern, abscess_or_boils_or_carbuncle, rapid_progression, systemic_illness, immunocompromised, near_eye_or_genitals, genital_ulcers, sti_or_genital_pathway, scrotal_or_testicular_pain, extensive_or_recurrent_fungal_rash, pregnancy, pediatric_pathway, specialist_directed_dermatology_plan
- `tinea_cruris_uncomplicated_no_cellulitis_or_immunocompromised_host.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: secondary_skin_infection_concern, abscess_or_boils_or_carbuncle, rapid_progression, systemic_illness, immunocompromised, near_eye_or_genitals, genital_ulcers, sti_or_genital_pathway, scrotal_or_testicular_pain, extensive_or_recurrent_fungal_rash, pregnancy, pediatric_pathway, specialist_directed_dermatology_plan
- `tinea_cruris_uncomplicated_no_cellulitis_or_immunocompromised_host.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `tinea_cruris_uncomplicated_no_cellulitis_or_immunocompromised_host.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `tinea_cruris_uncomplicated_no_cellulitis_or_immunocompromised_host.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `tinea_cruris_uncomplicated_no_cellulitis_or_immunocompromised_host.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: secondary_skin_infection_concern, abscess_or_boils_or_carbuncle, rapid_progression, systemic_illness, immunocompromised, near_eye_or_genitals, genital_ulcers, sti_or_genital_pathway, scrotal_or_testicular_pain, extensive_or_recurrent_fungal_rash, pregnancy, pediatric_pathway, specialist_directed_dermatology_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit tinea cruris, also called jock itch.

WHAT WE FOUND:
Your clinician diagnosed an uncomplicated fungal groin rash. We did not find cellulitis, abscess, genital sores, STI concern, or an immunocompromised-host problem today.

WHAT TO DO AT HOME:
- Keep the groin area clean and dry.
- Change out of sweaty clothing promptly.
- Avoid sharing towels or clothing until symptoms are improving.

MEDICATIONS:
- Use antifungal medicine only as prescribed or recommended, and follow the label.
- Do not use steroid creams on the rash unless your clinician specifically told you to.

RETURN TO ED IF:
- Spreading redness, warmth, pus, fever, red streaks, or rapidly worsening pain.
- Genital sores, penile or vaginal discharge, testicular pain, or STI concern.
- Rash spreads widely, keeps returning, or does not improve with the plan.

FOLLOW UP:
Follow up with primary care or dermatology if symptoms are not improving, recur often, or spread despite the plan.
```
