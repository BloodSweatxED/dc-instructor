# Asymptomatic elevated blood pressure without end-organ symptoms

Phenotype ID: `asymptomatic_elevated_blood_pressure_no_end_organ_symptoms`

Status: `draft`

## Inclusion Criteria

- Adult with elevated blood pressure or asymptomatic hypertension documented at ED discharge.
- Explicit clinician documentation that no end-organ symptoms or hypertensive emergency concern are present.
- Concrete outpatient follow-up plan documented.

## Exclusions

- Blood pressure at hypertensive crisis threshold without individualized plan.
- Any end-organ symptom such as chest pain, shortness of breath, neurologic symptoms, severe headache, vision change, confusion, decreased urination, hematuria, or tearing chest or back pain.
- Pregnancy or postpartum pathway.
- Stimulant or cocaine-associated hypertension, secondary hypertension concern, or no reliable follow-up plan.

## Must-Not-Miss Diagnoses

- Hypertensive emergency.
- Stroke or intracranial hemorrhage.
- Acute coronary syndrome.
- Aortic dissection.
- Acute heart failure.
- Preeclampsia or postpartum hypertensive emergency.

## Primitive List

- `asymptomatic_elevated_blood_pressure_no_end_organ_symptoms.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `asymptomatic_elevated_blood_pressure_no_end_organ_symptoms.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: hypertensive_crisis_threshold, hypertension_end_organ_symptoms, chest_pain, respiratory_distress, neurologic_deficit, vision_change, pregnancy, postpartum, poor_follow_up, sepsis, unstable_vitals
- `asymptomatic_elevated_blood_pressure_no_end_organ_symptoms.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `asymptomatic_elevated_blood_pressure_no_end_organ_symptoms.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `asymptomatic_elevated_blood_pressure_no_end_organ_symptoms.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `asymptomatic_elevated_blood_pressure_no_end_organ_symptoms.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: hypertensive_crisis_threshold, hypertension_end_organ_symptoms, chest_pain, respiratory_distress, neurologic_deficit, vision_change, pregnancy, postpartum, poor_follow_up, sepsis, unstable_vitals
- `asymptomatic_elevated_blood_pressure_no_end_organ_symptoms.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: hypertensive_crisis_threshold, hypertension_end_organ_symptoms, chest_pain, respiratory_distress, neurologic_deficit, vision_change, pregnancy, postpartum, poor_follow_up, sepsis, unstable_vitals
- `asymptomatic_elevated_blood_pressure_no_end_organ_symptoms.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `asymptomatic_elevated_blood_pressure_no_end_organ_symptoms.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `asymptomatic_elevated_blood_pressure_no_end_organ_symptoms.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `asymptomatic_elevated_blood_pressure_no_end_organ_symptoms.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: hypertensive_crisis_threshold, hypertension_end_organ_symptoms, chest_pain, respiratory_distress, neurologic_deficit, vision_change, pregnancy, postpartum, poor_follow_up, sepsis, unstable_vitals

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your blood pressure was high today.

WHAT WE FOUND:
You did not have symptoms today suggesting a blood pressure emergency. Your clinician felt it was safe to continue follow-up outside the ED.

WHAT TO DO AT HOME:
- Recheck your blood pressure as your clinician instructed.
- Take your usual blood pressure medicines exactly as prescribed.
- Avoid changing or doubling medicines unless your clinician told you to.

MEDICATIONS:
- Take any new or changed blood pressure medicine exactly as prescribed.
- Do not stop blood pressure medicine without talking with a clinician.

RETURN TO ED IF:
- Chest pain, trouble breathing, severe headache, confusion, fainting, weakness, trouble speaking, or vision changes.
- New back pain, severe belly pain, or neurologic symptoms.
- Blood pressure is very high and you feel ill or unsafe at home.

FOLLOW UP:
Follow up with primary care or urgent care in the timeframe your clinician gave you to recheck blood pressure and adjust medicines if needed.
```
