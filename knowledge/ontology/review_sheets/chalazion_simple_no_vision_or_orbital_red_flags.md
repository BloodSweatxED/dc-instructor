# Simple chalazion without vision or orbital red flags

Phenotype ID: `chalazion_simple_no_vision_or_orbital_red_flags`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of simple chalazion.
- No vision change, severe eye pain, orbital cellulitis concern, eye trauma, contact lens complication, infection concern, recurrent mass, or specialist-directed eye plan.

## Exclusions

- Vision change, severe eye pain, photophobia, pain with eye movement, orbital or periorbital cellulitis concern, or eye trauma.
- Contact lens complication, recurrent or persistent eyelid mass, immune compromise, systemic illness, pediatric pathway, or specialist-directed ophthalmology plan.
- Medication selection not supplied by clinician.

## Must-Not-Miss Diagnoses

- Orbital cellulitis.
- Periorbital cellulitis.
- Corneal ulcer or keratitis.
- Eyelid malignancy mimic.

## Primitive List

- `chalazion_simple_no_vision_or_orbital_red_flags.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `chalazion_simple_no_vision_or_orbital_red_flags.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: vision_change, severe_eye_pain, photophobia, periorbital_or_orbital_cellulitis_concern, eye_trauma_or_foreign_body, contact_lens_use, corneal_ulcer_or_keratitis_concern, recurrent_or_persistent_eyelid_mass, immunocompromised, pediatric_pathway, systemic_illness, specialist_directed_ophthalmology_plan
- `chalazion_simple_no_vision_or_orbital_red_flags.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `chalazion_simple_no_vision_or_orbital_red_flags.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `chalazion_simple_no_vision_or_orbital_red_flags.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `chalazion_simple_no_vision_or_orbital_red_flags.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: vision_change, severe_eye_pain, photophobia, periorbital_or_orbital_cellulitis_concern, eye_trauma_or_foreign_body, contact_lens_use, corneal_ulcer_or_keratitis_concern, recurrent_or_persistent_eyelid_mass, immunocompromised, pediatric_pathway, systemic_illness, specialist_directed_ophthalmology_plan
- `chalazion_simple_no_vision_or_orbital_red_flags.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: vision_change, severe_eye_pain, photophobia, periorbital_or_orbital_cellulitis_concern, eye_trauma_or_foreign_body, contact_lens_use, corneal_ulcer_or_keratitis_concern, recurrent_or_persistent_eyelid_mass, immunocompromised, pediatric_pathway, systemic_illness, specialist_directed_ophthalmology_plan
- `chalazion_simple_no_vision_or_orbital_red_flags.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `chalazion_simple_no_vision_or_orbital_red_flags.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `chalazion_simple_no_vision_or_orbital_red_flags.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `chalazion_simple_no_vision_or_orbital_red_flags.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: vision_change, severe_eye_pain, photophobia, periorbital_or_orbital_cellulitis_concern, eye_trauma_or_foreign_body, contact_lens_use, corneal_ulcer_or_keratitis_concern, recurrent_or_persistent_eyelid_mass, immunocompromised, pediatric_pathway, systemic_illness, specialist_directed_ophthalmology_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit a chalazion, a blocked oil gland in the eyelid.

WHAT WE FOUND:
Your clinician diagnosed a simple chalazion. We did not find vision changes, severe eye pain, eye injury, or signs of a deeper infection around the eye today.

WHAT TO DO AT HOME:
- Use warm compresses as your clinician instructed.
- Keep the eyelid clean and avoid eye makeup until improving.
- Do not squeeze, pop, or cut the eyelid bump.

MEDICATIONS:
- Use eye medicine only if it was prescribed.
- Do not put non-eye medicines or harsh products in the eye.

RETURN TO ED IF:
- Vision changes, severe eye pain, pain with eye movement, or worsening eye redness.
- Fever, rapidly worsening eyelid swelling, drainage, or spreading redness around the eye.
- The bump becomes recurrent, persistent, or interferes with vision.

FOLLOW UP:
Follow up with primary care, urgent care, optometry, or ophthalmology if symptoms are not improving, recur, or affect vision.
```
