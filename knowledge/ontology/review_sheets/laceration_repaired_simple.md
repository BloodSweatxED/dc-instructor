# Simple laceration repair

Phenotype ID: `laceration_repaired_simple`

Status: `reviewed`

## Inclusion Criteria

- Simple repaired laceration with no tendon, nerve, vessel, joint, or open fracture concern.

## Exclusions

- Bite wounds requiring special counseling.
- Open fracture, tendon injury, nerve injury, joint violation, or high-pressure injection injury.

## Must-Not-Miss Diagnoses

- Tendon injury.
- Nerve or vascular injury.
- Open fracture.
- Joint violation.
- Infection.

## Primitive List

- `laceration_repaired_simple.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only | unsafe modifiers: none
- `laceration_repaired_simple.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier | unsafe modifiers: bite_wound, hand_tendon_risk, joint_violation, open_fracture, dirty_wound
- `laceration_repaired_simple.home_care.home_care_1.v1` | `home_care` | audit: source_supported | unsafe modifiers: none
- `laceration_repaired_simple.home_care.home_care_2.v1` | `home_care` | audit: source_supported | unsafe modifiers: none
- `laceration_repaired_simple.home_care.home_care_3.v1` | `home_care` | audit: source_supported | unsafe modifiers: none
- `laceration_repaired_simple.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier | unsafe modifiers: bite_wound, hand_tendon_risk, joint_violation, open_fracture, dirty_wound
- `laceration_repaired_simple.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier | unsafe modifiers: bite_wound, hand_tendon_risk, joint_violation, open_fracture, dirty_wound
- `laceration_repaired_simple.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only | unsafe modifiers: none
- `laceration_repaired_simple.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only | unsafe modifiers: none
- `laceration_repaired_simple.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only | unsafe modifiers: none
- `laceration_repaired_simple.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier | unsafe modifiers: bite_wound, hand_tendon_risk, joint_violation, open_fracture, dirty_wound

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your cut was cleaned and repaired today.

WHAT WE FOUND:
We checked the wound and repaired it because it was safe to close. No emergency complication was found during today's exam.

WHAT TO DO AT HOME:
- Keep the wound clean and dry today.
- After the first day, gentle soap and water is usually okay unless told otherwise.
- Do not soak the wound until it is healed.

MEDICATIONS:
- Take antibiotics only if they were prescribed.
- Use acetaminophen or ibuprofen only if you can take it safely and follow the label.

RETURN TO ED IF:
- Fever, pus, spreading redness, red streaks, or worsening swelling.
- Bleeding that will not stop with firm pressure.
- New numbness, weakness, color change, or the wound opens.

FOLLOW UP:
Follow up for wound check or suture removal on the schedule your clinician gave you.
```
