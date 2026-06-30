# Foot tendinitis without rupture or diabetic-foot red flags

Phenotype ID: `foot_tendinitis_uncomplicated_no_rupture_or_diabetic_foot`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of uncomplicated foot tendinitis.
- No tendon rupture, fracture/dislocation concern, open wound, infection, diabetic-foot/PVD/neuropathy risk, neurovascular compromise, inability to bear weight, high-energy trauma, or specialist-directed plan.

## Exclusions

- Tendon rupture, fracture or dislocation concern, open wound, infection concern, diabetic foot, PVD, neuropathy, neurovascular compromise, inability to bear weight, high-energy trauma, or specialist-directed podiatry/orthopedic plan.

## Must-Not-Miss Diagnoses

- Foot fracture.
- Tendon rupture.
- Diabetic foot infection.
- Neurovascular compromise.

## Primitive List

- `foot_tendinitis_uncomplicated_no_rupture_or_diabetic_foot.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `foot_tendinitis_uncomplicated_no_rupture_or_diabetic_foot.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: tendon_or_ligament_rupture_concern, fracture_or_dislocation_concern, open_wound, septic_joint_or_infection_concern, diabetic_foot, diabetes_general_risk, peripheral_vascular_disease, neuropathy_foot_risk, neurovascular_compromise, unable_to_bear_weight_lower_extremity, high_energy_trauma, specialist_directed_podiatry_plan, specialist_directed_orthopedic_plan
- `foot_tendinitis_uncomplicated_no_rupture_or_diabetic_foot.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `foot_tendinitis_uncomplicated_no_rupture_or_diabetic_foot.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `foot_tendinitis_uncomplicated_no_rupture_or_diabetic_foot.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `foot_tendinitis_uncomplicated_no_rupture_or_diabetic_foot.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: tendon_or_ligament_rupture_concern, fracture_or_dislocation_concern, open_wound, septic_joint_or_infection_concern, diabetic_foot, diabetes_general_risk, peripheral_vascular_disease, neuropathy_foot_risk, neurovascular_compromise, unable_to_bear_weight_lower_extremity, high_energy_trauma, specialist_directed_podiatry_plan, specialist_directed_orthopedic_plan
- `foot_tendinitis_uncomplicated_no_rupture_or_diabetic_foot.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: tendon_or_ligament_rupture_concern, fracture_or_dislocation_concern, open_wound, septic_joint_or_infection_concern, diabetic_foot, diabetes_general_risk, peripheral_vascular_disease, neuropathy_foot_risk, neurovascular_compromise, unable_to_bear_weight_lower_extremity, high_energy_trauma, specialist_directed_podiatry_plan, specialist_directed_orthopedic_plan
- `foot_tendinitis_uncomplicated_no_rupture_or_diabetic_foot.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `foot_tendinitis_uncomplicated_no_rupture_or_diabetic_foot.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `foot_tendinitis_uncomplicated_no_rupture_or_diabetic_foot.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `foot_tendinitis_uncomplicated_no_rupture_or_diabetic_foot.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: tendon_or_ligament_rupture_concern, fracture_or_dislocation_concern, open_wound, septic_joint_or_infection_concern, diabetic_foot, diabetes_general_risk, peripheral_vascular_disease, neuropathy_foot_risk, neurovascular_compromise, unable_to_bear_weight_lower_extremity, high_energy_trauma, specialist_directed_podiatry_plan, specialist_directed_orthopedic_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit uncomplicated foot tendinitis.

WHAT WE FOUND:
Your clinician diagnosed foot tendinitis. We did not find tendon rupture, fracture, infection, poor blood flow, or diabetic-foot red flags today.

WHAT TO DO AT HOME:
- Rest from activities that make foot pain worse.
- Use ice, elevation, activity limits, footwear changes, or therapy exercises only as your clinician recommended.
- Return to walking and exercise gradually as symptoms improve.

MEDICATIONS:
- Use pain medicine only if prescribed or recommended, and follow the label.
- Do not use medicine to push through worsening pain or weakness.

RETURN TO ED IF:
- A pop, new deformity, inability to walk, or severe worsening pain.
- Fever, spreading redness, warmth, drainage, open wound, or a new foot ulcer.
- New numbness, weakness, blue or pale toes, black skin, or symptoms not improving as expected.

FOLLOW UP:
Follow up with primary care, sports medicine, orthopedics, podiatry, therapy, urgent care, or the ED if symptoms are not improving or your clinician told you to recheck.
```
