# Simple skin avulsion, skin tear, or abrasion without repair need

Phenotype ID: `skin_avulsion_or_abrasion_simple`

Status: `needs_review`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of simple skin abrasion, skin tear, or skin avulsion.
- Clinician documents no repair need and no retained foreign body, deep structure injury, infection concern, or high-risk wound pathway.
- Wound was cleaned and dressed with clinician-entered wound care instructions.

## Exclusions

- Wound needing sutures, staples, glue, operative repair, or laceration pathway.
- Burn, chemical exposure, high-pressure injection injury, crush injury, open fracture, joint violation, tendon/nerve/vascular concern, retained foreign body, bite wound, dirty wound, or infected wound.
- Diabetic foot wound, immunocompromised host, pediatric pathway, or specialist-directed wound plan.

## Must-Not-Miss Diagnoses

- Retained foreign body.
- Tendon, nerve, vascular, or joint injury.
- Open fracture.
- High-pressure injection injury.
- Wound infection.
- Burn or chemical injury.

## Primitive List

- `skin_avulsion_or_abrasion_simple.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `skin_avulsion_or_abrasion_simple.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: laceration_repair_needed, burn_or_chemical_wound, high_pressure_injection_injury, crush_injury, open_fracture, joint_violation, hand_tendon_risk, neurovascular_compromise, retained_foreign_body, bite_wound, dirty_wound, wound_infection_concern, diabetic_foot, immunocompromised, pediatric_pathway, specialist_directed_wound_plan
- `skin_avulsion_or_abrasion_simple.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `skin_avulsion_or_abrasion_simple.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `skin_avulsion_or_abrasion_simple.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `skin_avulsion_or_abrasion_simple.home_care.home_care_4.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `skin_avulsion_or_abrasion_simple.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: laceration_repair_needed, burn_or_chemical_wound, high_pressure_injection_injury, crush_injury, open_fracture, joint_violation, hand_tendon_risk, neurovascular_compromise, retained_foreign_body, bite_wound, dirty_wound, wound_infection_concern, diabetic_foot, immunocompromised, pediatric_pathway, specialist_directed_wound_plan
- `skin_avulsion_or_abrasion_simple.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: laceration_repair_needed, burn_or_chemical_wound, high_pressure_injection_injury, crush_injury, open_fracture, joint_violation, hand_tendon_risk, neurovascular_compromise, retained_foreign_body, bite_wound, dirty_wound, wound_infection_concern, diabetic_foot, immunocompromised, pediatric_pathway, specialist_directed_wound_plan
- `skin_avulsion_or_abrasion_simple.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `skin_avulsion_or_abrasion_simple.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `skin_avulsion_or_abrasion_simple.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `skin_avulsion_or_abrasion_simple.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: laceration_repair_needed, burn_or_chemical_wound, high_pressure_injection_injury, crush_injury, open_fracture, joint_violation, hand_tendon_risk, neurovascular_compromise, retained_foreign_body, bite_wound, dirty_wound, wound_infection_concern, diabetic_foot, immunocompromised, pediatric_pathway, specialist_directed_wound_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your clinician diagnosed a simple skin abrasion, skin tear, or skin avulsion.

WHAT WE FOUND:
Your clinician documented a superficial skin wound without a repair need, retained foreign body concern, deep structure injury, infection concern, or other wound red flag.

WHAT TO DO AT HOME:
- Keep the wound clean and follow the dressing plan your clinician gave you.
- Do not scrub, pick, or peel the injured skin.
- Protect the area from friction, soaking, or another injury while the skin is closing.
- Many abrasions heal new surface skin within 7 to 14 days. Skin tears and avulsions, especially in older adults, can take longer.

MEDICATIONS:
- Use only the dressing supplies, ointment, or medicines your clinician prescribed or said are safe.
- Do not start leftover antibiotics unless your clinician tells you to.

RETURN TO ED IF:
- Spreading redness, pus, red streaks, fever, worsening swelling, or worsening pain.
- Bleeding that will not stop with firm pressure or the wound starts opening wider.
- New numbness, weakness, color change, trouble moving the area, or concern that something is stuck in the wound.

FOLLOW UP:
Follow up with primary care, urgent care, wound clinic, or the ED in 2 to 3 days if the wound is not improving, or sooner if your clinician gave a specific schedule.
```
