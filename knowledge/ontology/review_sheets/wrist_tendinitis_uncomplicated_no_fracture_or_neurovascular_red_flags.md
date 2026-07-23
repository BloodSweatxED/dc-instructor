# Uncomplicated wrist tendinitis without fracture or neurovascular red flags

Phenotype ID: `wrist_tendinitis_uncomplicated_no_fracture_or_neurovascular_red_flags`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of uncomplicated wrist tendinitis/overuse strain.
- No fracture/dislocation concern, tendon rupture, flexor tenosynovitis concern, open wound, infection, neurovascular compromise, pregnancy/pediatric pathway, or specialist-directed plan.

## Exclusions

- Fracture/dislocation concern, FOOSH/scaphoid risk, tendon rupture, flexor tenosynovitis concern, open wound, infection, neurovascular compromise, severe pain, inability to use the hand, high-energy trauma, or crush injury.
- Pregnancy/pediatric pathway or specialist-directed hand/orthopedic plan.

## Must-Not-Miss Diagnoses

- Scaphoid fracture.
- Fracture or dislocation.
- Flexor tenosynovitis.
- Tendon rupture.
- Neurovascular compromise.

## Primitive List

- `wrist_tendinitis_uncomplicated_no_fracture_or_neurovascular_red_flags.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `wrist_tendinitis_uncomplicated_no_fracture_or_neurovascular_red_flags.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, foosh_scaphoid_risk, tendon_or_ligament_rupture_concern, flexor_tenosynovitis_concern, open_wound, secondary_skin_infection_concern, neurovascular_compromise, severe_pain, unable_to_use_limb, high_energy_trauma, crush_injury, pregnancy, pediatric_pathway, specialist_directed_orthopedic_plan
- `wrist_tendinitis_uncomplicated_no_fracture_or_neurovascular_red_flags.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `wrist_tendinitis_uncomplicated_no_fracture_or_neurovascular_red_flags.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `wrist_tendinitis_uncomplicated_no_fracture_or_neurovascular_red_flags.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `wrist_tendinitis_uncomplicated_no_fracture_or_neurovascular_red_flags.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, foosh_scaphoid_risk, tendon_or_ligament_rupture_concern, flexor_tenosynovitis_concern, open_wound, secondary_skin_infection_concern, neurovascular_compromise, severe_pain, unable_to_use_limb, high_energy_trauma, crush_injury, pregnancy, pediatric_pathway, specialist_directed_orthopedic_plan
- `wrist_tendinitis_uncomplicated_no_fracture_or_neurovascular_red_flags.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, foosh_scaphoid_risk, tendon_or_ligament_rupture_concern, flexor_tenosynovitis_concern, open_wound, secondary_skin_infection_concern, neurovascular_compromise, severe_pain, unable_to_use_limb, high_energy_trauma, crush_injury, pregnancy, pediatric_pathway, specialist_directed_orthopedic_plan
- `wrist_tendinitis_uncomplicated_no_fracture_or_neurovascular_red_flags.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `wrist_tendinitis_uncomplicated_no_fracture_or_neurovascular_red_flags.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `wrist_tendinitis_uncomplicated_no_fracture_or_neurovascular_red_flags.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `wrist_tendinitis_uncomplicated_no_fracture_or_neurovascular_red_flags.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, foosh_scaphoid_risk, tendon_or_ligament_rupture_concern, flexor_tenosynovitis_concern, open_wound, secondary_skin_infection_concern, neurovascular_compromise, severe_pain, unable_to_use_limb, high_energy_trauma, crush_injury, pregnancy, pediatric_pathway, specialist_directed_orthopedic_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit wrist tendinitis or an overuse wrist strain.

WHAT WE FOUND:
Your clinician diagnosed uncomplicated wrist tendinitis or overuse strain. We did not find fracture, tendon rupture, infection, neurovascular compromise, or another emergency problem today.

WHAT TO DO AT HOME:
- Rest from gripping or repetitive activity that worsens symptoms.
- Use a splint, ice, heat, stretching, or activity changes only as instructed.
- Return to activity gradually as symptoms improve.

MEDICATIONS:
- Use pain medicine only if prescribed or recommended, and follow the label.
- Avoid medicines your clinician told you to avoid.

RETURN TO ED IF:
- New numbness, weakness, color change, severe pain, or inability to use the hand.
- Fever, spreading redness, warmth, pus, or red streaks.
- New trauma, deformity, worsening swelling, or symptoms not improving.

FOLLOW UP:
Follow up with primary care, sports medicine, physical therapy, orthopedics, or hand surgery if pain, motion, or function is not improving.
```
