# Localized molluscum contagiosum without genital or immunocompromised-host features

Phenotype ID: `localized_molluscum_contagiosum_no_genital_or_immunocompromised_host`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of localized molluscum contagiosum.
- No genital, eye, extensive, secondary infection, immunocompromised-host, pediatric, pregnancy, or specialist-directed pathway.

## Exclusions

- Genital or sexually transmitted infection pathway, eye involvement, extensive or severe disease, immunocompromised host, or secondary infection.
- Pediatric pathway, pregnancy, poor follow-up, or specialist-directed dermatology plan.
- Uncertain rash diagnosis needing biopsy, STI testing, or another pathway.

## Must-Not-Miss Diagnoses

- Secondary skin infection.
- Genital STI pathway.
- Immunocompromised-host disseminated disease.
- Rash mimic requiring biopsy or urgent dermatology.

## Primitive List

- `localized_molluscum_contagiosum_no_genital_or_immunocompromised_host.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `localized_molluscum_contagiosum_no_genital_or_immunocompromised_host.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: molluscum_genital_eye_or_extensive, near_eye_or_genitals, secondary_skin_infection_concern, immunocompromised, pregnancy, pediatric_pathway, systemic_illness, poor_follow_up, specialist_directed_dermatology_plan
- `localized_molluscum_contagiosum_no_genital_or_immunocompromised_host.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `localized_molluscum_contagiosum_no_genital_or_immunocompromised_host.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `localized_molluscum_contagiosum_no_genital_or_immunocompromised_host.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `localized_molluscum_contagiosum_no_genital_or_immunocompromised_host.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: molluscum_genital_eye_or_extensive, near_eye_or_genitals, secondary_skin_infection_concern, immunocompromised, pregnancy, pediatric_pathway, systemic_illness, poor_follow_up, specialist_directed_dermatology_plan
- `localized_molluscum_contagiosum_no_genital_or_immunocompromised_host.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: molluscum_genital_eye_or_extensive, near_eye_or_genitals, secondary_skin_infection_concern, immunocompromised, pregnancy, pediatric_pathway, systemic_illness, poor_follow_up, specialist_directed_dermatology_plan
- `localized_molluscum_contagiosum_no_genital_or_immunocompromised_host.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `localized_molluscum_contagiosum_no_genital_or_immunocompromised_host.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `localized_molluscum_contagiosum_no_genital_or_immunocompromised_host.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `localized_molluscum_contagiosum_no_genital_or_immunocompromised_host.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: molluscum_genital_eye_or_extensive, near_eye_or_genitals, secondary_skin_infection_concern, immunocompromised, pregnancy, pediatric_pathway, systemic_illness, poor_follow_up, specialist_directed_dermatology_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit molluscum contagiosum, a contagious viral skin condition.

WHAT WE FOUND:
Your clinician diagnosed localized molluscum today. We did not find genital involvement, eye involvement, secondary infection, or a high-risk immune-system concern today.

WHAT TO DO AT HOME:
- Avoid scratching or picking at bumps.
- Do not shave over the bumps.
- Avoid sharing towels or clothing that touched the bumps.

MEDICATIONS:
- Use skin medicine only if prescribed or specifically recommended by your clinician.
- Do not try to cut, burn, or remove bumps yourself.

RETURN TO ED IF:
- Spreading redness, warmth, pus, fever, or severe pain.
- Bumps involve the eye, genitals, or spread widely.
- You have a weakened immune system or symptoms worsen despite the plan you were given.

FOLLOW UP:
Follow up with primary care or dermatology if bumps are spreading, bothersome, infected-appearing, or not improving as expected.
```
