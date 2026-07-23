# Localized flea bites without infection or anaphylaxis

Phenotype ID: `localized_flea_bites_no_infection_or_anaphylaxis`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of localized flea bites.
- No anaphylaxis, systemic allergic reaction, secondary infection, necrotic spider bite, tick-borne illness concern, or snakebite concern.

## Exclusions

- Anaphylaxis, systemic allergic reaction, secondary infection, necrotic spider or scorpion concern, tick-borne illness concern, snakebite concern, immunocompromised host, or specialist-directed allergy plan.

## Must-Not-Miss Diagnoses

- Anaphylaxis.
- Cellulitis.
- Tick-borne illness.
- Venomous bite or sting emergency.

## Primitive List

- `localized_flea_bites_no_infection_or_anaphylaxis.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `localized_flea_bites_no_infection_or_anaphylaxis.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: anaphylaxis, airway_symptoms, systemic_allergic_reaction, secondary_skin_infection_concern, necrotic_spider_or_scorpion_concern, tick_borne_illness_concern, snakebite_concern, immunocompromised, specialist_directed_allergy_plan
- `localized_flea_bites_no_infection_or_anaphylaxis.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `localized_flea_bites_no_infection_or_anaphylaxis.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `localized_flea_bites_no_infection_or_anaphylaxis.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `localized_flea_bites_no_infection_or_anaphylaxis.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: anaphylaxis, airway_symptoms, systemic_allergic_reaction, secondary_skin_infection_concern, necrotic_spider_or_scorpion_concern, tick_borne_illness_concern, snakebite_concern, immunocompromised, specialist_directed_allergy_plan
- `localized_flea_bites_no_infection_or_anaphylaxis.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: anaphylaxis, airway_symptoms, systemic_allergic_reaction, secondary_skin_infection_concern, necrotic_spider_or_scorpion_concern, tick_borne_illness_concern, snakebite_concern, immunocompromised, specialist_directed_allergy_plan
- `localized_flea_bites_no_infection_or_anaphylaxis.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `localized_flea_bites_no_infection_or_anaphylaxis.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `localized_flea_bites_no_infection_or_anaphylaxis.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `localized_flea_bites_no_infection_or_anaphylaxis.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: anaphylaxis, airway_symptoms, systemic_allergic_reaction, secondary_skin_infection_concern, necrotic_spider_or_scorpion_concern, tick_borne_illness_concern, snakebite_concern, immunocompromised, specialist_directed_allergy_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit a local skin reaction from flea bites.

WHAT WE FOUND:
Your clinician diagnosed localized flea bites. We did not find signs of anaphylaxis, serious allergic reaction, spreading infection, or a bite emergency today.

WHAT TO DO AT HOME:
- Avoid scratching the bites.
- Wash the area gently with soap and water.
- Use cool compresses for itching or swelling.

MEDICATIONS:
- Use itch or allergy medicines only if prescribed or recommended.
- Use acetaminophen or ibuprofen only if you can take it safely and follow the label.

RETURN TO ED IF:
- Trouble breathing, throat swelling, vomiting after a bite, fainting, or a bodywide reaction.
- Spreading redness, pus, fever, red streaks, or worsening warmth.
- Symptoms that worsen or do not improve as expected.

FOLLOW UP:
Follow up with primary care, urgent care, or the ED if symptoms are not improving or your clinician told you to recheck.
```
