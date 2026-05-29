# Nonspecific abdominal pain with reassuring ED workup

Phenotype ID: `abdominal_pain_nonspecific_reassuring_workup`

Status: `draft`

## Inclusion Criteria

- Abdominal pain with reassuring ED assessment and no surgical abdomen at discharge.

## Exclusions

- Pregnancy-related abdominal pain.
- Appendicitis, obstruction, ischemia, perforation, or sepsis concern.
- Uncontrolled pain or vomiting.

## Must-Not-Miss Diagnoses

- Appendicitis.
- Bowel obstruction.
- Bowel ischemia.
- Perforation.
- Ectopic pregnancy.
- AAA.

## Primitive List

- `abdominal_pain_nonspecific_reassuring_workup.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_needed, clinician_judgment_only | unsafe modifiers: none
- `abdominal_pain_nonspecific_reassuring_workup.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_needed, clinician_judgment_only, unsafe_without_modifier | unsafe modifiers: pregnancy, elderly, immunocompromised, peritoneal_signs, uncontrolled_vomiting
- `abdominal_pain_nonspecific_reassuring_workup.home_care.home_care_1.v1` | `home_care` | audit: source_needed | unsafe modifiers: none
- `abdominal_pain_nonspecific_reassuring_workup.home_care.home_care_2.v1` | `home_care` | audit: source_needed | unsafe modifiers: none
- `abdominal_pain_nonspecific_reassuring_workup.home_care.home_care_3.v1` | `home_care` | audit: source_needed | unsafe modifiers: none
- `abdominal_pain_nonspecific_reassuring_workup.medications.medication_guidance_1.v1` | `medications` | audit: source_needed, clinician_judgment_only, unsafe_without_modifier | unsafe modifiers: pregnancy, elderly, immunocompromised, peritoneal_signs, uncontrolled_vomiting
- `abdominal_pain_nonspecific_reassuring_workup.medications.medication_guidance_2.v1` | `medications` | audit: source_needed, clinician_judgment_only, unsafe_without_modifier | unsafe modifiers: pregnancy, elderly, immunocompromised, peritoneal_signs, uncontrolled_vomiting
- `abdominal_pain_nonspecific_reassuring_workup.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_needed, clinician_judgment_only | unsafe modifiers: none
- `abdominal_pain_nonspecific_reassuring_workup.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_needed, clinician_judgment_only | unsafe modifiers: none
- `abdominal_pain_nonspecific_reassuring_workup.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_needed, clinician_judgment_only | unsafe modifiers: none
- `abdominal_pain_nonspecific_reassuring_workup.follow_up.default_follow_up.v1` | `follow_up` | audit: source_needed, clinician_judgment_only, unsafe_without_modifier | unsafe modifiers: pregnancy, elderly, immunocompromised, peritoneal_signs, uncontrolled_vomiting

## Assembled Six-Section Output

```text
DIAGNOSIS:
You were evaluated for abdominal pain today.

WHAT WE FOUND:
Your ED evaluation was reassuring today. We did not find a clear emergency cause, but early problems can change after discharge.

WHAT TO DO AT HOME:
- Drink fluids as you are able.
- Start with bland foods if your stomach feels upset.
- Avoid alcohol and heavy meals until you feel better.

MEDICATIONS:
- Take prescribed nausea or stomach medicine exactly as directed.
- Use pain medicine only as instructed by your clinician.

RETURN TO ED IF:
- Worsening or one-sided belly pain, repeated vomiting, fainting, or confusion.
- Fever, bloody stool, black stool, vomiting blood, or a swollen hard belly.
- New chest pain, trouble breathing, or pain with pregnancy concern.

FOLLOW UP:
Follow up with primary care or return for recheck as instructed.
```
