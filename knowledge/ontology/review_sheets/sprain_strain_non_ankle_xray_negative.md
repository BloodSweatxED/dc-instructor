# Deprecated broad non-ankle sprain or strain with negative x-ray

Phenotype ID: `sprain_strain_non_ankle_xray_negative`

Status: `retired`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of sprain or strain outside the ankle pathway.
- X-ray was performed and documented negative for fracture.
- Neurovascular exam documented intact.
- No suspected ligament rupture, tendon rupture, occult fracture pattern, septic joint, compartment syndrome, inability to bear weight for lower-extremity sites, or high-risk site modifier.

## Exclusions

- Ankle sprain pathway, no x-ray performed, positive fracture, dislocation, open wound, open fracture, high-energy trauma, or crush injury.
- Suspected tendon rupture, ligament rupture, scaphoid tenderness pattern, compartment syndrome concern, septic joint or infection concern, neurovascular compromise, or specialist-directed orthopedic plan.
- Inability to bear weight for lower-extremity injuries, elbow or foot sprain/strain sites pending separate v1 review, pediatric growth plate pathway, or elderly/osteoporotic high-risk knee, shoulder, or wrist injury.

## Must-Not-Miss Diagnoses

- Occult fracture.
- Dislocation.
- Tendon rupture.
- Ligament rupture requiring urgent follow-up.
- Septic joint.
- Compartment syndrome.
- Scaphoid fracture.

## Primitive List

- `sprain_strain_non_ankle_xray_negative.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `sprain_strain_non_ankle_xray_negative.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: ankle_sprain_pathway, no_xray_performed, fracture_seen, dislocation, open_wound, open_fracture, high_energy_trauma, crush_injury, neurovascular_compromise, tendon_or_ligament_rupture_concern, scaphoid_tenderness_pattern, compartment_syndrome_concern, septic_joint_or_infection_concern, unable_to_bear_weight_lower_extremity, elbow_or_foot_site_pending_split, pediatric_growth_plate_pathway, elderly_osteoporotic_high_risk_msk, specialist_directed_orthopedic_plan
- `sprain_strain_non_ankle_xray_negative.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `sprain_strain_non_ankle_xray_negative.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `sprain_strain_non_ankle_xray_negative.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `sprain_strain_non_ankle_xray_negative.home_care.home_care_4.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `sprain_strain_non_ankle_xray_negative.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: ankle_sprain_pathway, no_xray_performed, fracture_seen, dislocation, open_wound, open_fracture, high_energy_trauma, crush_injury, neurovascular_compromise, tendon_or_ligament_rupture_concern, scaphoid_tenderness_pattern, compartment_syndrome_concern, septic_joint_or_infection_concern, unable_to_bear_weight_lower_extremity, elbow_or_foot_site_pending_split, pediatric_growth_plate_pathway, elderly_osteoporotic_high_risk_msk, specialist_directed_orthopedic_plan
- `sprain_strain_non_ankle_xray_negative.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: ankle_sprain_pathway, no_xray_performed, fracture_seen, dislocation, open_wound, open_fracture, high_energy_trauma, crush_injury, neurovascular_compromise, tendon_or_ligament_rupture_concern, scaphoid_tenderness_pattern, compartment_syndrome_concern, septic_joint_or_infection_concern, unable_to_bear_weight_lower_extremity, elbow_or_foot_site_pending_split, pediatric_growth_plate_pathway, elderly_osteoporotic_high_risk_msk, specialist_directed_orthopedic_plan
- `sprain_strain_non_ankle_xray_negative.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `sprain_strain_non_ankle_xray_negative.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `sprain_strain_non_ankle_xray_negative.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `sprain_strain_non_ankle_xray_negative.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: ankle_sprain_pathway, no_xray_performed, fracture_seen, dislocation, open_wound, open_fracture, high_energy_trauma, crush_injury, neurovascular_compromise, tendon_or_ligament_rupture_concern, scaphoid_tenderness_pattern, compartment_syndrome_concern, septic_joint_or_infection_concern, unable_to_bear_weight_lower_extremity, elbow_or_foot_site_pending_split, pediatric_growth_plate_pathway, elderly_osteoporotic_high_risk_msk, specialist_directed_orthopedic_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your clinician diagnosed a sprain or strain. Your x-ray did not show a fracture.

WHAT WE FOUND:
Your clinician documented that an x-ray was performed and did not show a fracture, and that blood flow, feeling, and movement were intact.

WHAT TO DO AT HOME:
- Protect the injured area with the brace, wrap, sling, splint, crutches, or activity limits your clinician gave you.
- Rest from painful activity at first, then slowly return to normal movement as symptoms allow.
- Raise the injured area when you can, especially while swelling is present.
- Minor sprains and strains may improve over several days. Moderate injuries often take several weeks, and high-grade injuries need follow-up.

MEDICATIONS:
- Use only the medicines your clinician prescribed or said are safe for you.
- Do not take extra doses or combine medicines unless your clinician told you to.

RETURN TO ED IF:
- New numbness, weakness, color change, coldness, or trouble moving the injured area.
- Worsening pain out of proportion, tight or hard swelling, or pain that does not improve with rest and elevation.
- Fever, spreading redness or warmth, pus, or severe pain with movement.

FOLLOW UP:
Follow up with primary care, urgent care, sports medicine, or orthopedics in 5 to 7 days if pain, swelling, movement, or walking is not improving, or sooner if your clinician gave a specific plan.
```
