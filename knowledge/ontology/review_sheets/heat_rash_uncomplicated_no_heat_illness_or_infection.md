# Uncomplicated heat rash without heat illness or infection

Phenotype ID: `heat_rash_uncomplicated_no_heat_illness_or_infection`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of uncomplicated heat rash.
- No heat illness, dehydration, secondary infection, severe/widespread rash, systemic illness, high-risk host pathway, or specialist-directed plan.

## Exclusions

- Heat exhaustion, heat stroke, syncope, confusion, dehydration, persistent vomiting, or unstable vital signs.
- Cellulitis, abscess, pus, fever, severe pain, blistering/peeling rash, severe cutaneous adverse reaction, or systemic illness.
- Pregnancy, pediatric pathway, immunocompromised host, or specialist-directed dermatology plan.

## Must-Not-Miss Diagnoses

- Heat stroke.
- Heat exhaustion.
- Secondary skin infection.
- Severe cutaneous adverse reaction.

## Primitive List

- `heat_rash_uncomplicated_no_heat_illness_or_infection.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `heat_rash_uncomplicated_no_heat_illness_or_infection.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: heat_illness_or_dehydration, syncope_or_fainting, altered_mental_status_not_resolved, unstable_vitals, secondary_skin_infection_concern, abscess_or_boils_or_carbuncle, severe_cutaneous_adverse_reaction, skin_peeling_or_sloughing, eczema_severe_or_widespread, systemic_illness, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_dermatology_plan
- `heat_rash_uncomplicated_no_heat_illness_or_infection.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `heat_rash_uncomplicated_no_heat_illness_or_infection.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `heat_rash_uncomplicated_no_heat_illness_or_infection.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `heat_rash_uncomplicated_no_heat_illness_or_infection.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: heat_illness_or_dehydration, syncope_or_fainting, altered_mental_status_not_resolved, unstable_vitals, secondary_skin_infection_concern, abscess_or_boils_or_carbuncle, severe_cutaneous_adverse_reaction, skin_peeling_or_sloughing, eczema_severe_or_widespread, systemic_illness, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_dermatology_plan
- `heat_rash_uncomplicated_no_heat_illness_or_infection.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: heat_illness_or_dehydration, syncope_or_fainting, altered_mental_status_not_resolved, unstable_vitals, secondary_skin_infection_concern, abscess_or_boils_or_carbuncle, severe_cutaneous_adverse_reaction, skin_peeling_or_sloughing, eczema_severe_or_widespread, systemic_illness, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_dermatology_plan
- `heat_rash_uncomplicated_no_heat_illness_or_infection.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `heat_rash_uncomplicated_no_heat_illness_or_infection.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `heat_rash_uncomplicated_no_heat_illness_or_infection.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `heat_rash_uncomplicated_no_heat_illness_or_infection.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: heat_illness_or_dehydration, syncope_or_fainting, altered_mental_status_not_resolved, unstable_vitals, secondary_skin_infection_concern, abscess_or_boils_or_carbuncle, severe_cutaneous_adverse_reaction, skin_peeling_or_sloughing, eczema_severe_or_widespread, systemic_illness, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_dermatology_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit heat rash.

WHAT WE FOUND:
Your clinician diagnosed uncomplicated heat rash. We did not find heat exhaustion, heat stroke, dehydration, or skin infection today.

WHAT TO DO AT HOME:
- Move to a cooler environment and avoid overheating while the rash heals.
- Keep the skin cool and dry.
- Wear loose, breathable clothing when possible.

MEDICATIONS:
- Use skin medicine only if prescribed or recommended.
- Use acetaminophen or ibuprofen only if you can take it safely and follow the label.

RETURN TO ED IF:
- Confusion, fainting, severe weakness, vomiting, dehydration, or symptoms after heat exposure that feel severe.
- Fever, spreading redness, warmth, pus, red streaks, or worsening pain.
- The rash becomes widespread, blistering, or does not improve after cooling measures.

FOLLOW UP:
Follow up with primary care or urgent care if symptoms are not improving or if the rash keeps coming back.
```
