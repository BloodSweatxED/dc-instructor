# Phase 46 Conjunctivitis Source Plan

Target phenotype: `conjunctivitis_uncomplicated_no_contact_lens`.

Clinical label: Uncomplicated conjunctivitis without contact lens or red flags.

Source cards:

- `cdc.conjunctivitis`
- `medlineplus.conjunctivitis`

Proposed inclusion boundary:

- Adult with clinician diagnosis or discharge impression of conjunctivitis or pink eye.
- No contact lens use.
- No eye trauma, foreign body, chemical exposure, corneal concern, severe pain, photophobia, vision change, herpes/zoster concern, or orbital/periorbital cellulitis concern.

Proposed hard blockers:

- `contact_lens_use`
- `eye_trauma_or_foreign_body`
- `severe_eye_pain`
- `photophobia`
- `vision_change`
- `herpes_or_zoster_eye_concern`
- `periorbital_or_orbital_cellulitis_concern`
- `immunocompromised`
- `pregnancy`

Guardrails:

- Do not promote conjunctivitis in this cycle.
- Do not use broad red eye, eye discharge, or itchy eye as standalone runtime terms.
- Do not infer antibiotic eye-drop instructions.
- Do not use conjunctivitis as a catch-all eye complaint fallback.
