# Toe tendinitis without rupture or diabetic-foot red flags

Phenotype ID: `toe_tendinitis_uncomplicated_no_rupture_or_diabetic_foot`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of uncomplicated toe tendinitis.
- No tendon rupture, fracture/dislocation concern, open wound, infection, diabetic-foot/PVD/neuropathy risk, neurovascular compromise, inability to bear weight, pregnancy/pediatric pathway, or specialist-directed plan.

## Exclusions

- Tendon rupture, fracture or dislocation concern, open wound, infection concern, diabetic foot, PVD, neuropathy, neurovascular compromise, inability to bear weight, high-energy trauma, pregnancy/pediatric pathway, or specialist-directed podiatry/orthopedic plan.

## Must-Not-Miss Diagnoses

- Toe tendon rupture.
- Toe fracture or dislocation.
- Diabetic foot infection.
- Neurovascular compromise.

## Primitive List

- `toe_tendinitis_uncomplicated_no_rupture_or_diabetic_foot.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `toe_tendinitis_uncomplicated_no_rupture_or_diabetic_foot.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: tendon_or_ligament_rupture_concern, fracture_or_dislocation_concern, open_wound, septic_joint_or_infection_concern, diabetic_foot, diabetes_general_risk, peripheral_vascular_disease, neuropathy_foot_risk, neurovascular_compromise, unable_to_bear_weight_lower_extremity, high_energy_trauma, specialist_directed_podiatry_plan, specialist_directed_orthopedic_plan
- `toe_tendinitis_uncomplicated_no_rupture_or_diabetic_foot.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `toe_tendinitis_uncomplicated_no_rupture_or_diabetic_foot.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `toe_tendinitis_uncomplicated_no_rupture_or_diabetic_foot.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `toe_tendinitis_uncomplicated_no_rupture_or_diabetic_foot.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: tendon_or_ligament_rupture_concern, fracture_or_dislocation_concern, open_wound, septic_joint_or_infection_concern, diabetic_foot, diabetes_general_risk, peripheral_vascular_disease, neuropathy_foot_risk, neurovascular_compromise, unable_to_bear_weight_lower_extremity, high_energy_trauma, specialist_directed_podiatry_plan, specialist_directed_orthopedic_plan
- `toe_tendinitis_uncomplicated_no_rupture_or_diabetic_foot.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: tendon_or_ligament_rupture_concern, fracture_or_dislocation_concern, open_wound, septic_joint_or_infection_concern, diabetic_foot, diabetes_general_risk, peripheral_vascular_disease, neuropathy_foot_risk, neurovascular_compromise, unable_to_bear_weight_lower_extremity, high_energy_trauma, specialist_directed_podiatry_plan, specialist_directed_orthopedic_plan
- `toe_tendinitis_uncomplicated_no_rupture_or_diabetic_foot.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `toe_tendinitis_uncomplicated_no_rupture_or_diabetic_foot.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `toe_tendinitis_uncomplicated_no_rupture_or_diabetic_foot.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `toe_tendinitis_uncomplicated_no_rupture_or_diabetic_foot.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: tendon_or_ligament_rupture_concern, fracture_or_dislocation_concern, open_wound, septic_joint_or_infection_concern, diabetic_foot, diabetes_general_risk, peripheral_vascular_disease, neuropathy_foot_risk, neurovascular_compromise, unable_to_bear_weight_lower_extremity, high_energy_trauma, specialist_directed_podiatry_plan, specialist_directed_orthopedic_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit uncomplicated toe tendinitis.

WHAT WE FOUND:
Your clinician diagnosed toe tendinitis. We did not find tendon rupture, fracture, infection, poor blood flow, diabetic-foot red flags, or another toe emergency today.

WHAT TO DO AT HOME:
- Rest the toe from activity that makes pain worse.
- Use ice, heat, gentle motion, support, or activity limits only as your clinician recommended.
- Return to normal activity gradually as symptoms improve.

MEDICATIONS:
- Use pain medicine only if prescribed or recommended, and follow the label.
- Do not use medicine to push through worsening pain, numbness, or weakness.

RETURN TO ED IF:
- A pop, new deformity, inability to walk, blue or pale toe, black skin, or severe worsening pain.
- New deformity, severe worsening pain, inability to use the area, or a new injury.
- Fever, spreading redness, warmth, drainage, or symptoms not improving as expected.

FOLLOW UP:
Follow up with primary care, podiatry, sports medicine, orthopedics, therapy, urgent care, or the ED if symptoms are not improving or your clinician told you to recheck.
```
