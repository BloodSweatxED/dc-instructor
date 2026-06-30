# Uncomplicated hives without anaphylaxis or mucosal lesions

Phenotype ID: `uncomplicated_hives_no_anaphylaxis_or_mucosal_lesions`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of uncomplicated hives or urticaria.
- No anaphylaxis, airway symptoms, mucosal lesions, systemic illness, pregnancy/pediatric pathway, or specialist-directed allergy plan.

## Exclusions

- Anaphylaxis, airway symptoms, mucosal lesions, skin peeling, target lesions, systemic illness, infection concern, pregnancy/pediatric pathway, or specialist-directed allergy plan.

## Must-Not-Miss Diagnoses

- Anaphylaxis.
- Airway swelling.
- Severe cutaneous adverse reaction.
- Systemic illness.

## Primitive List

- `uncomplicated_hives_no_anaphylaxis_or_mucosal_lesions.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `uncomplicated_hives_no_anaphylaxis_or_mucosal_lesions.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: anaphylaxis, airway_symptoms, systemic_allergic_reaction, mucosal_lesions, systemic_illness, biphasic_reaction_concern, pregnancy, pediatric_pathway, specialist_directed_allergy_plan
- `uncomplicated_hives_no_anaphylaxis_or_mucosal_lesions.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `uncomplicated_hives_no_anaphylaxis_or_mucosal_lesions.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `uncomplicated_hives_no_anaphylaxis_or_mucosal_lesions.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `uncomplicated_hives_no_anaphylaxis_or_mucosal_lesions.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: anaphylaxis, airway_symptoms, systemic_allergic_reaction, mucosal_lesions, systemic_illness, biphasic_reaction_concern, pregnancy, pediatric_pathway, specialist_directed_allergy_plan
- `uncomplicated_hives_no_anaphylaxis_or_mucosal_lesions.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: anaphylaxis, airway_symptoms, systemic_allergic_reaction, mucosal_lesions, systemic_illness, biphasic_reaction_concern, pregnancy, pediatric_pathway, specialist_directed_allergy_plan
- `uncomplicated_hives_no_anaphylaxis_or_mucosal_lesions.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `uncomplicated_hives_no_anaphylaxis_or_mucosal_lesions.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `uncomplicated_hives_no_anaphylaxis_or_mucosal_lesions.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `uncomplicated_hives_no_anaphylaxis_or_mucosal_lesions.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: anaphylaxis, airway_symptoms, systemic_allergic_reaction, mucosal_lesions, systemic_illness, biphasic_reaction_concern, pregnancy, pediatric_pathway, specialist_directed_allergy_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit uncomplicated hives.

WHAT WE FOUND:
Your clinician diagnosed hives and did not find anaphylaxis, mucosal lesions, infection, or another emergency problem today.

WHAT TO DO AT HOME:
- Avoid the trigger if one was identified.
- Use cool compresses if they help itching.
- Do not scratch the rash if you can avoid it.

MEDICATIONS:
- Take antihistamines or other medicines only as prescribed or recommended.
- Do not take sedating medicine before driving or working if it makes you sleepy.

RETURN TO ED IF:
- Trouble breathing, throat or tongue swelling, fainting, vomiting with rash, or symptoms involving more than one body system.
- Skin peeling, mouth sores, target lesions, fever, or feeling very ill.
- Hives that keep returning, worsen quickly, or do not improve as expected.

FOLLOW UP:
Follow up with primary care, allergy, urgent care, or the ED if symptoms are not improving or your clinician told you to recheck.
```
