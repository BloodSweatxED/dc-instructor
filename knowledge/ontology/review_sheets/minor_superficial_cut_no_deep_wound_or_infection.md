# Minor superficial cut without deep wound or infection red flags

Phenotype ID: `minor_superficial_cut_no_deep_wound_or_infection`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of minor superficial cut not requiring repair.
- No deep structure injury, tendon/nerve/blood-vessel injury, joint violation, open fracture, retained foreign body, bite wound, dirty wound requiring separate pathway, infection, diabetic-foot risk, pregnancy/pediatric pathway, or specialist-directed plan.

## Exclusions

- Repair-needed laceration, tendon/nerve/blood-vessel injury, joint violation, open fracture, retained foreign body, bite wound, dirty wound, infection concern, neurovascular compromise, severe pain, delayed high-risk presentation, diabetic foot, immunocompromised host, pregnancy/pediatric pathway, or specialist-directed wound plan.

## Must-Not-Miss Diagnoses

- Tendon, nerve, or blood-vessel injury.
- Retained foreign body.
- Open fracture or joint violation.
- Wound infection.

## Primitive List

- `minor_superficial_cut_no_deep_wound_or_infection.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `minor_superficial_cut_no_deep_wound_or_infection.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: laceration_repair_needed, hand_tendon_risk, joint_violation, open_fracture, retained_foreign_body, bite_wound, dirty_wound, wound_infection_concern, neurovascular_compromise, severe_pain, delayed_wound_presentation, diabetic_foot, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_wound_plan
- `minor_superficial_cut_no_deep_wound_or_infection.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `minor_superficial_cut_no_deep_wound_or_infection.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `minor_superficial_cut_no_deep_wound_or_infection.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `minor_superficial_cut_no_deep_wound_or_infection.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: laceration_repair_needed, hand_tendon_risk, joint_violation, open_fracture, retained_foreign_body, bite_wound, dirty_wound, wound_infection_concern, neurovascular_compromise, severe_pain, delayed_wound_presentation, diabetic_foot, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_wound_plan
- `minor_superficial_cut_no_deep_wound_or_infection.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: laceration_repair_needed, hand_tendon_risk, joint_violation, open_fracture, retained_foreign_body, bite_wound, dirty_wound, wound_infection_concern, neurovascular_compromise, severe_pain, delayed_wound_presentation, diabetic_foot, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_wound_plan
- `minor_superficial_cut_no_deep_wound_or_infection.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `minor_superficial_cut_no_deep_wound_or_infection.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `minor_superficial_cut_no_deep_wound_or_infection.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `minor_superficial_cut_no_deep_wound_or_infection.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: laceration_repair_needed, hand_tendon_risk, joint_violation, open_fracture, retained_foreign_body, bite_wound, dirty_wound, wound_infection_concern, neurovascular_compromise, severe_pain, delayed_wound_presentation, diabetic_foot, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_wound_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit a minor superficial cut.

WHAT WE FOUND:
Your clinician diagnosed a minor superficial cut. We did not find tendon, nerve, blood-vessel, joint, bone, retained foreign-body, bite, or infection concern today.

WHAT TO DO AT HOME:
- Keep the wound clean and dry as your clinician instructed.
- Change dressings, use soap and water, and protect the area only as your clinician recommended.
- Avoid soaking, picking, or reopening the cut.

MEDICATIONS:
- Use pain medicine only if prescribed or recommended, and follow the label.
- Use antibiotic ointment, tetanus care, or other wound treatment only if your clinician recommended it.

RETURN TO ED IF:
- Fever, spreading redness, warmth, pus, red streaks, worsening swelling, or worsening pain.
- Numbness, weakness, trouble moving the area, bleeding that will not stop, or concern that something is still in the wound.
- The wound opens, worsens, or does not improve as expected.

FOLLOW UP:
Follow up with primary care, urgent care, wound care, hand clinic, or the ED if symptoms are not improving or your clinician told you to recheck.
```
