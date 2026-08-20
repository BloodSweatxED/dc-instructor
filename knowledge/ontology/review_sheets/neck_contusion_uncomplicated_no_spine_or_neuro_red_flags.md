# Neck contusion without spine or neurologic red flags

Phenotype ID: `neck_contusion_uncomplicated_no_spine_or_neuro_red_flags`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of uncomplicated neck contusion.
- No cervical spine fracture concern, midline cervical tenderness, neurologic deficit, infection concern, pregnancy/pediatric pathway, or specialist-directed spine plan.

## Exclusions

- Cervical spine fracture or major trauma concern, midline cervical tenderness, new neurologic deficit, severe pain, infection concern, pregnancy/pediatric pathway, or specialist-directed spine plan.

## Must-Not-Miss Diagnoses

- Cervical spine fracture.
- Spinal cord injury.
- Vascular or neurologic emergency.
- Deep neck infection.

## Primitive List

- `neck_contusion_uncomplicated_no_spine_or_neuro_red_flags.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `neck_contusion_uncomplicated_no_spine_or_neuro_red_flags.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_trauma_concern, midline_cervical_tenderness, new_neurologic_deficit, severe_pain, systemic_illness, specialist_directed_spine_plan
- `neck_contusion_uncomplicated_no_spine_or_neuro_red_flags.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `neck_contusion_uncomplicated_no_spine_or_neuro_red_flags.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `neck_contusion_uncomplicated_no_spine_or_neuro_red_flags.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `neck_contusion_uncomplicated_no_spine_or_neuro_red_flags.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_trauma_concern, midline_cervical_tenderness, new_neurologic_deficit, severe_pain, systemic_illness, specialist_directed_spine_plan
- `neck_contusion_uncomplicated_no_spine_or_neuro_red_flags.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_trauma_concern, midline_cervical_tenderness, new_neurologic_deficit, severe_pain, systemic_illness, specialist_directed_spine_plan
- `neck_contusion_uncomplicated_no_spine_or_neuro_red_flags.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `neck_contusion_uncomplicated_no_spine_or_neuro_red_flags.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `neck_contusion_uncomplicated_no_spine_or_neuro_red_flags.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `neck_contusion_uncomplicated_no_spine_or_neuro_red_flags.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_trauma_concern, midline_cervical_tenderness, new_neurologic_deficit, severe_pain, systemic_illness, specialist_directed_spine_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit an uncomplicated neck contusion.

WHAT WE FOUND:
Your clinician diagnosed a neck contusion. We did not find cervical spine fracture concern, midline cervical tenderness, neurologic deficit, or another neck emergency today.

WHAT TO DO AT HOME:
- Rest the neck from activity that makes pain worse.
- Use ice, heat, gentle motion, support, or activity limits only as your clinician recommended.
- Return to normal activity gradually as symptoms improve.

MEDICATIONS:
- Use pain medicine only if prescribed or recommended, and follow the label.
- Do not use medicine to push through worsening pain, numbness, or weakness.

RETURN TO ED IF:
- New arm or leg weakness, numbness, trouble walking, severe headache, or worsening neck pain.
- New deformity, severe worsening pain, inability to use the area, or a new injury.
- Fever, spreading redness, warmth, drainage, or symptoms not improving as expected.

FOLLOW UP:
Follow up with primary care, sports medicine, spine clinic, urgent care, or the ED if symptoms are not improving or your clinician told you to recheck.
```
