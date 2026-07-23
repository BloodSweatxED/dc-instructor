# Localized common wart without genital or immunocompromised-host red flags

Phenotype ID: `localized_common_wart_no_genital_or_immunocompromised_host`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of localized common wart.
- No genital wart/STI pathway, near-eye lesion, infection, immunocompromised host, pregnancy/pediatric pathway, or diagnostic uncertainty.

## Exclusions

- Genital wart/STI pathway, near-eye lesion, infection concern, immunocompromised host, rapidly enlarging/bleeding lesion, pregnancy/pediatric pathway, or specialist-directed dermatology plan.

## Must-Not-Miss Diagnoses

- Genital/STI pathway.
- Skin infection.
- Immunocompromised host.
- Diagnostic uncertainty.

## Primitive List

- `localized_common_wart_no_genital_or_immunocompromised_host.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `localized_common_wart_no_genital_or_immunocompromised_host.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: sti_or_genital_pathway, near_eye_or_genitals, secondary_skin_infection_concern, immunocompromised, mass_red_flag_or_diagnostic_uncertainty, pregnancy, pediatric_pathway, specialist_directed_dermatology_plan
- `localized_common_wart_no_genital_or_immunocompromised_host.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `localized_common_wart_no_genital_or_immunocompromised_host.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `localized_common_wart_no_genital_or_immunocompromised_host.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `localized_common_wart_no_genital_or_immunocompromised_host.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: sti_or_genital_pathway, near_eye_or_genitals, secondary_skin_infection_concern, immunocompromised, mass_red_flag_or_diagnostic_uncertainty, pregnancy, pediatric_pathway, specialist_directed_dermatology_plan
- `localized_common_wart_no_genital_or_immunocompromised_host.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: sti_or_genital_pathway, near_eye_or_genitals, secondary_skin_infection_concern, immunocompromised, mass_red_flag_or_diagnostic_uncertainty, pregnancy, pediatric_pathway, specialist_directed_dermatology_plan
- `localized_common_wart_no_genital_or_immunocompromised_host.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `localized_common_wart_no_genital_or_immunocompromised_host.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `localized_common_wart_no_genital_or_immunocompromised_host.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `localized_common_wart_no_genital_or_immunocompromised_host.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: sti_or_genital_pathway, near_eye_or_genitals, secondary_skin_infection_concern, immunocompromised, mass_red_flag_or_diagnostic_uncertainty, pregnancy, pediatric_pathway, specialist_directed_dermatology_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit a localized common wart.

WHAT WE FOUND:
Your clinician diagnosed a localized common wart and did not find infection, genital involvement, or another emergency problem today.

WHAT TO DO AT HOME:
- Do not pick, cut, or dig at the wart.
- Keep it covered if it is irritated or likely to spread.
- Avoid sharing items that rub the area.

MEDICATIONS:
- Use wart treatment only if your clinician recommended it.
- Stop any treatment that causes severe pain, spreading redness, or an open wound.

RETURN TO ED IF:
- Spreading redness, pus, fever, severe pain, or the area turns black.
- The wart is on the genitals, near the eye, or you are immunocompromised.
- Rapid growth, bleeding, diagnostic uncertainty, or symptoms not improving as expected.

FOLLOW UP:
Follow up with primary care, dermatology, urgent care, or the ED if symptoms are not improving or your clinician told you to recheck.
```
