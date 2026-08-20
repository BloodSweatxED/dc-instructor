# Uncomplicated bunion without infection or diabetic-foot risk

Phenotype ID: `bunion_uncomplicated_no_infection_or_diabetic_foot`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of uncomplicated bunion.
- No infection, open wound, diabetic-foot/PVD/neuropathy risk, trauma/fracture concern, neurovascular compromise, inability to bear weight, pregnancy/pediatric pathway, or specialist-directed plan.

## Exclusions

- Cellulitis, abscess, pus, open wound, ulcer, fever, systemic illness, fracture/dislocation concern, neurovascular compromise, inability to bear weight, severe pain, or ischemic/black skin change.
- Diabetic foot risk, neuropathy, PVD, pregnancy/pediatric pathway, or specialist-directed podiatry/orthopedic plan.

## Must-Not-Miss Diagnoses

- Diabetic foot infection.
- Cellulitis or abscess.
- Fracture or dislocation.
- Neurovascular compromise.
- Ischemic toe.

## Primitive List

- `bunion_uncomplicated_no_infection_or_diabetic_foot.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `bunion_uncomplicated_no_infection_or_diabetic_foot.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: secondary_skin_infection_concern, open_wound, diabetic_foot, diabetes_general_risk, neuropathy_foot_risk, peripheral_vascular_disease, fracture_or_dislocation_concern, neurovascular_compromise, unable_to_bear_weight_lower_extremity, severe_pain, systemic_illness, pregnancy, pediatric_pathway, specialist_directed_podiatry_plan, specialist_directed_orthopedic_plan
- `bunion_uncomplicated_no_infection_or_diabetic_foot.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `bunion_uncomplicated_no_infection_or_diabetic_foot.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `bunion_uncomplicated_no_infection_or_diabetic_foot.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `bunion_uncomplicated_no_infection_or_diabetic_foot.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: secondary_skin_infection_concern, open_wound, diabetic_foot, diabetes_general_risk, neuropathy_foot_risk, peripheral_vascular_disease, fracture_or_dislocation_concern, neurovascular_compromise, unable_to_bear_weight_lower_extremity, severe_pain, systemic_illness, pregnancy, pediatric_pathway, specialist_directed_podiatry_plan, specialist_directed_orthopedic_plan
- `bunion_uncomplicated_no_infection_or_diabetic_foot.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: secondary_skin_infection_concern, open_wound, diabetic_foot, diabetes_general_risk, neuropathy_foot_risk, peripheral_vascular_disease, fracture_or_dislocation_concern, neurovascular_compromise, unable_to_bear_weight_lower_extremity, severe_pain, systemic_illness, pregnancy, pediatric_pathway, specialist_directed_podiatry_plan, specialist_directed_orthopedic_plan
- `bunion_uncomplicated_no_infection_or_diabetic_foot.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `bunion_uncomplicated_no_infection_or_diabetic_foot.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `bunion_uncomplicated_no_infection_or_diabetic_foot.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `bunion_uncomplicated_no_infection_or_diabetic_foot.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: secondary_skin_infection_concern, open_wound, diabetic_foot, diabetes_general_risk, neuropathy_foot_risk, peripheral_vascular_disease, fracture_or_dislocation_concern, neurovascular_compromise, unable_to_bear_weight_lower_extremity, severe_pain, systemic_illness, pregnancy, pediatric_pathway, specialist_directed_podiatry_plan, specialist_directed_orthopedic_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit a bunion, a painful bump near the base of the big toe.

WHAT WE FOUND:
Your clinician diagnosed an uncomplicated bunion. We did not find infection, diabetic-foot risk, trauma, neurovascular compromise, or another emergency problem today.

WHAT TO DO AT HOME:
- Wear wider or roomier shoes if recommended.
- Use padding or shoe changes only as instructed.
- Avoid pressure or friction that worsens the area.

MEDICATIONS:
- Use pain medicine only if prescribed or recommended, and follow the label.
- Avoid medicines your clinician told you to avoid.

RETURN TO ED IF:
- Fever, spreading redness, warmth, pus, red streaks, or open wound.
- New numbness, weakness, cold/blue toe, black skin, or poor circulation.
- New injury, inability to walk, or severe worsening pain.

FOLLOW UP:
Follow up with primary care, podiatry, or orthopedics if pain persists, shoe wear remains difficult, or your clinician told you to recheck.
```
