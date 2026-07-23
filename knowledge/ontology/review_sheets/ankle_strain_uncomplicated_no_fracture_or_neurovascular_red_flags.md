# Ankle strain without fracture or neurovascular red flags

Phenotype ID: `ankle_strain_uncomplicated_no_fracture_or_neurovascular_red_flags`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of uncomplicated ankle strain.
- No fracture concern, tendon rupture concern, infection, neurovascular compromise, inability to bear weight, or high-energy trauma.

## Exclusions

- Fracture or dislocation concern, tendon or ligament rupture concern, neurovascular compromise, septic joint or infection concern, inability to bear weight, high-energy trauma, or specialist-directed orthopedic plan.

## Must-Not-Miss Diagnoses

- Ankle fracture or dislocation.
- Achilles or tendon rupture.
- Septic joint.
- Neurovascular compromise.

## Primitive List

- `ankle_strain_uncomplicated_no_fracture_or_neurovascular_red_flags.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `ankle_strain_uncomplicated_no_fracture_or_neurovascular_red_flags.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, tendon_or_ligament_rupture_concern, neurovascular_compromise, septic_joint_or_infection_concern, unable_to_bear_weight_lower_extremity, high_energy_trauma, specialist_directed_orthopedic_plan
- `ankle_strain_uncomplicated_no_fracture_or_neurovascular_red_flags.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `ankle_strain_uncomplicated_no_fracture_or_neurovascular_red_flags.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `ankle_strain_uncomplicated_no_fracture_or_neurovascular_red_flags.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `ankle_strain_uncomplicated_no_fracture_or_neurovascular_red_flags.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, tendon_or_ligament_rupture_concern, neurovascular_compromise, septic_joint_or_infection_concern, unable_to_bear_weight_lower_extremity, high_energy_trauma, specialist_directed_orthopedic_plan
- `ankle_strain_uncomplicated_no_fracture_or_neurovascular_red_flags.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, tendon_or_ligament_rupture_concern, neurovascular_compromise, septic_joint_or_infection_concern, unable_to_bear_weight_lower_extremity, high_energy_trauma, specialist_directed_orthopedic_plan
- `ankle_strain_uncomplicated_no_fracture_or_neurovascular_red_flags.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `ankle_strain_uncomplicated_no_fracture_or_neurovascular_red_flags.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `ankle_strain_uncomplicated_no_fracture_or_neurovascular_red_flags.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `ankle_strain_uncomplicated_no_fracture_or_neurovascular_red_flags.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, tendon_or_ligament_rupture_concern, neurovascular_compromise, septic_joint_or_infection_concern, unable_to_bear_weight_lower_extremity, high_energy_trauma, specialist_directed_orthopedic_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit an ankle strain.

WHAT WE FOUND:
Your clinician diagnosed an ankle strain. We did not find signs of fracture, tendon rupture, infection, or poor blood flow today.

WHAT TO DO AT HOME:
- Rest the ankle as instructed.
- Use ice wrapped in a cloth for short periods.
- Return to activity gradually as pain improves.

MEDICATIONS:
- Use acetaminophen or ibuprofen only if you can take it safely and follow the label.
- Use medicines only as prescribed or recommended.

RETURN TO ED IF:
- New numbness, blue or pale toes, inability to walk, or severe worsening pain.
- A pop with loss of strength, new deformity, fever, or spreading redness.
- Symptoms that worsen or do not improve as expected.

FOLLOW UP:
Follow up with primary care, sports medicine, orthopedics, urgent care, or the ED if symptoms are not improving or your clinician told you to recheck.
```
