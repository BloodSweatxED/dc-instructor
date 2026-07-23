# Uncomplicated plantar fasciitis without trauma or neurovascular red flags

Phenotype ID: `plantar_fasciitis_uncomplicated_no_trauma_or_neurovascular_red_flags`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of uncomplicated plantar fasciitis.
- No trauma/fracture concern, infection, open wound, diabetic-foot/PVD/neuropathy risk, neurovascular compromise, inability to walk, pregnancy/pediatric pathway, or specialist-directed plan.

## Exclusions

- Trauma, fracture/dislocation concern, inability to bear weight, neurovascular compromise, open wound, cellulitis, abscess, fever, or systemic illness.
- Diabetic foot risk, neuropathy, PVD, pregnancy/pediatric pathway, or specialist-directed podiatry/orthopedic plan.

## Must-Not-Miss Diagnoses

- Calcaneal fracture.
- Diabetic foot infection.
- Neurovascular compromise.
- Septic joint or deep infection.

## Primitive List

- `plantar_fasciitis_uncomplicated_no_trauma_or_neurovascular_red_flags.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `plantar_fasciitis_uncomplicated_no_trauma_or_neurovascular_red_flags.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, unable_to_bear_weight_lower_extremity, neurovascular_compromise, open_wound, secondary_skin_infection_concern, diabetic_foot, diabetes_general_risk, neuropathy_foot_risk, peripheral_vascular_disease, systemic_illness, pregnancy, pediatric_pathway, specialist_directed_podiatry_plan, specialist_directed_orthopedic_plan
- `plantar_fasciitis_uncomplicated_no_trauma_or_neurovascular_red_flags.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `plantar_fasciitis_uncomplicated_no_trauma_or_neurovascular_red_flags.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `plantar_fasciitis_uncomplicated_no_trauma_or_neurovascular_red_flags.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `plantar_fasciitis_uncomplicated_no_trauma_or_neurovascular_red_flags.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, unable_to_bear_weight_lower_extremity, neurovascular_compromise, open_wound, secondary_skin_infection_concern, diabetic_foot, diabetes_general_risk, neuropathy_foot_risk, peripheral_vascular_disease, systemic_illness, pregnancy, pediatric_pathway, specialist_directed_podiatry_plan, specialist_directed_orthopedic_plan
- `plantar_fasciitis_uncomplicated_no_trauma_or_neurovascular_red_flags.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, unable_to_bear_weight_lower_extremity, neurovascular_compromise, open_wound, secondary_skin_infection_concern, diabetic_foot, diabetes_general_risk, neuropathy_foot_risk, peripheral_vascular_disease, systemic_illness, pregnancy, pediatric_pathway, specialist_directed_podiatry_plan, specialist_directed_orthopedic_plan
- `plantar_fasciitis_uncomplicated_no_trauma_or_neurovascular_red_flags.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `plantar_fasciitis_uncomplicated_no_trauma_or_neurovascular_red_flags.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `plantar_fasciitis_uncomplicated_no_trauma_or_neurovascular_red_flags.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `plantar_fasciitis_uncomplicated_no_trauma_or_neurovascular_red_flags.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, unable_to_bear_weight_lower_extremity, neurovascular_compromise, open_wound, secondary_skin_infection_concern, diabetic_foot, diabetes_general_risk, neuropathy_foot_risk, peripheral_vascular_disease, systemic_illness, pregnancy, pediatric_pathway, specialist_directed_podiatry_plan, specialist_directed_orthopedic_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit plantar fasciitis, irritation of tissue on the bottom of the foot.

WHAT WE FOUND:
Your clinician diagnosed uncomplicated plantar fasciitis. We did not find fracture concern, infection, diabetic-foot risk, or neurovascular problem today.

WHAT TO DO AT HOME:
- Rest from activities that worsen the pain.
- Use supportive shoes or inserts if recommended.
- Do gentle stretches only as instructed and stop if pain worsens.

MEDICATIONS:
- Use pain medicine only if prescribed or recommended, and follow the label.
- Avoid medicines your clinician told you to avoid.

RETURN TO ED IF:
- Unable to walk, new numbness, weakness, cold/blue foot, or severe worsening pain.
- Fever, spreading redness, pus, open wound, or red streaks.
- New injury, fracture concern, or symptoms not improving with the plan.

FOLLOW UP:
Follow up with primary care, podiatry, sports medicine, or orthopedics if pain persists or walking remains limited.
```
