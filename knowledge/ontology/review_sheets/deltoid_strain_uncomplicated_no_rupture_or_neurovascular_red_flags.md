# Deltoid strain without rupture or neurovascular red flags

Phenotype ID: `deltoid_strain_uncomplicated_no_rupture_or_neurovascular_red_flags`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of uncomplicated deltoid strain.
- No fracture/dislocation concern, tendon rupture concern, infection, neurovascular compromise, high-energy trauma, pregnancy/pediatric pathway, or specialist-directed plan.

## Exclusions

- Fracture or dislocation concern, tendon rupture concern, open wound, infection concern, neurovascular compromise, high-energy trauma, inability to use the limb, pregnancy/pediatric pathway, or specialist-directed orthopedic plan.

## Must-Not-Miss Diagnoses

- Rotator cuff rupture.
- Shoulder fracture or dislocation.
- Neurovascular compromise.
- Referred chest pain when symptoms are not clearly shoulder strain.

## Primitive List

- `deltoid_strain_uncomplicated_no_rupture_or_neurovascular_red_flags.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `deltoid_strain_uncomplicated_no_rupture_or_neurovascular_red_flags.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, tendon_or_ligament_rupture_concern, open_wound, septic_joint_or_infection_concern, neurovascular_compromise, high_energy_trauma, unable_to_use_limb, specialist_directed_orthopedic_plan
- `deltoid_strain_uncomplicated_no_rupture_or_neurovascular_red_flags.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `deltoid_strain_uncomplicated_no_rupture_or_neurovascular_red_flags.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `deltoid_strain_uncomplicated_no_rupture_or_neurovascular_red_flags.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `deltoid_strain_uncomplicated_no_rupture_or_neurovascular_red_flags.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, tendon_or_ligament_rupture_concern, open_wound, septic_joint_or_infection_concern, neurovascular_compromise, high_energy_trauma, unable_to_use_limb, specialist_directed_orthopedic_plan
- `deltoid_strain_uncomplicated_no_rupture_or_neurovascular_red_flags.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, tendon_or_ligament_rupture_concern, open_wound, septic_joint_or_infection_concern, neurovascular_compromise, high_energy_trauma, unable_to_use_limb, specialist_directed_orthopedic_plan
- `deltoid_strain_uncomplicated_no_rupture_or_neurovascular_red_flags.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `deltoid_strain_uncomplicated_no_rupture_or_neurovascular_red_flags.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `deltoid_strain_uncomplicated_no_rupture_or_neurovascular_red_flags.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `deltoid_strain_uncomplicated_no_rupture_or_neurovascular_red_flags.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, tendon_or_ligament_rupture_concern, open_wound, septic_joint_or_infection_concern, neurovascular_compromise, high_energy_trauma, unable_to_use_limb, specialist_directed_orthopedic_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit a deltoid strain.

WHAT WE FOUND:
Your clinician diagnosed a deltoid strain. We did not find fracture, tendon rupture, infection, or poor blood flow today.

WHAT TO DO AT HOME:
- Rest the shoulder from activity that makes pain worse.
- Use ice, heat, gentle motion, support, or activity limits only as your clinician recommended.
- Return to normal activity gradually as symptoms improve.

MEDICATIONS:
- Use pain medicine only if prescribed or recommended, and follow the label.
- Do not use medicine to push through worsening pain, numbness, or weakness.

RETURN TO ED IF:
- New numbness, weakness, blue or pale fingers, or severe worsening pain.
- A pop, new deformity, inability to use the arm, fever, spreading redness, or drainage.
- Symptoms that worsen or do not improve as expected.

FOLLOW UP:
Follow up with primary care, sports medicine, orthopedics, physical therapy, urgent care, or the ED if symptoms are not improving or your clinician told you to recheck.
```
