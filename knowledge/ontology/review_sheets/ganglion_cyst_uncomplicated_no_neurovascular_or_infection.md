# Uncomplicated ganglion cyst without neurovascular symptoms or infection

Phenotype ID: `ganglion_cyst_uncomplicated_no_neurovascular_or_infection`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of uncomplicated ganglion cyst.
- No infection, open wound, neurovascular compromise, trauma/fracture concern, rapidly enlarging or diagnostically uncertain mass, pregnancy/pediatric pathway, or specialist-directed plan.

## Exclusions

- Neurovascular compromise, severe pain, infection, open wound, trauma/fracture concern, rapidly enlarging mass, hard/fixed mass, malignancy concern, or diagnostic uncertainty.
- Pregnancy/pediatric pathway or specialist-directed orthopedic/hand plan.

## Must-Not-Miss Diagnoses

- Neurovascular compromise.
- Infected cyst or abscess.
- Fracture or tendon injury mimic.
- Concerning soft-tissue mass.

## Primitive List

- `ganglion_cyst_uncomplicated_no_neurovascular_or_infection.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `ganglion_cyst_uncomplicated_no_neurovascular_or_infection.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: neurovascular_compromise, severe_pain, secondary_skin_infection_concern, open_wound, fracture_or_dislocation_concern, mass_red_flag_or_diagnostic_uncertainty, pregnancy, pediatric_pathway, specialist_directed_orthopedic_plan
- `ganglion_cyst_uncomplicated_no_neurovascular_or_infection.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `ganglion_cyst_uncomplicated_no_neurovascular_or_infection.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `ganglion_cyst_uncomplicated_no_neurovascular_or_infection.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `ganglion_cyst_uncomplicated_no_neurovascular_or_infection.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: neurovascular_compromise, severe_pain, secondary_skin_infection_concern, open_wound, fracture_or_dislocation_concern, mass_red_flag_or_diagnostic_uncertainty, pregnancy, pediatric_pathway, specialist_directed_orthopedic_plan
- `ganglion_cyst_uncomplicated_no_neurovascular_or_infection.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: neurovascular_compromise, severe_pain, secondary_skin_infection_concern, open_wound, fracture_or_dislocation_concern, mass_red_flag_or_diagnostic_uncertainty, pregnancy, pediatric_pathway, specialist_directed_orthopedic_plan
- `ganglion_cyst_uncomplicated_no_neurovascular_or_infection.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `ganglion_cyst_uncomplicated_no_neurovascular_or_infection.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `ganglion_cyst_uncomplicated_no_neurovascular_or_infection.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `ganglion_cyst_uncomplicated_no_neurovascular_or_infection.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: neurovascular_compromise, severe_pain, secondary_skin_infection_concern, open_wound, fracture_or_dislocation_concern, mass_red_flag_or_diagnostic_uncertainty, pregnancy, pediatric_pathway, specialist_directed_orthopedic_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit a ganglion cyst, a fluid-filled swelling near a joint or tendon.

WHAT WE FOUND:
Your clinician diagnosed an uncomplicated ganglion cyst. We did not find infection, neurovascular compromise, trauma, or a concerning mass feature today.

WHAT TO DO AT HOME:
- Protect the area from repeated pressure or irritation.
- Avoid trying to puncture, squeeze, or drain the cyst at home.
- Use the splint or activity changes only if your clinician recommended them.

MEDICATIONS:
- Use pain medicine only if prescribed or recommended, and follow the label.
- Avoid medicines your clinician told you to avoid.

RETURN TO ED IF:
- New numbness, weakness, color change, severe pain, or trouble using the hand or wrist.
- Fever, spreading redness, warmth, pus, or red streaks.
- The mass grows quickly, becomes hard/fixed, follows trauma, or the diagnosis is uncertain.

FOLLOW UP:
Follow up with primary care, orthopedics, hand surgery, or sports medicine if symptoms persist, function is limited, or your clinician told you to recheck.
```
