# Localized plantar wart without diabetic foot or immunocompromised host

Phenotype ID: `localized_plantar_wart_no_diabetic_foot_or_immunocompromised_host`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of localized plantar wart.
- No diabetic-foot pathway, open wound, infection, immunocompromised host, genital wart, severe pain/ambulation problem, or specialist-directed plan.

## Exclusions

- Diabetes with foot risk, neuropathy, PVD, open wound, cellulitis, abscess, bleeding wart, severe pain, inability to walk, or immunocompromised host.
- Genital wart/STI pathway, mucosal wart, pregnancy/pediatric pathway, or specialist-directed podiatry/dermatology plan.

## Must-Not-Miss Diagnoses

- Diabetic foot wound.
- Cellulitis.
- Melanoma or wart mimic.
- Genital wart/STI pathway.

## Primitive List

- `localized_plantar_wart_no_diabetic_foot_or_immunocompromised_host.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `localized_plantar_wart_no_diabetic_foot_or_immunocompromised_host.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: diabetic_foot, diabetes_general_risk, peripheral_vascular_disease, neuropathy_foot_risk, open_wound, secondary_skin_infection_concern, wound_infection_concern, immunocompromised, near_eye_or_genitals, plantar_wart_complicated_or_extensive, unable_to_walk, pregnancy, pediatric_pathway, specialist_directed_podiatry_plan, specialist_directed_dermatology_plan
- `localized_plantar_wart_no_diabetic_foot_or_immunocompromised_host.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `localized_plantar_wart_no_diabetic_foot_or_immunocompromised_host.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `localized_plantar_wart_no_diabetic_foot_or_immunocompromised_host.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `localized_plantar_wart_no_diabetic_foot_or_immunocompromised_host.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: diabetic_foot, diabetes_general_risk, peripheral_vascular_disease, neuropathy_foot_risk, open_wound, secondary_skin_infection_concern, wound_infection_concern, immunocompromised, near_eye_or_genitals, plantar_wart_complicated_or_extensive, unable_to_walk, pregnancy, pediatric_pathway, specialist_directed_podiatry_plan, specialist_directed_dermatology_plan
- `localized_plantar_wart_no_diabetic_foot_or_immunocompromised_host.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: diabetic_foot, diabetes_general_risk, peripheral_vascular_disease, neuropathy_foot_risk, open_wound, secondary_skin_infection_concern, wound_infection_concern, immunocompromised, near_eye_or_genitals, plantar_wart_complicated_or_extensive, unable_to_walk, pregnancy, pediatric_pathway, specialist_directed_podiatry_plan, specialist_directed_dermatology_plan
- `localized_plantar_wart_no_diabetic_foot_or_immunocompromised_host.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `localized_plantar_wart_no_diabetic_foot_or_immunocompromised_host.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `localized_plantar_wart_no_diabetic_foot_or_immunocompromised_host.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `localized_plantar_wart_no_diabetic_foot_or_immunocompromised_host.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: diabetic_foot, diabetes_general_risk, peripheral_vascular_disease, neuropathy_foot_risk, open_wound, secondary_skin_infection_concern, wound_infection_concern, immunocompromised, near_eye_or_genitals, plantar_wart_complicated_or_extensive, unable_to_walk, pregnancy, pediatric_pathway, specialist_directed_podiatry_plan, specialist_directed_dermatology_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit a plantar wart, a wart on the bottom of the foot.

WHAT WE FOUND:
Your clinician diagnosed a localized plantar wart. We did not find a diabetic-foot wound, skin infection, genital wart pathway, or immunocompromised-host risk today.

WHAT TO DO AT HOME:
- Keep the area clean and dry.
- Do not pick, cut, or dig into the wart.
- Avoid sharing towels, razors, nail tools, or footwear.

MEDICATIONS:
- Use wart medicine only if prescribed or recommended, and follow the label.
- Do not use acid or freezing treatments on broken skin or high-risk feet unless your clinician told you to.

RETURN TO ED IF:
- Spreading redness, pus, fever, red streaks, or severe worsening pain.
- New foot wound, numbness, black skin, or trouble walking.
- Warts are genital, rapidly spreading, bleeding, or occurring with immune compromise.

FOLLOW UP:
Follow up with primary care, dermatology, or podiatry if pain persists, walking is affected, or treatment is not working.
```
