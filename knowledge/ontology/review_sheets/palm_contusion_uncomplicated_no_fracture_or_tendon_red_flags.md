# Palm contusion without fracture or tendon red flags

Phenotype ID: `palm_contusion_uncomplicated_no_fracture_or_tendon_red_flags`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of uncomplicated palm contusion.
- No fracture concern, tendon injury, open wound, infection, or neurovascular compromise.

## Exclusions

- Fracture or dislocation concern, tendon injury, open wound, infection, neurovascular compromise, high-energy trauma, or specialist-directed hand plan.

## Must-Not-Miss Diagnoses

- Hand fracture.
- Tendon injury.
- Neurovascular compromise.
- Deep hand infection.

## Primitive List

- `palm_contusion_uncomplicated_no_fracture_or_tendon_red_flags.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `palm_contusion_uncomplicated_no_fracture_or_tendon_red_flags.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, hand_tendon_risk, open_wound, septic_joint_or_infection_concern, neurovascular_compromise, high_energy_trauma, specialist_directed_orthopedic_plan
- `palm_contusion_uncomplicated_no_fracture_or_tendon_red_flags.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `palm_contusion_uncomplicated_no_fracture_or_tendon_red_flags.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `palm_contusion_uncomplicated_no_fracture_or_tendon_red_flags.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `palm_contusion_uncomplicated_no_fracture_or_tendon_red_flags.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, hand_tendon_risk, open_wound, septic_joint_or_infection_concern, neurovascular_compromise, high_energy_trauma, specialist_directed_orthopedic_plan
- `palm_contusion_uncomplicated_no_fracture_or_tendon_red_flags.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, hand_tendon_risk, open_wound, septic_joint_or_infection_concern, neurovascular_compromise, high_energy_trauma, specialist_directed_orthopedic_plan
- `palm_contusion_uncomplicated_no_fracture_or_tendon_red_flags.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `palm_contusion_uncomplicated_no_fracture_or_tendon_red_flags.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `palm_contusion_uncomplicated_no_fracture_or_tendon_red_flags.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `palm_contusion_uncomplicated_no_fracture_or_tendon_red_flags.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, hand_tendon_risk, open_wound, septic_joint_or_infection_concern, neurovascular_compromise, high_energy_trauma, specialist_directed_orthopedic_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit a palm bruise.

WHAT WE FOUND:
Your clinician diagnosed a palm bruise. We did not find signs of fracture, tendon injury, infection, or poor blood flow today.

WHAT TO DO AT HOME:
- Rest the hand as needed.
- Use ice wrapped in a cloth for short periods.
- Keep the hand elevated when swelling is present.

MEDICATIONS:
- Use acetaminophen or ibuprofen only if you can take it safely and follow the label.
- Use medicines only as prescribed or recommended.

RETURN TO ED IF:
- New numbness, weakness, blue or pale fingers, or trouble moving the fingers.
- Worsening pain, swelling, spreading redness, pus, or fever.
- Symptoms that worsen or do not improve as expected.

FOLLOW UP:
Follow up with primary care, hand clinic, urgent care, or the ED if symptoms are not improving or your clinician told you to recheck.
```
