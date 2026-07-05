# Chest wall contusion without cardiopulmonary red flags

Phenotype ID: `chest_wall_contusion_uncomplicated_no_cardiopulmonary_red_flags`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of uncomplicated chest wall contusion.
- No fracture/dislocation concern, deep infection, neurovascular compromise, high-energy trauma, pregnancy/pediatric pathway, or specialist-directed plan.

## Exclusions

- Fracture/dislocation concern, open wound, infection concern, neurovascular compromise, severe or rapidly worsening pain, high-energy trauma, immunocompromised host, pregnancy/pediatric pathway, or specialist-directed orthopedic plan.

## Must-Not-Miss Diagnoses

- Fracture or dislocation.
- Deep infection.
- Neurovascular compromise.
- Compartment syndrome or evolving emergency pain pattern.

## Primitive List

- `chest_wall_contusion_uncomplicated_no_cardiopulmonary_red_flags.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `chest_wall_contusion_uncomplicated_no_cardiopulmonary_red_flags.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: cardiac_or_pe_chest_pain_concern, chest_pain, fracture_or_dislocation_concern, high_energy_trauma, hypoxia, immunocompromised, neurovascular_compromise, open_wound, pediatric_pathway, pregnancy, respiratory_distress, severe_pain, specialist_directed_orthopedic_plan
- `chest_wall_contusion_uncomplicated_no_cardiopulmonary_red_flags.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `chest_wall_contusion_uncomplicated_no_cardiopulmonary_red_flags.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `chest_wall_contusion_uncomplicated_no_cardiopulmonary_red_flags.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `chest_wall_contusion_uncomplicated_no_cardiopulmonary_red_flags.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: cardiac_or_pe_chest_pain_concern, chest_pain, fracture_or_dislocation_concern, high_energy_trauma, hypoxia, immunocompromised, neurovascular_compromise, open_wound, pediatric_pathway, pregnancy, respiratory_distress, severe_pain, specialist_directed_orthopedic_plan
- `chest_wall_contusion_uncomplicated_no_cardiopulmonary_red_flags.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: cardiac_or_pe_chest_pain_concern, chest_pain, fracture_or_dislocation_concern, high_energy_trauma, hypoxia, immunocompromised, neurovascular_compromise, open_wound, pediatric_pathway, pregnancy, respiratory_distress, severe_pain, specialist_directed_orthopedic_plan
- `chest_wall_contusion_uncomplicated_no_cardiopulmonary_red_flags.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `chest_wall_contusion_uncomplicated_no_cardiopulmonary_red_flags.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `chest_wall_contusion_uncomplicated_no_cardiopulmonary_red_flags.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `chest_wall_contusion_uncomplicated_no_cardiopulmonary_red_flags.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: cardiac_or_pe_chest_pain_concern, chest_pain, fracture_or_dislocation_concern, high_energy_trauma, hypoxia, immunocompromised, neurovascular_compromise, open_wound, pediatric_pathway, pregnancy, respiratory_distress, severe_pain, specialist_directed_orthopedic_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit an uncomplicated chest wall contusion.

WHAT WE FOUND:
Your clinician diagnosed an uncomplicated chest wall contusion. We did not find fracture or dislocation concern, infection, nerve or blood-flow problems, or another emergency today.

WHAT TO DO AT HOME:
- Rest the chest wall from activity that makes pain worse.
- Use ice, heat, gentle motion, support, or activity limits only as your clinician recommended.
- Return to normal activity gradually as symptoms improve.

MEDICATIONS:
- Use pain medicine only if prescribed or recommended, and follow the label.
- Do not use medicine to push through worsening pain, weakness, numbness, fever, or swelling.

RETURN TO ED IF:
- Fever, rapidly worsening swelling, severe pain, or feeling very ill.
- New numbness, weakness, blue or pale skin, deformity, or inability to use the area.
- Symptoms that worsen or do not improve as expected.

FOLLOW UP:
Follow up with primary care, sports medicine, orthopedics, therapy, urgent care, or the ED if symptoms are not improving or your clinician told you to recheck.
```
