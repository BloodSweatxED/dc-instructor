# Healing wound without infection or dehiscence

Phenotype ID: `healing_wound_no_infection_or_dehiscence`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of healing wound or wound healing normally.
- No infection, dehiscence/wound opening, bleeding problem, deep structure injury, high-risk wound context, pregnancy/pediatric pathway, or specialist-directed plan.

## Exclusions

- Wound infection, dehiscence, wound opening, uncontrolled bleeding, open fracture, tendon/nerve/vessel/bone concern, joint violation, bite wound, dirty wound, delayed high-risk presentation, severe pain, or neurovascular compromise.
- Diabetic-foot risk, immunocompromise, pregnancy/pediatric pathway, or specialist-directed wound plan.

## Must-Not-Miss Diagnoses

- Wound infection.
- Wound dehiscence.
- Deep structure injury.
- Open fracture.
- Neurovascular compromise.

## Primitive List

- `healing_wound_no_infection_or_dehiscence.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `healing_wound_no_infection_or_dehiscence.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: wound_infection_concern, wound_dehiscence, open_fracture, hand_tendon_risk, joint_violation, bite_wound, dirty_wound, delayed_wound_presentation, severe_pain, neurovascular_compromise, diabetic_foot, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_wound_plan
- `healing_wound_no_infection_or_dehiscence.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `healing_wound_no_infection_or_dehiscence.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `healing_wound_no_infection_or_dehiscence.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `healing_wound_no_infection_or_dehiscence.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: wound_infection_concern, wound_dehiscence, open_fracture, hand_tendon_risk, joint_violation, bite_wound, dirty_wound, delayed_wound_presentation, severe_pain, neurovascular_compromise, diabetic_foot, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_wound_plan
- `healing_wound_no_infection_or_dehiscence.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: wound_infection_concern, wound_dehiscence, open_fracture, hand_tendon_risk, joint_violation, bite_wound, dirty_wound, delayed_wound_presentation, severe_pain, neurovascular_compromise, diabetic_foot, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_wound_plan
- `healing_wound_no_infection_or_dehiscence.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `healing_wound_no_infection_or_dehiscence.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `healing_wound_no_infection_or_dehiscence.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `healing_wound_no_infection_or_dehiscence.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: wound_infection_concern, wound_dehiscence, open_fracture, hand_tendon_risk, joint_violation, bite_wound, dirty_wound, delayed_wound_presentation, severe_pain, neurovascular_compromise, diabetic_foot, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_wound_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your wound appears to be healing.

WHAT WE FOUND:
Your clinician checked the wound and documented that it is healing without infection, wound opening, or another emergency problem today.

WHAT TO DO AT HOME:
- Keep following the wound-care plan your clinician gave you.
- Keep the wound clean and protected.
- Do not soak, scrub, or pick at the healing tissue unless your clinician said it is safe.

MEDICATIONS:
- Take antibiotics only if your clinician prescribed them.
- Use pain medicine only if prescribed or recommended, and follow the label.

RETURN TO ED IF:
- Spreading redness, warmth, pus, red streaks, fever, or worsening swelling.
- The wound opens, edges separate, bleeding will not stop, or pain becomes severe.
- New numbness, weakness, color change, or concern for a deeper injury.

FOLLOW UP:
Follow up as instructed for wound check, suture or staple care, or scar/healing concerns.
```
