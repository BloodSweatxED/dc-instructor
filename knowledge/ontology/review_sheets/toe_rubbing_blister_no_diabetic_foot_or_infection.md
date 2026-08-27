# Toe rubbing blister without diabetic-foot or infection red flags

Phenotype ID: `toe_rubbing_blister_no_diabetic_foot_or_infection`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of uncomplicated toe rubbing blister.
- No infection, burn pathway, widespread blistering, medication reaction, mucosal involvement, high-risk host, pregnancy/pediatric pathway, diabetic-foot/PVD/neuropathy risk, or specialist-directed plan.

## Exclusions

- Cellulitis, abscess, pus, open infected wound, fever, systemic illness, burn, chemical/electrical injury, widespread blistering, mucosal lesions, severe cutaneous adverse reaction concern, immunocompromised host, pregnancy/pediatric pathway, diabetic foot risk, neuropathy, PVD, or specialist-directed wound/podiatry plan.

## Must-Not-Miss Diagnoses

- Burn injury.
- Cellulitis or abscess.
- Severe cutaneous adverse reaction.
- Diabetic foot infection.

## Primitive List

- `toe_rubbing_blister_no_diabetic_foot_or_infection.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `toe_rubbing_blister_no_diabetic_foot_or_infection.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: secondary_skin_infection_concern, wound_infection_concern, open_wound, burn_high_risk_depth_location_or_mechanism, large_blistering_or_high_risk_burn, diabetic_foot, diabetes_general_risk, neuropathy_foot_risk, peripheral_vascular_disease, skin_peeling_or_sloughing, mucosal_lesions, severe_cutaneous_adverse_reaction, systemic_illness, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_wound_plan, specialist_directed_podiatry_plan
- `toe_rubbing_blister_no_diabetic_foot_or_infection.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `toe_rubbing_blister_no_diabetic_foot_or_infection.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `toe_rubbing_blister_no_diabetic_foot_or_infection.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `toe_rubbing_blister_no_diabetic_foot_or_infection.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: secondary_skin_infection_concern, wound_infection_concern, open_wound, burn_high_risk_depth_location_or_mechanism, large_blistering_or_high_risk_burn, diabetic_foot, diabetes_general_risk, neuropathy_foot_risk, peripheral_vascular_disease, skin_peeling_or_sloughing, mucosal_lesions, severe_cutaneous_adverse_reaction, systemic_illness, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_wound_plan, specialist_directed_podiatry_plan
- `toe_rubbing_blister_no_diabetic_foot_or_infection.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: secondary_skin_infection_concern, wound_infection_concern, open_wound, burn_high_risk_depth_location_or_mechanism, large_blistering_or_high_risk_burn, diabetic_foot, diabetes_general_risk, neuropathy_foot_risk, peripheral_vascular_disease, skin_peeling_or_sloughing, mucosal_lesions, severe_cutaneous_adverse_reaction, systemic_illness, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_wound_plan, specialist_directed_podiatry_plan
- `toe_rubbing_blister_no_diabetic_foot_or_infection.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `toe_rubbing_blister_no_diabetic_foot_or_infection.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `toe_rubbing_blister_no_diabetic_foot_or_infection.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `toe_rubbing_blister_no_diabetic_foot_or_infection.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: secondary_skin_infection_concern, wound_infection_concern, open_wound, burn_high_risk_depth_location_or_mechanism, large_blistering_or_high_risk_burn, diabetic_foot, diabetes_general_risk, neuropathy_foot_risk, peripheral_vascular_disease, skin_peeling_or_sloughing, mucosal_lesions, severe_cutaneous_adverse_reaction, systemic_illness, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_wound_plan, specialist_directed_podiatry_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit an uncomplicated toe rubbing blister.

WHAT WE FOUND:
Your clinician diagnosed an uncomplicated toe rubbing blister. We did not find infection, burn injury, widespread blistering, diabetic-foot risk, or another emergency problem today.

WHAT TO DO AT HOME:
- Protect the blister from more rubbing or pressure.
- Keep the area clean and dry unless your clinician told you something different.
- Do not pop, cut, or peel the blister unless your clinician instructed you to.

MEDICATIONS:
- Use pain medicine only if prescribed or recommended, and follow the label.
- Use creams, ointments, or antibiotics only if your clinician prescribed or recommended them.

RETURN TO ED IF:
- Spreading redness, warmth, pus, red streaks, fever, or worsening swelling.
- Skin peeling, mouth sores, widespread blisters, severe pain, or a blister from a burn or chemical exposure.
- Numbness, black skin, poor circulation, a new foot ulcer, or symptoms not improving as expected.

FOLLOW UP:
Follow up with primary care, podiatry, urgent care, or the ED if the blister is not healing or your clinician told you to recheck.
```
