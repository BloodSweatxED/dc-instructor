# Shoulder overuse tendinitis without rupture or neurovascular red flags

Phenotype ID: `shoulder_overuse_tendinitis_no_rupture_or_neurovascular_red_flags`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of uncomplicated shoulder tendinitis/overuse strain.
- No tendon rupture, fracture/dislocation concern, septic joint/infection concern, neurovascular compromise, high-energy trauma, pregnancy/pediatric pathway, or specialist-directed plan.

## Exclusions

- Tendon rupture, fracture/dislocation concern, acute traumatic mechanism with instability, septic joint/infection concern, red hot joint, open wound, neurovascular compromise, severe pain, or inability to use the arm.
- Pregnancy/pediatric pathway or specialist-directed orthopedic plan.

## Must-Not-Miss Diagnoses

- Rotator cuff rupture.
- Fracture or dislocation.
- Septic joint.
- Neurovascular compromise.
- Referred cardiac pain when presentation is not clearly shoulder overuse.

## Primitive List

- `shoulder_overuse_tendinitis_no_rupture_or_neurovascular_red_flags.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `shoulder_overuse_tendinitis_no_rupture_or_neurovascular_red_flags.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: tendon_or_ligament_rupture_concern, fracture_or_dislocation_concern, septic_joint_or_infection_concern, open_wound, neurovascular_compromise, severe_pain, unable_to_use_limb, high_energy_trauma, cardiac_or_pe_chest_pain_concern, pregnancy, pediatric_pathway, specialist_directed_orthopedic_plan
- `shoulder_overuse_tendinitis_no_rupture_or_neurovascular_red_flags.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `shoulder_overuse_tendinitis_no_rupture_or_neurovascular_red_flags.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `shoulder_overuse_tendinitis_no_rupture_or_neurovascular_red_flags.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `shoulder_overuse_tendinitis_no_rupture_or_neurovascular_red_flags.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: tendon_or_ligament_rupture_concern, fracture_or_dislocation_concern, septic_joint_or_infection_concern, open_wound, neurovascular_compromise, severe_pain, unable_to_use_limb, high_energy_trauma, cardiac_or_pe_chest_pain_concern, pregnancy, pediatric_pathway, specialist_directed_orthopedic_plan
- `shoulder_overuse_tendinitis_no_rupture_or_neurovascular_red_flags.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: tendon_or_ligament_rupture_concern, fracture_or_dislocation_concern, septic_joint_or_infection_concern, open_wound, neurovascular_compromise, severe_pain, unable_to_use_limb, high_energy_trauma, cardiac_or_pe_chest_pain_concern, pregnancy, pediatric_pathway, specialist_directed_orthopedic_plan
- `shoulder_overuse_tendinitis_no_rupture_or_neurovascular_red_flags.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `shoulder_overuse_tendinitis_no_rupture_or_neurovascular_red_flags.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `shoulder_overuse_tendinitis_no_rupture_or_neurovascular_red_flags.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `shoulder_overuse_tendinitis_no_rupture_or_neurovascular_red_flags.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: tendon_or_ligament_rupture_concern, fracture_or_dislocation_concern, septic_joint_or_infection_concern, open_wound, neurovascular_compromise, severe_pain, unable_to_use_limb, high_energy_trauma, cardiac_or_pe_chest_pain_concern, pregnancy, pediatric_pathway, specialist_directed_orthopedic_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit shoulder tendinitis or an overuse shoulder strain.

WHAT WE FOUND:
Your clinician diagnosed uncomplicated shoulder tendinitis or overuse strain. We did not find tendon rupture, fracture, dislocation, infection, neurovascular compromise, or another emergency problem today.

WHAT TO DO AT HOME:
- Rest from lifting or overhead activity that worsens pain.
- Use ice, heat, a sling, stretching, or activity changes only as instructed.
- Return to activity gradually as pain and motion improve.

MEDICATIONS:
- Use pain medicine only if prescribed or recommended, and follow the label.
- Avoid medicines your clinician told you to avoid.

RETURN TO ED IF:
- New weakness, numbness, color change, severe pain, or inability to use the arm.
- Fever, red hot joint, spreading redness, or feeling very ill.
- New trauma, deformity, or symptoms not improving.

FOLLOW UP:
Follow up with primary care, sports medicine, physical therapy, or orthopedics if pain, motion, or strength is not improving.
```
