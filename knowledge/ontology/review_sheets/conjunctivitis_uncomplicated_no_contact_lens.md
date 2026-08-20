# Uncomplicated conjunctivitis without contact lens or red flags

Phenotype ID: `conjunctivitis_uncomplicated_no_contact_lens`

Status: `retired`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of conjunctivitis or pink eye.
- No contact lens use documented.
- No eye trauma, foreign body, chemical exposure, corneal ulcer or keratitis concern, acute glaucoma mimic, severe pain, photophobia, vision change, herpes/zoster concern, or orbital/periorbital cellulitis concern.

## Exclusions

- Contact lens use.
- Eye trauma, foreign body, chemical exposure, corneal abrasion, corneal ulcer, or keratitis concern.
- Severe eye pain, photophobia, vision change, proptosis, pain with eye movement, or periorbital/orbital cellulitis concern.
- Herpes or zoster eye concern.
- Immunocompromised host, pregnancy, infant/pediatric pathway, or specialist-directed ophthalmology plan.

## Must-Not-Miss Diagnoses

- Keratitis or corneal ulcer.
- Corneal abrasion or foreign body.
- Acute glaucoma.
- Uveitis or iritis.
- Herpes or zoster eye disease.
- Orbital cellulitis.

## Primitive List

- `conjunctivitis_uncomplicated_no_contact_lens.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `conjunctivitis_uncomplicated_no_contact_lens.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: contact_lens_use, chemical_eye_exposure, corneal_ulcer_or_keratitis_concern, acute_glaucoma_mimic, eye_trauma_or_foreign_body, severe_eye_pain, photophobia, vision_change, herpes_or_zoster_eye_concern, periorbital_or_orbital_cellulitis_concern, immunocompromised, pregnancy
- `conjunctivitis_uncomplicated_no_contact_lens.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `conjunctivitis_uncomplicated_no_contact_lens.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `conjunctivitis_uncomplicated_no_contact_lens.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `conjunctivitis_uncomplicated_no_contact_lens.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: contact_lens_use, chemical_eye_exposure, corneal_ulcer_or_keratitis_concern, acute_glaucoma_mimic, eye_trauma_or_foreign_body, severe_eye_pain, photophobia, vision_change, herpes_or_zoster_eye_concern, periorbital_or_orbital_cellulitis_concern, immunocompromised, pregnancy
- `conjunctivitis_uncomplicated_no_contact_lens.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: contact_lens_use, chemical_eye_exposure, corneal_ulcer_or_keratitis_concern, acute_glaucoma_mimic, eye_trauma_or_foreign_body, severe_eye_pain, photophobia, vision_change, herpes_or_zoster_eye_concern, periorbital_or_orbital_cellulitis_concern, immunocompromised, pregnancy
- `conjunctivitis_uncomplicated_no_contact_lens.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `conjunctivitis_uncomplicated_no_contact_lens.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `conjunctivitis_uncomplicated_no_contact_lens.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `conjunctivitis_uncomplicated_no_contact_lens.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: contact_lens_use, chemical_eye_exposure, corneal_ulcer_or_keratitis_concern, acute_glaucoma_mimic, eye_trauma_or_foreign_body, severe_eye_pain, photophobia, vision_change, herpes_or_zoster_eye_concern, periorbital_or_orbital_cellulitis_concern, immunocompromised, pregnancy

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit conjunctivitis, also called pink eye.

WHAT WE FOUND:
Your clinician did not document contact lens risk, eye injury, vision loss, or another eye emergency in these discharge instructions.

WHAT TO DO AT HOME:
- Wash your hands often and avoid touching or rubbing the eye.
- Do not share towels, pillowcases, makeup, or eye drops.
- Use a clean warm or cool compress if your clinician said it is safe.

MEDICATIONS:
- Use only the eye drops or medicines your clinician prescribed or said are safe for you.
- Do not use contact lenses until your clinician says it is safe.

RETURN TO ED IF:
- Eye pain, light sensitivity, vision changes, or worsening redness.
- Swelling around the eye, trouble moving the eye, fever, or feeling very ill.
- Symptoms get worse, do not improve as expected, or you were exposed to chemicals or an eye injury.

FOLLOW UP:
Follow up with primary care, urgent care, or an eye clinician as instructed.
```
