# Uncomplicated rib contusion without fracture or cardiopulmonary red flags

Phenotype ID: `rib_contusion_uncomplicated_no_fracture_or_cardiopulmonary_red_flags`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of uncomplicated rib/chest wall contusion.
- No fracture concern, pneumothorax/pulmonary injury concern, cardiac/PE concern, hypoxia, hemoptysis, syncope, pregnancy/pediatric pathway, or specialist-directed plan.

## Exclusions

- Fracture/dislocation concern, high-energy trauma, pneumothorax or pulmonary injury concern, hypoxia, hemoptysis, cardiac/PE concern, syncope, fever/systemic illness, severe pain, or unstable vitals.
- Pregnancy/pediatric pathway or specialist-directed trauma/orthopedic plan.

## Must-Not-Miss Diagnoses

- Rib fracture.
- Pneumothorax.
- Pulmonary contusion.
- Acute coronary syndrome mimic.
- Pulmonary embolism mimic.

## Primitive List

- `rib_contusion_uncomplicated_no_fracture_or_cardiopulmonary_red_flags.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `rib_contusion_uncomplicated_no_fracture_or_cardiopulmonary_red_flags.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, high_energy_trauma, hypoxia, hemoptysis, cardiac_or_pe_chest_pain_concern, syncope_or_fainting, systemic_illness, severe_pain, unstable_vitals, pregnancy, pediatric_pathway, specialist_directed_orthopedic_plan
- `rib_contusion_uncomplicated_no_fracture_or_cardiopulmonary_red_flags.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `rib_contusion_uncomplicated_no_fracture_or_cardiopulmonary_red_flags.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `rib_contusion_uncomplicated_no_fracture_or_cardiopulmonary_red_flags.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `rib_contusion_uncomplicated_no_fracture_or_cardiopulmonary_red_flags.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, high_energy_trauma, hypoxia, hemoptysis, cardiac_or_pe_chest_pain_concern, syncope_or_fainting, systemic_illness, severe_pain, unstable_vitals, pregnancy, pediatric_pathway, specialist_directed_orthopedic_plan
- `rib_contusion_uncomplicated_no_fracture_or_cardiopulmonary_red_flags.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, high_energy_trauma, hypoxia, hemoptysis, cardiac_or_pe_chest_pain_concern, syncope_or_fainting, systemic_illness, severe_pain, unstable_vitals, pregnancy, pediatric_pathway, specialist_directed_orthopedic_plan
- `rib_contusion_uncomplicated_no_fracture_or_cardiopulmonary_red_flags.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `rib_contusion_uncomplicated_no_fracture_or_cardiopulmonary_red_flags.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `rib_contusion_uncomplicated_no_fracture_or_cardiopulmonary_red_flags.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `rib_contusion_uncomplicated_no_fracture_or_cardiopulmonary_red_flags.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, high_energy_trauma, hypoxia, hemoptysis, cardiac_or_pe_chest_pain_concern, syncope_or_fainting, systemic_illness, severe_pain, unstable_vitals, pregnancy, pediatric_pathway, specialist_directed_orthopedic_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit a rib or chest wall bruise.

WHAT WE FOUND:
Your clinician diagnosed an uncomplicated rib or chest wall contusion. We did not find fracture concern, lung injury, heart or blood-clot concern, or another emergency problem today.

WHAT TO DO AT HOME:
- Rest from activities that worsen the pain.
- Use ice, heat, or gentle movement only as instructed.
- Take slow deep breaths as your clinician instructed so you do not avoid breathing because of pain.

MEDICATIONS:
- Use pain medicine only if prescribed or recommended, and follow the label.
- Avoid medicines your clinician told you to avoid.

RETURN TO ED IF:
- Shortness of breath, coughing blood, fainting, pressure-like chest pain, or pain with exertion.
- Fever, worsening cough, or feeling very ill.
- Severe worsening pain, new trauma, or symptoms not improving.

FOLLOW UP:
Follow up with primary care or urgent care if pain or breathing comfort is not improving.
```
