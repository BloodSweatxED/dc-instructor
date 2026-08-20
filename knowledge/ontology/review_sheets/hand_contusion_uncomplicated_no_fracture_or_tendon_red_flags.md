# Hand contusion without fracture, tendon, or neurovascular red flags

Phenotype ID: `hand_contusion_uncomplicated_no_fracture_or_tendon_red_flags`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of uncomplicated hand contusion.
- No emergency red flags, pregnancy/pediatric pathway, or specialist-directed plan.

## Exclusions

- Red flags requiring a separate ED pathway, unstable vital signs, pregnancy/pediatric pathway, or specialist-directed plan.

## Must-Not-Miss Diagnoses

- Fracture or dislocation.
- Tendon rupture.
- Neurovascular compromise.
- Infection.

## Primitive List

- `hand_contusion_uncomplicated_no_fracture_or_tendon_red_flags.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `hand_contusion_uncomplicated_no_fracture_or_tendon_red_flags.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, hand_tendon_risk, neurovascular_compromise, severe_pain, open_wound, specialist_directed_orthopedic_plan
- `hand_contusion_uncomplicated_no_fracture_or_tendon_red_flags.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `hand_contusion_uncomplicated_no_fracture_or_tendon_red_flags.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `hand_contusion_uncomplicated_no_fracture_or_tendon_red_flags.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `hand_contusion_uncomplicated_no_fracture_or_tendon_red_flags.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, hand_tendon_risk, neurovascular_compromise, severe_pain, open_wound, specialist_directed_orthopedic_plan
- `hand_contusion_uncomplicated_no_fracture_or_tendon_red_flags.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, hand_tendon_risk, neurovascular_compromise, severe_pain, open_wound, specialist_directed_orthopedic_plan
- `hand_contusion_uncomplicated_no_fracture_or_tendon_red_flags.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `hand_contusion_uncomplicated_no_fracture_or_tendon_red_flags.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `hand_contusion_uncomplicated_no_fracture_or_tendon_red_flags.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `hand_contusion_uncomplicated_no_fracture_or_tendon_red_flags.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, hand_tendon_risk, neurovascular_compromise, severe_pain, open_wound, specialist_directed_orthopedic_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit uncomplicated hand contusion.

WHAT WE FOUND:
Your clinician diagnosed hand contusion. We did not find red flags requiring a separate emergency pathway today.

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
