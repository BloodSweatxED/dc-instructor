# Viral conjunctivitis without contact lens or vision red flags

Phenotype ID: `viral_conjunctivitis_uncomplicated_no_contact_lens_or_vision_red_flags`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of uncomplicated viral conjunctivitis.
- No contact lens use, eye pain, photophobia, vision change, corneal concern, trauma, or specialist-directed ophthalmology plan.

## Exclusions

- Contact lens use, eye pain, photophobia, vision change, corneal ulcer/keratitis concern, eye trauma, chemical exposure, immunocompromised host, pregnancy/pediatric pathway, or specialist-directed ophthalmology plan.

## Must-Not-Miss Diagnoses

- Corneal ulcer or keratitis.
- Acute glaucoma mimic.
- Eye trauma or foreign body.
- Vision-threatening infection.

## Primitive List

- `viral_conjunctivitis_uncomplicated_no_contact_lens_or_vision_red_flags.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `viral_conjunctivitis_uncomplicated_no_contact_lens_or_vision_red_flags.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: contact_lens_use, ocular_symptoms, vision_change, corneal_ulcer_or_keratitis_concern, eye_trauma_or_foreign_body, specialist_directed_ophthalmology_plan
- `viral_conjunctivitis_uncomplicated_no_contact_lens_or_vision_red_flags.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `viral_conjunctivitis_uncomplicated_no_contact_lens_or_vision_red_flags.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `viral_conjunctivitis_uncomplicated_no_contact_lens_or_vision_red_flags.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `viral_conjunctivitis_uncomplicated_no_contact_lens_or_vision_red_flags.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: contact_lens_use, ocular_symptoms, vision_change, corneal_ulcer_or_keratitis_concern, eye_trauma_or_foreign_body, specialist_directed_ophthalmology_plan
- `viral_conjunctivitis_uncomplicated_no_contact_lens_or_vision_red_flags.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: contact_lens_use, ocular_symptoms, vision_change, corneal_ulcer_or_keratitis_concern, eye_trauma_or_foreign_body, specialist_directed_ophthalmology_plan
- `viral_conjunctivitis_uncomplicated_no_contact_lens_or_vision_red_flags.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `viral_conjunctivitis_uncomplicated_no_contact_lens_or_vision_red_flags.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `viral_conjunctivitis_uncomplicated_no_contact_lens_or_vision_red_flags.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `viral_conjunctivitis_uncomplicated_no_contact_lens_or_vision_red_flags.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: contact_lens_use, ocular_symptoms, vision_change, corneal_ulcer_or_keratitis_concern, eye_trauma_or_foreign_body, specialist_directed_ophthalmology_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit uncomplicated viral conjunctivitis.

WHAT WE FOUND:
Your clinician diagnosed viral conjunctivitis. We did not find contact lens risk, vision change, eye pain, trauma, or cornea emergency signs today.

WHAT TO DO AT HOME:
- Wash your hands often.
- Avoid touching or rubbing the eyes.
- Do not share towels, eye makeup, or contact lens supplies.

MEDICATIONS:
- Use eye medicines or allergy medicines only if prescribed or recommended.
- Do not use leftover eye drops unless your clinician said they are safe.

RETURN TO ED IF:
- Eye pain, light sensitivity, vision change, severe redness, or worsening swelling.
- Contact lens use with worsening symptoms.
- Symptoms that worsen or do not improve as expected.

FOLLOW UP:
Follow up with primary care, urgent care, eye clinic, or the ED if symptoms are not improving or your clinician told you to recheck.
```
