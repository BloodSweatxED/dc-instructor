# Minor superficial burn, small area, without high-risk features

Phenotype ID: `minor_superficial_burn_small_area_no_high_risk_features`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of small superficial minor burn.
- No deep/partial/full-thickness burn concern, circumferential burn, face/hand/genital/major joint location, inhalation injury, infection, chemical/electrical burn, high-risk host, pregnancy/pediatric pathway, or specialist-directed burn plan.

## Exclusions

- Deep, white, charred, circumferential, large, face/hand/genital/major joint burn, inhalation injury, chemical/electrical burn, infection, fever, or systemic illness.
- Diabetes, immunocompromised host, pregnancy/pediatric pathway, unreliable wound care, or specialist-directed burn plan.

## Must-Not-Miss Diagnoses

- Deep burn.
- Inhalation injury.
- Circumferential burn.
- Burn infection.
- High-risk location burn.

## Primitive List

- `minor_superficial_burn_small_area_no_high_risk_features.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `minor_superficial_burn_small_area_no_high_risk_features.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: burn_high_risk_depth_location_or_mechanism, inhalation_injury_concern, secondary_skin_infection_concern, wound_infection_concern, systemic_illness, diabetes_general_risk, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_burn_plan
- `minor_superficial_burn_small_area_no_high_risk_features.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `minor_superficial_burn_small_area_no_high_risk_features.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `minor_superficial_burn_small_area_no_high_risk_features.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `minor_superficial_burn_small_area_no_high_risk_features.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: burn_high_risk_depth_location_or_mechanism, inhalation_injury_concern, secondary_skin_infection_concern, wound_infection_concern, systemic_illness, diabetes_general_risk, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_burn_plan
- `minor_superficial_burn_small_area_no_high_risk_features.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: burn_high_risk_depth_location_or_mechanism, inhalation_injury_concern, secondary_skin_infection_concern, wound_infection_concern, systemic_illness, diabetes_general_risk, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_burn_plan
- `minor_superficial_burn_small_area_no_high_risk_features.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `minor_superficial_burn_small_area_no_high_risk_features.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `minor_superficial_burn_small_area_no_high_risk_features.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `minor_superficial_burn_small_area_no_high_risk_features.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: burn_high_risk_depth_location_or_mechanism, inhalation_injury_concern, secondary_skin_infection_concern, wound_infection_concern, systemic_illness, diabetes_general_risk, immunocompromised, pregnancy, pediatric_pathway, specialist_directed_burn_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit a minor superficial burn.

WHAT WE FOUND:
Your clinician diagnosed a small minor burn. We did not find a deep burn, infection, inhalation injury, high-risk location, or another emergency problem today.

WHAT TO DO AT HOME:
- Keep the burn clean and protected.
- Avoid more heat, sun, friction, or chemical exposure to the area.
- Do not pop blisters or put unsafe substances on the burn.

MEDICATIONS:
- Use burn cream, dressing supplies, or pain medicine only as prescribed or recommended.
- Do not apply butter, oils, toothpaste, or harsh chemicals.

RETURN TO ED IF:
- Increasing redness, warmth, pus, red streaks, fever, or worsening pain.
- Trouble breathing, cough after smoke exposure, face burn, hand/genital burn, circumferential burn, or deep/white/charred skin.
- Burn is larger than expected, crosses a joint, or is not healing.

FOLLOW UP:
Follow up with primary care, urgent care, burn care, or the ED as instructed, especially if pain, redness, or healing is not improving.
```
