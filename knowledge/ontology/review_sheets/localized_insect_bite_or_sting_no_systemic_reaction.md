# Localized insect bite or sting without systemic reaction

Phenotype ID: `localized_insect_bite_or_sting_no_systemic_reaction`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of localized insect bite or sting reaction.
- No anaphylaxis, airway symptoms, systemic reaction, venomous spider/scorpion/snake pathway, tick-borne illness concern, or cellulitis.

## Exclusions

- Anaphylaxis, airway symptoms, hypotension, syncope, vomiting, or bodywide reaction.
- Cellulitis, abscess, necrosis, severe pain, or systemic illness.
- Black widow, brown recluse, scorpion, tick-borne illness, snakebite, or specialist-directed allergy plan.

## Must-Not-Miss Diagnoses

- Anaphylaxis.
- Cellulitis.
- Necrotic spider bite.
- Scorpion envenomation.
- Tick-borne illness.
- Snakebite.

## Primitive List

- `localized_insect_bite_or_sting_no_systemic_reaction.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `localized_insect_bite_or_sting_no_systemic_reaction.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: anaphylaxis, airway_symptoms, hypotension, syncope_or_fainting, systemic_allergic_reaction, secondary_skin_infection_concern, necrotic_spider_or_scorpion_concern, tick_borne_illness_concern, snakebite_concern, specialist_directed_allergy_plan
- `localized_insect_bite_or_sting_no_systemic_reaction.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `localized_insect_bite_or_sting_no_systemic_reaction.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `localized_insect_bite_or_sting_no_systemic_reaction.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `localized_insect_bite_or_sting_no_systemic_reaction.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: anaphylaxis, airway_symptoms, hypotension, syncope_or_fainting, systemic_allergic_reaction, secondary_skin_infection_concern, necrotic_spider_or_scorpion_concern, tick_borne_illness_concern, snakebite_concern, specialist_directed_allergy_plan
- `localized_insect_bite_or_sting_no_systemic_reaction.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: anaphylaxis, airway_symptoms, hypotension, syncope_or_fainting, systemic_allergic_reaction, secondary_skin_infection_concern, necrotic_spider_or_scorpion_concern, tick_borne_illness_concern, snakebite_concern, specialist_directed_allergy_plan
- `localized_insect_bite_or_sting_no_systemic_reaction.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `localized_insect_bite_or_sting_no_systemic_reaction.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `localized_insect_bite_or_sting_no_systemic_reaction.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `localized_insect_bite_or_sting_no_systemic_reaction.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: anaphylaxis, airway_symptoms, hypotension, syncope_or_fainting, systemic_allergic_reaction, secondary_skin_infection_concern, necrotic_spider_or_scorpion_concern, tick_borne_illness_concern, snakebite_concern, specialist_directed_allergy_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit a localized insect bite or sting reaction.

WHAT WE FOUND:
Your exam was reassuring for a local skin reaction. We did not find signs of anaphylaxis, severe venom reaction, or spreading infection today.

WHAT TO DO AT HOME:
- Wash the area with soap and water.
- Use a cold pack wrapped in cloth for short periods if it helps.
- Avoid scratching the area.

MEDICATIONS:
- Use itch medicine, allergy medicine, or pain medicine only as directed on the label or by your clinician.
- Use an epinephrine injector only if one was prescribed and you were instructed to use it.

RETURN TO ED IF:
- Trouble breathing, wheezing, throat tightness, face or mouth swelling, fainting, or vomiting.
- Spreading redness, pus, fever, red streaks, or worsening pain.
- A black widow, brown recluse, scorpion, tick-borne illness, or snakebite concern comes up.

FOLLOW UP:
Follow up with primary care or allergy clinic if symptoms persist, worsen, or reactions keep happening.
```
