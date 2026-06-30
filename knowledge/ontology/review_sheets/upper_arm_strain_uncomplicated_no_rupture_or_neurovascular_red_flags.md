# Upper arm strain without rupture or neurovascular red flags

Phenotype ID: `upper_arm_strain_uncomplicated_no_rupture_or_neurovascular_red_flags`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of uncomplicated upper arm strain.
- No fracture concern, tendon rupture concern, infection, or neurovascular compromise.

## Exclusions

- Fracture or dislocation concern, tendon rupture concern, open wound, infection, neurovascular compromise, high-energy trauma, or specialist-directed orthopedic plan.

## Must-Not-Miss Diagnoses

- Humerus fracture.
- Biceps or triceps rupture.
- Neurovascular compromise.
- Compartment syndrome.

## Primitive List

- `upper_arm_strain_uncomplicated_no_rupture_or_neurovascular_red_flags.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `upper_arm_strain_uncomplicated_no_rupture_or_neurovascular_red_flags.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, tendon_or_ligament_rupture_concern, open_wound, septic_joint_or_infection_concern, neurovascular_compromise, high_energy_trauma, unable_to_use_limb, specialist_directed_orthopedic_plan
- `upper_arm_strain_uncomplicated_no_rupture_or_neurovascular_red_flags.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `upper_arm_strain_uncomplicated_no_rupture_or_neurovascular_red_flags.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `upper_arm_strain_uncomplicated_no_rupture_or_neurovascular_red_flags.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `upper_arm_strain_uncomplicated_no_rupture_or_neurovascular_red_flags.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, tendon_or_ligament_rupture_concern, open_wound, septic_joint_or_infection_concern, neurovascular_compromise, high_energy_trauma, unable_to_use_limb, specialist_directed_orthopedic_plan
- `upper_arm_strain_uncomplicated_no_rupture_or_neurovascular_red_flags.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, tendon_or_ligament_rupture_concern, open_wound, septic_joint_or_infection_concern, neurovascular_compromise, high_energy_trauma, unable_to_use_limb, specialist_directed_orthopedic_plan
- `upper_arm_strain_uncomplicated_no_rupture_or_neurovascular_red_flags.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `upper_arm_strain_uncomplicated_no_rupture_or_neurovascular_red_flags.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `upper_arm_strain_uncomplicated_no_rupture_or_neurovascular_red_flags.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `upper_arm_strain_uncomplicated_no_rupture_or_neurovascular_red_flags.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, tendon_or_ligament_rupture_concern, open_wound, septic_joint_or_infection_concern, neurovascular_compromise, high_energy_trauma, unable_to_use_limb, specialist_directed_orthopedic_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit an upper arm strain.

WHAT WE FOUND:
Your clinician diagnosed an upper arm strain. We did not find signs of fracture, tendon rupture, infection, or poor blood flow today.

WHAT TO DO AT HOME:
- Rest the arm as needed.
- Use ice wrapped in a cloth for short periods.
- Avoid heavy lifting until pain is improving.

MEDICATIONS:
- Use acetaminophen or ibuprofen only if you can take it safely and follow the label.
- Use medicines only as prescribed or recommended.

RETURN TO ED IF:
- New numbness, weakness, blue or pale fingers, or severe worsening pain.
- New deformity, inability to use the arm, fever, redness, or swelling.
- Symptoms that worsen or do not improve as expected.

FOLLOW UP:
Follow up with primary care, orthopedics, urgent care, or the ED if symptoms are not improving or your clinician told you to recheck.
```
