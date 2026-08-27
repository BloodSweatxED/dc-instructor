# Uncomplicated bursitis without septic-joint or trauma concern

Phenotype ID: `bursitis_uncomplicated_no_septic_joint_or_trauma`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of uncomplicated bursitis.
- No septic joint or infection concern, open wound, trauma/fracture concern, neurovascular compromise, inability to use limb, high-risk host, pregnancy/pediatric pathway, or specialist-directed plan.

## Exclusions

- Septic joint concern, red/hot joint, fever, cellulitis, abscess, open wound, systemic illness, fracture/dislocation concern, neurovascular compromise, inability to use limb, severe pain, or high-energy trauma.
- Immunocompromised host, pregnancy/pediatric pathway, or specialist-directed orthopedic plan.

## Must-Not-Miss Diagnoses

- Septic joint.
- Septic bursitis.
- Fracture or dislocation.
- Neurovascular compromise.
- Cellulitis or abscess.

## Primitive List

- `bursitis_uncomplicated_no_septic_joint_or_trauma.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `bursitis_uncomplicated_no_septic_joint_or_trauma.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: septic_joint_or_infection_concern, secondary_skin_infection_concern, open_wound, systemic_illness, fracture_or_dislocation_concern, neurovascular_compromise, unable_to_use_limb, severe_pain, high_energy_trauma, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_orthopedic_plan
- `bursitis_uncomplicated_no_septic_joint_or_trauma.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `bursitis_uncomplicated_no_septic_joint_or_trauma.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `bursitis_uncomplicated_no_septic_joint_or_trauma.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `bursitis_uncomplicated_no_septic_joint_or_trauma.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: septic_joint_or_infection_concern, secondary_skin_infection_concern, open_wound, systemic_illness, fracture_or_dislocation_concern, neurovascular_compromise, unable_to_use_limb, severe_pain, high_energy_trauma, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_orthopedic_plan
- `bursitis_uncomplicated_no_septic_joint_or_trauma.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: septic_joint_or_infection_concern, secondary_skin_infection_concern, open_wound, systemic_illness, fracture_or_dislocation_concern, neurovascular_compromise, unable_to_use_limb, severe_pain, high_energy_trauma, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_orthopedic_plan
- `bursitis_uncomplicated_no_septic_joint_or_trauma.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `bursitis_uncomplicated_no_septic_joint_or_trauma.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `bursitis_uncomplicated_no_septic_joint_or_trauma.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `bursitis_uncomplicated_no_septic_joint_or_trauma.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: septic_joint_or_infection_concern, secondary_skin_infection_concern, open_wound, systemic_illness, fracture_or_dislocation_concern, neurovascular_compromise, unable_to_use_limb, severe_pain, high_energy_trauma, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_orthopedic_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit bursitis, irritation or inflammation of a cushion near a joint.

WHAT WE FOUND:
Your clinician diagnosed uncomplicated bursitis. We did not find septic joint concern, infection, trauma, neurovascular compromise, or another emergency problem today.

WHAT TO DO AT HOME:
- Rest the area from activities or pressure that worsen pain.
- Use padding, ice, or support only as instructed.
- Return to activity gradually as symptoms improve.

MEDICATIONS:
- Use pain medicine only if prescribed or recommended, and follow the label.
- Take antibiotics only if your clinician prescribed them for a separate reason.

RETURN TO ED IF:
- Fever, spreading redness, warmth, pus, red streaks, or feeling very ill.
- Severe worsening joint pain, inability to move the joint, new injury, or inability to use the limb.
- New numbness, weakness, color change, or symptoms not improving with the plan.

FOLLOW UP:
Follow up with primary care, sports medicine, occupational health, or orthopedics if swelling or function is not improving.
```
