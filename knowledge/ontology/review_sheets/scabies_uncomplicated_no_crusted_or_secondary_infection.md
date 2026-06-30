# Uncomplicated scabies without crusted disease or secondary infection

Phenotype ID: `scabies_uncomplicated_no_crusted_or_secondary_infection`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of uncomplicated scabies.
- No crusted scabies, institutional outbreak plan, secondary infection, systemic illness, or immunocompromised-host pathway.

## Exclusions

- Crusted scabies, institutional outbreak, public-health-directed plan, or immunocompromised host.
- Secondary bacterial infection, cellulitis, abscess, systemic illness, or severe diffuse rash.
- Medication selection or repeat-treatment schedule not supplied by clinician.

## Must-Not-Miss Diagnoses

- Crusted scabies.
- Cellulitis.
- Sepsis.
- Severe cutaneous adverse reaction mimic.

## Primitive List

- `scabies_uncomplicated_no_crusted_or_secondary_infection.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `scabies_uncomplicated_no_crusted_or_secondary_infection.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: crusted_scabies_or_institutional_outbreak, secondary_skin_infection_concern, abscess_concern, severe_cutaneous_adverse_reaction, immunocompromised, systemic_illness, nursing_home_patient, poor_follow_up
- `scabies_uncomplicated_no_crusted_or_secondary_infection.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `scabies_uncomplicated_no_crusted_or_secondary_infection.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `scabies_uncomplicated_no_crusted_or_secondary_infection.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `scabies_uncomplicated_no_crusted_or_secondary_infection.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: crusted_scabies_or_institutional_outbreak, secondary_skin_infection_concern, abscess_concern, severe_cutaneous_adverse_reaction, immunocompromised, systemic_illness, nursing_home_patient, poor_follow_up
- `scabies_uncomplicated_no_crusted_or_secondary_infection.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: crusted_scabies_or_institutional_outbreak, secondary_skin_infection_concern, abscess_concern, severe_cutaneous_adverse_reaction, immunocompromised, systemic_illness, nursing_home_patient, poor_follow_up
- `scabies_uncomplicated_no_crusted_or_secondary_infection.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `scabies_uncomplicated_no_crusted_or_secondary_infection.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `scabies_uncomplicated_no_crusted_or_secondary_infection.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `scabies_uncomplicated_no_crusted_or_secondary_infection.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: crusted_scabies_or_institutional_outbreak, secondary_skin_infection_concern, abscess_concern, severe_cutaneous_adverse_reaction, immunocompromised, systemic_illness, nursing_home_patient, poor_follow_up

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit scabies, a contagious skin mite infestation.

WHAT WE FOUND:
Your clinician diagnosed scabies today. We did not find signs of crusted scabies, a deeper skin infection, or another emergency rash problem.

WHAT TO DO AT HOME:
- Avoid close skin-to-skin contact until you have followed the treatment plan.
- Wash clothing, towels, and bedding as your clinician instructed.
- Tell close contacts to follow the plan your clinician gave you.

MEDICATIONS:
- Use the scabies medicine exactly as prescribed.
- Do not use extra doses or over-the-counter products unless your clinician told you to.

RETURN TO ED IF:
- Fever, spreading redness, pus, red streaks, or severe pain.
- Thick crusting rash, widespread worsening rash, or symptoms in an immunocompromised person.
- You cannot complete the treatment plan or close contacts keep getting symptoms.

FOLLOW UP:
Follow up with primary care, urgent care, or dermatology if symptoms are not improving after treatment or if household spread continues.
```
