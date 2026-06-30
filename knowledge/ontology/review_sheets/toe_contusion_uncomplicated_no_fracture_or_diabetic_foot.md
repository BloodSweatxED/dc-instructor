# Toe contusion without fracture or diabetic-foot red flags

Phenotype ID: `toe_contusion_uncomplicated_no_fracture_or_diabetic_foot`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of uncomplicated toe contusion.
- No emergency red flags, pregnancy/pediatric pathway, or specialist-directed plan.

## Exclusions

- Red flags requiring a separate ED pathway, unstable vital signs, pregnancy/pediatric pathway, or specialist-directed plan.

## Must-Not-Miss Diagnoses

- Fracture or dislocation.
- Tendon rupture.
- Neurovascular compromise.
- Infection.

## Primitive List

- `toe_contusion_uncomplicated_no_fracture_or_diabetic_foot.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `toe_contusion_uncomplicated_no_fracture_or_diabetic_foot.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, neurovascular_compromise, diabetic_foot, open_wound, severe_pain, specialist_directed_orthopedic_plan
- `toe_contusion_uncomplicated_no_fracture_or_diabetic_foot.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `toe_contusion_uncomplicated_no_fracture_or_diabetic_foot.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `toe_contusion_uncomplicated_no_fracture_or_diabetic_foot.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `toe_contusion_uncomplicated_no_fracture_or_diabetic_foot.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, neurovascular_compromise, diabetic_foot, open_wound, severe_pain, specialist_directed_orthopedic_plan
- `toe_contusion_uncomplicated_no_fracture_or_diabetic_foot.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, neurovascular_compromise, diabetic_foot, open_wound, severe_pain, specialist_directed_orthopedic_plan
- `toe_contusion_uncomplicated_no_fracture_or_diabetic_foot.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `toe_contusion_uncomplicated_no_fracture_or_diabetic_foot.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `toe_contusion_uncomplicated_no_fracture_or_diabetic_foot.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `toe_contusion_uncomplicated_no_fracture_or_diabetic_foot.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, neurovascular_compromise, diabetic_foot, open_wound, severe_pain, specialist_directed_orthopedic_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit uncomplicated toe contusion.

WHAT WE FOUND:
Your clinician diagnosed toe contusion. We did not find red flags requiring a separate emergency pathway today.

WHAT TO DO AT HOME:
- Rest the sore area as instructed.
- Use ice, compression, elevation, gentle motion, or activity limits only as your clinician recommended.
- Avoid activity that causes sharp or worsening pain until you are improving.

MEDICATIONS:
- Use pain medicine only if prescribed or recommended, and follow the label.
- Do not combine medicines unless your clinician said it is safe.

RETURN TO ED IF:
- Worsening severe pain, new swelling, numbness, weakness, color change, or trouble using the limb.
- New deformity, inability to use the area, or concern for fracture, dislocation, or tendon injury.
- Fever, spreading redness, warmth, drainage, or symptoms not improving as expected.

FOLLOW UP:
Follow up with primary care, sports medicine, orthopedics, urgent care, or the ED if symptoms are not improving or your clinician told you to recheck.
```
