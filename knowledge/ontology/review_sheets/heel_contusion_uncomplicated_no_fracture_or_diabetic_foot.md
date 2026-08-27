# Heel contusion without fracture or diabetic-foot red flags

Phenotype ID: `heel_contusion_uncomplicated_no_fracture_or_diabetic_foot`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of uncomplicated heel contusion.
- No fracture concern, diabetic-foot pathway, infection, wound, or neurovascular compromise.

## Exclusions

- Fracture or dislocation concern, open wound, diabetic foot, peripheral vascular disease, neuropathy, infection, high-energy trauma, or specialist-directed podiatry plan.

## Must-Not-Miss Diagnoses

- Calcaneus fracture.
- Diabetic foot infection.
- Neurovascular compromise.
- Compartment syndrome.

## Primitive List

- `heel_contusion_uncomplicated_no_fracture_or_diabetic_foot.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `heel_contusion_uncomplicated_no_fracture_or_diabetic_foot.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, open_wound, diabetic_foot, peripheral_vascular_disease, neuropathy_foot_risk, septic_joint_or_infection_concern, high_energy_trauma, neurovascular_compromise, specialist_directed_podiatry_plan
- `heel_contusion_uncomplicated_no_fracture_or_diabetic_foot.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `heel_contusion_uncomplicated_no_fracture_or_diabetic_foot.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `heel_contusion_uncomplicated_no_fracture_or_diabetic_foot.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `heel_contusion_uncomplicated_no_fracture_or_diabetic_foot.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, open_wound, diabetic_foot, peripheral_vascular_disease, neuropathy_foot_risk, septic_joint_or_infection_concern, high_energy_trauma, neurovascular_compromise, specialist_directed_podiatry_plan
- `heel_contusion_uncomplicated_no_fracture_or_diabetic_foot.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, open_wound, diabetic_foot, peripheral_vascular_disease, neuropathy_foot_risk, septic_joint_or_infection_concern, high_energy_trauma, neurovascular_compromise, specialist_directed_podiatry_plan
- `heel_contusion_uncomplicated_no_fracture_or_diabetic_foot.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `heel_contusion_uncomplicated_no_fracture_or_diabetic_foot.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `heel_contusion_uncomplicated_no_fracture_or_diabetic_foot.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `heel_contusion_uncomplicated_no_fracture_or_diabetic_foot.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: fracture_or_dislocation_concern, open_wound, diabetic_foot, peripheral_vascular_disease, neuropathy_foot_risk, septic_joint_or_infection_concern, high_energy_trauma, neurovascular_compromise, specialist_directed_podiatry_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit a heel bruise.

WHAT WE FOUND:
Your clinician diagnosed a heel bruise. We did not find signs of fracture, poor circulation, infection, or a diabetic-foot emergency today.

WHAT TO DO AT HOME:
- Rest the heel as needed.
- Use ice wrapped in a cloth for short periods.
- Raise the foot when you can.

MEDICATIONS:
- Use acetaminophen or ibuprofen only if you can take it safely and follow the label.
- Use medicines only as prescribed or recommended.

RETURN TO ED IF:
- Worsening pain, new numbness, blue or pale toes, or inability to walk.
- Spreading redness, fever, pus, or a new wound.
- Symptoms that worsen or do not improve as expected.

FOLLOW UP:
Follow up with primary care, podiatry, urgent care, or the ED if symptoms are not improving or your clinician told you to recheck.
```
