# Mild allergic rhinitis without wheeze or anaphylaxis

Phenotype ID: `mild_allergic_rhinitis_no_wheeze_or_anaphylaxis`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of mild allergic rhinitis.
- No anaphylaxis, airway symptoms, wheeze/asthma flare, bacterial sinusitis concern, systemic illness, or specialist-directed allergy plan.

## Exclusions

- Anaphylaxis, throat/tongue swelling, wheeze, asthma/COPD exacerbation, respiratory distress, or hypoxia.
- Bacterial sinusitis concern, severe facial pain, fever, orbital symptoms, systemic illness, pregnancy/pediatric pathway, or specialist-directed allergy plan.

## Must-Not-Miss Diagnoses

- Anaphylaxis.
- Asthma exacerbation.
- Bacterial sinusitis complication.
- Orbital cellulitis.

## Primitive List

- `mild_allergic_rhinitis_no_wheeze_or_anaphylaxis.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `mild_allergic_rhinitis_no_wheeze_or_anaphylaxis.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: airway_symptoms, anaphylaxis, systemic_allergic_reaction, hypoxia, respiratory_distress, copd_or_asthma_exacerbation_pathway, severe_bacterial_sinusitis_features, orbital_or_intracranial_sinusitis_concern, pregnancy, pediatric_pathway, specialist_directed_allergy_plan
- `mild_allergic_rhinitis_no_wheeze_or_anaphylaxis.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `mild_allergic_rhinitis_no_wheeze_or_anaphylaxis.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `mild_allergic_rhinitis_no_wheeze_or_anaphylaxis.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `mild_allergic_rhinitis_no_wheeze_or_anaphylaxis.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: airway_symptoms, anaphylaxis, systemic_allergic_reaction, hypoxia, respiratory_distress, copd_or_asthma_exacerbation_pathway, severe_bacterial_sinusitis_features, orbital_or_intracranial_sinusitis_concern, pregnancy, pediatric_pathway, specialist_directed_allergy_plan
- `mild_allergic_rhinitis_no_wheeze_or_anaphylaxis.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: airway_symptoms, anaphylaxis, systemic_allergic_reaction, hypoxia, respiratory_distress, copd_or_asthma_exacerbation_pathway, severe_bacterial_sinusitis_features, orbital_or_intracranial_sinusitis_concern, pregnancy, pediatric_pathway, specialist_directed_allergy_plan
- `mild_allergic_rhinitis_no_wheeze_or_anaphylaxis.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `mild_allergic_rhinitis_no_wheeze_or_anaphylaxis.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `mild_allergic_rhinitis_no_wheeze_or_anaphylaxis.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `mild_allergic_rhinitis_no_wheeze_or_anaphylaxis.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: airway_symptoms, anaphylaxis, systemic_allergic_reaction, hypoxia, respiratory_distress, copd_or_asthma_exacerbation_pathway, severe_bacterial_sinusitis_features, orbital_or_intracranial_sinusitis_concern, pregnancy, pediatric_pathway, specialist_directed_allergy_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit allergic rhinitis, also called hay fever or seasonal allergies.

WHAT WE FOUND:
Your clinician diagnosed mild allergic rhinitis. We did not find anaphylaxis, wheezing/asthma flare, bacterial sinusitis, or another emergency problem today.

WHAT TO DO AT HOME:
- Avoid known allergy triggers when possible.
- Wash your hands and face after heavy pollen or dust exposure.
- Use saline spray or rinses only if your clinician says they are safe for you.

MEDICATIONS:
- Use allergy medicine only if prescribed or recommended, and follow the label.
- Do not mix sedating medicines, alcohol, or driving unless you know how the medicine affects you.

RETURN TO ED IF:
- Trouble breathing, wheezing, throat/tongue swelling, fainting, or a bodywide allergic reaction.
- Fever, severe facial pain, worsening one-sided sinus symptoms, or symptoms lasting longer than expected.
- Symptoms do not improve with the plan you were given.

FOLLOW UP:
Follow up with primary care or allergy care if symptoms are not improving, recur often, or interfere with sleep or breathing.
```
