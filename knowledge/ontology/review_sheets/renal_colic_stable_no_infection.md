# Renal colic, stable, no infection concern

Phenotype ID: `renal_colic_stable_no_infection`

Status: `draft`

## Inclusion Criteria

- Suspected or confirmed renal colic, stable for outpatient management.
- No fever, sepsis, solitary kidney emergency, or uncontrolled symptoms.

## Exclusions

- Infected obstructing stone concern.
- Solitary kidney, transplant kidney, pregnancy, renal failure, or uncontrolled pain/vomiting.

## Must-Not-Miss Diagnoses

- Infected obstructing stone.
- Abdominal aortic emergency mimic.
- Testicular torsion mimic.
- Pyelonephritis.

## Primitive List

- `renal_colic_stable_no_infection.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_needed, clinician_judgment_only | unsafe modifiers: none
- `renal_colic_stable_no_infection.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_needed, clinician_judgment_only, unsafe_without_modifier | unsafe modifiers: fever, solitary_kidney, pregnancy, renal_failure, uncontrolled_pain
- `renal_colic_stable_no_infection.home_care.home_care_1.v1` | `home_care` | audit: source_needed | unsafe modifiers: none
- `renal_colic_stable_no_infection.home_care.home_care_2.v1` | `home_care` | audit: source_needed | unsafe modifiers: none
- `renal_colic_stable_no_infection.home_care.home_care_3.v1` | `home_care` | audit: source_needed | unsafe modifiers: none
- `renal_colic_stable_no_infection.medications.medication_guidance_1.v1` | `medications` | audit: source_needed, clinician_judgment_only, unsafe_without_modifier | unsafe modifiers: fever, solitary_kidney, pregnancy, renal_failure, uncontrolled_pain
- `renal_colic_stable_no_infection.medications.medication_guidance_2.v1` | `medications` | audit: source_needed, clinician_judgment_only, unsafe_without_modifier | unsafe modifiers: fever, solitary_kidney, pregnancy, renal_failure, uncontrolled_pain
- `renal_colic_stable_no_infection.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_needed, clinician_judgment_only | unsafe modifiers: none
- `renal_colic_stable_no_infection.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_needed, clinician_judgment_only | unsafe modifiers: none
- `renal_colic_stable_no_infection.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_needed, clinician_judgment_only | unsafe modifiers: none
- `renal_colic_stable_no_infection.follow_up.default_follow_up.v1` | `follow_up` | audit: source_needed, clinician_judgment_only, unsafe_without_modifier | unsafe modifiers: fever, solitary_kidney, pregnancy, renal_failure, uncontrolled_pain

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit a kidney stone.

WHAT WE FOUND:
Your ED evaluation was reassuring enough for home care today. We did not find signs of a dangerous kidney infection or blocked infected kidney.

WHAT TO DO AT HOME:
- Drink fluids as you are able.
- Use a urine strainer if one was given.
- Save any passed stone if your clinician asked you to.

MEDICATIONS:
- Take prescribed pain or nausea medicine exactly as directed.
- Use acetaminophen or ibuprofen only if you can take it safely and follow the label.

RETURN TO ED IF:
- Fever, chills, worsening flank pain, repeated vomiting, or feeling very ill.
- You cannot urinate.
- Pain cannot be controlled with the plan you were given.

FOLLOW UP:
Follow up with urology or primary care as instructed.
```
