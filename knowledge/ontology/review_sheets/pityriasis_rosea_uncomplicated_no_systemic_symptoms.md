# Uncomplicated pityriasis rosea without systemic symptoms

Phenotype ID: `pityriasis_rosea_uncomplicated_no_systemic_symptoms`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of uncomplicated pityriasis rosea.
- No severe cutaneous adverse reaction, mucosal lesions, infection, systemic illness, pregnancy, immunocompromised host, or specialist-directed plan.

## Exclusions

- Severe cutaneous adverse reaction, mucosal lesions, skin peeling/sloughing, target lesions, cellulitis, abscess, fever, or systemic illness.
- Pregnancy, medication reaction concern, immunocompromised host, pediatric pathway, STI/syphilis concern, or specialist-directed dermatology plan.

## Must-Not-Miss Diagnoses

- Severe cutaneous adverse reaction.
- Secondary syphilis or STI mimic.
- Pityriasis rosea in pregnancy.
- Secondary skin infection.

## Primitive List

- `pityriasis_rosea_uncomplicated_no_systemic_symptoms.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `pityriasis_rosea_uncomplicated_no_systemic_symptoms.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: severe_cutaneous_adverse_reaction, skin_peeling_or_sloughing, mucosal_lesions, secondary_skin_infection_concern, systemic_illness, pregnancy, immunocompromised, pediatric_pathway, sti_or_genital_pathway, specialist_directed_dermatology_plan
- `pityriasis_rosea_uncomplicated_no_systemic_symptoms.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `pityriasis_rosea_uncomplicated_no_systemic_symptoms.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `pityriasis_rosea_uncomplicated_no_systemic_symptoms.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `pityriasis_rosea_uncomplicated_no_systemic_symptoms.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: severe_cutaneous_adverse_reaction, skin_peeling_or_sloughing, mucosal_lesions, secondary_skin_infection_concern, systemic_illness, pregnancy, immunocompromised, pediatric_pathway, sti_or_genital_pathway, specialist_directed_dermatology_plan
- `pityriasis_rosea_uncomplicated_no_systemic_symptoms.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: severe_cutaneous_adverse_reaction, skin_peeling_or_sloughing, mucosal_lesions, secondary_skin_infection_concern, systemic_illness, pregnancy, immunocompromised, pediatric_pathway, sti_or_genital_pathway, specialist_directed_dermatology_plan
- `pityriasis_rosea_uncomplicated_no_systemic_symptoms.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `pityriasis_rosea_uncomplicated_no_systemic_symptoms.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `pityriasis_rosea_uncomplicated_no_systemic_symptoms.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `pityriasis_rosea_uncomplicated_no_systemic_symptoms.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: severe_cutaneous_adverse_reaction, skin_peeling_or_sloughing, mucosal_lesions, secondary_skin_infection_concern, systemic_illness, pregnancy, immunocompromised, pediatric_pathway, sti_or_genital_pathway, specialist_directed_dermatology_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit pityriasis rosea, a common self-limited rash.

WHAT WE FOUND:
Your clinician diagnosed uncomplicated pityriasis rosea. We did not find drug-rash warning signs, infection, pregnancy-related concern, or systemic illness today.

WHAT TO DO AT HOME:
- Avoid scratching when possible.
- Use gentle skin care and avoid harsh soaps or fragranced products.
- Keep follow-up if the rash changes or does not improve as expected.

MEDICATIONS:
- Use itch or skin medicine only if prescribed or recommended.
- Stop any new product that worsens the rash unless your clinician told you otherwise.

RETURN TO ED IF:
- Fever, feeling very ill, spreading redness, pus, severe pain, or red streaks.
- Mouth sores, eye pain, skin peeling, blistering, target-like lesions, or facial swelling.
- Pregnancy, new medication concern, or rash that rapidly worsens or does not follow the expected course.

FOLLOW UP:
Follow up with primary care or dermatology if symptoms persist, worsen, recur, or the diagnosis is uncertain.
```
