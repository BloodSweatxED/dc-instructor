# Uncomplicated head lice without secondary infection

Phenotype ID: `pediculosis_capitis_uncomplicated_no_secondary_infection`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of uncomplicated scalp head lice.
- No secondary skin infection, eyelash/eyebrow involvement, body lice, pubic lice/STI pathway, systemic allergic reaction, pregnancy/pediatric pathway, or specialist-directed plan.

## Exclusions

- Cellulitis, impetigo, abscess, pus, fever, or systemic illness.
- Eyelash/eyebrow lice, body lice, pubic lice/STI pathway, treatment toxicity, immunocompromised host, pregnancy/pediatric pathway, or specialist-directed dermatology plan.

## Must-Not-Miss Diagnoses

- Secondary skin infection.
- Treatment toxicity.
- Pubic lice/STI pathway.
- Eyelash lice needing eye-specific care.

## Primitive List

- `pediculosis_capitis_uncomplicated_no_secondary_infection.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `pediculosis_capitis_uncomplicated_no_secondary_infection.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: secondary_skin_infection_concern, abscess_or_boils_or_carbuncle, systemic_illness, head_lice_complicated_or_non_scalp, chemical_exposure_or_toxic_treatment, near_eye_or_genitals, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_dermatology_plan
- `pediculosis_capitis_uncomplicated_no_secondary_infection.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `pediculosis_capitis_uncomplicated_no_secondary_infection.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `pediculosis_capitis_uncomplicated_no_secondary_infection.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `pediculosis_capitis_uncomplicated_no_secondary_infection.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: secondary_skin_infection_concern, abscess_or_boils_or_carbuncle, systemic_illness, head_lice_complicated_or_non_scalp, chemical_exposure_or_toxic_treatment, near_eye_or_genitals, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_dermatology_plan
- `pediculosis_capitis_uncomplicated_no_secondary_infection.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: secondary_skin_infection_concern, abscess_or_boils_or_carbuncle, systemic_illness, head_lice_complicated_or_non_scalp, chemical_exposure_or_toxic_treatment, near_eye_or_genitals, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_dermatology_plan
- `pediculosis_capitis_uncomplicated_no_secondary_infection.medications.medication_guidance_3.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: secondary_skin_infection_concern, abscess_or_boils_or_carbuncle, systemic_illness, head_lice_complicated_or_non_scalp, chemical_exposure_or_toxic_treatment, near_eye_or_genitals, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_dermatology_plan
- `pediculosis_capitis_uncomplicated_no_secondary_infection.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `pediculosis_capitis_uncomplicated_no_secondary_infection.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `pediculosis_capitis_uncomplicated_no_secondary_infection.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `pediculosis_capitis_uncomplicated_no_secondary_infection.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: secondary_skin_infection_concern, abscess_or_boils_or_carbuncle, systemic_illness, head_lice_complicated_or_non_scalp, chemical_exposure_or_toxic_treatment, near_eye_or_genitals, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_dermatology_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit head lice, also called pediculosis capitis.

WHAT WE FOUND:
Your clinician diagnosed uncomplicated scalp head lice. We did not find secondary skin infection, body or pubic lice, eyelash involvement, or another emergency problem today.

WHAT TO DO AT HOME:
- Avoid sharing combs, brushes, hats, towels, pillows, or hair items until treatment is complete.
- Check close contacts as your clinician recommended.
- Wash recently used bedding, hats, and towels according to the plan you were given.

MEDICATIONS:
- Use lice medicine only as prescribed or recommended, and follow the directions closely.
- Do not use extra doses, pesticides, gasoline, kerosene, or home chemicals on the scalp.
- Ask before repeating treatment if symptoms continue.

RETURN TO ED IF:
- Spreading redness, pus, fever, swollen painful skin, or red streaks.
- Lice involve eyelashes, eyebrows, body hair, or pubic hair.
- Rash, swelling, trouble breathing, or severe irritation after a treatment.

FOLLOW UP:
Follow up with primary care, dermatology, or school/occupational health if lice persist, contacts keep getting reinfested, or treatment is not working.
```
