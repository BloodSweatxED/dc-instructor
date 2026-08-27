# Medial epicondylitis without fracture or neurovascular red flags

Phenotype ID: `medial_epicondylitis_uncomplicated_no_fracture_or_neurovascular_red_flags`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of uncomplicated medial epicondylitis or golfer's elbow.
- No fracture/dislocation concern, tendon rupture, elbow instability/UCL concern, ulnar nerve symptoms, neurovascular compromise, infection, high-energy trauma, or specialist-directed plan.

## Exclusions

- Fracture or dislocation concern, tendon rupture, distal biceps or triceps concern, elbow instability or UCL concern, ulnar nerve symptoms, neurovascular compromise, septic joint or infection concern, open wound, high-energy trauma, or specialist-directed orthopedic plan.

## Must-Not-Miss Diagnoses

- Elbow fracture or dislocation.
- UCL injury or elbow instability.
- Ulnar nerve injury.
- Septic joint.

## Primitive List

- `medial_epicondylitis_uncomplicated_no_fracture_or_neurovascular_red_flags.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `medial_epicondylitis_uncomplicated_no_fracture_or_neurovascular_red_flags.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, tendon_or_ligament_rupture_concern, distal_biceps_or_triceps_concern, elbow_instability_or_ucl_lcl_concern, ulnar_nerve_pattern, neurovascular_compromise, septic_joint_or_infection_concern, open_wound, high_energy_trauma, specialist_directed_orthopedic_plan
- `medial_epicondylitis_uncomplicated_no_fracture_or_neurovascular_red_flags.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `medial_epicondylitis_uncomplicated_no_fracture_or_neurovascular_red_flags.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `medial_epicondylitis_uncomplicated_no_fracture_or_neurovascular_red_flags.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `medial_epicondylitis_uncomplicated_no_fracture_or_neurovascular_red_flags.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, tendon_or_ligament_rupture_concern, distal_biceps_or_triceps_concern, elbow_instability_or_ucl_lcl_concern, ulnar_nerve_pattern, neurovascular_compromise, septic_joint_or_infection_concern, open_wound, high_energy_trauma, specialist_directed_orthopedic_plan
- `medial_epicondylitis_uncomplicated_no_fracture_or_neurovascular_red_flags.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, tendon_or_ligament_rupture_concern, distal_biceps_or_triceps_concern, elbow_instability_or_ucl_lcl_concern, ulnar_nerve_pattern, neurovascular_compromise, septic_joint_or_infection_concern, open_wound, high_energy_trauma, specialist_directed_orthopedic_plan
- `medial_epicondylitis_uncomplicated_no_fracture_or_neurovascular_red_flags.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `medial_epicondylitis_uncomplicated_no_fracture_or_neurovascular_red_flags.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `medial_epicondylitis_uncomplicated_no_fracture_or_neurovascular_red_flags.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `medial_epicondylitis_uncomplicated_no_fracture_or_neurovascular_red_flags.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, tendon_or_ligament_rupture_concern, distal_biceps_or_triceps_concern, elbow_instability_or_ucl_lcl_concern, ulnar_nerve_pattern, neurovascular_compromise, septic_joint_or_infection_concern, open_wound, high_energy_trauma, specialist_directed_orthopedic_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit medial epicondylitis, often called golfer's elbow.

WHAT WE FOUND:
Your clinician diagnosed uncomplicated medial epicondylitis. We did not find fracture, tendon rupture, elbow instability, nerve or blood-flow problems, or infection today.

WHAT TO DO AT HOME:
- Rest from activities that trigger sharp elbow pain.
- Use ice, stretching, therapy exercises, or a brace only as your clinician recommended.
- Return to gripping, throwing, lifting, and repetitive forearm activity gradually as symptoms improve.

MEDICATIONS:
- Use pain medicine only if prescribed or recommended, and follow the label.
- Do not use medicine to push through worsening pain, numbness, or weakness.

RETURN TO ED IF:
- New numbness or tingling in the ring or little finger, hand weakness, blue or pale fingers, or trouble using the hand.
- A pop, new deformity, inability to bend or straighten the elbow, or severe worsening pain.
- Fever, a red hot swollen joint, new injury, or symptoms not improving as expected.

FOLLOW UP:
Follow up with primary care, sports medicine, orthopedics, therapy, urgent care, or the ED if symptoms are not improving or your clinician told you to recheck.
```
