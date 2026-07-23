# Olecranon bursitis without septic joint or trauma red flags

Phenotype ID: `olecranon_bursitis_uncomplicated_no_septic_joint_or_trauma`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of uncomplicated olecranon bursitis.
- No septic joint or infection concern, open wound, fracture/dislocation concern, high-energy trauma, neurovascular compromise, immunocompromised host, or specialist-directed plan.

## Exclusions

- Septic joint, cellulitis, abscess, pus, fever, open wound, fracture or dislocation concern, high-energy trauma, neurovascular compromise, immunocompromised host, or specialist-directed orthopedic plan.

## Must-Not-Miss Diagnoses

- Septic bursitis.
- Septic joint.
- Elbow fracture.
- Cellulitis.

## Primitive List

- `olecranon_bursitis_uncomplicated_no_septic_joint_or_trauma.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `olecranon_bursitis_uncomplicated_no_septic_joint_or_trauma.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: septic_joint_or_infection_concern, secondary_skin_infection_concern, abscess_or_boils_or_carbuncle, systemic_illness, open_wound, fracture_or_dislocation_concern, high_energy_trauma, neurovascular_compromise, immunocompromised, specialist_directed_orthopedic_plan
- `olecranon_bursitis_uncomplicated_no_septic_joint_or_trauma.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `olecranon_bursitis_uncomplicated_no_septic_joint_or_trauma.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `olecranon_bursitis_uncomplicated_no_septic_joint_or_trauma.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `olecranon_bursitis_uncomplicated_no_septic_joint_or_trauma.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: septic_joint_or_infection_concern, secondary_skin_infection_concern, abscess_or_boils_or_carbuncle, systemic_illness, open_wound, fracture_or_dislocation_concern, high_energy_trauma, neurovascular_compromise, immunocompromised, specialist_directed_orthopedic_plan
- `olecranon_bursitis_uncomplicated_no_septic_joint_or_trauma.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: septic_joint_or_infection_concern, secondary_skin_infection_concern, abscess_or_boils_or_carbuncle, systemic_illness, open_wound, fracture_or_dislocation_concern, high_energy_trauma, neurovascular_compromise, immunocompromised, specialist_directed_orthopedic_plan
- `olecranon_bursitis_uncomplicated_no_septic_joint_or_trauma.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `olecranon_bursitis_uncomplicated_no_septic_joint_or_trauma.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `olecranon_bursitis_uncomplicated_no_septic_joint_or_trauma.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `olecranon_bursitis_uncomplicated_no_septic_joint_or_trauma.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: septic_joint_or_infection_concern, secondary_skin_infection_concern, abscess_or_boils_or_carbuncle, systemic_illness, open_wound, fracture_or_dislocation_concern, high_energy_trauma, neurovascular_compromise, immunocompromised, specialist_directed_orthopedic_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit uncomplicated olecranon bursitis, swelling over the back of the elbow.

WHAT WE FOUND:
Your clinician diagnosed uncomplicated olecranon bursitis. We did not find septic joint, spreading infection, fracture, open wound, or another elbow emergency today.

WHAT TO DO AT HOME:
- Avoid leaning on or putting pressure on the elbow.
- Use padding, rest, ice, or activity limits only as your clinician recommended.
- Keep the skin over the elbow clean and protected.

MEDICATIONS:
- Use pain medicine only if prescribed or recommended, and follow the label.
- Take antibiotics only if they were prescribed for you.

RETURN TO ED IF:
- Fever, spreading redness, warmth, pus, red streaks, or feeling very ill.
- New injury, open wound, severe pain, inability to move the elbow, numbness, or color change in the hand.
- Swelling that rapidly worsens or does not improve as expected.

FOLLOW UP:
Follow up with primary care, sports medicine, orthopedics, urgent care, or the ED if swelling is not improving or your clinician told you to recheck.
```
