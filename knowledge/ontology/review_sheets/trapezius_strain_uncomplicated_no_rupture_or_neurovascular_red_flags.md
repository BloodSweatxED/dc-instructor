# Trapezius strain without rupture or neurovascular red flags

Phenotype ID: `trapezius_strain_uncomplicated_no_rupture_or_neurovascular_red_flags`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of uncomplicated trapezius strain.
- No fracture/dislocation concern, tendon rupture, neurovascular compromise, infection, cardiopulmonary red flags, pregnancy/pediatric pathway, or specialist-directed plan.

## Exclusions

- Fracture/dislocation concern, tendon rupture, severe pain, neurovascular compromise, infection concern, cardiopulmonary red flags, pregnancy/pediatric pathway, or specialist-directed plan.

## Must-Not-Miss Diagnoses

- Fracture or dislocation.
- Tendon rupture.
- Neurovascular compromise.
- Cardiopulmonary mimic.

## Primitive List

- `trapezius_strain_uncomplicated_no_rupture_or_neurovascular_red_flags.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `trapezius_strain_uncomplicated_no_rupture_or_neurovascular_red_flags.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, tendon_or_ligament_rupture_concern, neurovascular_compromise, severe_pain, chest_pain, respiratory_distress, specialist_directed_orthopedic_plan
- `trapezius_strain_uncomplicated_no_rupture_or_neurovascular_red_flags.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `trapezius_strain_uncomplicated_no_rupture_or_neurovascular_red_flags.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `trapezius_strain_uncomplicated_no_rupture_or_neurovascular_red_flags.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `trapezius_strain_uncomplicated_no_rupture_or_neurovascular_red_flags.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, tendon_or_ligament_rupture_concern, neurovascular_compromise, severe_pain, chest_pain, respiratory_distress, specialist_directed_orthopedic_plan
- `trapezius_strain_uncomplicated_no_rupture_or_neurovascular_red_flags.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, tendon_or_ligament_rupture_concern, neurovascular_compromise, severe_pain, chest_pain, respiratory_distress, specialist_directed_orthopedic_plan
- `trapezius_strain_uncomplicated_no_rupture_or_neurovascular_red_flags.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `trapezius_strain_uncomplicated_no_rupture_or_neurovascular_red_flags.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `trapezius_strain_uncomplicated_no_rupture_or_neurovascular_red_flags.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `trapezius_strain_uncomplicated_no_rupture_or_neurovascular_red_flags.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, tendon_or_ligament_rupture_concern, neurovascular_compromise, severe_pain, chest_pain, respiratory_distress, specialist_directed_orthopedic_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit uncomplicated trapezius strain.

WHAT WE FOUND:
Your clinician diagnosed trapezius strain. We did not find fracture, tendon rupture, neurovascular compromise, infection, or another emergency pathway today.

WHAT TO DO AT HOME:
- Rest the sore area as instructed.
- Use ice, heat, gentle motion, posture changes, or activity limits only as your clinician recommended.
- Avoid activity that causes sharp or worsening pain until you are improving.

MEDICATIONS:
- Use pain medicine only if prescribed or recommended, and follow the label.
- Do not combine medicines unless your clinician said it is safe.

RETURN TO ED IF:
- Worsening severe pain, new weakness, numbness, color change, or trouble using the arm.
- New trauma, deformity, chest pain, trouble breathing, or neurologic symptoms.
- Fever, spreading redness, warmth, drainage, or symptoms not improving as expected.

FOLLOW UP:
Follow up with primary care, sports medicine, orthopedics, urgent care, or the ED if symptoms are not improving or your clinician told you to recheck.
```
