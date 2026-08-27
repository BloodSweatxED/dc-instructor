# Ear canal irritation after swimming without otitis externa or foreign body red flags

Phenotype ID: `ear_canal_irritation_after_swimming_no_otitis_externa_or_foreign_body`

Status: `reviewed`

## Inclusion Criteria

- Adult with clinician diagnosis or discharge impression of uncomplicated ear canal irritation after swimming.
- No emergency red flags, pregnancy/pediatric pathway, or specialist-directed plan.

## Exclusions

- Red flags requiring a separate ED pathway, unstable vital signs, pregnancy/pediatric pathway, or specialist-directed plan.

## Must-Not-Miss Diagnoses

- Posterior or severe bleeding.
- Deep infection.
- Foreign body or trauma.
- High-risk host complication.

## Primitive List

- `ear_canal_irritation_after_swimming_no_otitis_externa_or_foreign_body.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `ear_canal_irritation_after_swimming_no_otitis_externa_or_foreign_body.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: ear_trauma_or_foreign_body, mastoiditis_or_deep_ear_infection_concern, diabetes_general_risk, immunocompromised, fever, specialist_directed_ent_plan
- `ear_canal_irritation_after_swimming_no_otitis_externa_or_foreign_body.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `ear_canal_irritation_after_swimming_no_otitis_externa_or_foreign_body.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `ear_canal_irritation_after_swimming_no_otitis_externa_or_foreign_body.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `ear_canal_irritation_after_swimming_no_otitis_externa_or_foreign_body.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: ear_trauma_or_foreign_body, mastoiditis_or_deep_ear_infection_concern, diabetes_general_risk, immunocompromised, fever, specialist_directed_ent_plan
- `ear_canal_irritation_after_swimming_no_otitis_externa_or_foreign_body.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: ear_trauma_or_foreign_body, mastoiditis_or_deep_ear_infection_concern, diabetes_general_risk, immunocompromised, fever, specialist_directed_ent_plan
- `ear_canal_irritation_after_swimming_no_otitis_externa_or_foreign_body.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `ear_canal_irritation_after_swimming_no_otitis_externa_or_foreign_body.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `ear_canal_irritation_after_swimming_no_otitis_externa_or_foreign_body.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `ear_canal_irritation_after_swimming_no_otitis_externa_or_foreign_body.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: ear_trauma_or_foreign_body, mastoiditis_or_deep_ear_infection_concern, diabetes_general_risk, immunocompromised, fever, specialist_directed_ent_plan

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit uncomplicated ear canal irritation after swimming.

WHAT WE FOUND:
Your clinician diagnosed ear canal irritation after swimming. We did not find red flags requiring a separate emergency pathway today.

WHAT TO DO AT HOME:
- Avoid picking, probing, or putting objects into the affected area.
- Use the care plan your clinician recommended.
- Keep follow-up if your clinician asked for recheck.

MEDICATIONS:
- Use medicines only if prescribed or recommended.
- Do not add leftover antibiotics, drops, sprays, or packing care unless your clinician told you to.

RETURN TO ED IF:
- Bleeding that will not stop, worsening pain, fever, swelling, or feeling very ill.
- Dizziness, fainting, severe headache, trouble breathing, or new neurologic symptoms.
- Symptoms that recur, worsen, or do not improve as expected.

FOLLOW UP:
Follow up with primary care, ENT, urgent care, or the ED if symptoms are not improving or your clinician told you to recheck.
```
