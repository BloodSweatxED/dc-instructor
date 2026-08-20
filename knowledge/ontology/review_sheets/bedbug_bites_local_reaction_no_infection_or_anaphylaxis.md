# Bedbug bites with local reaction and no infection or anaphylaxis

Phenotype ID: `bedbug_bites_local_reaction_no_infection_or_anaphylaxis`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of bedbug bites with local skin reaction.
- No anaphylaxis, systemic allergic reaction, secondary infection, systemic illness, high-risk host pathway, or uncertain bite diagnosis needing another pathway.

## Exclusions

- Anaphylaxis, airway symptoms, hypotension, syncope, diffuse hives, or systemic allergic reaction.
- Secondary skin infection, cellulitis, abscess, fever, systemic illness, immunocompromised host, or poor follow-up.
- Tick, spider, scorpion, snake, or travel-related disease concern.

## Must-Not-Miss Diagnoses

- Anaphylaxis.
- Cellulitis.
- Scabies or other infestation mimic.
- Tick-borne illness when relevant.

## Primitive List

- `bedbug_bites_local_reaction_no_infection_or_anaphylaxis.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `bedbug_bites_local_reaction_no_infection_or_anaphylaxis.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: anaphylaxis, airway_symptoms, hypotension, syncope_or_fainting, systemic_allergic_reaction, secondary_skin_infection_concern, abscess_concern, systemic_illness, immunocompromised, tick_borne_illness_concern, necrotic_spider_or_scorpion_concern, snakebite_concern, poor_follow_up
- `bedbug_bites_local_reaction_no_infection_or_anaphylaxis.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `bedbug_bites_local_reaction_no_infection_or_anaphylaxis.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `bedbug_bites_local_reaction_no_infection_or_anaphylaxis.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `bedbug_bites_local_reaction_no_infection_or_anaphylaxis.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: anaphylaxis, airway_symptoms, hypotension, syncope_or_fainting, systemic_allergic_reaction, secondary_skin_infection_concern, abscess_concern, systemic_illness, immunocompromised, tick_borne_illness_concern, necrotic_spider_or_scorpion_concern, snakebite_concern, poor_follow_up
- `bedbug_bites_local_reaction_no_infection_or_anaphylaxis.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: anaphylaxis, airway_symptoms, hypotension, syncope_or_fainting, systemic_allergic_reaction, secondary_skin_infection_concern, abscess_concern, systemic_illness, immunocompromised, tick_borne_illness_concern, necrotic_spider_or_scorpion_concern, snakebite_concern, poor_follow_up
- `bedbug_bites_local_reaction_no_infection_or_anaphylaxis.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `bedbug_bites_local_reaction_no_infection_or_anaphylaxis.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `bedbug_bites_local_reaction_no_infection_or_anaphylaxis.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `bedbug_bites_local_reaction_no_infection_or_anaphylaxis.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: anaphylaxis, airway_symptoms, hypotension, syncope_or_fainting, systemic_allergic_reaction, secondary_skin_infection_concern, abscess_concern, systemic_illness, immunocompromised, tick_borne_illness_concern, necrotic_spider_or_scorpion_concern, snakebite_concern, poor_follow_up

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit local skin reactions from bedbug bites.

WHAT WE FOUND:
Your clinician diagnosed bedbug bites today. We did not find anaphylaxis, secondary skin infection, or another emergency rash problem.

WHAT TO DO AT HOME:
- Avoid scratching the bites.
- Keep the skin clean.
- Address the bedbug source in the home or sleeping area to prevent more bites.

MEDICATIONS:
- Use itch medicine or skin cream only as directed by your clinician or the product label.
- Use acetaminophen or ibuprofen only if you can take it safely and follow the label.

RETURN TO ED IF:
- Trouble breathing, throat swelling, fainting, or widespread allergic symptoms.
- Fever, spreading redness, warmth, pus, red streaks, or severe pain.
- Bites continue because the infestation cannot be controlled.

FOLLOW UP:
Follow up with primary care, urgent care, or dermatology if itching is not improving, signs of infection develop, or bites continue.
```
