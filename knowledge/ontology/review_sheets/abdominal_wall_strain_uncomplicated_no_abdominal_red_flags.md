# Abdominal wall strain without abdominal red flags

Phenotype ID: `abdominal_wall_strain_uncomplicated_no_abdominal_red_flags`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of uncomplicated abdominal wall strain.
- No emergency red flags, pregnancy/pediatric pathway, or specialist-directed plan.

## Exclusions

- Red flags requiring a separate ED pathway, unstable vital signs, pregnancy/pediatric pathway, or specialist-directed plan.

## Must-Not-Miss Diagnoses

- Surgical abdomen.
- Hernia complication.
- GI bleeding.
- Intra-abdominal infection.

## Primitive List

- `abdominal_wall_strain_uncomplicated_no_abdominal_red_flags.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `abdominal_wall_strain_uncomplicated_no_abdominal_red_flags.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: severe_or_focal_abdominal_pain, peritoneal_signs, persistent_vomiting, fever, gi_bleeding, surgical_abdomen, specialist_directed_orthopedic_plan
- `abdominal_wall_strain_uncomplicated_no_abdominal_red_flags.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `abdominal_wall_strain_uncomplicated_no_abdominal_red_flags.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `abdominal_wall_strain_uncomplicated_no_abdominal_red_flags.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `abdominal_wall_strain_uncomplicated_no_abdominal_red_flags.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: severe_or_focal_abdominal_pain, peritoneal_signs, persistent_vomiting, fever, gi_bleeding, surgical_abdomen, specialist_directed_orthopedic_plan
- `abdominal_wall_strain_uncomplicated_no_abdominal_red_flags.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: severe_or_focal_abdominal_pain, peritoneal_signs, persistent_vomiting, fever, gi_bleeding, surgical_abdomen, specialist_directed_orthopedic_plan
- `abdominal_wall_strain_uncomplicated_no_abdominal_red_flags.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `abdominal_wall_strain_uncomplicated_no_abdominal_red_flags.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `abdominal_wall_strain_uncomplicated_no_abdominal_red_flags.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `abdominal_wall_strain_uncomplicated_no_abdominal_red_flags.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: severe_or_focal_abdominal_pain, peritoneal_signs, persistent_vomiting, fever, gi_bleeding, surgical_abdomen, specialist_directed_orthopedic_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit uncomplicated abdominal wall strain.

WHAT WE FOUND:
Your clinician diagnosed abdominal wall strain. We did not find red flags requiring a separate emergency pathway today.

WHAT TO DO AT HOME:
- Rest the sore area as instructed.
- Use ice, compression, elevation, gentle motion, or activity limits only as your clinician recommended.
- Avoid activity that causes sharp or worsening pain until you are improving.

MEDICATIONS:
- Use pain medicine only if prescribed or recommended, and follow the label.
- Do not combine medicines unless your clinician said it is safe.

RETURN TO ED IF:
- Severe or worsening abdominal pain, fever, repeated vomiting, fainting, or a swollen belly.
- Blood in stool, black stool, trouble urinating, or new testicular/pelvic pain.
- Pain that stops feeling like the abdominal wall and becomes deeper or more constant.

FOLLOW UP:
Follow up with primary care, sports medicine, orthopedics, urgent care, or the ED if symptoms are not improving or your clinician told you to recheck.
```
