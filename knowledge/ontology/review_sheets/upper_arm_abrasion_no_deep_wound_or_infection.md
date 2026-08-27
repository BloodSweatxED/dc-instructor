# Upper-arm abrasion without deep wound or infection

Phenotype ID: `upper_arm_abrasion_no_deep_wound_or_infection`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of superficial upper arm abrasion.
- No deep wound, repair-needed laceration, tendon/nerve/vessel injury, retained foreign body, infection, bite, burn, diabetic foot, or specialist wound plan.

## Exclusions

- Deep wound, repair-needed laceration, bite wound, dirty wound, crush injury, burn or chemical wound, retained foreign body, tendon/nerve/vessel injury, wound infection, diabetic foot risk, pregnancy/pediatric pathway, or specialist-directed wound plan.

## Must-Not-Miss Diagnoses

- Infected wound.
- Retained foreign body.
- Tendon, nerve, or vascular injury.
- Open fracture or joint violation.

## Primitive List

- `upper_arm_abrasion_no_deep_wound_or_infection.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `upper_arm_abrasion_no_deep_wound_or_infection.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: bite_wound, burn_or_chemical_wound, delayed_wound_presentation, dirty_wound, fever, high_pressure_injection_injury, immunocompromised, laceration_repair_needed, open_wound, pediatric_pathway, pregnancy, retained_foreign_body, secondary_skin_infection_concern, sepsis, specialist_directed_wound_plan, wound_infection_concern
- `upper_arm_abrasion_no_deep_wound_or_infection.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `upper_arm_abrasion_no_deep_wound_or_infection.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `upper_arm_abrasion_no_deep_wound_or_infection.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `upper_arm_abrasion_no_deep_wound_or_infection.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: bite_wound, burn_or_chemical_wound, delayed_wound_presentation, dirty_wound, fever, high_pressure_injection_injury, immunocompromised, laceration_repair_needed, open_wound, pediatric_pathway, pregnancy, retained_foreign_body, secondary_skin_infection_concern, sepsis, specialist_directed_wound_plan, wound_infection_concern
- `upper_arm_abrasion_no_deep_wound_or_infection.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: bite_wound, burn_or_chemical_wound, delayed_wound_presentation, dirty_wound, fever, high_pressure_injection_injury, immunocompromised, laceration_repair_needed, open_wound, pediatric_pathway, pregnancy, retained_foreign_body, secondary_skin_infection_concern, sepsis, specialist_directed_wound_plan, wound_infection_concern
- `upper_arm_abrasion_no_deep_wound_or_infection.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `upper_arm_abrasion_no_deep_wound_or_infection.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `upper_arm_abrasion_no_deep_wound_or_infection.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `upper_arm_abrasion_no_deep_wound_or_infection.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: bite_wound, burn_or_chemical_wound, delayed_wound_presentation, dirty_wound, fever, high_pressure_injection_injury, immunocompromised, laceration_repair_needed, open_wound, pediatric_pathway, pregnancy, retained_foreign_body, secondary_skin_infection_concern, sepsis, specialist_directed_wound_plan, wound_infection_concern

## Assembled Six-Section Output

```text
DIAGNOSIS:
You were treated for a upper arm abrasion.

WHAT WE FOUND:
Your clinician diagnosed a superficial upper arm abrasion. We did not find a deep wound, tendon injury, debris concern, or infection today.

WHAT TO DO AT HOME:
- Keep the area clean and dry today.
- Wash gently with soap and water when your clinician says it is okay.
- Do not scrub, pick, or dig at the wound.

MEDICATIONS:
- Use antibiotic ointment, dressings, or pain medicine only if prescribed or recommended.
- Use acetaminophen or ibuprofen only if you can take it safely and follow the label.

RETURN TO ED IF:
- Fever, pus, spreading redness, red streaks, worsening warmth, or swelling.
- Bleeding that will not stop with firm pressure.
- New numbness, weakness, color change, worsening pain, or concern that something is stuck in the wound.

FOLLOW UP:
Follow up with primary care, urgent care, or the ED if the wound is not improving, if you were told to recheck, or if tetanus questions remain.
```
