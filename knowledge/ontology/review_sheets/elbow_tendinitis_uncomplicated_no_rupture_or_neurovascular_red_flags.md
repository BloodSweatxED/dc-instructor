# Elbow tendinitis without rupture or neurovascular red flags

Phenotype ID: `elbow_tendinitis_uncomplicated_no_rupture_or_neurovascular_red_flags`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of uncomplicated elbow tendinitis.
- No tendon rupture, fracture/dislocation concern, distal biceps/triceps concern, elbow instability, ulnar nerve symptoms, infection, neurovascular compromise, high-energy trauma, or specialist-directed plan.

## Exclusions

- Tendon rupture, distal biceps or triceps concern, fracture or dislocation concern, elbow instability, ulnar nerve symptoms, open wound, infection concern, neurovascular compromise, high-energy trauma, inability to use the limb, or specialist-directed orthopedic plan.

## Must-Not-Miss Diagnoses

- Distal biceps or triceps tendon rupture.
- Elbow fracture or dislocation.
- Ulnar nerve injury.
- Septic joint.

## Primitive List

- `elbow_tendinitis_uncomplicated_no_rupture_or_neurovascular_red_flags.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `elbow_tendinitis_uncomplicated_no_rupture_or_neurovascular_red_flags.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: tendon_or_ligament_rupture_concern, distal_biceps_or_triceps_concern, fracture_or_dislocation_concern, elbow_instability_or_ucl_lcl_concern, ulnar_nerve_pattern, open_wound, septic_joint_or_infection_concern, neurovascular_compromise, high_energy_trauma, unable_to_use_limb, specialist_directed_orthopedic_plan
- `elbow_tendinitis_uncomplicated_no_rupture_or_neurovascular_red_flags.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `elbow_tendinitis_uncomplicated_no_rupture_or_neurovascular_red_flags.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `elbow_tendinitis_uncomplicated_no_rupture_or_neurovascular_red_flags.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `elbow_tendinitis_uncomplicated_no_rupture_or_neurovascular_red_flags.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: tendon_or_ligament_rupture_concern, distal_biceps_or_triceps_concern, fracture_or_dislocation_concern, elbow_instability_or_ucl_lcl_concern, ulnar_nerve_pattern, open_wound, septic_joint_or_infection_concern, neurovascular_compromise, high_energy_trauma, unable_to_use_limb, specialist_directed_orthopedic_plan
- `elbow_tendinitis_uncomplicated_no_rupture_or_neurovascular_red_flags.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: tendon_or_ligament_rupture_concern, distal_biceps_or_triceps_concern, fracture_or_dislocation_concern, elbow_instability_or_ucl_lcl_concern, ulnar_nerve_pattern, open_wound, septic_joint_or_infection_concern, neurovascular_compromise, high_energy_trauma, unable_to_use_limb, specialist_directed_orthopedic_plan
- `elbow_tendinitis_uncomplicated_no_rupture_or_neurovascular_red_flags.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `elbow_tendinitis_uncomplicated_no_rupture_or_neurovascular_red_flags.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `elbow_tendinitis_uncomplicated_no_rupture_or_neurovascular_red_flags.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `elbow_tendinitis_uncomplicated_no_rupture_or_neurovascular_red_flags.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: tendon_or_ligament_rupture_concern, distal_biceps_or_triceps_concern, fracture_or_dislocation_concern, elbow_instability_or_ucl_lcl_concern, ulnar_nerve_pattern, open_wound, septic_joint_or_infection_concern, neurovascular_compromise, high_energy_trauma, unable_to_use_limb, specialist_directed_orthopedic_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit uncomplicated elbow tendinitis.

WHAT WE FOUND:
Your clinician diagnosed elbow tendinitis. We did not find tendon rupture, fracture, elbow instability, nerve or blood-flow problems, infection, or another elbow emergency today.

WHAT TO DO AT HOME:
- Rest from activities that make elbow pain worse.
- Use ice, gentle motion, activity limits, or therapy exercises only as your clinician recommended.
- Return to lifting, gripping, and repetitive work gradually as symptoms improve.

MEDICATIONS:
- Use pain medicine only if prescribed or recommended, and follow the label.
- Do not use medicine to push through worsening pain or weakness.

RETURN TO ED IF:
- New numbness, weakness, blue or pale fingers, or trouble using the hand.
- A pop, new deformity, elbow instability, inability to bend or straighten the elbow, or severe worsening pain.
- Fever, a red hot swollen joint, new injury, or symptoms not improving as expected.

FOLLOW UP:
Follow up with primary care, sports medicine, orthopedics, therapy, urgent care, or the ED if symptoms are not improving or your clinician told you to recheck.
```
