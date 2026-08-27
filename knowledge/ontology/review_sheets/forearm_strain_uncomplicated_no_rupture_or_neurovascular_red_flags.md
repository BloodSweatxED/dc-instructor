# Forearm strain without rupture or neurovascular red flags

Phenotype ID: `forearm_strain_uncomplicated_no_rupture_or_neurovascular_red_flags`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of uncomplicated forearm strain.
- No fracture/dislocation concern, tendon rupture, neurovascular compromise, infection, pregnancy/pediatric pathway, or specialist-directed plan.

## Exclusions

- Fracture/dislocation concern, tendon rupture, severe pain, neurovascular compromise, infection concern, inability to use the limb, or high-risk trauma context.
- Pregnancy/pediatric pathway or specialist-directed orthopedic plan.

## Must-Not-Miss Diagnoses

- Fracture or dislocation.
- Tendon rupture.
- Neurovascular compromise.
- Compartment syndrome.

## Primitive List

- `forearm_strain_uncomplicated_no_rupture_or_neurovascular_red_flags.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `forearm_strain_uncomplicated_no_rupture_or_neurovascular_red_flags.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, tendon_or_ligament_rupture_concern, neurovascular_compromise, severe_pain, pregnancy, pediatric_pathway, specialist_directed_orthopedic_plan
- `forearm_strain_uncomplicated_no_rupture_or_neurovascular_red_flags.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `forearm_strain_uncomplicated_no_rupture_or_neurovascular_red_flags.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `forearm_strain_uncomplicated_no_rupture_or_neurovascular_red_flags.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `forearm_strain_uncomplicated_no_rupture_or_neurovascular_red_flags.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, tendon_or_ligament_rupture_concern, neurovascular_compromise, severe_pain, pregnancy, pediatric_pathway, specialist_directed_orthopedic_plan
- `forearm_strain_uncomplicated_no_rupture_or_neurovascular_red_flags.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, tendon_or_ligament_rupture_concern, neurovascular_compromise, severe_pain, pregnancy, pediatric_pathway, specialist_directed_orthopedic_plan
- `forearm_strain_uncomplicated_no_rupture_or_neurovascular_red_flags.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `forearm_strain_uncomplicated_no_rupture_or_neurovascular_red_flags.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `forearm_strain_uncomplicated_no_rupture_or_neurovascular_red_flags.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `forearm_strain_uncomplicated_no_rupture_or_neurovascular_red_flags.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, tendon_or_ligament_rupture_concern, neurovascular_compromise, severe_pain, pregnancy, pediatric_pathway, specialist_directed_orthopedic_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit an uncomplicated forearm strain.

WHAT WE FOUND:
Your clinician diagnosed a forearm strain. We did not find a fracture, tendon rupture, circulation problem, nerve problem, or another emergency problem today.

WHAT TO DO AT HOME:
- Rest the injured area as instructed.
- Use ice, compression, elevation, gentle motion, or activity limits only as your clinician recommended.
- Avoid activity that causes sharp or worsening pain until you are improving.

MEDICATIONS:
- Use pain medicine only if prescribed or recommended, and follow the label.
- Do not combine medicines unless your clinician said it is safe.

RETURN TO ED IF:
- Worsening severe pain, new swelling, numbness, weakness, color change, or trouble using the limb.
- A pop with loss of strength, new deformity, or concern for tendon rupture.
- Fever, redness spreading over the area, or symptoms not improving as expected.

FOLLOW UP:
Follow up with primary care, sports medicine, orthopedics, urgent care, or the ED if symptoms are not improving or your clinician told you to recheck.
```
