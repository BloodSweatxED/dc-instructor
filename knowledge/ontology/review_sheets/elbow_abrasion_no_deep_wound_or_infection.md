# Elbow abrasion without deep wound or infection red flags

Phenotype ID: `elbow_abrasion_no_deep_wound_or_infection`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of minor elbow abrasion.
- No repair-needed laceration, deep structure injury, retained foreign body, bite wound, dirty wound requiring separate pathway, infection, diabetic-foot risk when relevant, pregnancy/pediatric pathway, or specialist-directed plan.

## Exclusions

- Repair-needed laceration, tendon/nerve/blood-vessel injury, joint violation, open fracture, retained foreign body, bite wound, dirty wound, infection concern, neurovascular compromise, severe pain, delayed high-risk presentation, diabetic foot when relevant, immunocompromised host, pregnancy/pediatric pathway, or specialist-directed wound plan.

## Must-Not-Miss Diagnoses

- Tendon, nerve, or blood-vessel injury.
- Retained foreign body.
- Open fracture or joint violation.
- Wound infection.

## Primitive List

- `elbow_abrasion_no_deep_wound_or_infection.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `elbow_abrasion_no_deep_wound_or_infection.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: bite_wound, delayed_wound_presentation, dirty_wound, immunocompromised, joint_violation, laceration_repair_needed, neurovascular_compromise, open_fracture, pediatric_pathway, pregnancy, retained_foreign_body, severe_pain, specialist_directed_wound_plan, wound_infection_concern
- `elbow_abrasion_no_deep_wound_or_infection.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `elbow_abrasion_no_deep_wound_or_infection.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `elbow_abrasion_no_deep_wound_or_infection.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `elbow_abrasion_no_deep_wound_or_infection.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: bite_wound, delayed_wound_presentation, dirty_wound, immunocompromised, joint_violation, laceration_repair_needed, neurovascular_compromise, open_fracture, pediatric_pathway, pregnancy, retained_foreign_body, severe_pain, specialist_directed_wound_plan, wound_infection_concern
- `elbow_abrasion_no_deep_wound_or_infection.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: bite_wound, delayed_wound_presentation, dirty_wound, immunocompromised, joint_violation, laceration_repair_needed, neurovascular_compromise, open_fracture, pediatric_pathway, pregnancy, retained_foreign_body, severe_pain, specialist_directed_wound_plan, wound_infection_concern
- `elbow_abrasion_no_deep_wound_or_infection.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `elbow_abrasion_no_deep_wound_or_infection.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `elbow_abrasion_no_deep_wound_or_infection.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `elbow_abrasion_no_deep_wound_or_infection.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: bite_wound, delayed_wound_presentation, dirty_wound, immunocompromised, joint_violation, laceration_repair_needed, neurovascular_compromise, open_fracture, pediatric_pathway, pregnancy, retained_foreign_body, severe_pain, specialist_directed_wound_plan, wound_infection_concern

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit a minor elbow abrasion.

WHAT WE FOUND:
Your clinician diagnosed a minor elbow abrasion. We did not find a deep wound, retained foreign body, bite wound, infection, or another wound emergency today.

WHAT TO DO AT HOME:
- Keep the area clean and dry as your clinician instructed.
- Change dressings, wash gently, and protect the area only as your clinician recommended.
- Avoid soaking, picking, or reopening the abrasion.

MEDICATIONS:
- Use pain medicine only if prescribed or recommended, and follow the label.
- Use antibiotic ointment, tetanus care, or other wound treatment only if your clinician recommended it.

RETURN TO ED IF:
- Fever, spreading redness, warmth, pus, red streaks, worsening swelling, or worsening pain.
- Numbness, weakness, trouble moving the area, bleeding that will not stop, or concern that something is still in the wound.
- The wound opens, worsens, or does not improve as expected.

FOLLOW UP:
Follow up with primary care, urgent care, wound care, or the ED if symptoms are not improving or your clinician told you to recheck.
```
