# Uncomplicated tendinitis without rupture or infection concern

Phenotype ID: `tendinitis_uncomplicated_no_rupture_or_infection`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of uncomplicated tendinitis/tendonitis.
- No tendon rupture concern, infection, open wound, fracture/dislocation concern, neurovascular compromise, high-energy trauma, pregnancy/pediatric pathway, or specialist-directed plan.

## Exclusions

- Tendon rupture concern, inability to move/use limb, infection, open wound, fever, systemic illness, fracture/dislocation concern, neurovascular compromise, compartment syndrome, or high-energy trauma.
- Pregnancy/pediatric pathway or specialist-directed orthopedic/sports medicine plan.

## Must-Not-Miss Diagnoses

- Tendon rupture.
- Septic joint or deep infection.
- Fracture or dislocation.
- Neurovascular compromise.
- Compartment syndrome.

## Primitive List

- `tendinitis_uncomplicated_no_rupture_or_infection.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `tendinitis_uncomplicated_no_rupture_or_infection.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: tendon_or_ligament_rupture_concern, unable_to_use_limb, secondary_skin_infection_concern, open_wound, systemic_illness, fracture_or_dislocation_concern, neurovascular_compromise, compartment_syndrome_concern, high_energy_trauma, pregnancy, pediatric_pathway, specialist_directed_orthopedic_plan
- `tendinitis_uncomplicated_no_rupture_or_infection.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `tendinitis_uncomplicated_no_rupture_or_infection.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `tendinitis_uncomplicated_no_rupture_or_infection.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `tendinitis_uncomplicated_no_rupture_or_infection.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: tendon_or_ligament_rupture_concern, unable_to_use_limb, secondary_skin_infection_concern, open_wound, systemic_illness, fracture_or_dislocation_concern, neurovascular_compromise, compartment_syndrome_concern, high_energy_trauma, pregnancy, pediatric_pathway, specialist_directed_orthopedic_plan
- `tendinitis_uncomplicated_no_rupture_or_infection.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: tendon_or_ligament_rupture_concern, unable_to_use_limb, secondary_skin_infection_concern, open_wound, systemic_illness, fracture_or_dislocation_concern, neurovascular_compromise, compartment_syndrome_concern, high_energy_trauma, pregnancy, pediatric_pathway, specialist_directed_orthopedic_plan
- `tendinitis_uncomplicated_no_rupture_or_infection.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `tendinitis_uncomplicated_no_rupture_or_infection.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `tendinitis_uncomplicated_no_rupture_or_infection.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `tendinitis_uncomplicated_no_rupture_or_infection.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: tendon_or_ligament_rupture_concern, unable_to_use_limb, secondary_skin_infection_concern, open_wound, systemic_illness, fracture_or_dislocation_concern, neurovascular_compromise, compartment_syndrome_concern, high_energy_trauma, pregnancy, pediatric_pathway, specialist_directed_orthopedic_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit tendinitis, irritation or inflammation of a tendon.

WHAT WE FOUND:
Your clinician diagnosed uncomplicated tendinitis. We did not find tendon rupture, infection, fracture, neurovascular compromise, or another emergency problem today.

WHAT TO DO AT HOME:
- Rest from activities that worsen the pain.
- Use ice, support, or activity changes only as instructed.
- Return to activity gradually as symptoms improve.

MEDICATIONS:
- Use pain medicine only if prescribed or recommended, and follow the label.
- Avoid medicines your clinician told you to avoid.

RETURN TO ED IF:
- A pop, sudden weakness, inability to move the area, or concern for tendon rupture.
- Fever, spreading redness, warmth, pus, or severe worsening pain.
- New numbness, color change, injury, fracture concern, or trouble using the limb.

FOLLOW UP:
Follow up with primary care, sports medicine, occupational health, or orthopedics if function is not improving or your clinician told you to recheck.
```
