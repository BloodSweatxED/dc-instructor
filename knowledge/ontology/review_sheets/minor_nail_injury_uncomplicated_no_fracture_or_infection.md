# Minor nail injury without fracture, nail-bed laceration, or infection

Phenotype ID: `minor_nail_injury_uncomplicated_no_fracture_or_infection`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of minor nail injury/subungual bruising.
- No open fracture, nail-bed laceration needing repair, crush injury emergency, infection, neurovascular compromise, diabetic-foot/PVD/neuropathy risk, pregnancy/pediatric pathway, or specialist-directed plan.

## Exclusions

- Open fracture, fracture/dislocation concern, nail-bed laceration needing repair, severe crush injury, uncontrolled pain, infection, open wound with contamination, neurovascular compromise, or inability to use digit.
- Diabetic foot risk, neuropathy, PVD, pregnancy/pediatric pathway, or specialist-directed hand/podiatry plan.

## Must-Not-Miss Diagnoses

- Open fracture.
- Nail-bed laceration.
- Neurovascular compromise.
- Cellulitis or abscess.
- Diabetic foot injury.

## Primitive List

- `minor_nail_injury_uncomplicated_no_fracture_or_infection.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `minor_nail_injury_uncomplicated_no_fracture_or_infection.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: open_fracture, fracture_or_dislocation_concern, severe_pain, secondary_skin_infection_concern, open_wound, neurovascular_compromise, diabetic_foot, neuropathy_foot_risk, peripheral_vascular_disease, pregnancy, pediatric_pathway, specialist_directed_wound_plan, specialist_directed_podiatry_plan, specialist_directed_orthopedic_plan
- `minor_nail_injury_uncomplicated_no_fracture_or_infection.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `minor_nail_injury_uncomplicated_no_fracture_or_infection.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `minor_nail_injury_uncomplicated_no_fracture_or_infection.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `minor_nail_injury_uncomplicated_no_fracture_or_infection.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: open_fracture, fracture_or_dislocation_concern, severe_pain, secondary_skin_infection_concern, open_wound, neurovascular_compromise, diabetic_foot, neuropathy_foot_risk, peripheral_vascular_disease, pregnancy, pediatric_pathway, specialist_directed_wound_plan, specialist_directed_podiatry_plan, specialist_directed_orthopedic_plan
- `minor_nail_injury_uncomplicated_no_fracture_or_infection.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: open_fracture, fracture_or_dislocation_concern, severe_pain, secondary_skin_infection_concern, open_wound, neurovascular_compromise, diabetic_foot, neuropathy_foot_risk, peripheral_vascular_disease, pregnancy, pediatric_pathway, specialist_directed_wound_plan, specialist_directed_podiatry_plan, specialist_directed_orthopedic_plan
- `minor_nail_injury_uncomplicated_no_fracture_or_infection.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `minor_nail_injury_uncomplicated_no_fracture_or_infection.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `minor_nail_injury_uncomplicated_no_fracture_or_infection.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `minor_nail_injury_uncomplicated_no_fracture_or_infection.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: open_fracture, fracture_or_dislocation_concern, severe_pain, secondary_skin_infection_concern, open_wound, neurovascular_compromise, diabetic_foot, neuropathy_foot_risk, peripheral_vascular_disease, pregnancy, pediatric_pathway, specialist_directed_wound_plan, specialist_directed_podiatry_plan, specialist_directed_orthopedic_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit a minor nail injury.

WHAT WE FOUND:
Your clinician diagnosed a minor nail injury. We did not find open fracture, nail-bed laceration needing repair, infection, neurovascular compromise, or another emergency problem today.

WHAT TO DO AT HOME:
- Keep the nail area clean and protected.
- Avoid picking, cutting, or drilling the nail at home.
- Protect the finger or toe from repeat injury while it heals.

MEDICATIONS:
- Use pain medicine only if prescribed or recommended, and follow the label.
- Take antibiotics only if your clinician prescribed them for a separate reason.

RETURN TO ED IF:
- Severe worsening pain, numbness, color change, or inability to move the finger or toe.
- Spreading redness, warmth, pus, red streaks, fever, or worsening swelling.
- The nail lifts off, the wound opens, or there is new fracture concern.

FOLLOW UP:
Follow up with primary care, urgent care, podiatry, or hand/orthopedic care if pain or nail healing is not improving.
```
