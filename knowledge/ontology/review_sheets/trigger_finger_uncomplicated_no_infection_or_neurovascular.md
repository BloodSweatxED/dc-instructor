# Uncomplicated trigger finger without infection or neurovascular symptoms

Phenotype ID: `trigger_finger_uncomplicated_no_infection_or_neurovascular`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of uncomplicated trigger finger/thumb.
- No infection, open wound, tendon rupture, neurovascular compromise, trauma/fracture concern, pregnancy/pediatric pathway, or specialist-directed plan.

## Exclusions

- Infection, open wound, flexor tenosynovitis concern, tendon rupture, neurovascular compromise, fracture/dislocation concern, severe pain, or inability to move the finger.
- Pregnancy/pediatric pathway or specialist-directed hand/orthopedic plan.

## Must-Not-Miss Diagnoses

- Flexor tenosynovitis.
- Tendon rupture.
- Fracture or dislocation.
- Neurovascular compromise.
- Cellulitis or abscess.

## Primitive List

- `trigger_finger_uncomplicated_no_infection_or_neurovascular.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `trigger_finger_uncomplicated_no_infection_or_neurovascular.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: secondary_skin_infection_concern, open_wound, flexor_tenosynovitis_concern, tendon_or_ligament_rupture_concern, neurovascular_compromise, fracture_or_dislocation_concern, severe_pain, unable_to_use_limb, pregnancy, pediatric_pathway, specialist_directed_orthopedic_plan
- `trigger_finger_uncomplicated_no_infection_or_neurovascular.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `trigger_finger_uncomplicated_no_infection_or_neurovascular.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `trigger_finger_uncomplicated_no_infection_or_neurovascular.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `trigger_finger_uncomplicated_no_infection_or_neurovascular.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: secondary_skin_infection_concern, open_wound, flexor_tenosynovitis_concern, tendon_or_ligament_rupture_concern, neurovascular_compromise, fracture_or_dislocation_concern, severe_pain, unable_to_use_limb, pregnancy, pediatric_pathway, specialist_directed_orthopedic_plan
- `trigger_finger_uncomplicated_no_infection_or_neurovascular.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: secondary_skin_infection_concern, open_wound, flexor_tenosynovitis_concern, tendon_or_ligament_rupture_concern, neurovascular_compromise, fracture_or_dislocation_concern, severe_pain, unable_to_use_limb, pregnancy, pediatric_pathway, specialist_directed_orthopedic_plan
- `trigger_finger_uncomplicated_no_infection_or_neurovascular.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `trigger_finger_uncomplicated_no_infection_or_neurovascular.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `trigger_finger_uncomplicated_no_infection_or_neurovascular.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `trigger_finger_uncomplicated_no_infection_or_neurovascular.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: secondary_skin_infection_concern, open_wound, flexor_tenosynovitis_concern, tendon_or_ligament_rupture_concern, neurovascular_compromise, fracture_or_dislocation_concern, severe_pain, unable_to_use_limb, pregnancy, pediatric_pathway, specialist_directed_orthopedic_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit trigger finger, where a finger or thumb catches or locks with movement.

WHAT WE FOUND:
Your clinician diagnosed uncomplicated trigger finger. We did not find infection, tendon rupture, neurovascular compromise, trauma, or another emergency problem today.

WHAT TO DO AT HOME:
- Rest from gripping or repetitive activity that worsens symptoms.
- Use a splint or activity changes only as instructed.
- Do not force the finger if it locks painfully.

MEDICATIONS:
- Use pain medicine only if prescribed or recommended, and follow the label.
- Avoid medicines your clinician told you to avoid.

RETURN TO ED IF:
- New numbness, weakness, color change, severe pain, or inability to move the finger.
- Fever, spreading redness, warmth, pus, or red streaks.
- New injury, tendon rupture concern, or symptoms not improving.

FOLLOW UP:
Follow up with primary care, sports medicine, orthopedics, or hand surgery if symptoms persist or function is limited.
```
