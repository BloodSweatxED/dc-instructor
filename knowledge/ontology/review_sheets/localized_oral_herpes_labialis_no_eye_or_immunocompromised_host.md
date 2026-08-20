# Localized oral herpes labialis without eye involvement or immunocompromised host

Phenotype ID: `localized_oral_herpes_labialis_no_eye_or_immunocompromised_host`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of localized oral herpes labialis or cold sore.
- No eye involvement, genital involvement, disseminated disease, CNS/systemic illness, pregnancy/newborn exposure, immunocompromised host, or specialist-directed plan.

## Exclusions

- Eye pain, red eye, vision change, vesicles near eye, genital lesions, disseminated rash, severe headache, confusion, fever, or systemic illness.
- Pregnancy, newborn exposure, immunocompromised host, severe eczema flare/eczema herpeticum concern, or specialist-directed antiviral/ophthalmology/dermatology plan.
- Medication selection not supplied by clinician.

## Must-Not-Miss Diagnoses

- Herpes keratitis.
- Disseminated HSV.
- HSV encephalitis.
- Eczema herpeticum.

## Primitive List

- `localized_oral_herpes_labialis_no_eye_or_immunocompromised_host.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `localized_oral_herpes_labialis_no_eye_or_immunocompromised_host.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: herpes_or_zoster_eye_concern, ocular_symptoms, vision_change, near_eye_or_genitals, genital_ulcers, oral_herpes_high_risk_or_complicated, meningitis_or_cns_infection_concern, systemic_illness, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_dermatology_plan, specialist_directed_ophthalmology_plan
- `localized_oral_herpes_labialis_no_eye_or_immunocompromised_host.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `localized_oral_herpes_labialis_no_eye_or_immunocompromised_host.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `localized_oral_herpes_labialis_no_eye_or_immunocompromised_host.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `localized_oral_herpes_labialis_no_eye_or_immunocompromised_host.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: herpes_or_zoster_eye_concern, ocular_symptoms, vision_change, near_eye_or_genitals, genital_ulcers, oral_herpes_high_risk_or_complicated, meningitis_or_cns_infection_concern, systemic_illness, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_dermatology_plan, specialist_directed_ophthalmology_plan
- `localized_oral_herpes_labialis_no_eye_or_immunocompromised_host.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: herpes_or_zoster_eye_concern, ocular_symptoms, vision_change, near_eye_or_genitals, genital_ulcers, oral_herpes_high_risk_or_complicated, meningitis_or_cns_infection_concern, systemic_illness, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_dermatology_plan, specialist_directed_ophthalmology_plan
- `localized_oral_herpes_labialis_no_eye_or_immunocompromised_host.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `localized_oral_herpes_labialis_no_eye_or_immunocompromised_host.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `localized_oral_herpes_labialis_no_eye_or_immunocompromised_host.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `localized_oral_herpes_labialis_no_eye_or_immunocompromised_host.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: herpes_or_zoster_eye_concern, ocular_symptoms, vision_change, near_eye_or_genitals, genital_ulcers, oral_herpes_high_risk_or_complicated, meningitis_or_cns_infection_concern, systemic_illness, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_dermatology_plan, specialist_directed_ophthalmology_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit a cold sore, also called oral herpes labialis.

WHAT WE FOUND:
Your clinician diagnosed localized oral herpes labialis. We did not find eye involvement, genital involvement, disseminated disease, or immunocompromised-host risk today.

WHAT TO DO AT HOME:
- Avoid touching the sore except when cleaning the area or applying medicine.
- Wash your hands after touching the area.
- Avoid kissing, oral sex, or sharing lip products while sores are active.

MEDICATIONS:
- Use antiviral medicine only if prescribed and exactly as directed.
- Use acetaminophen or ibuprofen only if you can take it safely and follow the label.

RETURN TO ED IF:
- Eye pain, eye redness, vision change, or sores near the eye.
- Fever, confusion, severe headache, widespread rash, or rapidly spreading sores.
- Symptoms occur in a newborn exposure context, pregnancy concern, or immunocompromised host.

FOLLOW UP:
Follow up with primary care, urgent care, dermatology, or ophthalmology as instructed, especially if outbreaks recur or symptoms are not improving.
```
