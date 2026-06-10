# Phase 222 Promotion Decision

Date: 2026-06-03

Clinician review source: Phase 221 revision review.

Promoted to reviewed ontology mode:

- `skin_avulsion_or_abrasion_simple`
- `acute_otitis_media_uncomplicated`
- `suture_removal_or_wound_check_no_infection`

Still draft-only:

- `sprain_strain_non_ankle_xray_negative`

## Modifier Disposition

`skin_avulsion_or_abrasion_simple`:

- `immunocompromised` remains a true runtime blocker for v1.
- `diabetes_general_risk`, `peripheral_vascular_disease`, `anticoagulated`, and `delayed_wound_presentation` are output modifiers.
- Bite wounds, dirty wounds, infected wounds, repair need, deep-structure concern, and diabetic foot remain true blockers.

`acute_otitis_media_uncomplicated`:

- `elderly_frail` and `diabetes_general_risk` are output modifiers.
- `watchful_waiting_follow_up_unreliable` remains a runtime blocker scoped to the watchful-waiting pathway by its trigger terms.
- Immunocompromise, mastoiditis/deep infection concern, meningitis/CNS infection concern, venous sinus thrombosis concern, tubes/perforation, acute hearing loss, facial weakness/neurologic ear sign, pediatric pathway, recurrent/chronic pathway, unstable vitals, and ENT-directed plans remain true blockers.

`suture_removal_or_wound_check_no_infection`:

- `diabetes_general_risk`, `peripheral_vascular_disease`, and `anticoagulated` are output modifiers.
- Runtime now requires clinician-documented expected healing or explicit wound clearance plus clinician-entered wound follow-up plan.
- Wound readiness alone is not sufficient.
- Immunocompromise, diabetic foot, infection concern, dehiscence, high-risk locations, retained foreign body, dirty wound, bite wound, poor follow-up, pediatric pathway, and specialist-directed wound plan remain true blockers.

## Output Modifier Delivery

Output modifiers are returned in ontology metadata as `output_modifiers` and displayed in the review banner. They do not silently alter patient-facing text. The clinician must review the modifier note before using the output.

## Remaining Concern

`sprain_strain_non_ankle_xray_negative` remains draft-only because elbow and foot cases still match at low confidence.
