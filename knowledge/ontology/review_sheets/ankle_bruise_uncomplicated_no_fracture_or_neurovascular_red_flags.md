# Uncomplicated ankle bruise without fracture or neurovascular red flags

Phenotype ID: `ankle_bruise_uncomplicated_no_fracture_or_neurovascular_red_flags`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of uncomplicated ankle bruise/contusion.
- No fracture/dislocation concern, open wound, infection, neurovascular compromise, inability to bear weight, high-energy trauma, pregnancy/pediatric pathway, or specialist-directed plan.

## Exclusions

- Fracture/dislocation concern, open wound, infection, neurovascular compromise, severe pain, inability to bear weight, high-energy trauma, crush injury, compartment syndrome concern, anticoagulation/bleeding risk, or unexplained bruising/abuse concern.
- Pregnancy/pediatric pathway or specialist-directed orthopedic plan.

## Must-Not-Miss Diagnoses

- Fracture or dislocation.
- Neurovascular compromise.
- Compartment syndrome.
- Cellulitis or abscess.
- Bleeding disorder or unsafe bruising pattern.

## Primitive List

- `ankle_bruise_uncomplicated_no_fracture_or_neurovascular_red_flags.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `ankle_bruise_uncomplicated_no_fracture_or_neurovascular_red_flags.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, open_wound, secondary_skin_infection_concern, neurovascular_compromise, severe_pain, unable_to_bear_weight_lower_extremity, high_energy_trauma, crush_injury, compartment_syndrome_concern, anticoagulated, unexplained_bruising_or_abuse_concern, pregnancy, pediatric_pathway, specialist_directed_orthopedic_plan
- `ankle_bruise_uncomplicated_no_fracture_or_neurovascular_red_flags.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `ankle_bruise_uncomplicated_no_fracture_or_neurovascular_red_flags.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `ankle_bruise_uncomplicated_no_fracture_or_neurovascular_red_flags.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `ankle_bruise_uncomplicated_no_fracture_or_neurovascular_red_flags.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, open_wound, secondary_skin_infection_concern, neurovascular_compromise, severe_pain, unable_to_bear_weight_lower_extremity, high_energy_trauma, crush_injury, compartment_syndrome_concern, anticoagulated, unexplained_bruising_or_abuse_concern, pregnancy, pediatric_pathway, specialist_directed_orthopedic_plan
- `ankle_bruise_uncomplicated_no_fracture_or_neurovascular_red_flags.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, open_wound, secondary_skin_infection_concern, neurovascular_compromise, severe_pain, unable_to_bear_weight_lower_extremity, high_energy_trauma, crush_injury, compartment_syndrome_concern, anticoagulated, unexplained_bruising_or_abuse_concern, pregnancy, pediatric_pathway, specialist_directed_orthopedic_plan
- `ankle_bruise_uncomplicated_no_fracture_or_neurovascular_red_flags.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `ankle_bruise_uncomplicated_no_fracture_or_neurovascular_red_flags.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `ankle_bruise_uncomplicated_no_fracture_or_neurovascular_red_flags.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `ankle_bruise_uncomplicated_no_fracture_or_neurovascular_red_flags.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, open_wound, secondary_skin_infection_concern, neurovascular_compromise, severe_pain, unable_to_bear_weight_lower_extremity, high_energy_trauma, crush_injury, compartment_syndrome_concern, anticoagulated, unexplained_bruising_or_abuse_concern, pregnancy, pediatric_pathway, specialist_directed_orthopedic_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit an ankle bruise.

WHAT WE FOUND:
Your clinician diagnosed an uncomplicated ankle bruise. We did not find fracture concern, open wound, neurovascular compromise, infection, or another emergency problem today.

WHAT TO DO AT HOME:
- Rest from activity that worsens pain.
- Use ice, elevation, compression, or support only as instructed.
- Return to walking and activity gradually as symptoms improve.

MEDICATIONS:
- Use pain medicine only if prescribed or recommended, and follow the label.
- Avoid medicines your clinician told you to avoid.

RETURN TO ED IF:
- New numbness, color change, severe pain, or inability to walk.
- Spreading redness, warmth, pus, fever, or worsening swelling.
- New deformity, worsening pain, or symptoms not improving.

FOLLOW UP:
Follow up with primary care, sports medicine, or orthopedics if pain, swelling, or walking is not improving.
```
