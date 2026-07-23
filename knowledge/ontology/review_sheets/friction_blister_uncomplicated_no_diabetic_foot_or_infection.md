# Uncomplicated friction blister without diabetic-foot risk or infection

Phenotype ID: `friction_blister_uncomplicated_no_diabetic_foot_or_infection`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of uncomplicated friction blister.
- No infection, burn pathway, diabetic-foot/PVD/neuropathy risk, widespread blistering, medication reaction, mucosal involvement, high-risk host, pregnancy/pediatric pathway, or specialist-directed plan.

## Exclusions

- Cellulitis, abscess, pus, open infected wound, fever, systemic illness, burn, chemical/electrical injury, widespread blistering, mucosal lesions, or severe cutaneous adverse reaction concern.
- Diabetic foot risk, neuropathy, PVD, immunocompromised host, pregnancy/pediatric pathway, or specialist-directed wound/podiatry plan.

## Must-Not-Miss Diagnoses

- Burn injury.
- Diabetic foot infection.
- Cellulitis or abscess.
- Severe cutaneous adverse reaction.
- Neurovascular compromise.

## Primitive List

- `friction_blister_uncomplicated_no_diabetic_foot_or_infection.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `friction_blister_uncomplicated_no_diabetic_foot_or_infection.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: secondary_skin_infection_concern, wound_infection_concern, open_wound, burn_high_risk_depth_location_or_mechanism, large_blistering_or_high_risk_burn, diabetic_foot, diabetes_general_risk, neuropathy_foot_risk, peripheral_vascular_disease, skin_peeling_or_sloughing, mucosal_lesions, severe_cutaneous_adverse_reaction, systemic_illness, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_wound_plan, specialist_directed_podiatry_plan
- `friction_blister_uncomplicated_no_diabetic_foot_or_infection.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `friction_blister_uncomplicated_no_diabetic_foot_or_infection.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `friction_blister_uncomplicated_no_diabetic_foot_or_infection.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `friction_blister_uncomplicated_no_diabetic_foot_or_infection.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: secondary_skin_infection_concern, wound_infection_concern, open_wound, burn_high_risk_depth_location_or_mechanism, large_blistering_or_high_risk_burn, diabetic_foot, diabetes_general_risk, neuropathy_foot_risk, peripheral_vascular_disease, skin_peeling_or_sloughing, mucosal_lesions, severe_cutaneous_adverse_reaction, systemic_illness, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_wound_plan, specialist_directed_podiatry_plan
- `friction_blister_uncomplicated_no_diabetic_foot_or_infection.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: secondary_skin_infection_concern, wound_infection_concern, open_wound, burn_high_risk_depth_location_or_mechanism, large_blistering_or_high_risk_burn, diabetic_foot, diabetes_general_risk, neuropathy_foot_risk, peripheral_vascular_disease, skin_peeling_or_sloughing, mucosal_lesions, severe_cutaneous_adverse_reaction, systemic_illness, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_wound_plan, specialist_directed_podiatry_plan
- `friction_blister_uncomplicated_no_diabetic_foot_or_infection.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `friction_blister_uncomplicated_no_diabetic_foot_or_infection.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `friction_blister_uncomplicated_no_diabetic_foot_or_infection.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `friction_blister_uncomplicated_no_diabetic_foot_or_infection.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: secondary_skin_infection_concern, wound_infection_concern, open_wound, burn_high_risk_depth_location_or_mechanism, large_blistering_or_high_risk_burn, diabetic_foot, diabetes_general_risk, neuropathy_foot_risk, peripheral_vascular_disease, skin_peeling_or_sloughing, mucosal_lesions, severe_cutaneous_adverse_reaction, systemic_illness, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_wound_plan, specialist_directed_podiatry_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit a simple friction blister.

WHAT WE FOUND:
Your clinician diagnosed an uncomplicated friction blister. We did not find infection, burn injury, diabetic-foot risk, or another emergency problem today.

WHAT TO DO AT HOME:
- Keep the blister clean and protected.
- Avoid friction or pressure on the area while it heals.
- Do not pop or cut the blister unless your clinician gave you a specific plan.

MEDICATIONS:
- Use dressing supplies or pain medicine only as prescribed or recommended.
- Do not put harsh chemicals or non-medical products on the blister.

RETURN TO ED IF:
- Spreading redness, warmth, pus, red streaks, fever, or worsening pain.
- Black skin, numbness, weakness, poor circulation, or a wound on a diabetic or insensate foot.
- Blisters become widespread, involve the mouth or eyes, or follow a new medication.

FOLLOW UP:
Follow up with primary care, podiatry, urgent care, or the ED if the blister is not healing or your clinician told you to recheck.
```
