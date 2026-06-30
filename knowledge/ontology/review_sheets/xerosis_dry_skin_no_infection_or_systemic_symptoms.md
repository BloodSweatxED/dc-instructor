# Dry skin or xerosis without infection or systemic symptoms

Phenotype ID: `xerosis_dry_skin_no_infection_or_systemic_symptoms`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of uncomplicated dry skin or xerosis.
- No secondary infection, severe eczema/psoriasis pathway, severe cutaneous adverse reaction, systemic illness, high-risk host, or specialist-directed plan.

## Exclusions

- Cellulitis, abscess, pus, bleeding fissures requiring wound care, systemic illness, severe itch with widespread rash, or severe cutaneous adverse reaction.
- Severe eczema/psoriasis flare, immunocompromised host, pregnancy/pediatric pathway, or specialist-directed dermatology plan.

## Must-Not-Miss Diagnoses

- Secondary skin infection.
- Severe cutaneous adverse reaction.
- Eczema herpeticum.
- Systemic disease with skin findings.

## Primitive List

- `xerosis_dry_skin_no_infection_or_systemic_symptoms.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `xerosis_dry_skin_no_infection_or_systemic_symptoms.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: secondary_skin_infection_concern, abscess_or_boils_or_carbuncle, wound_infection_concern, severe_cutaneous_adverse_reaction, skin_peeling_or_sloughing, mucosal_lesions, eczema_severe_or_widespread, dry_skin_complicated_or_systemic, systemic_illness, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_dermatology_plan
- `xerosis_dry_skin_no_infection_or_systemic_symptoms.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `xerosis_dry_skin_no_infection_or_systemic_symptoms.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `xerosis_dry_skin_no_infection_or_systemic_symptoms.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `xerosis_dry_skin_no_infection_or_systemic_symptoms.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: secondary_skin_infection_concern, abscess_or_boils_or_carbuncle, wound_infection_concern, severe_cutaneous_adverse_reaction, skin_peeling_or_sloughing, mucosal_lesions, eczema_severe_or_widespread, dry_skin_complicated_or_systemic, systemic_illness, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_dermatology_plan
- `xerosis_dry_skin_no_infection_or_systemic_symptoms.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: secondary_skin_infection_concern, abscess_or_boils_or_carbuncle, wound_infection_concern, severe_cutaneous_adverse_reaction, skin_peeling_or_sloughing, mucosal_lesions, eczema_severe_or_widespread, dry_skin_complicated_or_systemic, systemic_illness, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_dermatology_plan
- `xerosis_dry_skin_no_infection_or_systemic_symptoms.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `xerosis_dry_skin_no_infection_or_systemic_symptoms.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `xerosis_dry_skin_no_infection_or_systemic_symptoms.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `xerosis_dry_skin_no_infection_or_systemic_symptoms.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: secondary_skin_infection_concern, abscess_or_boils_or_carbuncle, wound_infection_concern, severe_cutaneous_adverse_reaction, skin_peeling_or_sloughing, mucosal_lesions, eczema_severe_or_widespread, dry_skin_complicated_or_systemic, systemic_illness, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_dermatology_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit dry skin, also called xerosis.

WHAT WE FOUND:
Your clinician diagnosed uncomplicated dry skin. We did not find infection, severe eczema, drug-rash warning signs, or systemic illness today.

WHAT TO DO AT HOME:
- Use fragrance-free moisturizer often, especially after washing.
- Use warm, not hot, water and gentle cleansers.
- Avoid scratching when possible and protect cracked skin from irritation.

MEDICATIONS:
- Use skin medicine only if prescribed or recommended.
- Avoid harsh products, alcohol-based products, or steroid creams unless your clinician told you to use them.

RETURN TO ED IF:
- Spreading redness, warmth, pus, fever, red streaks, or worsening pain.
- Bleeding cracks that do not heal, severe itching, widespread rash, or skin peeling/blistering.
- Symptoms do not improve with the plan you were given.

FOLLOW UP:
Follow up with primary care or dermatology if symptoms persist, recur, or become severe.
```
