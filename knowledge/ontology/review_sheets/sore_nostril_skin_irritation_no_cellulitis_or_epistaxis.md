# Sore nostril skin irritation without cellulitis or epistaxis red flags

Phenotype ID: `sore_nostril_skin_irritation_no_cellulitis_or_epistaxis`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of localized sore nostril skin irritation skin reaction.
- No anaphylaxis, systemic allergic reaction, mucosal involvement, skin infection, severe medication reaction, pregnancy/pediatric pathway, or specialist-directed plan.

## Exclusions

- Anaphylaxis, airway symptoms, hypotension, systemic allergic reaction, mucosal lesions, severe cutaneous adverse reaction, skin infection, rapidly progressive rash, immunocompromised host, pregnancy/pediatric pathway, or specialist-directed dermatology/allergy plan.

## Must-Not-Miss Diagnoses

- Anaphylaxis.
- Cellulitis.
- Severe cutaneous adverse reaction.
- Systemic allergic reaction.

## Primitive List

- `sore_nostril_skin_irritation_no_cellulitis_or_epistaxis.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `sore_nostril_skin_irritation_no_cellulitis_or_epistaxis.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: airway_symptoms, anaphylaxis, facial_or_nasal_trauma, fever, hypotension, immunocompromised, mucosal_lesions, near_eye_or_genitals, pediatric_pathway, posterior_epistaxis_or_uncontrolled_bleeding, pregnancy, rapid_progression, secondary_skin_infection_concern, sepsis, severe_cutaneous_adverse_reaction, specialist_directed_dermatology_plan, specialist_directed_ent_plan, systemic_allergic_reaction
- `sore_nostril_skin_irritation_no_cellulitis_or_epistaxis.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `sore_nostril_skin_irritation_no_cellulitis_or_epistaxis.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `sore_nostril_skin_irritation_no_cellulitis_or_epistaxis.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `sore_nostril_skin_irritation_no_cellulitis_or_epistaxis.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: airway_symptoms, anaphylaxis, facial_or_nasal_trauma, fever, hypotension, immunocompromised, mucosal_lesions, near_eye_or_genitals, pediatric_pathway, posterior_epistaxis_or_uncontrolled_bleeding, pregnancy, rapid_progression, secondary_skin_infection_concern, sepsis, severe_cutaneous_adverse_reaction, specialist_directed_dermatology_plan, specialist_directed_ent_plan, systemic_allergic_reaction
- `sore_nostril_skin_irritation_no_cellulitis_or_epistaxis.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: airway_symptoms, anaphylaxis, facial_or_nasal_trauma, fever, hypotension, immunocompromised, mucosal_lesions, near_eye_or_genitals, pediatric_pathway, posterior_epistaxis_or_uncontrolled_bleeding, pregnancy, rapid_progression, secondary_skin_infection_concern, sepsis, severe_cutaneous_adverse_reaction, specialist_directed_dermatology_plan, specialist_directed_ent_plan, systemic_allergic_reaction
- `sore_nostril_skin_irritation_no_cellulitis_or_epistaxis.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `sore_nostril_skin_irritation_no_cellulitis_or_epistaxis.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `sore_nostril_skin_irritation_no_cellulitis_or_epistaxis.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `sore_nostril_skin_irritation_no_cellulitis_or_epistaxis.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: airway_symptoms, anaphylaxis, facial_or_nasal_trauma, fever, hypotension, immunocompromised, mucosal_lesions, near_eye_or_genitals, pediatric_pathway, posterior_epistaxis_or_uncontrolled_bleeding, pregnancy, rapid_progression, secondary_skin_infection_concern, sepsis, severe_cutaneous_adverse_reaction, specialist_directed_dermatology_plan, specialist_directed_ent_plan, systemic_allergic_reaction

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit a localized skin reaction from sore nostril skin irritation.

WHAT WE FOUND:
Your clinician diagnosed a localized sore nostril skin irritation skin reaction. We did not find anaphylaxis, skin infection, mucosal involvement, or severe medication reaction today.

WHAT TO DO AT HOME:
- Avoid the suspected trigger if it is known.
- Wash gently with mild soap and water, and avoid scrubbing the rash.
- Use cool compresses, moisturizers, or coverings only as your clinician recommended.

MEDICATIONS:
- Use creams, ointments, itch medicine, or allergy medicine only if prescribed or recommended.
- Do not use leftover steroid, antibiotic, or allergy medicine unless your clinician told you to.

RETURN TO ED IF:
- Trouble breathing, throat tightness, swelling of the lips or tongue, fainting, or a bodywide reaction.
- Fever, spreading redness, warmth, pus, red streaks, rapidly worsening rash, skin peeling, or mouth sores.
- Symptoms that worsen or do not improve as expected.

FOLLOW UP:
Follow up with primary care, urgent care, dermatology, ENT, or the ED if symptoms are not improving or your clinician told you to recheck.
```
