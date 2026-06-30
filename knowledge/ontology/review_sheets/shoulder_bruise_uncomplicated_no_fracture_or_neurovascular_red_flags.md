# Uncomplicated shoulder bruise without fracture or neurovascular red flags

Phenotype ID: `shoulder_bruise_uncomplicated_no_fracture_or_neurovascular_red_flags`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of uncomplicated shoulder bruise/contusion.
- No fracture/dislocation concern, tendon rupture, open wound, infection, neurovascular compromise, high-energy trauma, cardiopulmonary mimic, pregnancy/pediatric pathway, or specialist-directed plan.

## Exclusions

- Fracture/dislocation concern, tendon rupture, open wound, infection, neurovascular compromise, severe pain, inability to use limb, high-energy trauma, crush injury, compartment syndrome concern, anticoagulation/bleeding risk, unexplained bruising/abuse concern, or cardiac/PE mimic.
- Pregnancy/pediatric pathway or specialist-directed orthopedic plan.

## Must-Not-Miss Diagnoses

- Fracture or dislocation.
- Tendon rupture.
- Neurovascular compromise.
- Compartment syndrome.
- Cardiopulmonary mimic when presentation is not clearly local trauma.

## Primitive List

- `shoulder_bruise_uncomplicated_no_fracture_or_neurovascular_red_flags.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `shoulder_bruise_uncomplicated_no_fracture_or_neurovascular_red_flags.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, tendon_or_ligament_rupture_concern, open_wound, secondary_skin_infection_concern, neurovascular_compromise, severe_pain, unable_to_use_limb, high_energy_trauma, crush_injury, compartment_syndrome_concern, anticoagulated, unexplained_bruising_or_abuse_concern, cardiac_or_pe_chest_pain_concern, pregnancy, pediatric_pathway, specialist_directed_orthopedic_plan
- `shoulder_bruise_uncomplicated_no_fracture_or_neurovascular_red_flags.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `shoulder_bruise_uncomplicated_no_fracture_or_neurovascular_red_flags.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `shoulder_bruise_uncomplicated_no_fracture_or_neurovascular_red_flags.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `shoulder_bruise_uncomplicated_no_fracture_or_neurovascular_red_flags.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, tendon_or_ligament_rupture_concern, open_wound, secondary_skin_infection_concern, neurovascular_compromise, severe_pain, unable_to_use_limb, high_energy_trauma, crush_injury, compartment_syndrome_concern, anticoagulated, unexplained_bruising_or_abuse_concern, cardiac_or_pe_chest_pain_concern, pregnancy, pediatric_pathway, specialist_directed_orthopedic_plan
- `shoulder_bruise_uncomplicated_no_fracture_or_neurovascular_red_flags.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, tendon_or_ligament_rupture_concern, open_wound, secondary_skin_infection_concern, neurovascular_compromise, severe_pain, unable_to_use_limb, high_energy_trauma, crush_injury, compartment_syndrome_concern, anticoagulated, unexplained_bruising_or_abuse_concern, cardiac_or_pe_chest_pain_concern, pregnancy, pediatric_pathway, specialist_directed_orthopedic_plan
- `shoulder_bruise_uncomplicated_no_fracture_or_neurovascular_red_flags.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `shoulder_bruise_uncomplicated_no_fracture_or_neurovascular_red_flags.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `shoulder_bruise_uncomplicated_no_fracture_or_neurovascular_red_flags.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `shoulder_bruise_uncomplicated_no_fracture_or_neurovascular_red_flags.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, tendon_or_ligament_rupture_concern, open_wound, secondary_skin_infection_concern, neurovascular_compromise, severe_pain, unable_to_use_limb, high_energy_trauma, crush_injury, compartment_syndrome_concern, anticoagulated, unexplained_bruising_or_abuse_concern, cardiac_or_pe_chest_pain_concern, pregnancy, pediatric_pathway, specialist_directed_orthopedic_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit a shoulder bruise.

WHAT WE FOUND:
Your clinician diagnosed an uncomplicated shoulder bruise. We did not find fracture or dislocation concern, tendon rupture, open wound, neurovascular compromise, or another emergency problem today.

WHAT TO DO AT HOME:
- Rest from lifting or activity that worsens pain.
- Use ice, heat, a sling, or gentle movement only as instructed.
- Return to activity gradually as symptoms improve.

MEDICATIONS:
- Use pain medicine only if prescribed or recommended, and follow the label.
- Avoid medicines your clinician told you to avoid.

RETURN TO ED IF:
- New numbness, weakness, color change, severe pain, or inability to use the arm.
- Spreading redness, warmth, pus, fever, or worsening swelling.
- New deformity, chest pain, shortness of breath, or symptoms not improving.

FOLLOW UP:
Follow up with primary care, sports medicine, or orthopedics if pain, motion, or strength is not improving.
```
