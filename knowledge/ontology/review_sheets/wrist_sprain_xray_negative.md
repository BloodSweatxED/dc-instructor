# Wrist sprain with negative x-ray

Phenotype ID: `wrist_sprain_xray_negative`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of wrist sprain or strain.
- X-ray was performed and documented negative for fracture.
- Neurovascular exam documented intact.
- Clinician documented no scaphoid tenderness or snuffbox tenderness concern.

## Exclusions

- No x-ray performed, positive fracture, dislocation, open wound, high-energy trauma, crush injury, or FOOSH with scaphoid concern.
- Scaphoid tenderness pattern, suspected tendon or ligament rupture, compartment syndrome concern, septic joint or infection concern, neurovascular compromise, or specialist-directed orthopedic plan.
- Pediatric growth plate pathway, elderly/osteoporotic high-risk wrist injury, or hand tendon risk.

## Must-Not-Miss Diagnoses

- Occult scaphoid fracture.
- Other occult wrist fracture.
- Dislocation.
- Tendon rupture.
- Compartment syndrome.
- Septic joint.

## Primitive List

- `wrist_sprain_xray_negative.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `wrist_sprain_xray_negative.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: no_xray_performed, fracture_seen, dislocation, open_wound, open_fracture, high_energy_trauma, crush_injury, foosh_scaphoid_risk, neurovascular_compromise, tendon_or_ligament_rupture_concern, scaphoid_tenderness_pattern, compartment_syndrome_concern, septic_joint_or_infection_concern, pediatric_growth_plate_pathway, elderly_osteoporotic_high_risk_msk, hand_tendon_risk, specialist_directed_orthopedic_plan
- `wrist_sprain_xray_negative.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `wrist_sprain_xray_negative.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `wrist_sprain_xray_negative.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `wrist_sprain_xray_negative.home_care.home_care_4.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `wrist_sprain_xray_negative.home_care.home_care_5.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `wrist_sprain_xray_negative.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: no_xray_performed, fracture_seen, dislocation, open_wound, open_fracture, high_energy_trauma, crush_injury, foosh_scaphoid_risk, neurovascular_compromise, tendon_or_ligament_rupture_concern, scaphoid_tenderness_pattern, compartment_syndrome_concern, septic_joint_or_infection_concern, pediatric_growth_plate_pathway, elderly_osteoporotic_high_risk_msk, hand_tendon_risk, specialist_directed_orthopedic_plan
- `wrist_sprain_xray_negative.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: no_xray_performed, fracture_seen, dislocation, open_wound, open_fracture, high_energy_trauma, crush_injury, foosh_scaphoid_risk, neurovascular_compromise, tendon_or_ligament_rupture_concern, scaphoid_tenderness_pattern, compartment_syndrome_concern, septic_joint_or_infection_concern, pediatric_growth_plate_pathway, elderly_osteoporotic_high_risk_msk, hand_tendon_risk, specialist_directed_orthopedic_plan
- `wrist_sprain_xray_negative.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `wrist_sprain_xray_negative.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `wrist_sprain_xray_negative.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `wrist_sprain_xray_negative.return_precautions.return_precaution_4.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `wrist_sprain_xray_negative.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: no_xray_performed, fracture_seen, dislocation, open_wound, open_fracture, high_energy_trauma, crush_injury, foosh_scaphoid_risk, neurovascular_compromise, tendon_or_ligament_rupture_concern, scaphoid_tenderness_pattern, compartment_syndrome_concern, septic_joint_or_infection_concern, pediatric_growth_plate_pathway, elderly_osteoporotic_high_risk_msk, hand_tendon_risk, specialist_directed_orthopedic_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your clinician diagnosed a wrist sprain. Your x-ray did not show a fracture.

WHAT WE FOUND:
Your x-ray did not show a broken bone. Your clinician checked the blood flow, feeling, and movement in your hand and fingers and they were normal. Your clinician also checked specific areas of your wrist for signs of a deeper injury and did not find any.

WHAT TO DO AT HOME:
- Protect your wrist with the splint, wrap, or activity limits your clinician gave you.
- Rest from painful gripping, lifting, or pushing at first, then slowly return to normal movement as symptoms allow.
- Raise the wrist when you can, especially while swelling is present.
- Minor wrist sprains may improve over several days. Moderate injuries often take several weeks and need follow-up.
- If your pain and swelling are not improving within 3 to 5 days, do not wait for your scheduled follow-up. Go sooner.

MEDICATIONS:
- Use only the medicines your clinician prescribed or said are safe for you.
- Do not take extra doses or combine medicines unless your clinician told you to.

RETURN TO ED IF:
- New numbness, weakness, color change, coldness, or trouble moving the hand or fingers.
- Pain at the base of your thumb or along the thumb side of your wrist that is getting worse, not better.
- Worsening pain out of proportion, tight or hard swelling, or pain that does not improve with rest and elevation.
- Fever, redness, warmth, pus, or severe pain with movement.

FOLLOW UP:
See your doctor, urgent care, sports medicine, or orthopedics in 5 to 7 days. Wrist injuries can sometimes hide a small fracture that does not show up on the first x-ray. A follow-up visit confirms your wrist is healing the way it should. Go sooner if your clinician gave you a specific plan or if your pain is getting worse.
```
