# Lower leg strain without rupture or neurovascular red flags

Phenotype ID: `lower_leg_strain_uncomplicated_no_rupture_or_neurovascular_red_flags`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of uncomplicated lower leg strain.
- No fracture concern, tendon rupture concern, infection, or neurovascular compromise.

## Exclusions

- Fracture or dislocation concern, tendon rupture concern, open wound, infection, neurovascular compromise, inability to bear weight, high-energy trauma, or specialist-directed orthopedic plan.

## Must-Not-Miss Diagnoses

- Tibia or fibula fracture.
- Tendon rupture.
- Neurovascular compromise.
- Compartment syndrome.

## Primitive List

- `lower_leg_strain_uncomplicated_no_rupture_or_neurovascular_red_flags.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `lower_leg_strain_uncomplicated_no_rupture_or_neurovascular_red_flags.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, tendon_or_ligament_rupture_concern, open_wound, septic_joint_or_infection_concern, neurovascular_compromise, unable_to_bear_weight_lower_extremity, high_energy_trauma, specialist_directed_orthopedic_plan
- `lower_leg_strain_uncomplicated_no_rupture_or_neurovascular_red_flags.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `lower_leg_strain_uncomplicated_no_rupture_or_neurovascular_red_flags.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `lower_leg_strain_uncomplicated_no_rupture_or_neurovascular_red_flags.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `lower_leg_strain_uncomplicated_no_rupture_or_neurovascular_red_flags.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, tendon_or_ligament_rupture_concern, open_wound, septic_joint_or_infection_concern, neurovascular_compromise, unable_to_bear_weight_lower_extremity, high_energy_trauma, specialist_directed_orthopedic_plan
- `lower_leg_strain_uncomplicated_no_rupture_or_neurovascular_red_flags.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, tendon_or_ligament_rupture_concern, open_wound, septic_joint_or_infection_concern, neurovascular_compromise, unable_to_bear_weight_lower_extremity, high_energy_trauma, specialist_directed_orthopedic_plan
- `lower_leg_strain_uncomplicated_no_rupture_or_neurovascular_red_flags.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `lower_leg_strain_uncomplicated_no_rupture_or_neurovascular_red_flags.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `lower_leg_strain_uncomplicated_no_rupture_or_neurovascular_red_flags.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `lower_leg_strain_uncomplicated_no_rupture_or_neurovascular_red_flags.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, tendon_or_ligament_rupture_concern, open_wound, septic_joint_or_infection_concern, neurovascular_compromise, unable_to_bear_weight_lower_extremity, high_energy_trauma, specialist_directed_orthopedic_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit a lower leg strain.

WHAT WE FOUND:
Your clinician diagnosed a lower leg strain. We did not find signs of fracture, tendon rupture, infection, or poor blood flow today.

WHAT TO DO AT HOME:
- Rest the leg as needed.
- Use ice wrapped in a cloth for short periods.
- Raise the leg when swelling is present.

MEDICATIONS:
- Use acetaminophen or ibuprofen only if you can take it safely and follow the label.
- Use medicines only as prescribed or recommended.

RETURN TO ED IF:
- New numbness, weakness, blue or pale toes, or severe worsening pain.
- Inability to walk, new deformity, fever, redness, or swelling.
- Symptoms that worsen or do not improve as expected.

FOLLOW UP:
Follow up with primary care, orthopedics, urgent care, or the ED if symptoms are not improving or your clinician told you to recheck.
```
