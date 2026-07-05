# Dry cracked heels without diabetic-foot or infection red flags

Phenotype ID: `dry_cracked_heels_no_diabetic_foot_or_infection`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of dry cracked heels or localized xerosis.
- No secondary infection, open wound/ulcer, diabetic-foot/PVD/neuropathy risk, severe cutaneous adverse reaction, immunocompromised host, pregnancy/pediatric pathway, or specialist-directed plan.

## Exclusions

- Secondary infection, open wound or foot ulcer, diabetic foot, PVD, neuropathy, severe cutaneous adverse reaction, mucosal lesions, systemic illness, immunocompromised host, pregnancy/pediatric pathway, or specialist-directed dermatology/podiatry plan.

## Must-Not-Miss Diagnoses

- Cellulitis.
- Diabetic foot wound.
- Ischemic foot.
- Severe cutaneous adverse reaction.

## Primitive List

- `dry_cracked_heels_no_diabetic_foot_or_infection.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `dry_cracked_heels_no_diabetic_foot_or_infection.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: secondary_skin_infection_concern, open_wound, wound_infection_concern, diabetic_foot, diabetes_general_risk, peripheral_vascular_disease, neuropathy_foot_risk, severe_cutaneous_adverse_reaction, skin_peeling_or_sloughing, mucosal_lesions, systemic_illness, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_dermatology_plan, specialist_directed_podiatry_plan
- `dry_cracked_heels_no_diabetic_foot_or_infection.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `dry_cracked_heels_no_diabetic_foot_or_infection.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `dry_cracked_heels_no_diabetic_foot_or_infection.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `dry_cracked_heels_no_diabetic_foot_or_infection.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: secondary_skin_infection_concern, open_wound, wound_infection_concern, diabetic_foot, diabetes_general_risk, peripheral_vascular_disease, neuropathy_foot_risk, severe_cutaneous_adverse_reaction, skin_peeling_or_sloughing, mucosal_lesions, systemic_illness, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_dermatology_plan, specialist_directed_podiatry_plan
- `dry_cracked_heels_no_diabetic_foot_or_infection.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: secondary_skin_infection_concern, open_wound, wound_infection_concern, diabetic_foot, diabetes_general_risk, peripheral_vascular_disease, neuropathy_foot_risk, severe_cutaneous_adverse_reaction, skin_peeling_or_sloughing, mucosal_lesions, systemic_illness, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_dermatology_plan, specialist_directed_podiatry_plan
- `dry_cracked_heels_no_diabetic_foot_or_infection.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `dry_cracked_heels_no_diabetic_foot_or_infection.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `dry_cracked_heels_no_diabetic_foot_or_infection.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `dry_cracked_heels_no_diabetic_foot_or_infection.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: secondary_skin_infection_concern, open_wound, wound_infection_concern, diabetic_foot, diabetes_general_risk, peripheral_vascular_disease, neuropathy_foot_risk, severe_cutaneous_adverse_reaction, skin_peeling_or_sloughing, mucosal_lesions, systemic_illness, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_dermatology_plan, specialist_directed_podiatry_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit dry, cracked skin on the heels.

WHAT WE FOUND:
Your clinician diagnosed dry, cracked heels. We did not find spreading infection, open ulcer, diabetic-foot risk, poor circulation, or a systemic skin emergency today.

WHAT TO DO AT HOME:
- Use a gentle moisturizer as your clinician recommended.
- Avoid harsh soaps, irritating chemicals, and friction when you can.
- Keep the skin clean and protected from new cracking.

MEDICATIONS:
- Use skin medicines only if prescribed or recommended.
- Do not use leftover antibiotic or steroid creams unless your clinician said they are safe.

RETURN TO ED IF:
- Spreading redness, pus, fever, red streaks, warmth, or worsening pain.
- Black skin, numbness, poor circulation, a new foot ulcer, or bleeding cracks that do not heal.
- Skin peeling, mouth sores, widespread rash, or symptoms that worsen.

FOLLOW UP:
Follow up with primary care, podiatry, urgent care, dermatology, or the ED if symptoms are not improving or your clinician told you to recheck.
```
