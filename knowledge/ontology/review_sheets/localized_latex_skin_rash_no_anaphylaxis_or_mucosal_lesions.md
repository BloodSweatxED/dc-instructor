# Localized latex skin rash without anaphylaxis or mucosal lesions

Phenotype ID: `localized_latex_skin_rash_no_anaphylaxis_or_mucosal_lesions`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of localized latex contact skin reaction.
- No anaphylaxis, systemic allergic reaction, mucosal involvement, skin infection, severe medication reaction, pregnancy/pediatric pathway, or specialist-directed plan.

## Exclusions

- Anaphylaxis, airway symptoms, hypotension, systemic allergic reaction, mucosal lesions, severe cutaneous adverse reaction, skin infection, rapidly progressive rash, burn or chemical exposure, immunocompromised host, pregnancy/pediatric pathway, or specialist-directed dermatology/allergy plan.

## Must-Not-Miss Diagnoses

- Anaphylaxis.
- Cellulitis.
- Severe cutaneous adverse reaction.
- Systemic allergic reaction.

## Primitive List

- `localized_latex_skin_rash_no_anaphylaxis_or_mucosal_lesions.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `localized_latex_skin_rash_no_anaphylaxis_or_mucosal_lesions.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: anaphylaxis, airway_symptoms, hypotension, systemic_allergic_reaction, mucosal_lesions, severe_cutaneous_adverse_reaction, secondary_skin_infection_concern, rapid_progression, fever, sepsis, burn_or_chemical_wound, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_dermatology_plan
- `localized_latex_skin_rash_no_anaphylaxis_or_mucosal_lesions.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `localized_latex_skin_rash_no_anaphylaxis_or_mucosal_lesions.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `localized_latex_skin_rash_no_anaphylaxis_or_mucosal_lesions.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `localized_latex_skin_rash_no_anaphylaxis_or_mucosal_lesions.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: anaphylaxis, airway_symptoms, hypotension, systemic_allergic_reaction, mucosal_lesions, severe_cutaneous_adverse_reaction, secondary_skin_infection_concern, rapid_progression, fever, sepsis, burn_or_chemical_wound, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_dermatology_plan
- `localized_latex_skin_rash_no_anaphylaxis_or_mucosal_lesions.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: anaphylaxis, airway_symptoms, hypotension, systemic_allergic_reaction, mucosal_lesions, severe_cutaneous_adverse_reaction, secondary_skin_infection_concern, rapid_progression, fever, sepsis, burn_or_chemical_wound, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_dermatology_plan
- `localized_latex_skin_rash_no_anaphylaxis_or_mucosal_lesions.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `localized_latex_skin_rash_no_anaphylaxis_or_mucosal_lesions.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `localized_latex_skin_rash_no_anaphylaxis_or_mucosal_lesions.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `localized_latex_skin_rash_no_anaphylaxis_or_mucosal_lesions.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: anaphylaxis, airway_symptoms, hypotension, systemic_allergic_reaction, mucosal_lesions, severe_cutaneous_adverse_reaction, secondary_skin_infection_concern, rapid_progression, fever, sepsis, burn_or_chemical_wound, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_dermatology_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit a localized skin reaction from latex contact.

WHAT WE FOUND:
Your clinician diagnosed a localized latex contact skin reaction. We did not find anaphylaxis, mucosal involvement, skin infection, or another rash emergency today.

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
Follow up with primary care, urgent care, dermatology, allergy, or the ED if symptoms are not improving or your clinician told you to recheck.
```
