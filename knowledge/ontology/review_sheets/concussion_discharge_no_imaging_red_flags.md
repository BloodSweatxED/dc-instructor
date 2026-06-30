# Concussion discharge without imaging red flags

Phenotype ID: `concussion_discharge_no_imaging_red_flags`

Status: `reviewed`

## Inclusion Criteria

- Concussion symptoms with reassuring ED assessment and safe discharge plan.

## Exclusions

- Red flags for intracranial bleeding.
- Anticoagulation or bleeding disorder.
- Unreliable observation plan.

## Must-Not-Miss Diagnoses

- Intracranial hemorrhage.
- Cervical spine injury.
- Second-impact risk.
- Persistent neurologic deficit.

## Primitive List

- `concussion_discharge_no_imaging_red_flags.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only | unsafe modifiers: none
- `concussion_discharge_no_imaging_red_flags.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier | unsafe modifiers: athlete_return_to_play, anticoagulated, neurologic_deficit, persistent_vomiting
- `concussion_discharge_no_imaging_red_flags.home_care.home_care_1.v1` | `home_care` | audit: source_supported | unsafe modifiers: none
- `concussion_discharge_no_imaging_red_flags.home_care.home_care_2.v1` | `home_care` | audit: source_supported | unsafe modifiers: none
- `concussion_discharge_no_imaging_red_flags.home_care.home_care_3.v1` | `home_care` | audit: source_supported | unsafe modifiers: none
- `concussion_discharge_no_imaging_red_flags.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier | unsafe modifiers: athlete_return_to_play, anticoagulated, neurologic_deficit, persistent_vomiting
- `concussion_discharge_no_imaging_red_flags.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier | unsafe modifiers: athlete_return_to_play, anticoagulated, neurologic_deficit, persistent_vomiting
- `concussion_discharge_no_imaging_red_flags.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only | unsafe modifiers: none
- `concussion_discharge_no_imaging_red_flags.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only | unsafe modifiers: none
- `concussion_discharge_no_imaging_red_flags.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported, clinician_judgment_only | unsafe modifiers: none
- `concussion_discharge_no_imaging_red_flags.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier | unsafe modifiers: athlete_return_to_play, anticoagulated, neurologic_deficit, persistent_vomiting

## Assembled Six-Section Output

```text
DIAGNOSIS:
Your symptoms fit a concussion.

WHAT WE FOUND:
A concussion can happen after a hit or sudden movement of the head. Your exam today did not show an emergency danger sign requiring admission.

WHAT TO DO AT HOME:
- Rest your brain and body for the first day.
- Return to school, work, exercise, and screens slowly as symptoms allow.
- Avoid another head injury while symptoms are present.

MEDICATIONS:
- Use acetaminophen for headache if you can take it safely and follow the label.
- Avoid alcohol and sedating drugs unless your clinician says they are safe.

RETURN TO ED IF:
- Worsening headache, repeated vomiting, confusion, seizure, fainting, or trouble waking up.
- New weakness, numbness, trouble speaking, or vision changes.
- Any second head injury before you recover.

FOLLOW UP:
Follow up with primary care, sports medicine, or concussion clinic if symptoms persist or if you need return-to-play clearance.
```
