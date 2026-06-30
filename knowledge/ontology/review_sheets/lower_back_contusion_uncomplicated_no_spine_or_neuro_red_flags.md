# Lower back contusion without spine or neurologic red flags

Phenotype ID: `lower_back_contusion_uncomplicated_no_spine_or_neuro_red_flags`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of uncomplicated lower back contusion.
- No spine fracture concern, new neurologic deficit, cauda equina concern, spinal infection concern, severe pain, pregnancy/pediatric pathway, or specialist-directed spine plan.

## Exclusions

- Spine fracture or major trauma concern, cauda equina symptoms, new neurologic deficit, spinal infection concern, severe or progressive pain, pregnancy/pediatric pathway, or specialist-directed spine plan.

## Must-Not-Miss Diagnoses

- Spine fracture.
- Cauda equina syndrome.
- Spinal infection.
- New neurologic deficit.

## Primitive List

- `lower_back_contusion_uncomplicated_no_spine_or_neuro_red_flags.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `lower_back_contusion_uncomplicated_no_spine_or_neuro_red_flags.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_trauma_concern, cauda_equina_concern, new_neurologic_deficit, spinal_infection_concern, severe_pain, specialist_directed_spine_plan
- `lower_back_contusion_uncomplicated_no_spine_or_neuro_red_flags.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `lower_back_contusion_uncomplicated_no_spine_or_neuro_red_flags.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `lower_back_contusion_uncomplicated_no_spine_or_neuro_red_flags.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `lower_back_contusion_uncomplicated_no_spine_or_neuro_red_flags.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_trauma_concern, cauda_equina_concern, new_neurologic_deficit, spinal_infection_concern, severe_pain, specialist_directed_spine_plan
- `lower_back_contusion_uncomplicated_no_spine_or_neuro_red_flags.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_trauma_concern, cauda_equina_concern, new_neurologic_deficit, spinal_infection_concern, severe_pain, specialist_directed_spine_plan
- `lower_back_contusion_uncomplicated_no_spine_or_neuro_red_flags.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `lower_back_contusion_uncomplicated_no_spine_or_neuro_red_flags.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `lower_back_contusion_uncomplicated_no_spine_or_neuro_red_flags.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `lower_back_contusion_uncomplicated_no_spine_or_neuro_red_flags.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_trauma_concern, cauda_equina_concern, new_neurologic_deficit, spinal_infection_concern, severe_pain, specialist_directed_spine_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit an uncomplicated lower back contusion.

WHAT WE FOUND:
Your clinician diagnosed a lower back contusion. We did not find spine fracture concern, neurologic deficit, cauda equina symptoms, infection concern, or another back emergency today.

WHAT TO DO AT HOME:
- Rest the lower back from activity that makes pain worse.
- Use ice, heat, gentle motion, support, or activity limits only as your clinician recommended.
- Return to normal activity gradually as symptoms improve.

MEDICATIONS:
- Use pain medicine only if prescribed or recommended, and follow the label.
- Do not use medicine to push through worsening pain, numbness, or weakness.

RETURN TO ED IF:
- New leg weakness, numbness, saddle numbness, trouble urinating, loss of bowel control, or trouble walking.
- New deformity, severe worsening pain, inability to use the area, or a new injury.
- Fever, spreading redness, warmth, drainage, or symptoms not improving as expected.

FOLLOW UP:
Follow up with primary care, sports medicine, spine clinic, urgent care, or the ED if symptoms are not improving or your clinician told you to recheck.
```
