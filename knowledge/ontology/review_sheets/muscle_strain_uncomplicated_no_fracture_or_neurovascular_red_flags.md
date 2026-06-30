# Uncomplicated muscle strain without fracture or neurovascular red flags

Phenotype ID: `muscle_strain_uncomplicated_no_fracture_or_neurovascular_red_flags`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of uncomplicated muscle strain.
- No fracture/dislocation concern, tendon rupture, compartment syndrome, neurovascular compromise, high-energy trauma, open wound, infection, pregnancy/pediatric pathway, or specialist-directed plan.

## Exclusions

- Fracture/dislocation concern, tendon rupture, severe pain, compartment syndrome, neurovascular compromise, inability to use limb, high-energy trauma, open wound, infection, or systemic illness.
- Pregnancy/pediatric pathway, anticoagulation/bleeding concern, or specialist-directed orthopedic plan.

## Must-Not-Miss Diagnoses

- Fracture or dislocation.
- Tendon rupture.
- Compartment syndrome.
- Neurovascular injury.
- Septic joint or infection mimic.

## Primitive List

- `muscle_strain_uncomplicated_no_fracture_or_neurovascular_red_flags.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `muscle_strain_uncomplicated_no_fracture_or_neurovascular_red_flags.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, tendon_or_ligament_rupture_concern, severe_pain, compartment_syndrome_concern, neurovascular_compromise, unable_to_use_limb, high_energy_trauma, open_wound, secondary_skin_infection_concern, systemic_illness, pregnancy, pediatric_pathway, specialist_directed_orthopedic_plan
- `muscle_strain_uncomplicated_no_fracture_or_neurovascular_red_flags.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `muscle_strain_uncomplicated_no_fracture_or_neurovascular_red_flags.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `muscle_strain_uncomplicated_no_fracture_or_neurovascular_red_flags.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `muscle_strain_uncomplicated_no_fracture_or_neurovascular_red_flags.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, tendon_or_ligament_rupture_concern, severe_pain, compartment_syndrome_concern, neurovascular_compromise, unable_to_use_limb, high_energy_trauma, open_wound, secondary_skin_infection_concern, systemic_illness, pregnancy, pediatric_pathway, specialist_directed_orthopedic_plan
- `muscle_strain_uncomplicated_no_fracture_or_neurovascular_red_flags.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, tendon_or_ligament_rupture_concern, severe_pain, compartment_syndrome_concern, neurovascular_compromise, unable_to_use_limb, high_energy_trauma, open_wound, secondary_skin_infection_concern, systemic_illness, pregnancy, pediatric_pathway, specialist_directed_orthopedic_plan
- `muscle_strain_uncomplicated_no_fracture_or_neurovascular_red_flags.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `muscle_strain_uncomplicated_no_fracture_or_neurovascular_red_flags.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `muscle_strain_uncomplicated_no_fracture_or_neurovascular_red_flags.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `muscle_strain_uncomplicated_no_fracture_or_neurovascular_red_flags.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, tendon_or_ligament_rupture_concern, severe_pain, compartment_syndrome_concern, neurovascular_compromise, unable_to_use_limb, high_energy_trauma, open_wound, secondary_skin_infection_concern, systemic_illness, pregnancy, pediatric_pathway, specialist_directed_orthopedic_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit a muscle strain.

WHAT WE FOUND:
Your clinician diagnosed an uncomplicated muscle strain. We did not find fracture concern, tendon rupture, neurovascular problem, or another emergency problem today.

WHAT TO DO AT HOME:
- Rest from activities that worsen pain.
- Use ice or heat only as instructed.
- Return to activity gradually as symptoms improve.

MEDICATIONS:
- Use pain medicine only if prescribed or recommended, and follow the label.
- Avoid medicines your clinician told you to avoid.

RETURN TO ED IF:
- Severe worsening pain, tight swelling, numbness, weakness, color change, or trouble using the limb.
- New injury, fracture concern, inability to walk or use the limb, or symptoms not improving.
- Fever, redness, or swelling that suggests infection.

FOLLOW UP:
Follow up with primary care, sports medicine, occupational health, or orthopedics if function is not improving.
```
