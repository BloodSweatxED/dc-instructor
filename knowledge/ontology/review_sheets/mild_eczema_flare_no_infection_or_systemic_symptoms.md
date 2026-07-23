# Mild eczema flare without infection or systemic symptoms

Phenotype ID: `mild_eczema_flare_no_infection_or_systemic_symptoms`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of mild eczema or atopic dermatitis flare.
- No secondary infection, severe/widespread flare, systemic illness, severe cutaneous adverse reaction, eye/genital involvement, immunocompromised host, or specialist-directed plan.

## Exclusions

- Cellulitis, abscess, pus, fever, secondary infection, severe pain, or rapidly spreading rash.
- Skin peeling, blistering, mucosal lesions, eye/genital involvement, severe/widespread flare, immunocompromised host, pregnancy/pediatric pathway, or specialist-directed dermatology plan.
- Medication selection not supplied by clinician.

## Must-Not-Miss Diagnoses

- Secondary skin infection.
- Eczema herpeticum.
- Stevens-Johnson syndrome or toxic epidermal necrolysis.
- Anaphylaxis or severe allergic reaction mimic.

## Primitive List

- `mild_eczema_flare_no_infection_or_systemic_symptoms.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `mild_eczema_flare_no_infection_or_systemic_symptoms.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: secondary_skin_infection_concern, abscess_or_boils_or_carbuncle, severe_cutaneous_adverse_reaction, skin_peeling_or_sloughing, mucosal_lesions, eye_or_genital_rash_location, eczema_severe_or_widespread, rapid_progression, fever, systemic_illness, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_dermatology_plan
- `mild_eczema_flare_no_infection_or_systemic_symptoms.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `mild_eczema_flare_no_infection_or_systemic_symptoms.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `mild_eczema_flare_no_infection_or_systemic_symptoms.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `mild_eczema_flare_no_infection_or_systemic_symptoms.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: secondary_skin_infection_concern, abscess_or_boils_or_carbuncle, severe_cutaneous_adverse_reaction, skin_peeling_or_sloughing, mucosal_lesions, eye_or_genital_rash_location, eczema_severe_or_widespread, rapid_progression, fever, systemic_illness, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_dermatology_plan
- `mild_eczema_flare_no_infection_or_systemic_symptoms.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: secondary_skin_infection_concern, abscess_or_boils_or_carbuncle, severe_cutaneous_adverse_reaction, skin_peeling_or_sloughing, mucosal_lesions, eye_or_genital_rash_location, eczema_severe_or_widespread, rapid_progression, fever, systemic_illness, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_dermatology_plan
- `mild_eczema_flare_no_infection_or_systemic_symptoms.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `mild_eczema_flare_no_infection_or_systemic_symptoms.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `mild_eczema_flare_no_infection_or_systemic_symptoms.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `mild_eczema_flare_no_infection_or_systemic_symptoms.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: secondary_skin_infection_concern, abscess_or_boils_or_carbuncle, severe_cutaneous_adverse_reaction, skin_peeling_or_sloughing, mucosal_lesions, eye_or_genital_rash_location, eczema_severe_or_widespread, rapid_progression, fever, systemic_illness, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_dermatology_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit a mild eczema flare.

WHAT WE FOUND:
Your clinician diagnosed a mild eczema flare. We did not find infection, a severe drug rash, or systemic illness today.

WHAT TO DO AT HOME:
- Use fragrance-free moisturizer often, especially after bathing.
- Avoid scratching when possible and keep nails short.
- Avoid known triggers such as harsh soaps, fragrances, or irritating fabrics.

MEDICATIONS:
- Use steroid, anti-itch, or other skin medicine only if prescribed or recommended.
- Use acetaminophen or ibuprofen only if you can take it safely and follow the label.

RETURN TO ED IF:
- Fever, spreading redness, warmth, pus, red streaks, or rapidly worsening pain.
- Blistering, skin peeling, mouth sores, eye symptoms, or target-like rash.
- The rash becomes widespread, severe, or does not improve with the plan you were given.

FOLLOW UP:
Follow up with primary care or dermatology if symptoms are not improving, recur often, or require ongoing medicine adjustment.
```
