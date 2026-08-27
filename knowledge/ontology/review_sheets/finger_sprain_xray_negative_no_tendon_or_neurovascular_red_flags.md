# Finger sprain with negative x-ray and no tendon or neurovascular red flags

Phenotype ID: `finger_sprain_xray_negative_no_tendon_or_neurovascular_red_flags`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of finger sprain/strain.
- X-ray performed and negative, with intact neurovascular exam and no tendon injury, open wound, infection, high-risk mechanism, pregnancy/pediatric pathway, or specialist-directed plan.

## Exclusions

- Fracture or dislocation concern, tendon rupture, open wound, infection, flexor tenosynovitis concern, neurovascular compromise, severe pain, inability to move the finger, high-energy trauma, or crush injury.
- Pregnancy/pediatric pathway or specialist-directed hand/orthopedic plan.

## Must-Not-Miss Diagnoses

- Fracture or dislocation.
- Tendon rupture.
- Flexor tenosynovitis.
- Neurovascular compromise.
- Compartment syndrome.

## Primitive List

- `finger_sprain_xray_negative_no_tendon_or_neurovascular_red_flags.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `finger_sprain_xray_negative_no_tendon_or_neurovascular_red_flags.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, tendon_or_ligament_rupture_concern, open_wound, secondary_skin_infection_concern, flexor_tenosynovitis_concern, neurovascular_compromise, severe_pain, unable_to_use_limb, high_energy_trauma, crush_injury, pregnancy, pediatric_pathway, specialist_directed_orthopedic_plan
- `finger_sprain_xray_negative_no_tendon_or_neurovascular_red_flags.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `finger_sprain_xray_negative_no_tendon_or_neurovascular_red_flags.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `finger_sprain_xray_negative_no_tendon_or_neurovascular_red_flags.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `finger_sprain_xray_negative_no_tendon_or_neurovascular_red_flags.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, tendon_or_ligament_rupture_concern, open_wound, secondary_skin_infection_concern, flexor_tenosynovitis_concern, neurovascular_compromise, severe_pain, unable_to_use_limb, high_energy_trauma, crush_injury, pregnancy, pediatric_pathway, specialist_directed_orthopedic_plan
- `finger_sprain_xray_negative_no_tendon_or_neurovascular_red_flags.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, tendon_or_ligament_rupture_concern, open_wound, secondary_skin_infection_concern, flexor_tenosynovitis_concern, neurovascular_compromise, severe_pain, unable_to_use_limb, high_energy_trauma, crush_injury, pregnancy, pediatric_pathway, specialist_directed_orthopedic_plan
- `finger_sprain_xray_negative_no_tendon_or_neurovascular_red_flags.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `finger_sprain_xray_negative_no_tendon_or_neurovascular_red_flags.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `finger_sprain_xray_negative_no_tendon_or_neurovascular_red_flags.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `finger_sprain_xray_negative_no_tendon_or_neurovascular_red_flags.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, tendon_or_ligament_rupture_concern, open_wound, secondary_skin_infection_concern, flexor_tenosynovitis_concern, neurovascular_compromise, severe_pain, unable_to_use_limb, high_energy_trauma, crush_injury, pregnancy, pediatric_pathway, specialist_directed_orthopedic_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit a finger sprain.

WHAT WE FOUND:
Your clinician diagnosed a finger sprain. Your x-ray did not show a fracture, and we did not find tendon injury, infection, neurovascular compromise, or another emergency problem today.

WHAT TO DO AT HOME:
- Rest the finger from painful gripping or impact.
- Use splinting, buddy taping, ice, elevation, or activity changes only as instructed.
- Move the finger only in the way your clinician said is safe.

MEDICATIONS:
- Use pain medicine only if prescribed or recommended, and follow the label.
- Avoid medicines your clinician told you to avoid.

RETURN TO ED IF:
- New numbness, weakness, color change, severe pain, or inability to move the finger.
- Fever, spreading redness, warmth, pus, or red streaks.
- Worsening swelling, new deformity, or pain that is not improving.

FOLLOW UP:
Follow up with primary care, sports medicine, orthopedics, or hand surgery if pain, swelling, or motion is not improving.
```
