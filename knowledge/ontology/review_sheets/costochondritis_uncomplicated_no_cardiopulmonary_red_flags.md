# Uncomplicated costochondritis without cardiopulmonary red flags

Phenotype ID: `costochondritis_uncomplicated_no_cardiopulmonary_red_flags`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of uncomplicated costochondritis.
- No cardiac/PE concern, unresolved dyspnea, hypoxia, hemoptysis, fever/systemic illness, trauma/fracture concern, pregnancy/pediatric pathway, or specialist-directed plan.

## Exclusions

- Cardiac or PE concern, pressure/exertional chest pain, shortness of breath, hypoxia, hemoptysis, syncope, fever, systemic illness, trauma/fracture concern, or diagnostic uncertainty.
- Pregnancy/pediatric pathway or specialist-directed cardiology/pulmonary plan.

## Must-Not-Miss Diagnoses

- Acute coronary syndrome.
- Pulmonary embolism.
- Pneumothorax.
- Pneumonia.
- Rib fracture.

## Primitive List

- `costochondritis_uncomplicated_no_cardiopulmonary_red_flags.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `costochondritis_uncomplicated_no_cardiopulmonary_red_flags.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: chest_pain, cardiac_or_pe_chest_pain_concern, resolved_dyspnea_not_documented, hypoxia, hemoptysis, syncope_or_fainting, systemic_illness, fracture_or_trauma_concern, pregnancy, pediatric_pathway
- `costochondritis_uncomplicated_no_cardiopulmonary_red_flags.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `costochondritis_uncomplicated_no_cardiopulmonary_red_flags.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `costochondritis_uncomplicated_no_cardiopulmonary_red_flags.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `costochondritis_uncomplicated_no_cardiopulmonary_red_flags.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: chest_pain, cardiac_or_pe_chest_pain_concern, resolved_dyspnea_not_documented, hypoxia, hemoptysis, syncope_or_fainting, systemic_illness, fracture_or_trauma_concern, pregnancy, pediatric_pathway
- `costochondritis_uncomplicated_no_cardiopulmonary_red_flags.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: chest_pain, cardiac_or_pe_chest_pain_concern, resolved_dyspnea_not_documented, hypoxia, hemoptysis, syncope_or_fainting, systemic_illness, fracture_or_trauma_concern, pregnancy, pediatric_pathway
- `costochondritis_uncomplicated_no_cardiopulmonary_red_flags.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `costochondritis_uncomplicated_no_cardiopulmonary_red_flags.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `costochondritis_uncomplicated_no_cardiopulmonary_red_flags.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `costochondritis_uncomplicated_no_cardiopulmonary_red_flags.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: chest_pain, cardiac_or_pe_chest_pain_concern, resolved_dyspnea_not_documented, hypoxia, hemoptysis, syncope_or_fainting, systemic_illness, fracture_or_trauma_concern, pregnancy, pediatric_pathway

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit costochondritis, irritation where the ribs meet the breastbone.

WHAT WE FOUND:
Your clinician diagnosed uncomplicated costochondritis. We did not find cardiac, lung, trauma, or other emergency red flags today.

WHAT TO DO AT HOME:
- Rest from activities that worsen the pain.
- Use heat or ice only as instructed.
- Return to activity gradually as symptoms improve.

MEDICATIONS:
- Use pain medicine only if prescribed or recommended, and follow the label.
- Avoid medicines your clinician told you to avoid.

RETURN TO ED IF:
- Pressure-like chest pain, pain with exertion, fainting, sweating, or pain spreading to the arm, jaw, or back.
- Shortness of breath, coughing blood, fever, or feeling very ill.
- New trauma, severe worsening pain, or symptoms not improving.

FOLLOW UP:
Follow up with primary care if symptoms persist, recur, or your clinician told you to recheck.
```
