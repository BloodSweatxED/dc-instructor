# Ankle tendinitis without rupture or infection red flags

Phenotype ID: `ankle_tendinitis_uncomplicated_no_rupture_or_infection`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of uncomplicated ankle tendinitis.
- No fracture concern, tendon rupture concern, infection, or neurovascular compromise.

## Exclusions

- Fracture or dislocation concern, tendon rupture concern, open wound, infection, neurovascular compromise, inability to bear weight, diabetic-foot pathway, or specialist-directed orthopedic/podiatry plan.

## Must-Not-Miss Diagnoses

- Ankle fracture.
- Achilles or other tendon rupture.
- Septic joint or infection.
- Neurovascular compromise.

## Primitive List

- `ankle_tendinitis_uncomplicated_no_rupture_or_infection.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `ankle_tendinitis_uncomplicated_no_rupture_or_infection.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, tendon_or_ligament_rupture_concern, open_wound, septic_joint_or_infection_concern, neurovascular_compromise, unable_to_bear_weight_lower_extremity, diabetic_foot, specialist_directed_orthopedic_plan, specialist_directed_podiatry_plan
- `ankle_tendinitis_uncomplicated_no_rupture_or_infection.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `ankle_tendinitis_uncomplicated_no_rupture_or_infection.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `ankle_tendinitis_uncomplicated_no_rupture_or_infection.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `ankle_tendinitis_uncomplicated_no_rupture_or_infection.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, tendon_or_ligament_rupture_concern, open_wound, septic_joint_or_infection_concern, neurovascular_compromise, unable_to_bear_weight_lower_extremity, diabetic_foot, specialist_directed_orthopedic_plan, specialist_directed_podiatry_plan
- `ankle_tendinitis_uncomplicated_no_rupture_or_infection.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, tendon_or_ligament_rupture_concern, open_wound, septic_joint_or_infection_concern, neurovascular_compromise, unable_to_bear_weight_lower_extremity, diabetic_foot, specialist_directed_orthopedic_plan, specialist_directed_podiatry_plan
- `ankle_tendinitis_uncomplicated_no_rupture_or_infection.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `ankle_tendinitis_uncomplicated_no_rupture_or_infection.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `ankle_tendinitis_uncomplicated_no_rupture_or_infection.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `ankle_tendinitis_uncomplicated_no_rupture_or_infection.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, tendon_or_ligament_rupture_concern, open_wound, septic_joint_or_infection_concern, neurovascular_compromise, unable_to_bear_weight_lower_extremity, diabetic_foot, specialist_directed_orthopedic_plan, specialist_directed_podiatry_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit ankle tendinitis.

WHAT WE FOUND:
Your clinician diagnosed ankle tendinitis. We did not find signs of fracture, tendon rupture, infection, or poor blood flow today.

WHAT TO DO AT HOME:
- Rest the ankle as needed.
- Use ice wrapped in a cloth for short periods.
- Return to activity gradually as pain improves.

MEDICATIONS:
- Use acetaminophen or ibuprofen only if you can take it safely and follow the label.
- Use medicines only as prescribed or recommended.

RETURN TO ED IF:
- New numbness, blue or pale toes, inability to walk, or severe worsening pain.
- Fever, spreading redness, major swelling, or concern for infection.
- Symptoms that worsen or do not improve as expected.

FOLLOW UP:
Follow up with primary care, orthopedics, podiatry, urgent care, or the ED if symptoms are not improving or your clinician told you to recheck.
```
