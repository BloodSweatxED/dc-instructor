# Knee tendinitis without rupture or infection red flags

Phenotype ID: `knee_tendinitis_uncomplicated_no_rupture_or_infection`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of uncomplicated knee tendinitis.
- No tendon rupture, fracture/dislocation concern, septic joint or infection concern, large effusion, neurovascular compromise, inability to bear weight, high-energy trauma, or specialist-directed plan.

## Exclusions

- Tendon rupture, fracture or dislocation concern, septic joint or infection concern, large effusion, open wound, neurovascular compromise, inability to bear weight, high-energy trauma, or specialist-directed orthopedic plan.

## Must-Not-Miss Diagnoses

- Patellar or quadriceps tendon rupture.
- Knee fracture or dislocation.
- Septic joint.
- Neurovascular compromise.

## Primitive List

- `knee_tendinitis_uncomplicated_no_rupture_or_infection.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `knee_tendinitis_uncomplicated_no_rupture_or_infection.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: tendon_or_ligament_rupture_concern, fracture_or_dislocation_concern, septic_joint_or_infection_concern, acute_hemarthrosis_or_large_effusion, open_wound, neurovascular_compromise, unable_to_bear_weight_lower_extremity, high_energy_trauma, specialist_directed_orthopedic_plan
- `knee_tendinitis_uncomplicated_no_rupture_or_infection.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `knee_tendinitis_uncomplicated_no_rupture_or_infection.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `knee_tendinitis_uncomplicated_no_rupture_or_infection.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `knee_tendinitis_uncomplicated_no_rupture_or_infection.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: tendon_or_ligament_rupture_concern, fracture_or_dislocation_concern, septic_joint_or_infection_concern, acute_hemarthrosis_or_large_effusion, open_wound, neurovascular_compromise, unable_to_bear_weight_lower_extremity, high_energy_trauma, specialist_directed_orthopedic_plan
- `knee_tendinitis_uncomplicated_no_rupture_or_infection.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: tendon_or_ligament_rupture_concern, fracture_or_dislocation_concern, septic_joint_or_infection_concern, acute_hemarthrosis_or_large_effusion, open_wound, neurovascular_compromise, unable_to_bear_weight_lower_extremity, high_energy_trauma, specialist_directed_orthopedic_plan
- `knee_tendinitis_uncomplicated_no_rupture_or_infection.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `knee_tendinitis_uncomplicated_no_rupture_or_infection.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `knee_tendinitis_uncomplicated_no_rupture_or_infection.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `knee_tendinitis_uncomplicated_no_rupture_or_infection.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: tendon_or_ligament_rupture_concern, fracture_or_dislocation_concern, septic_joint_or_infection_concern, acute_hemarthrosis_or_large_effusion, open_wound, neurovascular_compromise, unable_to_bear_weight_lower_extremity, high_energy_trauma, specialist_directed_orthopedic_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit uncomplicated knee tendinitis.

WHAT WE FOUND:
Your clinician diagnosed knee tendinitis. We did not find tendon rupture, fracture, septic joint, poor blood flow, or another knee emergency today.

WHAT TO DO AT HOME:
- Rest from activities that make knee pain worse.
- Use ice, gentle motion, activity limits, or therapy exercises only as your clinician recommended.
- Return to activity gradually as symptoms improve.

MEDICATIONS:
- Use pain medicine only if prescribed or recommended, and follow the label.
- Do not use medicine to push through worsening pain or weakness.

RETURN TO ED IF:
- A pop, new deformity, inability to straighten the knee, inability to walk, or severe worsening pain.
- Fever, a red hot swollen knee, spreading redness, or feeling very ill.
- New numbness, weakness, blue or pale toes, or symptoms not improving as expected.

FOLLOW UP:
Follow up with primary care, sports medicine, orthopedics, therapy, urgent care, or the ED if symptoms are not improving or your clinician told you to recheck.
```
