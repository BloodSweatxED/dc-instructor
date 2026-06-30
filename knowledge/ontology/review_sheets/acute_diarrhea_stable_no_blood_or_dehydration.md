# Acute diarrhea, stable, without blood or dehydration

Phenotype ID: `acute_diarrhea_stable_no_blood_or_dehydration`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of acute uncomplicated diarrhea.
- Stable for discharge and able to hydrate, with no blood in stool, severe abdominal pain, dehydration, C diff risk, pregnancy/pediatric pathway, or high-risk host pathway.

## Exclusions

- Blood or black stool, severe abdominal pain, dehydration, inability to tolerate oral fluids, fever with severe illness, sepsis, or unstable vitals.
- Recent antibiotics/C diff concern, immunocompromised host, elderly frail pathway, pregnancy/pediatric pathway, travel/outbreak pathway needing public-health handling, or specialist-directed plan.

## Must-Not-Miss Diagnoses

- GI bleeding.
- Severe dehydration.
- Surgical abdomen.
- C diff colitis.
- Sepsis.

## Primitive List

- `acute_diarrhea_stable_no_blood_or_dehydration.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `acute_diarrhea_stable_no_blood_or_dehydration.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: gi_bleeding, severe_or_focal_abdominal_pain, dehydration_or_unable_to_drink, unable_to_tolerate_oral_fluids, c_diff_risk, sepsis, unstable_vitals, immunocompromised, elderly_frail, pregnancy, pediatric_pathway, travel_or_outbreak_diarrhea_pathway
- `acute_diarrhea_stable_no_blood_or_dehydration.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `acute_diarrhea_stable_no_blood_or_dehydration.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `acute_diarrhea_stable_no_blood_or_dehydration.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `acute_diarrhea_stable_no_blood_or_dehydration.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: gi_bleeding, severe_or_focal_abdominal_pain, dehydration_or_unable_to_drink, unable_to_tolerate_oral_fluids, c_diff_risk, sepsis, unstable_vitals, immunocompromised, elderly_frail, pregnancy, pediatric_pathway, travel_or_outbreak_diarrhea_pathway
- `acute_diarrhea_stable_no_blood_or_dehydration.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: gi_bleeding, severe_or_focal_abdominal_pain, dehydration_or_unable_to_drink, unable_to_tolerate_oral_fluids, c_diff_risk, sepsis, unstable_vitals, immunocompromised, elderly_frail, pregnancy, pediatric_pathway, travel_or_outbreak_diarrhea_pathway
- `acute_diarrhea_stable_no_blood_or_dehydration.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `acute_diarrhea_stable_no_blood_or_dehydration.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `acute_diarrhea_stable_no_blood_or_dehydration.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `acute_diarrhea_stable_no_blood_or_dehydration.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: gi_bleeding, severe_or_focal_abdominal_pain, dehydration_or_unable_to_drink, unable_to_tolerate_oral_fluids, c_diff_risk, sepsis, unstable_vitals, immunocompromised, elderly_frail, pregnancy, pediatric_pathway, travel_or_outbreak_diarrhea_pathway

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit acute diarrhea.

WHAT WE FOUND:
Your clinician diagnosed acute diarrhea that was safe for home care today. We did not find blood in the stool, severe dehydration, severe abdominal pain, or another emergency problem.

WHAT TO DO AT HOME:
- Drink fluids as your clinician said is safe for you.
- Start with foods you can tolerate and advance slowly.
- Wash your hands well to avoid spreading infection.

MEDICATIONS:
- Use diarrhea medicine only if prescribed or recommended.
- Do not use anti-diarrhea medicine if you develop fever, bloody stool, or severe belly pain unless your clinician told you to.

RETURN TO ED IF:
- Blood or black stool, severe belly pain, fainting, confusion, or fever.
- Signs of dehydration, such as very little urine, dizziness, dry mouth, or inability to keep fluids down.
- Symptoms persist longer than expected or worsen despite the plan.

FOLLOW UP:
Follow up with primary care or urgent care if symptoms are not improving, recur, or you were told to recheck.
```
