# Localized soap irritant contact dermatitis without infection or anaphylaxis

Phenotype ID: `localized_soap_irritant_contact_dermatitis_no_infection_or_anaphylaxis`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of localized soap irritant contact dermatitis.
- No anaphylaxis, infection, severe cutaneous adverse reaction, eye/genital location, burn or chemical wound, pregnancy/pediatric pathway, or immunocompromised host.

## Exclusions

- Anaphylaxis, airway symptoms, infection concern, severe cutaneous adverse reaction, eye or genital rash location, burn or chemical wound, immunocompromised host, pregnancy/pediatric pathway, or specialist-directed dermatology plan.

## Must-Not-Miss Diagnoses

- Anaphylaxis.
- Cellulitis.
- Severe cutaneous adverse reaction.
- Chemical burn.

## Primitive List

- `localized_soap_irritant_contact_dermatitis_no_infection_or_anaphylaxis.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `localized_soap_irritant_contact_dermatitis_no_infection_or_anaphylaxis.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: anaphylaxis, airway_symptoms, hypotension, secondary_skin_infection_concern, severe_cutaneous_adverse_reaction, skin_peeling_or_sloughing, mucosal_lesions, eye_or_genital_rash_location, burn_or_chemical_wound, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_dermatology_plan
- `localized_soap_irritant_contact_dermatitis_no_infection_or_anaphylaxis.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `localized_soap_irritant_contact_dermatitis_no_infection_or_anaphylaxis.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `localized_soap_irritant_contact_dermatitis_no_infection_or_anaphylaxis.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `localized_soap_irritant_contact_dermatitis_no_infection_or_anaphylaxis.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: anaphylaxis, airway_symptoms, hypotension, secondary_skin_infection_concern, severe_cutaneous_adverse_reaction, skin_peeling_or_sloughing, mucosal_lesions, eye_or_genital_rash_location, burn_or_chemical_wound, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_dermatology_plan
- `localized_soap_irritant_contact_dermatitis_no_infection_or_anaphylaxis.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: anaphylaxis, airway_symptoms, hypotension, secondary_skin_infection_concern, severe_cutaneous_adverse_reaction, skin_peeling_or_sloughing, mucosal_lesions, eye_or_genital_rash_location, burn_or_chemical_wound, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_dermatology_plan
- `localized_soap_irritant_contact_dermatitis_no_infection_or_anaphylaxis.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `localized_soap_irritant_contact_dermatitis_no_infection_or_anaphylaxis.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `localized_soap_irritant_contact_dermatitis_no_infection_or_anaphylaxis.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `localized_soap_irritant_contact_dermatitis_no_infection_or_anaphylaxis.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: anaphylaxis, airway_symptoms, hypotension, secondary_skin_infection_concern, severe_cutaneous_adverse_reaction, skin_peeling_or_sloughing, mucosal_lesions, eye_or_genital_rash_location, burn_or_chemical_wound, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_dermatology_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit localized irritant contact dermatitis from soap exposure.

WHAT WE FOUND:
Your clinician diagnosed localized soap irritant contact dermatitis. We did not find signs of anaphylaxis, severe skin reaction, eye or genital involvement, or spreading infection today.

WHAT TO DO AT HOME:
- Wash the area gently with water if the soap is still on the skin.
- Avoid the triggering soap or irritant.
- Avoid scratching the rash.

MEDICATIONS:
- Use skin or itch medicines only if prescribed or recommended.
- Do not use leftover steroid or antibiotic creams unless your clinician said they are safe.

RETURN TO ED IF:
- Trouble breathing, throat swelling, fainting, or a bodywide reaction.
- Fever, spreading redness, pus, red streaks, or worsening warmth.
- Rash near the eyes or genitals, skin peeling, mouth sores, or symptoms that worsen.

FOLLOW UP:
Follow up with primary care, urgent care, dermatology, or the ED if symptoms are not improving or your clinician told you to recheck.
```
