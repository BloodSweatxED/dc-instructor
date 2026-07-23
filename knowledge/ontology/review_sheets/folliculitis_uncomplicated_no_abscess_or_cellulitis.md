# Uncomplicated folliculitis without abscess or cellulitis

Phenotype ID: `folliculitis_uncomplicated_no_abscess_or_cellulitis`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of uncomplicated folliculitis.
- No abscess, boil, carbuncle, cellulitis, systemic illness, high-risk host pathway, genital pathway, or specialist-directed plan.

## Exclusions

- Abscess, boil, carbuncle, cellulitis, rapidly spreading infection, or systemic illness.
- Genital involvement, immunocompromised host, diabetes/PVD/neuropathy risk, recurrent disease, hot tub outbreak, or public-health-directed plan.
- Medication selection not supplied by clinician.

## Must-Not-Miss Diagnoses

- Abscess.
- Cellulitis.
- Necrotizing infection.
- Sepsis.

## Primitive List

- `folliculitis_uncomplicated_no_abscess_or_cellulitis.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `folliculitis_uncomplicated_no_abscess_or_cellulitis.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: abscess_or_boils_or_carbuncle, secondary_skin_infection_concern, near_eye_or_genitals, rapid_progression, necrotizing_infection_concern, immunocompromised, diabetes_general_risk, peripheral_vascular_disease, neuropathy_foot_risk, systemic_illness, sepsis, recurrent_or_outbreak_folliculitis, specialist_directed_wound_plan
- `folliculitis_uncomplicated_no_abscess_or_cellulitis.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `folliculitis_uncomplicated_no_abscess_or_cellulitis.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `folliculitis_uncomplicated_no_abscess_or_cellulitis.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `folliculitis_uncomplicated_no_abscess_or_cellulitis.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: abscess_or_boils_or_carbuncle, secondary_skin_infection_concern, near_eye_or_genitals, rapid_progression, necrotizing_infection_concern, immunocompromised, diabetes_general_risk, peripheral_vascular_disease, neuropathy_foot_risk, systemic_illness, sepsis, recurrent_or_outbreak_folliculitis, specialist_directed_wound_plan
- `folliculitis_uncomplicated_no_abscess_or_cellulitis.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: abscess_or_boils_or_carbuncle, secondary_skin_infection_concern, near_eye_or_genitals, rapid_progression, necrotizing_infection_concern, immunocompromised, diabetes_general_risk, peripheral_vascular_disease, neuropathy_foot_risk, systemic_illness, sepsis, recurrent_or_outbreak_folliculitis, specialist_directed_wound_plan
- `folliculitis_uncomplicated_no_abscess_or_cellulitis.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `folliculitis_uncomplicated_no_abscess_or_cellulitis.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `folliculitis_uncomplicated_no_abscess_or_cellulitis.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `folliculitis_uncomplicated_no_abscess_or_cellulitis.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: abscess_or_boils_or_carbuncle, secondary_skin_infection_concern, near_eye_or_genitals, rapid_progression, necrotizing_infection_concern, immunocompromised, diabetes_general_risk, peripheral_vascular_disease, neuropathy_foot_risk, systemic_illness, sepsis, recurrent_or_outbreak_folliculitis, specialist_directed_wound_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit folliculitis, irritation or infection of hair follicles.

WHAT WE FOUND:
Your clinician diagnosed uncomplicated folliculitis. We did not find an abscess, spreading cellulitis, or systemic illness today.

WHAT TO DO AT HOME:
- Keep the area clean and dry.
- Avoid shaving, friction, or tight clothing over the irritated area until it improves.
- Do not squeeze or pick at bumps.

MEDICATIONS:
- Use antibiotic, antifungal, or skin medicine only if prescribed and exactly as directed.
- Use acetaminophen or ibuprofen only if you can take it safely and follow the label.

RETURN TO ED IF:
- Fever, spreading redness, warmth, swelling, red streaks, or severe pain.
- A growing pus pocket, boil, or area that may need drainage.
- Symptoms spread quickly or worsen despite the plan you were given.

FOLLOW UP:
Follow up with primary care, urgent care, or dermatology if symptoms are not improving or if this keeps coming back.
```
