# Uncomplicated acute otitis media without mastoiditis concern

Phenotype ID: `acute_otitis_media_uncomplicated`

Status: `retired`

## Inclusion Criteria

- Adult patient with clinician diagnosis or discharge impression of acute otitis media, otitis media, or middle ear infection.
- Clinician-entered treatment plan is present for pain control, antibiotics, delayed antibiotics, watchful waiting, or other medication instructions.
- No mastoiditis, deep ear infection, eardrum perforation, tympanostomy tube complication, ear trauma, foreign body, otitis externa pathway, acute hearing loss, facial weakness, vertigo, severe systemic illness, or unstable vital signs documented.
- No pediatric, recurrent/chronic, immunocompromised-host, or specialist-directed ENT pathway.

## Exclusions

- Mastoiditis, deep ear infection, skull base infection, or severe systemic illness concern.
- Perforated eardrum, tympanostomy tube, ear trauma, ear foreign body, acute hearing loss, vertigo, facial weakness, or specialist-directed ENT plan.
- Otitis externa or ear canal infection pathway.
- Immunocompromised host, frail elderly patient, recurrent or chronic ear infection, or pediatric pathway requiring individualized instructions.

## Must-Not-Miss Diagnoses

- Mastoiditis.
- Perforated tympanic membrane.
- Ear foreign body.
- Sudden sensorineural hearing loss.
- Facial nerve palsy.
- Sepsis or deep ear infection.

## Primitive List

- `acute_otitis_media_uncomplicated.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `acute_otitis_media_uncomplicated.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: mastoiditis_or_deep_ear_infection_concern, severe_systemic_ear_infection, tympanic_membrane_perforation_or_tube, ear_trauma_or_foreign_body, otitis_externa_or_ear_canal_pathway, acute_hearing_loss, facial_weakness_or_neurologic_ear_sign, immunocompromised, elderly_frail, recurrent_or_chronic_ear_infection, pediatric_pathway, specialist_directed_ent_plan, unstable_vitals
- `acute_otitis_media_uncomplicated.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `acute_otitis_media_uncomplicated.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `acute_otitis_media_uncomplicated.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `acute_otitis_media_uncomplicated.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: mastoiditis_or_deep_ear_infection_concern, severe_systemic_ear_infection, tympanic_membrane_perforation_or_tube, ear_trauma_or_foreign_body, otitis_externa_or_ear_canal_pathway, acute_hearing_loss, facial_weakness_or_neurologic_ear_sign, immunocompromised, elderly_frail, recurrent_or_chronic_ear_infection, pediatric_pathway, specialist_directed_ent_plan, unstable_vitals
- `acute_otitis_media_uncomplicated.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: mastoiditis_or_deep_ear_infection_concern, severe_systemic_ear_infection, tympanic_membrane_perforation_or_tube, ear_trauma_or_foreign_body, otitis_externa_or_ear_canal_pathway, acute_hearing_loss, facial_weakness_or_neurologic_ear_sign, immunocompromised, elderly_frail, recurrent_or_chronic_ear_infection, pediatric_pathway, specialist_directed_ent_plan, unstable_vitals
- `acute_otitis_media_uncomplicated.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `acute_otitis_media_uncomplicated.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `acute_otitis_media_uncomplicated.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `acute_otitis_media_uncomplicated.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: mastoiditis_or_deep_ear_infection_concern, severe_systemic_ear_infection, tympanic_membrane_perforation_or_tube, ear_trauma_or_foreign_body, otitis_externa_or_ear_canal_pathway, acute_hearing_loss, facial_weakness_or_neurologic_ear_sign, immunocompromised, elderly_frail, recurrent_or_chronic_ear_infection, pediatric_pathway, specialist_directed_ent_plan, unstable_vitals

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your clinician diagnosed a middle ear infection called acute otitis media.

WHAT WE FOUND:
Your discharge plan did not document mastoiditis, eardrum rupture, ear tube complication, ear canal infection, or another ear emergency today.

WHAT TO DO AT HOME:
- Rest as needed and drink fluids if you are allowed to.
- Keep cotton swabs, earbuds, and other objects out of the ear unless your clinician told you otherwise.
- Use warm compresses only if they feel comfortable and your clinician said they are safe.

MEDICATIONS:
- Use only the pain medicine, ear drops, or antibiotics your clinician prescribed or said are safe for you.
- If your clinician gave you a delayed-antibiotic or watchful-waiting plan, follow those exact instructions instead of starting antibiotics on your own.

RETURN TO ED IF:
- Fever that is high or not improving, worsening ear pain, confusion, severe headache, or feeling very ill.
- Redness, swelling, or pain behind the ear, or the ear starts sticking out.
- New hearing loss, dizziness, facial weakness, fluid or blood draining from the ear, or symptoms that get worse after discharge.

FOLLOW UP:
Follow up on the schedule your clinician gave you, especially if symptoms are not improving.
```
