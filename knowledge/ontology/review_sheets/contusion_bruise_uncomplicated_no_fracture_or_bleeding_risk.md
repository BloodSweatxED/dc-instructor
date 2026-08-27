# Uncomplicated bruise or contusion without fracture or bleeding risk

Phenotype ID: `contusion_bruise_uncomplicated_no_fracture_or_bleeding_risk`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of uncomplicated bruise or soft-tissue contusion.
- No fracture/dislocation concern, compartment syndrome, neurovascular compromise, anticoagulation/bleeding disorder, non-accidental trauma concern, or specialist-directed plan.

## Exclusions

- Fracture, dislocation, open wound, severe pain, compartment syndrome, neurovascular compromise, inability to use limb, or high-energy trauma.
- Anticoagulation, bleeding disorder, unexplained bruising, abuse/assault concern, pregnancy/pediatric pathway, or specialist-directed orthopedic plan.

## Must-Not-Miss Diagnoses

- Fracture or dislocation.
- Compartment syndrome.
- Neurovascular injury.
- Bleeding disorder or anticoagulation complication.
- Non-accidental trauma.

## Primitive List

- `contusion_bruise_uncomplicated_no_fracture_or_bleeding_risk.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `contusion_bruise_uncomplicated_no_fracture_or_bleeding_risk.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, open_wound, severe_pain, compartment_syndrome_concern, neurovascular_compromise, unable_to_use_limb, high_energy_trauma, anticoagulated, bleeding_disorder, unexplained_bruising_or_abuse_concern, pregnancy, pediatric_pathway, specialist_directed_orthopedic_plan
- `contusion_bruise_uncomplicated_no_fracture_or_bleeding_risk.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `contusion_bruise_uncomplicated_no_fracture_or_bleeding_risk.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `contusion_bruise_uncomplicated_no_fracture_or_bleeding_risk.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `contusion_bruise_uncomplicated_no_fracture_or_bleeding_risk.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, open_wound, severe_pain, compartment_syndrome_concern, neurovascular_compromise, unable_to_use_limb, high_energy_trauma, anticoagulated, bleeding_disorder, unexplained_bruising_or_abuse_concern, pregnancy, pediatric_pathway, specialist_directed_orthopedic_plan
- `contusion_bruise_uncomplicated_no_fracture_or_bleeding_risk.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, open_wound, severe_pain, compartment_syndrome_concern, neurovascular_compromise, unable_to_use_limb, high_energy_trauma, anticoagulated, bleeding_disorder, unexplained_bruising_or_abuse_concern, pregnancy, pediatric_pathway, specialist_directed_orthopedic_plan
- `contusion_bruise_uncomplicated_no_fracture_or_bleeding_risk.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `contusion_bruise_uncomplicated_no_fracture_or_bleeding_risk.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `contusion_bruise_uncomplicated_no_fracture_or_bleeding_risk.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `contusion_bruise_uncomplicated_no_fracture_or_bleeding_risk.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, open_wound, severe_pain, compartment_syndrome_concern, neurovascular_compromise, unable_to_use_limb, high_energy_trauma, anticoagulated, bleeding_disorder, unexplained_bruising_or_abuse_concern, pregnancy, pediatric_pathway, specialist_directed_orthopedic_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit a bruise or soft-tissue contusion.

WHAT WE FOUND:
Your clinician diagnosed an uncomplicated bruise or contusion. We did not find fracture concern, dangerous bleeding risk, neurovascular problem, or abuse concern today.

WHAT TO DO AT HOME:
- Rest and protect the bruised area.
- Use cold packs early if your clinician said they are safe for you.
- Raise the area when practical to reduce swelling.

MEDICATIONS:
- Use pain medicine only as prescribed or recommended, and follow the label.
- Avoid medicines your clinician told you to avoid because of bleeding risk.

RETURN TO ED IF:
- Severe or worsening pain, numbness, weakness, color change, tight swelling, or trouble using the limb.
- Large unexplained bruises, bleeding that will not stop, black stool, fainting, or new bruises without injury.
- New concern for fracture, abuse, unsafe home situation, or symptoms not improving as expected.

FOLLOW UP:
Follow up with primary care, urgent care, occupational health, or orthopedics if pain, swelling, or function is not improving.
```
