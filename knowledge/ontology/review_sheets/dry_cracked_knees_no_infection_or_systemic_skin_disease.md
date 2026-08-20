# Dry cracked knees without infection or systemic skin-disease red flags

Phenotype ID: `dry_cracked_knees_no_infection_or_systemic_skin_disease`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of dry, cracked knee skin or knee xerosis.
- No skin infection, deep open wound, severe cutaneous reaction, systemic illness, immunocompromised host, pregnancy/pediatric pathway, or specialist-directed plan.

## Exclusions

- Skin infection, cellulitis, abscess, deep open wound, severe cutaneous adverse reaction, skin peeling or sloughing, mucosal lesions, systemic illness, immunocompromised host, pregnancy/pediatric pathway, or specialist-directed dermatology/wound plan.

## Must-Not-Miss Diagnoses

- Cellulitis.
- Abscess or wound infection.
- Severe cutaneous adverse reaction.
- Systemic skin disease flare requiring separate care.

## Primitive List

- `dry_cracked_knees_no_infection_or_systemic_skin_disease.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `dry_cracked_knees_no_infection_or_systemic_skin_disease.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: secondary_skin_infection_concern, abscess_or_boils_or_carbuncle, open_wound, wound_infection_concern, severe_cutaneous_adverse_reaction, skin_peeling_or_sloughing, mucosal_lesions, systemic_illness, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_dermatology_plan, specialist_directed_wound_plan
- `dry_cracked_knees_no_infection_or_systemic_skin_disease.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `dry_cracked_knees_no_infection_or_systemic_skin_disease.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `dry_cracked_knees_no_infection_or_systemic_skin_disease.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `dry_cracked_knees_no_infection_or_systemic_skin_disease.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: secondary_skin_infection_concern, abscess_or_boils_or_carbuncle, open_wound, wound_infection_concern, severe_cutaneous_adverse_reaction, skin_peeling_or_sloughing, mucosal_lesions, systemic_illness, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_dermatology_plan, specialist_directed_wound_plan
- `dry_cracked_knees_no_infection_or_systemic_skin_disease.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: secondary_skin_infection_concern, abscess_or_boils_or_carbuncle, open_wound, wound_infection_concern, severe_cutaneous_adverse_reaction, skin_peeling_or_sloughing, mucosal_lesions, systemic_illness, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_dermatology_plan, specialist_directed_wound_plan
- `dry_cracked_knees_no_infection_or_systemic_skin_disease.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `dry_cracked_knees_no_infection_or_systemic_skin_disease.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `dry_cracked_knees_no_infection_or_systemic_skin_disease.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `dry_cracked_knees_no_infection_or_systemic_skin_disease.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: secondary_skin_infection_concern, abscess_or_boils_or_carbuncle, open_wound, wound_infection_concern, severe_cutaneous_adverse_reaction, skin_peeling_or_sloughing, mucosal_lesions, systemic_illness, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_dermatology_plan, specialist_directed_wound_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit dry, cracked skin on the knees.

WHAT WE FOUND:
Your clinician diagnosed dry, cracked knee skin. We did not find skin infection, open deep wound, severe rash, systemic illness, or another skin emergency today.

WHAT TO DO AT HOME:
- Use gentle skin care and avoid harsh soaps, scrubbing, or triggers that worsen the dryness.
- Use moisturizer, protective covering, or activity limits only as your clinician recommended.
- Avoid picking or scratching the cracked skin.

MEDICATIONS:
- Use creams, ointments, itch medicine, or other skin medicine only if prescribed or recommended.
- Do not use leftover steroid, antibiotic, or antifungal medicine unless your clinician told you to.

RETURN TO ED IF:
- Fever, spreading redness, warmth, pus, red streaks, rapidly worsening pain, or worsening swelling.
- Skin peeling, mouth sores, a bodywide rash, or feeling very ill.
- Symptoms that worsen or do not improve as expected.

FOLLOW UP:
Follow up with primary care, urgent care, dermatology, or the ED if symptoms are not improving or your clinician told you to recheck.
```
