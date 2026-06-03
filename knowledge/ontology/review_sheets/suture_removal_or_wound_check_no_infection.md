# Suture removal or wound check without infection concern

Phenotype ID: `suture_removal_or_wound_check_no_infection`

Status: `needs_review`

## Inclusion Criteria

- Adult with clinician-documented wound check, suture removal, or staple removal plan.
- Clinician documents wound is healing as expected or ready for removal.
- No infection, dehiscence, retained foreign body, tendon/nerve/vascular risk, high-risk wound location, bite wound, open fracture, or specialist-directed wound plan.

## Exclusions

- Wound infection concern, pus, spreading redness, fever, red streaks, or systemic illness.
- Wound dehiscence, wound not ready for removal, early suture/staple loss, retained foreign body, tendon/nerve/vascular concern, open fracture, joint violation, bite wound, dirty wound, high-risk wound location, or poor follow-up.
- Pediatric pathway, immunocompromised host, diabetic foot wound, anticoagulation-related bleeding concern, or specialist-directed wound plan.

## Must-Not-Miss Diagnoses

- Wound infection.
- Wound dehiscence.
- Retained foreign body.
- Tendon, nerve, vascular, or joint injury.
- Open fracture.
- High-risk face, hand, joint, genital, scalp, or high-tension wound.
- Necrotizing infection.

## Primitive List

- `suture_removal_or_wound_check_no_infection.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `suture_removal_or_wound_check_no_infection.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: wound_infection_concern, wound_dehiscence, wound_not_ready_for_suture_removal, retained_foreign_body, hand_tendon_risk, joint_violation, high_risk_wound_location, open_fracture, bite_wound, dirty_wound, poor_follow_up, immunocompromised, diabetic_foot, pediatric_pathway, specialist_directed_wound_plan
- `suture_removal_or_wound_check_no_infection.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `suture_removal_or_wound_check_no_infection.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `suture_removal_or_wound_check_no_infection.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `suture_removal_or_wound_check_no_infection.home_care.home_care_4.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `suture_removal_or_wound_check_no_infection.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: wound_infection_concern, wound_dehiscence, wound_not_ready_for_suture_removal, retained_foreign_body, hand_tendon_risk, joint_violation, high_risk_wound_location, open_fracture, bite_wound, dirty_wound, poor_follow_up, immunocompromised, diabetic_foot, pediatric_pathway, specialist_directed_wound_plan
- `suture_removal_or_wound_check_no_infection.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: wound_infection_concern, wound_dehiscence, wound_not_ready_for_suture_removal, retained_foreign_body, hand_tendon_risk, joint_violation, high_risk_wound_location, open_fracture, bite_wound, dirty_wound, poor_follow_up, immunocompromised, diabetic_foot, pediatric_pathway, specialist_directed_wound_plan
- `suture_removal_or_wound_check_no_infection.medications.medication_guidance_3.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: wound_infection_concern, wound_dehiscence, wound_not_ready_for_suture_removal, retained_foreign_body, hand_tendon_risk, joint_violation, high_risk_wound_location, open_fracture, bite_wound, dirty_wound, poor_follow_up, immunocompromised, diabetic_foot, pediatric_pathway, specialist_directed_wound_plan
- `suture_removal_or_wound_check_no_infection.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `suture_removal_or_wound_check_no_infection.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `suture_removal_or_wound_check_no_infection.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `suture_removal_or_wound_check_no_infection.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: wound_infection_concern, wound_dehiscence, wound_not_ready_for_suture_removal, retained_foreign_body, hand_tendon_risk, joint_violation, high_risk_wound_location, open_fracture, bite_wound, dirty_wound, poor_follow_up, immunocompromised, diabetic_foot, pediatric_pathway, specialist_directed_wound_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your clinician checked your healing wound.

WHAT WE FOUND:
Your clinician documented the wound is healing as expected and did not document infection, wound opening, or another wound red flag.

WHAT TO DO AT HOME:
- Keep the area clean and follow the wound care instructions your clinician gave you.
- Do not pick at scabs, glue, strips, stitches, or staples.
- Protect the area from friction, soaking, or injury until your clinician says normal activity is safe.
- Most clean wounds continue to heal over 1 to 2 weeks. Scarring can take several months to fade.

MEDICATIONS:
- Use only the ointment, dressing supplies, or medicines your clinician prescribed or said are safe.
- Do not start leftover antibiotics unless your clinician tells you to.
- If you were prescribed antibiotics, do not stop them early unless your clinician tells you.

RETURN TO ED IF:
- Spreading redness, pus, red streaks, fever, worsening swelling, or worsening pain.
- The wound opens, bleeds and will not stop, or stitches or staples come out too early.
- New numbness, weakness, color change, or trouble moving the injured area.

FOLLOW UP:
Follow up on the wound schedule your clinician gave you. If no schedule was given and symptoms worsen or you are worried, arrange a recheck within 2 to 3 days.
```
