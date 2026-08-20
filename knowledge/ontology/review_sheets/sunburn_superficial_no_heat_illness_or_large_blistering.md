# Superficial sunburn without heat illness or large blistering

Phenotype ID: `sunburn_superficial_no_heat_illness_or_large_blistering`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of superficial sunburn.
- No heat illness, dehydration, large blistering, eye involvement, infection, systemic illness, or high-risk host pathway.

## Exclusions

- Heat exhaustion, heat stroke, syncope, confusion, dehydration, persistent vomiting, or unstable vital signs.
- Large blistering burn, face/eye/genital involvement, circumferential burn, chemical burn, infection concern, or severe pain.
- Pediatric, pregnancy, immunocompromised, or specialist-directed burn plan.

## Must-Not-Miss Diagnoses

- Heat stroke.
- Heat exhaustion.
- Severe burn.
- Secondary skin infection.

## Primitive List

- `sunburn_superficial_no_heat_illness_or_large_blistering.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `sunburn_superficial_no_heat_illness_or_large_blistering.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: heat_illness_or_dehydration, large_blistering_or_high_risk_burn, eye_or_genital_rash_location, chemical_eye_exposure, secondary_skin_infection_concern, severe_cutaneous_adverse_reaction, severe_eye_pain, vision_change, immunocompromised, pregnancy, pediatric_pathway, systemic_illness, unstable_vitals, specialist_directed_wound_plan
- `sunburn_superficial_no_heat_illness_or_large_blistering.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `sunburn_superficial_no_heat_illness_or_large_blistering.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `sunburn_superficial_no_heat_illness_or_large_blistering.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `sunburn_superficial_no_heat_illness_or_large_blistering.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: heat_illness_or_dehydration, large_blistering_or_high_risk_burn, eye_or_genital_rash_location, chemical_eye_exposure, secondary_skin_infection_concern, severe_cutaneous_adverse_reaction, severe_eye_pain, vision_change, immunocompromised, pregnancy, pediatric_pathway, systemic_illness, unstable_vitals, specialist_directed_wound_plan
- `sunburn_superficial_no_heat_illness_or_large_blistering.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: heat_illness_or_dehydration, large_blistering_or_high_risk_burn, eye_or_genital_rash_location, chemical_eye_exposure, secondary_skin_infection_concern, severe_cutaneous_adverse_reaction, severe_eye_pain, vision_change, immunocompromised, pregnancy, pediatric_pathway, systemic_illness, unstable_vitals, specialist_directed_wound_plan
- `sunburn_superficial_no_heat_illness_or_large_blistering.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `sunburn_superficial_no_heat_illness_or_large_blistering.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `sunburn_superficial_no_heat_illness_or_large_blistering.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `sunburn_superficial_no_heat_illness_or_large_blistering.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: heat_illness_or_dehydration, large_blistering_or_high_risk_burn, eye_or_genital_rash_location, chemical_eye_exposure, secondary_skin_infection_concern, severe_cutaneous_adverse_reaction, severe_eye_pain, vision_change, immunocompromised, pregnancy, pediatric_pathway, systemic_illness, unstable_vitals, specialist_directed_wound_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit a sunburn.

WHAT WE FOUND:
Your exam was reassuring for a superficial sunburn. We did not find heat illness, severe dehydration, large blistering, or another emergency skin problem today.

WHAT TO DO AT HOME:
- Stay out of the sun while the skin heals.
- Use cool compresses or cool baths for comfort.
- Drink fluids unless your clinician told you to limit fluids.

MEDICATIONS:
- Use acetaminophen or ibuprofen only if you can take it safely and follow the label.
- Use skin products only as directed by your clinician or the product label.

RETURN TO ED IF:
- Fever, chills, confusion, fainting, severe weakness, vomiting, or signs of dehydration.
- Large blisters, severe swelling, worsening pain, pus, or spreading redness.
- Eye pain, vision change, or sunburn involving the eye.

FOLLOW UP:
Follow up with primary care if pain, redness, or peeling is not improving, or sooner if symptoms worsen.
```
