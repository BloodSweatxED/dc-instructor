# Hip bursitis without septic-joint or trauma red flags

Phenotype ID: `hip_bursitis_uncomplicated_no_septic_joint_or_trauma`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of uncomplicated hip bursitis.
- No septic joint concern, skin infection, fracture/dislocation concern, neurovascular compromise, inability to bear weight, high-energy trauma, pregnancy/pediatric pathway, or specialist-directed plan.

## Exclusions

- Septic joint or infection concern, cellulitis, open wound, fracture/dislocation concern, neurovascular compromise, inability to bear weight, severe or rapidly worsening pain, high-energy trauma, immunocompromised host, pregnancy/pediatric pathway, or specialist-directed orthopedic plan.

## Must-Not-Miss Diagnoses

- Septic arthritis.
- Hip fracture or dislocation.
- Cellulitis or deep infection.
- Neurovascular compromise.

## Primitive List

- `hip_bursitis_uncomplicated_no_septic_joint_or_trauma.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `hip_bursitis_uncomplicated_no_septic_joint_or_trauma.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: septic_joint_or_infection_concern, secondary_skin_infection_concern, open_wound, systemic_illness, fracture_or_dislocation_concern, neurovascular_compromise, unable_to_bear_weight_lower_extremity, severe_pain, high_energy_trauma, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_orthopedic_plan
- `hip_bursitis_uncomplicated_no_septic_joint_or_trauma.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `hip_bursitis_uncomplicated_no_septic_joint_or_trauma.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `hip_bursitis_uncomplicated_no_septic_joint_or_trauma.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `hip_bursitis_uncomplicated_no_septic_joint_or_trauma.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: septic_joint_or_infection_concern, secondary_skin_infection_concern, open_wound, systemic_illness, fracture_or_dislocation_concern, neurovascular_compromise, unable_to_bear_weight_lower_extremity, severe_pain, high_energy_trauma, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_orthopedic_plan
- `hip_bursitis_uncomplicated_no_septic_joint_or_trauma.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: septic_joint_or_infection_concern, secondary_skin_infection_concern, open_wound, systemic_illness, fracture_or_dislocation_concern, neurovascular_compromise, unable_to_bear_weight_lower_extremity, severe_pain, high_energy_trauma, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_orthopedic_plan
- `hip_bursitis_uncomplicated_no_septic_joint_or_trauma.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `hip_bursitis_uncomplicated_no_septic_joint_or_trauma.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `hip_bursitis_uncomplicated_no_septic_joint_or_trauma.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `hip_bursitis_uncomplicated_no_septic_joint_or_trauma.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: septic_joint_or_infection_concern, secondary_skin_infection_concern, open_wound, systemic_illness, fracture_or_dislocation_concern, neurovascular_compromise, unable_to_bear_weight_lower_extremity, severe_pain, high_energy_trauma, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_orthopedic_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit uncomplicated hip bursitis.

WHAT WE FOUND:
Your clinician diagnosed hip bursitis. We did not find septic joint concern, fracture or dislocation concern, infection, poor blood flow, or another hip emergency today.

WHAT TO DO AT HOME:
- Rest the hip from activity that makes pain worse.
- Use ice, heat, gentle motion, support, or activity limits only as your clinician recommended.
- Return to normal activity gradually as symptoms improve.

MEDICATIONS:
- Use pain medicine only if prescribed or recommended, and follow the label.
- Do not use medicine to push through worsening pain, fever, weakness, or trouble walking.

RETURN TO ED IF:
- Fever, a red hot joint, rapidly worsening swelling, severe pain, or feeling very ill.
- New leg numbness, weakness, blue or pale foot, inability to walk, deformity, or a new injury.
- Symptoms that worsen or do not improve as expected.

FOLLOW UP:
Follow up with primary care, sports medicine, orthopedics, therapy, urgent care, or the ED if symptoms are not improving or your clinician told you to recheck.
```
