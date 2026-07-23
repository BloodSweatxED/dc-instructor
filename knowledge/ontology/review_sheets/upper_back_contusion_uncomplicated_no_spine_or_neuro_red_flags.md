# Upper back contusion without spine or neurologic red flags

Phenotype ID: `upper_back_contusion_uncomplicated_no_spine_or_neuro_red_flags`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of uncomplicated upper back contusion.
- No spine injury concern, fracture concern, neurologic deficit, infection, or high-energy trauma.

## Exclusions

- Midline spine tenderness, fracture or dislocation concern, neurologic deficit, high-energy trauma, infection concern, or specialist-directed spine plan.

## Must-Not-Miss Diagnoses

- Spine fracture.
- Spinal cord or nerve injury.
- Deep infection.
- Neurovascular compromise.

## Primitive List

- `upper_back_contusion_uncomplicated_no_spine_or_neuro_red_flags.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `upper_back_contusion_uncomplicated_no_spine_or_neuro_red_flags.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: midline_cervical_tenderness, fracture_or_dislocation_concern, neurologic_deficit, high_energy_trauma, septic_joint_or_infection_concern, specialist_directed_spine_plan
- `upper_back_contusion_uncomplicated_no_spine_or_neuro_red_flags.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `upper_back_contusion_uncomplicated_no_spine_or_neuro_red_flags.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `upper_back_contusion_uncomplicated_no_spine_or_neuro_red_flags.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `upper_back_contusion_uncomplicated_no_spine_or_neuro_red_flags.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: midline_cervical_tenderness, fracture_or_dislocation_concern, neurologic_deficit, high_energy_trauma, septic_joint_or_infection_concern, specialist_directed_spine_plan
- `upper_back_contusion_uncomplicated_no_spine_or_neuro_red_flags.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: midline_cervical_tenderness, fracture_or_dislocation_concern, neurologic_deficit, high_energy_trauma, septic_joint_or_infection_concern, specialist_directed_spine_plan
- `upper_back_contusion_uncomplicated_no_spine_or_neuro_red_flags.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `upper_back_contusion_uncomplicated_no_spine_or_neuro_red_flags.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `upper_back_contusion_uncomplicated_no_spine_or_neuro_red_flags.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `upper_back_contusion_uncomplicated_no_spine_or_neuro_red_flags.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: midline_cervical_tenderness, fracture_or_dislocation_concern, neurologic_deficit, high_energy_trauma, septic_joint_or_infection_concern, specialist_directed_spine_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit an upper back bruise.

WHAT WE FOUND:
Your clinician diagnosed an upper back bruise. We did not find signs of spine injury, fracture, nerve injury, infection, or poor blood flow today.

WHAT TO DO AT HOME:
- Rest the area as needed.
- Use ice wrapped in a cloth for short periods.
- Return to normal activity gradually as pain improves.

MEDICATIONS:
- Use acetaminophen or ibuprofen only if you can take it safely and follow the label.
- Use medicines only as prescribed or recommended.

RETURN TO ED IF:
- New weakness, numbness, trouble walking, loss of bladder or bowel control, or severe worsening pain.
- Fever, spreading redness, or new swelling.
- Symptoms that worsen or do not improve as expected.

FOLLOW UP:
Follow up with primary care, orthopedics, urgent care, or the ED if symptoms are not improving or your clinician told you to recheck.
```
