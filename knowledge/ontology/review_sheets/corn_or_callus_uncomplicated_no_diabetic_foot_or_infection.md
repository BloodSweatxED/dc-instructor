# Uncomplicated corn or callus without diabetic foot or infection

Phenotype ID: `corn_or_callus_uncomplicated_no_diabetic_foot_or_infection`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of uncomplicated corn or callus.
- No open wound, secondary infection, diabetic-foot/PVD/neuropathy risk, severe pain, inability to walk, or specialist-directed plan.

## Exclusions

- Diabetic foot risk, neuropathy, PVD, open wound, ulcer, cellulitis, abscess, bleeding crack, black skin, or systemic illness.
- Severe pain, inability to walk, pregnancy/pediatric pathway, or specialist-directed podiatry plan.

## Must-Not-Miss Diagnoses

- Diabetic foot wound.
- Cellulitis.
- Foot ulcer.
- Ischemic foot.

## Primitive List

- `corn_or_callus_uncomplicated_no_diabetic_foot_or_infection.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `corn_or_callus_uncomplicated_no_diabetic_foot_or_infection.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: diabetic_foot, diabetes_general_risk, peripheral_vascular_disease, neuropathy_foot_risk, open_wound, wound_infection_concern, secondary_skin_infection_concern, corn_callus_complicated_foot_risk, unable_to_walk, systemic_illness, pregnancy, pediatric_pathway, specialist_directed_podiatry_plan
- `corn_or_callus_uncomplicated_no_diabetic_foot_or_infection.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `corn_or_callus_uncomplicated_no_diabetic_foot_or_infection.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `corn_or_callus_uncomplicated_no_diabetic_foot_or_infection.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `corn_or_callus_uncomplicated_no_diabetic_foot_or_infection.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: diabetic_foot, diabetes_general_risk, peripheral_vascular_disease, neuropathy_foot_risk, open_wound, wound_infection_concern, secondary_skin_infection_concern, corn_callus_complicated_foot_risk, unable_to_walk, systemic_illness, pregnancy, pediatric_pathway, specialist_directed_podiatry_plan
- `corn_or_callus_uncomplicated_no_diabetic_foot_or_infection.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: diabetic_foot, diabetes_general_risk, peripheral_vascular_disease, neuropathy_foot_risk, open_wound, wound_infection_concern, secondary_skin_infection_concern, corn_callus_complicated_foot_risk, unable_to_walk, systemic_illness, pregnancy, pediatric_pathway, specialist_directed_podiatry_plan
- `corn_or_callus_uncomplicated_no_diabetic_foot_or_infection.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `corn_or_callus_uncomplicated_no_diabetic_foot_or_infection.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `corn_or_callus_uncomplicated_no_diabetic_foot_or_infection.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `corn_or_callus_uncomplicated_no_diabetic_foot_or_infection.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: diabetic_foot, diabetes_general_risk, peripheral_vascular_disease, neuropathy_foot_risk, open_wound, wound_infection_concern, secondary_skin_infection_concern, corn_callus_complicated_foot_risk, unable_to_walk, systemic_illness, pregnancy, pediatric_pathway, specialist_directed_podiatry_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit a corn or callus, thickened skin from pressure or friction.

WHAT WE FOUND:
Your clinician diagnosed an uncomplicated corn or callus. We did not find infection, an open wound, or diabetic-foot risk requiring a different plan today.

WHAT TO DO AT HOME:
- Reduce pressure or friction on the area when possible.
- Wear comfortable footwear or protective padding if recommended.
- Do not cut or shave thickened skin yourself.

MEDICATIONS:
- Use corn/callus products only if prescribed or recommended.
- Do not use acid pads or sharp tools on the feet if you have diabetes, numbness, poor circulation, or broken skin.

RETURN TO ED IF:
- Spreading redness, warmth, pus, fever, red streaks, or worsening pain.
- Open sore, bleeding crack, black skin, numbness, or new foot wound.
- Pain prevents walking or the area is not improving with pressure reduction.

FOLLOW UP:
Follow up with primary care or podiatry if pain persists, walking is affected, or you have diabetes, poor circulation, or numbness.
```
