# Superficial puncture wound without retained foreign body or infection

Phenotype ID: `superficial_puncture_wound_no_retained_foreign_body_or_infection`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of superficial puncture wound.
- No retained foreign body, deep structure injury, infection, bite wound, dirty/high-risk wound, diabetic-foot risk, pregnancy/pediatric pathway, or specialist-directed plan.

## Exclusions

- Retained foreign body, deep puncture, tendon/nerve/vessel/bone concern, joint violation, open fracture, bite wound, dirty wound, infection, neurovascular compromise, severe pain, or delayed high-risk presentation.
- Diabetic-foot risk, immunocompromise, pregnancy/pediatric pathway, or specialist-directed wound/orthopedic plan.

## Must-Not-Miss Diagnoses

- Retained foreign body.
- Deep structure injury.
- Joint violation.
- Open fracture.
- Wound infection.

## Primitive List

- `superficial_puncture_wound_no_retained_foreign_body_or_infection.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `superficial_puncture_wound_no_retained_foreign_body_or_infection.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: retained_foreign_body, hand_tendon_risk, joint_violation, open_fracture, bite_wound, dirty_wound, wound_infection_concern, neurovascular_compromise, severe_pain, delayed_wound_presentation, diabetic_foot, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_wound_plan, specialist_directed_orthopedic_plan
- `superficial_puncture_wound_no_retained_foreign_body_or_infection.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `superficial_puncture_wound_no_retained_foreign_body_or_infection.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `superficial_puncture_wound_no_retained_foreign_body_or_infection.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `superficial_puncture_wound_no_retained_foreign_body_or_infection.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: retained_foreign_body, hand_tendon_risk, joint_violation, open_fracture, bite_wound, dirty_wound, wound_infection_concern, neurovascular_compromise, severe_pain, delayed_wound_presentation, diabetic_foot, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_wound_plan, specialist_directed_orthopedic_plan
- `superficial_puncture_wound_no_retained_foreign_body_or_infection.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: retained_foreign_body, hand_tendon_risk, joint_violation, open_fracture, bite_wound, dirty_wound, wound_infection_concern, neurovascular_compromise, severe_pain, delayed_wound_presentation, diabetic_foot, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_wound_plan, specialist_directed_orthopedic_plan
- `superficial_puncture_wound_no_retained_foreign_body_or_infection.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `superficial_puncture_wound_no_retained_foreign_body_or_infection.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `superficial_puncture_wound_no_retained_foreign_body_or_infection.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `superficial_puncture_wound_no_retained_foreign_body_or_infection.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: retained_foreign_body, hand_tendon_risk, joint_violation, open_fracture, bite_wound, dirty_wound, wound_infection_concern, neurovascular_compromise, severe_pain, delayed_wound_presentation, diabetic_foot, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_wound_plan, specialist_directed_orthopedic_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit a superficial puncture wound.

WHAT WE FOUND:
Your clinician diagnosed a superficial puncture wound. We did not find a retained foreign body, deep structure injury, infection, or another emergency problem today.

WHAT TO DO AT HOME:
- Keep the wound clean and protected.
- Change dressings only as instructed.
- Do not dig into the wound or try to remove anything at home.

MEDICATIONS:
- Take antibiotics only if your clinician prescribed them.
- Use pain medicine only if prescribed or recommended, and follow the label.

RETURN TO ED IF:
- Spreading redness, warmth, pus, red streaks, fever, or worsening swelling.
- Numbness, weakness, severe pain, color change, or trouble moving the area.
- New concern for a retained object, dirty wound, bite wound, or wound opening.

FOLLOW UP:
Follow up with primary care, urgent care, wound care, or the ED if the wound is not improving or your clinician told you to recheck.
```
