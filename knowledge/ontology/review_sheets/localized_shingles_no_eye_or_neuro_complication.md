# Localized shingles without eye or neurologic complication

Phenotype ID: `localized_shingles_no_eye_or_neuro_complication`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of localized shingles or herpes zoster.
- No eye, face, ear, neurologic, disseminated, systemic, pregnancy, or immunocompromised-host complication documented.

## Exclusions

- Rash on the face, near the eye, ear involvement, vision symptoms, neurologic symptoms, meningitis or encephalitis concern.
- Disseminated rash, severe systemic illness, pneumonia concern, pregnancy, immunocompromised host, or uncontrolled pain.
- Specialist-directed ophthalmology, neurology, or infectious-disease plan.

## Must-Not-Miss Diagnoses

- Herpes zoster ophthalmicus.
- Ramsay Hunt syndrome.
- Meningitis or encephalitis.
- Disseminated zoster.

## Primitive List

- `localized_shingles_no_eye_or_neuro_complication.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `localized_shingles_no_eye_or_neuro_complication.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: zoster_eye_face_or_neuro_concern, herpes_or_zoster_eye_concern, ocular_symptoms, vision_change, meningitis_or_cns_infection_concern, neurologic_deficit, disseminated_or_complicated_zoster, secondary_skin_infection_concern, immunocompromised, pregnancy, systemic_illness, uncontrolled_pain, specialist_directed_neurology_plan
- `localized_shingles_no_eye_or_neuro_complication.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `localized_shingles_no_eye_or_neuro_complication.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `localized_shingles_no_eye_or_neuro_complication.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `localized_shingles_no_eye_or_neuro_complication.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: zoster_eye_face_or_neuro_concern, herpes_or_zoster_eye_concern, ocular_symptoms, vision_change, meningitis_or_cns_infection_concern, neurologic_deficit, disseminated_or_complicated_zoster, secondary_skin_infection_concern, immunocompromised, pregnancy, systemic_illness, uncontrolled_pain, specialist_directed_neurology_plan
- `localized_shingles_no_eye_or_neuro_complication.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: zoster_eye_face_or_neuro_concern, herpes_or_zoster_eye_concern, ocular_symptoms, vision_change, meningitis_or_cns_infection_concern, neurologic_deficit, disseminated_or_complicated_zoster, secondary_skin_infection_concern, immunocompromised, pregnancy, systemic_illness, uncontrolled_pain, specialist_directed_neurology_plan
- `localized_shingles_no_eye_or_neuro_complication.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `localized_shingles_no_eye_or_neuro_complication.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `localized_shingles_no_eye_or_neuro_complication.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `localized_shingles_no_eye_or_neuro_complication.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: zoster_eye_face_or_neuro_concern, herpes_or_zoster_eye_concern, ocular_symptoms, vision_change, meningitis_or_cns_infection_concern, neurologic_deficit, disseminated_or_complicated_zoster, secondary_skin_infection_concern, immunocompromised, pregnancy, systemic_illness, uncontrolled_pain, specialist_directed_neurology_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit shingles, also called herpes zoster.

WHAT WE FOUND:
Your clinician diagnosed a localized shingles rash. We did not find eye involvement, neurologic symptoms, disseminated rash, or another emergency complication today.

WHAT TO DO AT HOME:
- Keep the rash clean, dry, and covered when possible.
- Avoid scratching or picking at blisters.
- Avoid close contact with pregnant people, newborns, and immunocompromised people until the rash has crusted over.

MEDICATIONS:
- Take antiviral, pain, or itch medicine only if prescribed and exactly as directed.
- Use acetaminophen or ibuprofen only if you can take it safely and follow the label.

RETURN TO ED IF:
- Rash on the face, near the eye, eye pain, vision change, severe headache, confusion, weakness, or trouble walking.
- Fever, spreading redness, pus, or you feel very ill.
- Pain is uncontrolled or the rash spreads widely.

FOLLOW UP:
Follow up with primary care or dermatology as instructed, especially if pain persists after the rash improves.
```
