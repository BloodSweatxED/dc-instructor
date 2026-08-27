# Toe sprain with negative x-ray and no open wound or diabetic-foot risk

Phenotype ID: `toe_sprain_xray_negative_no_open_wound_or_diabetic_foot`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of toe sprain/strain.
- X-ray performed and negative, with intact neurovascular exam and no open wound, infection, diabetic-foot/PVD/neuropathy risk, pregnancy/pediatric pathway, or specialist-directed plan.

## Exclusions

- Fracture or dislocation concern, open wound, nail-bed injury requiring separate pathway, infection, neurovascular compromise, severe pain, inability to bear weight, high-energy trauma, or crush injury.
- Diabetic-foot risk, neuropathy, PVD, pregnancy/pediatric pathway, or specialist-directed podiatry/orthopedic plan.

## Must-Not-Miss Diagnoses

- Fracture or dislocation.
- Open fracture.
- Neurovascular compromise.
- Diabetic foot injury.
- Cellulitis or abscess.

## Primitive List

- `toe_sprain_xray_negative_no_open_wound_or_diabetic_foot.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `toe_sprain_xray_negative_no_open_wound_or_diabetic_foot.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, open_fracture, open_wound, secondary_skin_infection_concern, neurovascular_compromise, severe_pain, unable_to_bear_weight_lower_extremity, high_energy_trauma, crush_injury, diabetic_foot, neuropathy_foot_risk, peripheral_vascular_disease, pregnancy, pediatric_pathway, specialist_directed_podiatry_plan, specialist_directed_orthopedic_plan
- `toe_sprain_xray_negative_no_open_wound_or_diabetic_foot.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `toe_sprain_xray_negative_no_open_wound_or_diabetic_foot.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `toe_sprain_xray_negative_no_open_wound_or_diabetic_foot.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `toe_sprain_xray_negative_no_open_wound_or_diabetic_foot.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, open_fracture, open_wound, secondary_skin_infection_concern, neurovascular_compromise, severe_pain, unable_to_bear_weight_lower_extremity, high_energy_trauma, crush_injury, diabetic_foot, neuropathy_foot_risk, peripheral_vascular_disease, pregnancy, pediatric_pathway, specialist_directed_podiatry_plan, specialist_directed_orthopedic_plan
- `toe_sprain_xray_negative_no_open_wound_or_diabetic_foot.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, open_fracture, open_wound, secondary_skin_infection_concern, neurovascular_compromise, severe_pain, unable_to_bear_weight_lower_extremity, high_energy_trauma, crush_injury, diabetic_foot, neuropathy_foot_risk, peripheral_vascular_disease, pregnancy, pediatric_pathway, specialist_directed_podiatry_plan, specialist_directed_orthopedic_plan
- `toe_sprain_xray_negative_no_open_wound_or_diabetic_foot.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `toe_sprain_xray_negative_no_open_wound_or_diabetic_foot.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `toe_sprain_xray_negative_no_open_wound_or_diabetic_foot.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `toe_sprain_xray_negative_no_open_wound_or_diabetic_foot.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, open_fracture, open_wound, secondary_skin_infection_concern, neurovascular_compromise, severe_pain, unable_to_bear_weight_lower_extremity, high_energy_trauma, crush_injury, diabetic_foot, neuropathy_foot_risk, peripheral_vascular_disease, pregnancy, pediatric_pathway, specialist_directed_podiatry_plan, specialist_directed_orthopedic_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit a toe sprain.

WHAT WE FOUND:
Your clinician diagnosed a toe sprain. Your x-ray did not show a fracture, and we did not find an open wound, infection, diabetic-foot risk, neurovascular compromise, or another emergency problem today.

WHAT TO DO AT HOME:
- Rest from painful walking or pressure.
- Use buddy taping, a shoe, ice, elevation, or activity changes only as instructed.
- Protect the toe from repeat injury while it heals.

MEDICATIONS:
- Use pain medicine only if prescribed or recommended, and follow the label.
- Avoid medicines your clinician told you to avoid.

RETURN TO ED IF:
- New numbness, color change, severe pain, or worsening inability to walk.
- Spreading redness, warmth, pus, red streaks, fever, or an open wound.
- New deformity, worsening swelling, or symptoms not improving.

FOLLOW UP:
Follow up with primary care, sports medicine, podiatry, or orthopedics if pain, walking, or swelling is not improving.
```
