# Uncomplicated laryngitis without airway or deep-neck red flags

Phenotype ID: `laryngitis_uncomplicated_no_airway_or_deep_neck_red_flags`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of uncomplicated laryngitis.
- No airway symptoms, drooling, deep neck infection concern, severe throat pain, hemoptysis, neck mass, immunocompromised host, pregnancy/pediatric pathway, or specialist-directed ENT plan.

## Exclusions

- Airway symptoms, stridor, drooling, inability to swallow, deep neck infection concern, epiglottitis concern, severe throat pain, neck swelling, hemoptysis, or systemic illness.
- Immunocompromised host, pregnancy/pediatric pathway, voice-professional/specialist-directed plan, or prolonged/recurrent hoarseness requiring ENT evaluation.

## Must-Not-Miss Diagnoses

- Airway compromise.
- Epiglottitis.
- Deep neck infection.
- Laryngeal mass or malignancy signal.
- Hemoptysis.

## Primitive List

- `laryngitis_uncomplicated_no_airway_or_deep_neck_red_flags.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `laryngitis_uncomplicated_no_airway_or_deep_neck_red_flags.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: airway_symptoms, drooling, stridor_or_noisy_breathing, deep_neck_or_epiglottitis_concern, severe_throat_pain, neck_mass_or_swelling, hemoptysis, systemic_illness, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_ent_plan
- `laryngitis_uncomplicated_no_airway_or_deep_neck_red_flags.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `laryngitis_uncomplicated_no_airway_or_deep_neck_red_flags.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `laryngitis_uncomplicated_no_airway_or_deep_neck_red_flags.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `laryngitis_uncomplicated_no_airway_or_deep_neck_red_flags.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: airway_symptoms, drooling, stridor_or_noisy_breathing, deep_neck_or_epiglottitis_concern, severe_throat_pain, neck_mass_or_swelling, hemoptysis, systemic_illness, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_ent_plan
- `laryngitis_uncomplicated_no_airway_or_deep_neck_red_flags.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: airway_symptoms, drooling, stridor_or_noisy_breathing, deep_neck_or_epiglottitis_concern, severe_throat_pain, neck_mass_or_swelling, hemoptysis, systemic_illness, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_ent_plan
- `laryngitis_uncomplicated_no_airway_or_deep_neck_red_flags.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `laryngitis_uncomplicated_no_airway_or_deep_neck_red_flags.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `laryngitis_uncomplicated_no_airway_or_deep_neck_red_flags.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `laryngitis_uncomplicated_no_airway_or_deep_neck_red_flags.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: airway_symptoms, drooling, stridor_or_noisy_breathing, deep_neck_or_epiglottitis_concern, severe_throat_pain, neck_mass_or_swelling, hemoptysis, systemic_illness, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_ent_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit laryngitis, irritation or swelling around the voice box.

WHAT WE FOUND:
Your clinician diagnosed uncomplicated laryngitis. We did not find breathing trouble, drooling, deep neck infection concern, or another emergency problem today.

WHAT TO DO AT HOME:
- Rest your voice when possible.
- Drink fluids as tolerated.
- Avoid smoke, vaping, alcohol fumes, and other throat irritants.

MEDICATIONS:
- Use throat or pain medicine only if prescribed or recommended.
- Antibiotics are not part of this instruction unless your clinician gave you a separate plan.

RETURN TO ED IF:
- Trouble breathing, noisy breathing, drooling, inability to swallow, or neck swelling.
- Severe throat pain, stiff neck, fever with worsening illness, or coughing blood.
- Hoarseness lasts longer than expected or keeps returning.

FOLLOW UP:
Follow up with primary care or ENT if symptoms persist, recur, or your clinician told you to recheck.
```
