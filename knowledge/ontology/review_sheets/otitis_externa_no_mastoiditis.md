# Uncomplicated otitis externa without mastoiditis concern

Phenotype ID: `otitis_externa_no_mastoiditis`

Status: `retired`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of uncomplicated otitis externa or swimmer's ear.
- No mastoiditis, malignant otitis externa, middle-ear complication, ear trauma, foreign body, acute hearing loss, facial weakness, or systemic illness concern documented.

## Exclusions

- Mastoiditis, deep ear infection, skull base osteomyelitis, or malignant otitis externa concern.
- Diabetes, immunocompromised host, severe systemic illness, unstable vital signs, or fever needing separate planning.
- Perforated eardrum, tympanostomy tube, ear trauma, ear foreign body, acute hearing loss, vertigo, facial weakness, or specialist-directed ENT plan.

## Must-Not-Miss Diagnoses

- Mastoiditis.
- Malignant otitis externa.
- Skull base osteomyelitis.
- Perforated tympanic membrane.
- Ear foreign body.
- Sudden sensorineural hearing loss.

## Primitive List

- `otitis_externa_no_mastoiditis.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `otitis_externa_no_mastoiditis.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: mastoiditis_or_deep_ear_infection_concern, malignant_otitis_externa_risk, immunocompromised, fever, unstable_vitals, tympanic_membrane_perforation_or_tube, ear_trauma_or_foreign_body, acute_hearing_loss, facial_weakness_or_neurologic_ear_sign
- `otitis_externa_no_mastoiditis.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `otitis_externa_no_mastoiditis.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `otitis_externa_no_mastoiditis.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `otitis_externa_no_mastoiditis.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: mastoiditis_or_deep_ear_infection_concern, malignant_otitis_externa_risk, immunocompromised, fever, unstable_vitals, tympanic_membrane_perforation_or_tube, ear_trauma_or_foreign_body, acute_hearing_loss, facial_weakness_or_neurologic_ear_sign
- `otitis_externa_no_mastoiditis.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: mastoiditis_or_deep_ear_infection_concern, malignant_otitis_externa_risk, immunocompromised, fever, unstable_vitals, tympanic_membrane_perforation_or_tube, ear_trauma_or_foreign_body, acute_hearing_loss, facial_weakness_or_neurologic_ear_sign
- `otitis_externa_no_mastoiditis.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `otitis_externa_no_mastoiditis.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `otitis_externa_no_mastoiditis.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `otitis_externa_no_mastoiditis.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: mastoiditis_or_deep_ear_infection_concern, malignant_otitis_externa_risk, immunocompromised, fever, unstable_vitals, tympanic_membrane_perforation_or_tube, ear_trauma_or_foreign_body, acute_hearing_loss, facial_weakness_or_neurologic_ear_sign

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit otitis externa, also called swimmer's ear.

WHAT WE FOUND:
Your clinician did not document mastoiditis concern, a deep ear infection, eardrum rupture, or another ear emergency in these discharge instructions.

WHAT TO DO AT HOME:
- Keep the ear dry unless your clinician told you something different.
- Do not put cotton swabs, earbuds, or other objects into the ear canal.
- Avoid swimming until your clinician says it is safe.

MEDICATIONS:
- Use ear drops only as prescribed.
- Use acetaminophen or ibuprofen only if you can take it safely and follow the label.

RETURN TO ED IF:
- Fever, worsening pain, severe headache, confusion, or feeling very ill.
- Redness, swelling, or pain behind the ear, or the ear starts sticking out.
- New hearing loss, dizziness, facial weakness, or drainage that gets worse.

FOLLOW UP:
Follow up with primary care, urgent care, or an ear clinician as instructed.
```
