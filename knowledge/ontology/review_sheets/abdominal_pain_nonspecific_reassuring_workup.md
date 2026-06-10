# Abdominal pain recheck after reassuring ED evaluation

Phenotype ID: `abdominal_pain_nonspecific_reassuring_workup`

Status: `needs_review`

## Inclusion Criteria

- Abdominal pain evaluated in the ED with a reassuring exam and workup at discharge.
- No current surgical abdomen, unstable vital signs, or admission need.
- Patient discharged with explicit clinician-directed recheck plan.

## Exclusions

- Pregnancy or pregnancy concern.
- Localized or worsening pain concerning for appendicitis, obstruction, ischemia, perforation, or other surgical abdomen.
- Uncontrolled pain, repeated vomiting, fever, GI bleeding, sepsis concern, frailty, immunocompromise, or unreliable follow-up.

## Must-Not-Miss Diagnoses

- Appendicitis.
- Bowel obstruction.
- Bowel ischemia.
- Perforation.
- Ectopic pregnancy.
- AAA.
- Sepsis.

## Primitive List

- `abdominal_pain_nonspecific_reassuring_workup.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `abdominal_pain_nonspecific_reassuring_workup.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: pregnancy, elderly, immunocompromised, poor_follow_up, peritoneal_signs, uncontrolled_vomiting, fever, gi_bleeding, sepsis, unstable_vitals
- `abdominal_pain_nonspecific_reassuring_workup.home_care.home_care_1.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `abdominal_pain_nonspecific_reassuring_workup.home_care.home_care_2.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `abdominal_pain_nonspecific_reassuring_workup.home_care.home_care_3.v1` | `home_care` | audit: source_supported, notes | unsafe modifiers: none
- `abdominal_pain_nonspecific_reassuring_workup.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: pregnancy, elderly, immunocompromised, poor_follow_up, peritoneal_signs, uncontrolled_vomiting, fever, gi_bleeding, sepsis, unstable_vitals
- `abdominal_pain_nonspecific_reassuring_workup.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: pregnancy, elderly, immunocompromised, poor_follow_up, peritoneal_signs, uncontrolled_vomiting, fever, gi_bleeding, sepsis, unstable_vitals
- `abdominal_pain_nonspecific_reassuring_workup.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `abdominal_pain_nonspecific_reassuring_workup.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `abdominal_pain_nonspecific_reassuring_workup.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only, notes | unsafe modifiers: none
- `abdominal_pain_nonspecific_reassuring_workup.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier, notes | unsafe modifiers: pregnancy, elderly, immunocompromised, poor_follow_up, peritoneal_signs, uncontrolled_vomiting, fever, gi_bleeding, sepsis, unstable_vitals

## Assembled Six-Section Output

```text
DIAGNOSIS:
You were evaluated for abdominal pain today.

WHAT WE FOUND:
We did not find an emergency cause that needed surgery or admission, but abdominal pain can change after you leave.

WHAT TO DO AT HOME:
- Use the food and fluid plan your clinician gave you.
- Start with small sips and light foods if your stomach feels upset.
- Do not ignore symptoms that are getting worse just because today's evaluation was reassuring.

MEDICATIONS:
- Take prescribed nausea or stomach medicine exactly as directed.
- Use pain medicine only as instructed by your clinician. Do not take extra doses to cover worsening pain.

RETURN TO ED IF:
- Worsening, severe, or one-sided belly pain.
- Repeated vomiting, fainting, confusion, fever, bloody stool, black stool, or vomiting blood.
- A swollen hard belly, pain going to the shoulder or back, or any pregnancy concern.

FOLLOW UP:
Return for recheck as your clinician instructed.
```
