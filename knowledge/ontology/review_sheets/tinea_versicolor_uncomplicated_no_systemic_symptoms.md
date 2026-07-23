# Uncomplicated tinea versicolor without systemic symptoms

Phenotype ID: `tinea_versicolor_uncomplicated_no_systemic_symptoms`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of uncomplicated tinea versicolor.
- No secondary infection, severe cutaneous adverse reaction, systemic illness, immunocompromised host, pregnancy/pediatric pathway, or specialist-directed plan.

## Exclusions

- Cellulitis, abscess, pus, fever, systemic illness, severe cutaneous adverse reaction, mucosal lesions, or skin peeling/sloughing.
- Immunocompromised host, extensive/recurrent rash needing individualized plan, pregnancy/pediatric pathway, or specialist-directed dermatology plan.

## Must-Not-Miss Diagnoses

- Secondary skin infection.
- Severe cutaneous adverse reaction.
- Systemic illness with rash.
- Immunocompromised-host fungal disease.

## Primitive List

- `tinea_versicolor_uncomplicated_no_systemic_symptoms.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `tinea_versicolor_uncomplicated_no_systemic_symptoms.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: secondary_skin_infection_concern, abscess_or_boils_or_carbuncle, severe_cutaneous_adverse_reaction, skin_peeling_or_sloughing, mucosal_lesions, systemic_illness, immunocompromised, extensive_or_recurrent_fungal_rash, pregnancy, pediatric_pathway, specialist_directed_dermatology_plan
- `tinea_versicolor_uncomplicated_no_systemic_symptoms.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `tinea_versicolor_uncomplicated_no_systemic_symptoms.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `tinea_versicolor_uncomplicated_no_systemic_symptoms.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `tinea_versicolor_uncomplicated_no_systemic_symptoms.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: secondary_skin_infection_concern, abscess_or_boils_or_carbuncle, severe_cutaneous_adverse_reaction, skin_peeling_or_sloughing, mucosal_lesions, systemic_illness, immunocompromised, extensive_or_recurrent_fungal_rash, pregnancy, pediatric_pathway, specialist_directed_dermatology_plan
- `tinea_versicolor_uncomplicated_no_systemic_symptoms.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: secondary_skin_infection_concern, abscess_or_boils_or_carbuncle, severe_cutaneous_adverse_reaction, skin_peeling_or_sloughing, mucosal_lesions, systemic_illness, immunocompromised, extensive_or_recurrent_fungal_rash, pregnancy, pediatric_pathway, specialist_directed_dermatology_plan
- `tinea_versicolor_uncomplicated_no_systemic_symptoms.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `tinea_versicolor_uncomplicated_no_systemic_symptoms.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `tinea_versicolor_uncomplicated_no_systemic_symptoms.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `tinea_versicolor_uncomplicated_no_systemic_symptoms.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: secondary_skin_infection_concern, abscess_or_boils_or_carbuncle, severe_cutaneous_adverse_reaction, skin_peeling_or_sloughing, mucosal_lesions, systemic_illness, immunocompromised, extensive_or_recurrent_fungal_rash, pregnancy, pediatric_pathway, specialist_directed_dermatology_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit tinea versicolor, a superficial fungal skin rash.

WHAT WE FOUND:
Your clinician diagnosed uncomplicated tinea versicolor. We did not find cellulitis, drug-rash warning signs, systemic illness, or immunocompromised-host risk today.

WHAT TO DO AT HOME:
- Keep skin clean and dry.
- Avoid picking or scratching irritated areas.
- Protect affected skin from sunburn while the color changes fade.

MEDICATIONS:
- Use antifungal medicine only as prescribed or recommended.
- Skin color can take time to even out after the fungus is controlled.

RETURN TO ED IF:
- Spreading redness, warmth, pus, fever, red streaks, or worsening pain.
- Skin peeling, mouth sores, target-like rash, or facial swelling after a medicine.
- Rash becomes widespread, painful, recurrent, or does not improve with the plan.

FOLLOW UP:
Follow up with primary care or dermatology if symptoms persist, recur often, spread, or the diagnosis is uncertain.
```
