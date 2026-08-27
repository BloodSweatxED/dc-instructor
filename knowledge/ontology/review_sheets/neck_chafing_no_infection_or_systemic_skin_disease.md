# Neck chafing without infection or systemic skin disease

Phenotype ID: `neck_chafing_no_infection_or_systemic_skin_disease`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of neck chafing.
- No infection, abscess, deep wound, mucosal emergency, pregnancy/pediatric pathway, or specialist-directed plan.

## Exclusions

- Cellulitis, abscess, deep wound, severe or spreading rash, systemic illness, mucosal emergency, pregnancy/pediatric pathway, or specialist-directed plan.

## Must-Not-Miss Diagnoses

- Cellulitis or abscess.
- Deep-space oral infection when mouth symptoms are present.
- Severe cutaneous adverse reaction.
- Retained foreign body or deep wound.

## Primitive List

- `neck_chafing_no_infection_or_systemic_skin_disease.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `neck_chafing_no_infection_or_systemic_skin_disease.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fever, immunocompromised, mucosal_lesions, pediatric_pathway, pregnancy, rapid_progression, secondary_skin_infection_concern, sepsis, severe_cutaneous_adverse_reaction, specialist_directed_dermatology_plan
- `neck_chafing_no_infection_or_systemic_skin_disease.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `neck_chafing_no_infection_or_systemic_skin_disease.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `neck_chafing_no_infection_or_systemic_skin_disease.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `neck_chafing_no_infection_or_systemic_skin_disease.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fever, immunocompromised, mucosal_lesions, pediatric_pathway, pregnancy, rapid_progression, secondary_skin_infection_concern, sepsis, severe_cutaneous_adverse_reaction, specialist_directed_dermatology_plan
- `neck_chafing_no_infection_or_systemic_skin_disease.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fever, immunocompromised, mucosal_lesions, pediatric_pathway, pregnancy, rapid_progression, secondary_skin_infection_concern, sepsis, severe_cutaneous_adverse_reaction, specialist_directed_dermatology_plan
- `neck_chafing_no_infection_or_systemic_skin_disease.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `neck_chafing_no_infection_or_systemic_skin_disease.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `neck_chafing_no_infection_or_systemic_skin_disease.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `neck_chafing_no_infection_or_systemic_skin_disease.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fever, immunocompromised, mucosal_lesions, pediatric_pathway, pregnancy, rapid_progression, secondary_skin_infection_concern, sepsis, severe_cutaneous_adverse_reaction, specialist_directed_dermatology_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit neck chafing.

WHAT WE FOUND:
Your clinician diagnosed neck chafing. We did not find infection, deep injury, or another emergency skin or mouth problem today.

WHAT TO DO AT HOME:
- Keep the area clean and dry.
- Avoid the friction, product, or trigger that seems to be irritating the area.
- Use gentle skin or mouth care only as your clinician recommended.

MEDICATIONS:
- Use creams, ointments, rinses, itch medicine, or pain medicine only if prescribed or recommended.
- Do not use leftover antibiotics or steroid medicine unless your clinician told you to.

RETURN TO ED IF:
- Fever, spreading redness, warmth, pus, red streaks, rapidly worsening pain, or swelling.
- Mouth sores that spread, trouble swallowing, trouble opening your mouth, or face or neck swelling.
- Symptoms that worsen or do not improve as expected.

FOLLOW UP:
Follow up with primary care, urgent care, dentistry, dermatology, or the ED if symptoms are not improving or your clinician told you to recheck.
```
