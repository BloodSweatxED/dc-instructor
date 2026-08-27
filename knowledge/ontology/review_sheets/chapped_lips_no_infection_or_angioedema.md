# Chapped lips without infection or angioedema red flags

Phenotype ID: `chapped_lips_no_infection_or_angioedema`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of dry, cracked lips skin or lips xerosis.
- No skin infection, deep open wound, severe cutaneous reaction, systemic illness, immunocompromised host, pregnancy/pediatric pathway, or specialist-directed plan.

## Exclusions

- Skin infection, cellulitis, abscess, deep open wound, severe cutaneous adverse reaction, skin peeling or sloughing, mucosal lesions, systemic illness, immunocompromised host, pregnancy/pediatric pathway, or specialist-directed dermatology/wound plan.

## Must-Not-Miss Diagnoses

- Cellulitis.
- Abscess or wound infection.
- Severe cutaneous adverse reaction.
- Systemic skin disease flare requiring separate care.

## Primitive List

- `chapped_lips_no_infection_or_angioedema.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `chapped_lips_no_infection_or_angioedema.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: abscess_concern, airway_symptoms, anaphylaxis, deep_space_swelling, immunocompromised, mucosal_lesions, open_wound, pediatric_pathway, pregnancy, secondary_skin_infection_concern, severe_cutaneous_adverse_reaction, skin_peeling_or_sloughing, specialist_directed_dermatology_plan, specialist_directed_wound_plan, systemic_allergic_reaction, systemic_illness, wound_infection_concern
- `chapped_lips_no_infection_or_angioedema.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `chapped_lips_no_infection_or_angioedema.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `chapped_lips_no_infection_or_angioedema.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `chapped_lips_no_infection_or_angioedema.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: abscess_concern, airway_symptoms, anaphylaxis, deep_space_swelling, immunocompromised, mucosal_lesions, open_wound, pediatric_pathway, pregnancy, secondary_skin_infection_concern, severe_cutaneous_adverse_reaction, skin_peeling_or_sloughing, specialist_directed_dermatology_plan, specialist_directed_wound_plan, systemic_allergic_reaction, systemic_illness, wound_infection_concern
- `chapped_lips_no_infection_or_angioedema.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: abscess_concern, airway_symptoms, anaphylaxis, deep_space_swelling, immunocompromised, mucosal_lesions, open_wound, pediatric_pathway, pregnancy, secondary_skin_infection_concern, severe_cutaneous_adverse_reaction, skin_peeling_or_sloughing, specialist_directed_dermatology_plan, specialist_directed_wound_plan, systemic_allergic_reaction, systemic_illness, wound_infection_concern
- `chapped_lips_no_infection_or_angioedema.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `chapped_lips_no_infection_or_angioedema.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `chapped_lips_no_infection_or_angioedema.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `chapped_lips_no_infection_or_angioedema.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: abscess_concern, airway_symptoms, anaphylaxis, deep_space_swelling, immunocompromised, mucosal_lesions, open_wound, pediatric_pathway, pregnancy, secondary_skin_infection_concern, severe_cutaneous_adverse_reaction, skin_peeling_or_sloughing, specialist_directed_dermatology_plan, specialist_directed_wound_plan, systemic_allergic_reaction, systemic_illness, wound_infection_concern

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit dry, cracked skin on the lips.

WHAT WE FOUND:
Your clinician diagnosed dry, cracked lips skin. We did not find skin infection, open deep wound, severe rash, systemic illness, or another skin emergency today.

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
