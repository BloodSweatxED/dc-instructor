# Heel strain without rupture or diabetic-foot red flags

Phenotype ID: `heel_strain_uncomplicated_no_rupture_or_diabetic_foot`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of uncomplicated heel strain.
- No fracture concern, tendon rupture concern, infection, diabetic-foot pathway, or neurovascular compromise.

## Exclusions

- Fracture or dislocation concern, tendon rupture concern, open wound, infection, diabetic foot, peripheral vascular disease, neuropathy, inability to bear weight, high-energy trauma, or specialist-directed podiatry plan.

## Must-Not-Miss Diagnoses

- Calcaneus fracture.
- Achilles rupture.
- Diabetic foot infection.
- Neurovascular compromise.

## Primitive List

- `heel_strain_uncomplicated_no_rupture_or_diabetic_foot.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `heel_strain_uncomplicated_no_rupture_or_diabetic_foot.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, tendon_or_ligament_rupture_concern, open_wound, septic_joint_or_infection_concern, diabetic_foot, peripheral_vascular_disease, neuropathy_foot_risk, unable_to_bear_weight_lower_extremity, high_energy_trauma, neurovascular_compromise, specialist_directed_podiatry_plan
- `heel_strain_uncomplicated_no_rupture_or_diabetic_foot.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `heel_strain_uncomplicated_no_rupture_or_diabetic_foot.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `heel_strain_uncomplicated_no_rupture_or_diabetic_foot.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `heel_strain_uncomplicated_no_rupture_or_diabetic_foot.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, tendon_or_ligament_rupture_concern, open_wound, septic_joint_or_infection_concern, diabetic_foot, peripheral_vascular_disease, neuropathy_foot_risk, unable_to_bear_weight_lower_extremity, high_energy_trauma, neurovascular_compromise, specialist_directed_podiatry_plan
- `heel_strain_uncomplicated_no_rupture_or_diabetic_foot.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, tendon_or_ligament_rupture_concern, open_wound, septic_joint_or_infection_concern, diabetic_foot, peripheral_vascular_disease, neuropathy_foot_risk, unable_to_bear_weight_lower_extremity, high_energy_trauma, neurovascular_compromise, specialist_directed_podiatry_plan
- `heel_strain_uncomplicated_no_rupture_or_diabetic_foot.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `heel_strain_uncomplicated_no_rupture_or_diabetic_foot.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `heel_strain_uncomplicated_no_rupture_or_diabetic_foot.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `heel_strain_uncomplicated_no_rupture_or_diabetic_foot.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, tendon_or_ligament_rupture_concern, open_wound, septic_joint_or_infection_concern, diabetic_foot, peripheral_vascular_disease, neuropathy_foot_risk, unable_to_bear_weight_lower_extremity, high_energy_trauma, neurovascular_compromise, specialist_directed_podiatry_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit a heel strain.

WHAT WE FOUND:
Your clinician diagnosed a heel strain. We did not find signs of fracture, tendon rupture, infection, poor circulation, or a diabetic-foot emergency today.

WHAT TO DO AT HOME:
- Rest the heel as needed.
- Use ice wrapped in a cloth for short periods.
- Return to activity gradually as pain improves.

MEDICATIONS:
- Use acetaminophen or ibuprofen only if you can take it safely and follow the label.
- Use medicines only as prescribed or recommended.

RETURN TO ED IF:
- New numbness, blue or pale toes, inability to walk, or severe worsening pain.
- Fever, spreading redness, major swelling, or a new wound.
- Symptoms that worsen or do not improve as expected.

FOLLOW UP:
Follow up with primary care, podiatry, orthopedics, urgent care, or the ED if symptoms are not improving or your clinician told you to recheck.
```
