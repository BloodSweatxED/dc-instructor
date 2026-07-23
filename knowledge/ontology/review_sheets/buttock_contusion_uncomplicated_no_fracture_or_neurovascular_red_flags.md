# Buttock contusion without fracture or neurovascular red flags

Phenotype ID: `buttock_contusion_uncomplicated_no_fracture_or_neurovascular_red_flags`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of uncomplicated buttock contusion.
- No fracture/dislocation concern, neurovascular compromise, severe pain, compartment syndrome concern, pregnancy/pediatric pathway, or specialist-directed plan.

## Exclusions

- Fracture or dislocation concern, neurovascular compromise, severe pain, compartment syndrome concern, inability to walk, high-energy trauma, pregnancy/pediatric pathway, or specialist-directed orthopedic plan.

## Must-Not-Miss Diagnoses

- Pelvic or hip fracture.
- Neurovascular compromise.
- Compartment syndrome.
- Deep infection.

## Primitive List

- `buttock_contusion_uncomplicated_no_fracture_or_neurovascular_red_flags.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `buttock_contusion_uncomplicated_no_fracture_or_neurovascular_red_flags.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, neurovascular_compromise, severe_pain, compartment_syndrome_concern, unable_to_bear_weight_lower_extremity, high_energy_trauma, specialist_directed_orthopedic_plan
- `buttock_contusion_uncomplicated_no_fracture_or_neurovascular_red_flags.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `buttock_contusion_uncomplicated_no_fracture_or_neurovascular_red_flags.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `buttock_contusion_uncomplicated_no_fracture_or_neurovascular_red_flags.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `buttock_contusion_uncomplicated_no_fracture_or_neurovascular_red_flags.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, neurovascular_compromise, severe_pain, compartment_syndrome_concern, unable_to_bear_weight_lower_extremity, high_energy_trauma, specialist_directed_orthopedic_plan
- `buttock_contusion_uncomplicated_no_fracture_or_neurovascular_red_flags.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, neurovascular_compromise, severe_pain, compartment_syndrome_concern, unable_to_bear_weight_lower_extremity, high_energy_trauma, specialist_directed_orthopedic_plan
- `buttock_contusion_uncomplicated_no_fracture_or_neurovascular_red_flags.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `buttock_contusion_uncomplicated_no_fracture_or_neurovascular_red_flags.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `buttock_contusion_uncomplicated_no_fracture_or_neurovascular_red_flags.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `buttock_contusion_uncomplicated_no_fracture_or_neurovascular_red_flags.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, neurovascular_compromise, severe_pain, compartment_syndrome_concern, unable_to_bear_weight_lower_extremity, high_energy_trauma, specialist_directed_orthopedic_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit an uncomplicated buttock contusion.

WHAT WE FOUND:
Your clinician diagnosed a buttock contusion. We did not find fracture, dislocation, neurologic deficit, poor blood flow, or another emergency today.

WHAT TO DO AT HOME:
- Rest the sore area from activity that makes pain worse.
- Use ice, heat, gentle motion, support, or activity limits only as your clinician recommended.
- Return to normal activity gradually as symptoms improve.

MEDICATIONS:
- Use pain medicine only if prescribed or recommended, and follow the label.
- Do not use medicine to push through worsening pain, numbness, or weakness.

RETURN TO ED IF:
- New numbness, weakness, trouble walking, color change, or worsening swelling.
- New deformity, severe worsening pain, inability to use the area, or a new injury.
- Fever, spreading redness, warmth, drainage, or symptoms not improving as expected.

FOLLOW UP:
Follow up with primary care, sports medicine, orthopedics, urgent care, or the ED if symptoms are not improving or your clinician told you to recheck.
```
