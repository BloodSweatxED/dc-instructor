# Minor splinter removed without retained foreign body or infection

Phenotype ID: `minor_splinter_removed_no_retained_foreign_body_or_infection`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of minor superficial splinter removed.
- No retained foreign body, deep structure injury, infection, bite/dirty wound, diabetic-foot risk, pregnancy/pediatric pathway, or specialist-directed plan.

## Exclusions

- Retained foreign body, glass/metal or deep object concern, tendon/nerve/vessel/bone concern, joint violation, open fracture, dirty wound, bite wound, infection, neurovascular compromise, severe pain, or delayed high-risk presentation.
- Diabetic-foot risk, immunocompromise, pregnancy/pediatric pathway, or specialist-directed wound/hand plan.

## Must-Not-Miss Diagnoses

- Retained foreign body.
- Deep structure injury.
- Wound infection.
- Joint violation.
- Neurovascular compromise.

## Primitive List

- `minor_splinter_removed_no_retained_foreign_body_or_infection.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `minor_splinter_removed_no_retained_foreign_body_or_infection.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: retained_foreign_body, hand_tendon_risk, joint_violation, open_fracture, dirty_wound, bite_wound, wound_infection_concern, neurovascular_compromise, severe_pain, delayed_wound_presentation, diabetic_foot, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_wound_plan
- `minor_splinter_removed_no_retained_foreign_body_or_infection.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `minor_splinter_removed_no_retained_foreign_body_or_infection.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `minor_splinter_removed_no_retained_foreign_body_or_infection.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `minor_splinter_removed_no_retained_foreign_body_or_infection.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: retained_foreign_body, hand_tendon_risk, joint_violation, open_fracture, dirty_wound, bite_wound, wound_infection_concern, neurovascular_compromise, severe_pain, delayed_wound_presentation, diabetic_foot, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_wound_plan
- `minor_splinter_removed_no_retained_foreign_body_or_infection.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: retained_foreign_body, hand_tendon_risk, joint_violation, open_fracture, dirty_wound, bite_wound, wound_infection_concern, neurovascular_compromise, severe_pain, delayed_wound_presentation, diabetic_foot, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_wound_plan
- `minor_splinter_removed_no_retained_foreign_body_or_infection.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `minor_splinter_removed_no_retained_foreign_body_or_infection.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `minor_splinter_removed_no_retained_foreign_body_or_infection.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `minor_splinter_removed_no_retained_foreign_body_or_infection.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: retained_foreign_body, hand_tendon_risk, joint_violation, open_fracture, dirty_wound, bite_wound, wound_infection_concern, neurovascular_compromise, severe_pain, delayed_wound_presentation, diabetic_foot, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_wound_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your clinician removed a small superficial splinter.

WHAT WE FOUND:
Your clinician removed the splinter and did not find a retained foreign body, deep structure injury, infection, or another emergency problem today.

WHAT TO DO AT HOME:
- Keep the area clean and covered if instructed.
- Do not dig at the skin if it feels sore.
- Protect the area from repeat irritation while it heals.

MEDICATIONS:
- Take antibiotics only if your clinician prescribed them.
- Use pain medicine only if prescribed or recommended, and follow the label.

RETURN TO ED IF:
- Spreading redness, warmth, pus, red streaks, fever, or worsening swelling.
- Numbness, weakness, color change, severe pain, or trouble moving the area.
- Feeling like something remains in the wound or symptoms not improving.

FOLLOW UP:
Follow up with primary care, urgent care, wound care, or the ED if pain, redness, or foreign-body concern is not improving.
```
