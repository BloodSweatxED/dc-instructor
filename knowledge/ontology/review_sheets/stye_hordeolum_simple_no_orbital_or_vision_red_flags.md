# Simple stye without orbital or vision red flags

Phenotype ID: `stye_hordeolum_simple_no_orbital_or_vision_red_flags`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of simple stye, hordeolum, or localized eyelid bump.
- No contact lens pathway, vision change, severe eye pain, photophobia, trauma, foreign body, herpes or zoster concern, orbital or periorbital cellulitis concern, pregnancy, or immunocompromised-host pathway.

## Exclusions

- Vision change, severe eye pain, photophobia, pain with eye movement, proptosis, orbital or periorbital cellulitis concern.
- Contact lens use, eye trauma, foreign body, chemical exposure, corneal ulcer or keratitis concern, herpes or zoster eye concern, acute glaucoma mimic.
- Pregnancy, immunocompromised host, systemic illness, or specialist-directed ophthalmology plan.

## Must-Not-Miss Diagnoses

- Orbital cellulitis.
- Preseptal cellulitis requiring separate plan.
- Corneal ulcer or keratitis.
- Acute glaucoma mimic.

## Primitive List

- `stye_hordeolum_simple_no_orbital_or_vision_red_flags.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `stye_hordeolum_simple_no_orbital_or_vision_red_flags.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: contact_lens_use, vision_change, severe_eye_pain, photophobia, periorbital_or_orbital_cellulitis_concern, eye_trauma_or_foreign_body, chemical_eye_exposure, corneal_ulcer_or_keratitis_concern, acute_glaucoma_mimic, herpes_or_zoster_eye_concern, zoster_eye_face_or_neuro_concern, immunocompromised, pregnancy, systemic_illness
- `stye_hordeolum_simple_no_orbital_or_vision_red_flags.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `stye_hordeolum_simple_no_orbital_or_vision_red_flags.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `stye_hordeolum_simple_no_orbital_or_vision_red_flags.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `stye_hordeolum_simple_no_orbital_or_vision_red_flags.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: contact_lens_use, vision_change, severe_eye_pain, photophobia, periorbital_or_orbital_cellulitis_concern, eye_trauma_or_foreign_body, chemical_eye_exposure, corneal_ulcer_or_keratitis_concern, acute_glaucoma_mimic, herpes_or_zoster_eye_concern, zoster_eye_face_or_neuro_concern, immunocompromised, pregnancy, systemic_illness
- `stye_hordeolum_simple_no_orbital_or_vision_red_flags.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: contact_lens_use, vision_change, severe_eye_pain, photophobia, periorbital_or_orbital_cellulitis_concern, eye_trauma_or_foreign_body, chemical_eye_exposure, corneal_ulcer_or_keratitis_concern, acute_glaucoma_mimic, herpes_or_zoster_eye_concern, zoster_eye_face_or_neuro_concern, immunocompromised, pregnancy, systemic_illness
- `stye_hordeolum_simple_no_orbital_or_vision_red_flags.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `stye_hordeolum_simple_no_orbital_or_vision_red_flags.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `stye_hordeolum_simple_no_orbital_or_vision_red_flags.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `stye_hordeolum_simple_no_orbital_or_vision_red_flags.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: contact_lens_use, vision_change, severe_eye_pain, photophobia, periorbital_or_orbital_cellulitis_concern, eye_trauma_or_foreign_body, chemical_eye_exposure, corneal_ulcer_or_keratitis_concern, acute_glaucoma_mimic, herpes_or_zoster_eye_concern, zoster_eye_face_or_neuro_concern, immunocompromised, pregnancy, systemic_illness

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit a stye, also called a hordeolum.

WHAT WE FOUND:
Your exam was reassuring for a localized eyelid bump. We did not find vision changes, severe eye pain, eye injury, or signs of a deeper infection around the eye today.

WHAT TO DO AT HOME:
- Use warm compresses as your clinician instructed.
- Do not squeeze or pop the bump.
- Avoid eye makeup and contact lenses until your clinician says they are safe.

MEDICATIONS:
- Use eye medicine only if it was prescribed.
- Use acetaminophen or ibuprofen only if you can take it safely and follow the label.

RETURN TO ED IF:
- Vision change, severe eye pain, light sensitivity, or pain with eye movement.
- Fever, swelling spreading around the eye, the eye bulges, or you cannot open the eyelid.
- The bump gets much worse or does not improve with the plan you were given.

FOLLOW UP:
Follow up with primary care, urgent care, or eye care if symptoms are not improving, and sooner if any red flag develops.
```
