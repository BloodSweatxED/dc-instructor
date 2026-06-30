# Forearm tendinitis without rupture or neurovascular red flags

Phenotype ID: `forearm_tendinitis_uncomplicated_no_rupture_or_neurovascular_red_flags`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of uncomplicated forearm tendinitis.
- No tendon rupture, fracture/dislocation concern, hand tendon injury, infection, neurovascular compromise, high-energy trauma, or specialist-directed plan.

## Exclusions

- Tendon rupture, fracture or dislocation concern, hand tendon injury, open wound, infection concern, neurovascular compromise, high-energy trauma, inability to use the limb, or specialist-directed orthopedic plan.

## Must-Not-Miss Diagnoses

- Tendon rupture.
- Forearm fracture.
- Hand tendon injury.
- Neurovascular compromise.

## Primitive List

- `forearm_tendinitis_uncomplicated_no_rupture_or_neurovascular_red_flags.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `forearm_tendinitis_uncomplicated_no_rupture_or_neurovascular_red_flags.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: tendon_or_ligament_rupture_concern, fracture_or_dislocation_concern, hand_tendon_risk, open_wound, septic_joint_or_infection_concern, neurovascular_compromise, high_energy_trauma, unable_to_use_limb, specialist_directed_orthopedic_plan
- `forearm_tendinitis_uncomplicated_no_rupture_or_neurovascular_red_flags.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `forearm_tendinitis_uncomplicated_no_rupture_or_neurovascular_red_flags.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `forearm_tendinitis_uncomplicated_no_rupture_or_neurovascular_red_flags.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `forearm_tendinitis_uncomplicated_no_rupture_or_neurovascular_red_flags.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: tendon_or_ligament_rupture_concern, fracture_or_dislocation_concern, hand_tendon_risk, open_wound, septic_joint_or_infection_concern, neurovascular_compromise, high_energy_trauma, unable_to_use_limb, specialist_directed_orthopedic_plan
- `forearm_tendinitis_uncomplicated_no_rupture_or_neurovascular_red_flags.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: tendon_or_ligament_rupture_concern, fracture_or_dislocation_concern, hand_tendon_risk, open_wound, septic_joint_or_infection_concern, neurovascular_compromise, high_energy_trauma, unable_to_use_limb, specialist_directed_orthopedic_plan
- `forearm_tendinitis_uncomplicated_no_rupture_or_neurovascular_red_flags.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `forearm_tendinitis_uncomplicated_no_rupture_or_neurovascular_red_flags.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `forearm_tendinitis_uncomplicated_no_rupture_or_neurovascular_red_flags.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `forearm_tendinitis_uncomplicated_no_rupture_or_neurovascular_red_flags.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: tendon_or_ligament_rupture_concern, fracture_or_dislocation_concern, hand_tendon_risk, open_wound, septic_joint_or_infection_concern, neurovascular_compromise, high_energy_trauma, unable_to_use_limb, specialist_directed_orthopedic_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit uncomplicated forearm tendinitis.

WHAT WE FOUND:
Your clinician diagnosed forearm tendinitis. We did not find tendon rupture, fracture, infection, nerve or blood-flow problems, or another emergency pathway today.

WHAT TO DO AT HOME:
- Rest from activities that make forearm pain worse.
- Use ice, gentle motion, activity limits, or therapy exercises only as your clinician recommended.
- Return to lifting, gripping, and repetitive work gradually as symptoms improve.

MEDICATIONS:
- Use pain medicine only if prescribed or recommended, and follow the label.
- Do not use medicine to push through worsening pain or weakness.

RETURN TO ED IF:
- New numbness, weakness, blue or pale fingers, or trouble using the hand.
- A pop, new deformity, inability to bend or straighten the wrist or elbow, or severe worsening pain.
- Fever, spreading redness, warmth, drainage, new injury, or symptoms not improving as expected.

FOLLOW UP:
Follow up with primary care, sports medicine, orthopedics, therapy, urgent care, or the ED if symptoms are not improving or your clinician told you to recheck.
```
