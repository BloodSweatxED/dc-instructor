# Nasal dryness without epistaxis or infection red flags

Phenotype ID: `nasal_dryness_no_epistaxis_or_infection`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of dry, cracked nose skin or nose xerosis.
- No skin infection, deep open wound, severe cutaneous reaction, systemic illness, immunocompromised host, pregnancy/pediatric pathway, or specialist-directed plan.

## Exclusions

- Skin infection, cellulitis, abscess, deep open wound, severe cutaneous adverse reaction, skin peeling or sloughing, mucosal lesions, systemic illness, immunocompromised host, pregnancy/pediatric pathway, or specialist-directed dermatology/wound plan.

## Must-Not-Miss Diagnoses

- Cellulitis.
- Abscess or wound infection.
- Severe cutaneous adverse reaction.
- Systemic skin disease flare requiring separate care.
- Epistaxis requiring treatment.
- Nasal trauma.

## Primitive List

- `nasal_dryness_no_epistaxis_or_infection.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `nasal_dryness_no_epistaxis_or_infection.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: abscess_concern, facial_or_nasal_trauma, immunocompromised, mucosal_lesions, open_wound, pediatric_pathway, posterior_epistaxis_or_uncontrolled_bleeding, pregnancy, secondary_skin_infection_concern, severe_cutaneous_adverse_reaction, skin_peeling_or_sloughing, specialist_directed_dermatology_plan, specialist_directed_ent_plan, specialist_directed_wound_plan, systemic_illness, wound_infection_concern
- `nasal_dryness_no_epistaxis_or_infection.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `nasal_dryness_no_epistaxis_or_infection.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `nasal_dryness_no_epistaxis_or_infection.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `nasal_dryness_no_epistaxis_or_infection.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: abscess_concern, facial_or_nasal_trauma, immunocompromised, mucosal_lesions, open_wound, pediatric_pathway, posterior_epistaxis_or_uncontrolled_bleeding, pregnancy, secondary_skin_infection_concern, severe_cutaneous_adverse_reaction, skin_peeling_or_sloughing, specialist_directed_dermatology_plan, specialist_directed_ent_plan, specialist_directed_wound_plan, systemic_illness, wound_infection_concern
- `nasal_dryness_no_epistaxis_or_infection.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: abscess_concern, facial_or_nasal_trauma, immunocompromised, mucosal_lesions, open_wound, pediatric_pathway, posterior_epistaxis_or_uncontrolled_bleeding, pregnancy, secondary_skin_infection_concern, severe_cutaneous_adverse_reaction, skin_peeling_or_sloughing, specialist_directed_dermatology_plan, specialist_directed_ent_plan, specialist_directed_wound_plan, systemic_illness, wound_infection_concern
- `nasal_dryness_no_epistaxis_or_infection.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `nasal_dryness_no_epistaxis_or_infection.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `nasal_dryness_no_epistaxis_or_infection.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `nasal_dryness_no_epistaxis_or_infection.return_precautions.return_precaution_4.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `nasal_dryness_no_epistaxis_or_infection.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: abscess_concern, facial_or_nasal_trauma, immunocompromised, mucosal_lesions, open_wound, pediatric_pathway, posterior_epistaxis_or_uncontrolled_bleeding, pregnancy, secondary_skin_infection_concern, severe_cutaneous_adverse_reaction, skin_peeling_or_sloughing, specialist_directed_dermatology_plan, specialist_directed_ent_plan, specialist_directed_wound_plan, systemic_illness, wound_infection_concern

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit dry, cracked skin on the nose.

WHAT WE FOUND:
Your clinician diagnosed dry, cracked nose skin. We did not find skin infection, open deep wound, severe rash, systemic illness, or another skin emergency today.

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
- Nosebleed that will not stop, facial trauma, or worsening nasal swelling.

FOLLOW UP:
Follow up with primary care, urgent care, dermatology, or the ED if symptoms are not improving or your clinician told you to recheck.
```
