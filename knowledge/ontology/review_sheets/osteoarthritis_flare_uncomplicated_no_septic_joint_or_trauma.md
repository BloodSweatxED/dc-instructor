# Uncomplicated osteoarthritis flare without septic-joint or trauma concern

Phenotype ID: `osteoarthritis_flare_uncomplicated_no_septic_joint_or_trauma`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of uncomplicated osteoarthritis flare.
- No septic joint/infection concern, trauma/fracture concern, neurovascular compromise, inability to use limb, high-risk host, pregnancy/pediatric pathway, or specialist-directed plan.

## Exclusions

- Septic joint concern, fever, red hot joint, cellulitis, open wound, fracture/dislocation concern, neurovascular compromise, inability to use limb, severe pain, or high-energy trauma.
- Immunocompromised host, pregnancy/pediatric pathway, or specialist-directed orthopedic/rheumatology plan.

## Must-Not-Miss Diagnoses

- Septic joint.
- Fracture or dislocation.
- Neurovascular compromise.
- Cellulitis.
- Inflammatory arthritis emergency mimic.

## Primitive List

- `osteoarthritis_flare_uncomplicated_no_septic_joint_or_trauma.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `osteoarthritis_flare_uncomplicated_no_septic_joint_or_trauma.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: septic_joint_or_infection_concern, secondary_skin_infection_concern, open_wound, fracture_or_dislocation_concern, neurovascular_compromise, unable_to_use_limb, unable_to_bear_weight_lower_extremity, severe_pain, high_energy_trauma, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_orthopedic_plan
- `osteoarthritis_flare_uncomplicated_no_septic_joint_or_trauma.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `osteoarthritis_flare_uncomplicated_no_septic_joint_or_trauma.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `osteoarthritis_flare_uncomplicated_no_septic_joint_or_trauma.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `osteoarthritis_flare_uncomplicated_no_septic_joint_or_trauma.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: septic_joint_or_infection_concern, secondary_skin_infection_concern, open_wound, fracture_or_dislocation_concern, neurovascular_compromise, unable_to_use_limb, unable_to_bear_weight_lower_extremity, severe_pain, high_energy_trauma, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_orthopedic_plan
- `osteoarthritis_flare_uncomplicated_no_septic_joint_or_trauma.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: septic_joint_or_infection_concern, secondary_skin_infection_concern, open_wound, fracture_or_dislocation_concern, neurovascular_compromise, unable_to_use_limb, unable_to_bear_weight_lower_extremity, severe_pain, high_energy_trauma, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_orthopedic_plan
- `osteoarthritis_flare_uncomplicated_no_septic_joint_or_trauma.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `osteoarthritis_flare_uncomplicated_no_septic_joint_or_trauma.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `osteoarthritis_flare_uncomplicated_no_septic_joint_or_trauma.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `osteoarthritis_flare_uncomplicated_no_septic_joint_or_trauma.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: septic_joint_or_infection_concern, secondary_skin_infection_concern, open_wound, fracture_or_dislocation_concern, neurovascular_compromise, unable_to_use_limb, unable_to_bear_weight_lower_extremity, severe_pain, high_energy_trauma, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_orthopedic_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit an osteoarthritis flare.

WHAT WE FOUND:
Your clinician diagnosed an uncomplicated osteoarthritis flare. We did not find septic joint concern, trauma, neurovascular compromise, or another emergency problem today.

WHAT TO DO AT HOME:
- Rest from activities that worsen pain.
- Use heat, ice, supports, or activity changes only as instructed.
- Return to usual activity gradually as symptoms improve.

MEDICATIONS:
- Use pain medicine only if prescribed or recommended, and follow the label.
- Avoid medicines your clinician told you to avoid.

RETURN TO ED IF:
- Fever, red hot joint, spreading redness, or feeling very ill.
- New injury, severe worsening pain, inability to use the limb, or inability to walk.
- New numbness, weakness, cold/blue limb, or symptoms not improving.

FOLLOW UP:
Follow up with primary care, rheumatology, sports medicine, or orthopedics if pain or function is not improving.
```
