# Uncomplicated tinea pedis without cellulitis or diabetic foot risk

Phenotype ID: `tinea_pedis_uncomplicated_no_cellulitis_or_diabetic_foot`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of uncomplicated tinea pedis.
- No cellulitis, open wound, diabetic-foot pathway, immunocompromised host, nail/scalp/groin pathway, systemic illness, or specialist-directed plan.

## Exclusions

- Cellulitis, abscess, open wound, secondary infection, systemic illness, or rapidly spreading rash.
- Diabetes with foot wound/risk, PVD, neuropathy, immunocompromised host, nail/scalp/groin involvement, recurrent/extensive disease, or specialist-directed podiatry/dermatology plan.
- Medication selection not supplied by clinician.

## Must-Not-Miss Diagnoses

- Diabetic foot infection.
- Cellulitis.
- Abscess.
- Necrotizing infection.

## Primitive List

- `tinea_pedis_uncomplicated_no_cellulitis_or_diabetic_foot.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `tinea_pedis_uncomplicated_no_cellulitis_or_diabetic_foot.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: secondary_skin_infection_concern, abscess_or_boils_or_carbuncle, open_wound, wound_infection_concern, diabetic_foot, diabetes_general_risk, peripheral_vascular_disease, neuropathy_foot_risk, immunocompromised, scalp_or_nail_or_beard_fungal_infection, tinea_pedis_extensive_or_recurrent, systemic_illness, necrotizing_infection_concern, specialist_directed_podiatry_plan, specialist_directed_dermatology_plan
- `tinea_pedis_uncomplicated_no_cellulitis_or_diabetic_foot.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `tinea_pedis_uncomplicated_no_cellulitis_or_diabetic_foot.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `tinea_pedis_uncomplicated_no_cellulitis_or_diabetic_foot.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `tinea_pedis_uncomplicated_no_cellulitis_or_diabetic_foot.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: secondary_skin_infection_concern, abscess_or_boils_or_carbuncle, open_wound, wound_infection_concern, diabetic_foot, diabetes_general_risk, peripheral_vascular_disease, neuropathy_foot_risk, immunocompromised, scalp_or_nail_or_beard_fungal_infection, tinea_pedis_extensive_or_recurrent, systemic_illness, necrotizing_infection_concern, specialist_directed_podiatry_plan, specialist_directed_dermatology_plan
- `tinea_pedis_uncomplicated_no_cellulitis_or_diabetic_foot.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: secondary_skin_infection_concern, abscess_or_boils_or_carbuncle, open_wound, wound_infection_concern, diabetic_foot, diabetes_general_risk, peripheral_vascular_disease, neuropathy_foot_risk, immunocompromised, scalp_or_nail_or_beard_fungal_infection, tinea_pedis_extensive_or_recurrent, systemic_illness, necrotizing_infection_concern, specialist_directed_podiatry_plan, specialist_directed_dermatology_plan
- `tinea_pedis_uncomplicated_no_cellulitis_or_diabetic_foot.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `tinea_pedis_uncomplicated_no_cellulitis_or_diabetic_foot.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `tinea_pedis_uncomplicated_no_cellulitis_or_diabetic_foot.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `tinea_pedis_uncomplicated_no_cellulitis_or_diabetic_foot.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: secondary_skin_infection_concern, abscess_or_boils_or_carbuncle, open_wound, wound_infection_concern, diabetic_foot, diabetes_general_risk, peripheral_vascular_disease, neuropathy_foot_risk, immunocompromised, scalp_or_nail_or_beard_fungal_infection, tinea_pedis_extensive_or_recurrent, systemic_illness, necrotizing_infection_concern, specialist_directed_podiatry_plan, specialist_directed_dermatology_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit athlete's foot, also called tinea pedis.

WHAT WE FOUND:
Your clinician diagnosed uncomplicated tinea pedis. We did not find cellulitis, an open infected wound, or diabetic-foot risk requiring a different plan today.

WHAT TO DO AT HOME:
- Keep the feet clean and dry, especially between the toes.
- Change socks when damp and avoid sharing towels or footwear.
- Use shower shoes in shared wet areas when possible.

MEDICATIONS:
- Use antifungal medicine only if it was prescribed or recommended, and follow the label.
- Do not use steroid creams on the rash unless your clinician specifically told you to.

RETURN TO ED IF:
- Spreading redness, warmth, swelling, pus, fever, red streaks, or worsening pain.
- Open sores, black skin, numbness, or new foot wound.
- Symptoms are spreading, recurrent, or not improving with the plan you were given.

FOLLOW UP:
Follow up with primary care, urgent care, dermatology, or podiatry if symptoms are not improving or if this keeps coming back.
```
