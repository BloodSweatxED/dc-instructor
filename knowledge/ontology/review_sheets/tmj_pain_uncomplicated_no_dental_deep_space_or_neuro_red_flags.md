# Uncomplicated TMJ pain without dental, deep-space, or neurologic red flags

Phenotype ID: `tmj_pain_uncomplicated_no_dental_deep_space_or_neuro_red_flags`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of uncomplicated TMJ pain/disorder.
- No dental infection, deep-space infection, trismus, airway symptoms, trauma/fracture concern, neurologic deficit, cardiac chest pain mimic, pregnancy/pediatric pathway, or specialist-directed plan.

## Exclusions

- Dental infection, deep-space swelling, trismus, airway symptoms, drooling, fever/systemic illness, facial trauma/fracture concern, neurologic deficit, severe headache, or cardiac chest-pain concern.
- Pregnancy/pediatric pathway or specialist-directed ENT/dental/oral-surgery plan.

## Must-Not-Miss Diagnoses

- Deep-space neck infection.
- Dental abscess.
- Mandible fracture.
- Airway compromise.
- Acute coronary syndrome mimic.

## Primitive List

- `tmj_pain_uncomplicated_no_dental_deep_space_or_neuro_red_flags.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `tmj_pain_uncomplicated_no_dental_deep_space_or_neuro_red_flags.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: deep_space_swelling, trismus, airway_symptoms, drooling, systemic_illness, dental_or_facial_trauma_source, fracture_or_dislocation_concern, neurologic_deficit, cardiac_or_pe_chest_pain_concern, pregnancy, pediatric_pathway, specialist_directed_ent_plan
- `tmj_pain_uncomplicated_no_dental_deep_space_or_neuro_red_flags.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `tmj_pain_uncomplicated_no_dental_deep_space_or_neuro_red_flags.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `tmj_pain_uncomplicated_no_dental_deep_space_or_neuro_red_flags.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `tmj_pain_uncomplicated_no_dental_deep_space_or_neuro_red_flags.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: deep_space_swelling, trismus, airway_symptoms, drooling, systemic_illness, dental_or_facial_trauma_source, fracture_or_dislocation_concern, neurologic_deficit, cardiac_or_pe_chest_pain_concern, pregnancy, pediatric_pathway, specialist_directed_ent_plan
- `tmj_pain_uncomplicated_no_dental_deep_space_or_neuro_red_flags.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: deep_space_swelling, trismus, airway_symptoms, drooling, systemic_illness, dental_or_facial_trauma_source, fracture_or_dislocation_concern, neurologic_deficit, cardiac_or_pe_chest_pain_concern, pregnancy, pediatric_pathway, specialist_directed_ent_plan
- `tmj_pain_uncomplicated_no_dental_deep_space_or_neuro_red_flags.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `tmj_pain_uncomplicated_no_dental_deep_space_or_neuro_red_flags.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `tmj_pain_uncomplicated_no_dental_deep_space_or_neuro_red_flags.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `tmj_pain_uncomplicated_no_dental_deep_space_or_neuro_red_flags.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: deep_space_swelling, trismus, airway_symptoms, drooling, systemic_illness, dental_or_facial_trauma_source, fracture_or_dislocation_concern, neurologic_deficit, cardiac_or_pe_chest_pain_concern, pregnancy, pediatric_pathway, specialist_directed_ent_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit TMJ pain, irritation around the jaw joint.

WHAT WE FOUND:
Your clinician diagnosed uncomplicated TMJ pain. We did not find dental infection, deep-space infection, trauma, neurologic symptoms, or another emergency problem today.

WHAT TO DO AT HOME:
- Avoid hard chewing, gum, and wide jaw opening while symptoms are flaring.
- Use heat, ice, or jaw rest only as instructed.
- Eat softer foods for a short time if recommended.

MEDICATIONS:
- Use pain medicine only if prescribed or recommended, and follow the label.
- Avoid medicines your clinician told you to avoid.

RETURN TO ED IF:
- Face or neck swelling, fever, trouble swallowing, drooling, voice change, or trouble breathing.
- Cannot open the mouth, new trauma, dental swelling, severe headache, or neurologic symptoms.
- Chest pressure, fainting, or pain spreading to arm, jaw, or back.

FOLLOW UP:
Follow up with primary care, dentist, oral surgery, or ENT if symptoms persist, recur, or your clinician told you to recheck.
```
