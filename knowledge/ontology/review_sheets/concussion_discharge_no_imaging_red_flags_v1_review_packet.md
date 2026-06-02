# Concussion discharge without imaging red flags V1 Review Packet

Phenotype ID: `concussion_discharge_no_imaging_red_flags`

Clinical status: reviewed_for_limited_concussion_without_imaging_red_flags_use.

Production status: enabled with runtime modifier gates.

Reviewer: Andre / EM clinician-owner.

Review date: 2026-06-01.

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

## Source Audit

- `cdc.heads_up_concussion_symptoms` supports this phenotype's reviewed concepts.
- `cdc.mild_tbi_aftercare` supports this phenotype's reviewed concepts.
- CDC HEADS UP and CDC mild TBI guidance support danger signs, gradual return to activity, and clinician-directed return-to-school, work, driving, or play planning.
- Patient-facing text is locally authored. No WikEM prose is copied.

## Blocked Modifiers

- `athlete_return_to_play`
- `anticoagulated`
- `neurologic_deficit`
- `persistent_vomiting`
- `loss_of_consciousness`
- `intoxication`

## Primitive List

- `concussion_discharge_no_imaging_red_flags.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only
- `concussion_discharge_no_imaging_red_flags.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier
- `concussion_discharge_no_imaging_red_flags.home_care.home_care_1.v1` | `home_care` | audit: source_supported
- `concussion_discharge_no_imaging_red_flags.home_care.home_care_2.v1` | `home_care` | audit: source_supported
- `concussion_discharge_no_imaging_red_flags.home_care.home_care_3.v1` | `home_care` | audit: source_supported
- `concussion_discharge_no_imaging_red_flags.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, unsafe_without_modifier
- `concussion_discharge_no_imaging_red_flags.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, unsafe_without_modifier
- `concussion_discharge_no_imaging_red_flags.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported
- `concussion_discharge_no_imaging_red_flags.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported
- `concussion_discharge_no_imaging_red_flags.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported
- `concussion_discharge_no_imaging_red_flags.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier
- `concussion_discharge_no_imaging_red_flags.resources.source_link_1.v1` | `resources` | audit: source_supported
- `concussion_discharge_no_imaging_red_flags.resources.source_link_2.v1` | `resources` | audit: source_supported
- `concussion_discharge_no_imaging_red_flags.resources.followup_reminder.v1` | `resources` | audit: source_supported

## Patient-Facing Output

```text
DIAGNOSIS:
Your symptoms fit a concussion.

WHAT WE FOUND:
You came to the ED after a head injury. Your exam did not show an emergency danger sign requiring admission today, but concussion symptoms can change after you leave.

WHAT TO DO AT HOME:
- Rest your brain and body for the first day.
- Return to school, work, screens, and exercise slowly as symptoms allow.
- Avoid another head injury while symptoms are present.

MEDICATIONS:
- Use acetaminophen for headache only if it is safe for you and follow the label.
- Avoid alcohol, sedating drugs, and driving until you know you are thinking clearly and your clinician says it is safe.

RETURN TO ED IF:
- Come back right away for worsening headache, repeated vomiting, confusion, seizure, fainting, or trouble waking up.
- Come back for new weakness, numbness, trouble speaking, or vision changes.
- Come back after any second head injury before you recover.

FOLLOW UP:
Call your primary care doctor's office or clinic. Say, "I was in the emergency department and was diagnosed with a concussion. I need a follow-up visit within 1 week if symptoms persist, or sooner if you need return-to-play clearance."

RESOURCES:
- Bring these instructions to your follow-up visit.
- Learn more: CDC HEADS UP - Signs and Symptoms of Concussion (https://www.cdc.gov/heads-up/signs-symptoms/index.html).
- Learn more: CDC - What to Do After a Mild TBI or Concussion (https://www.cdc.gov/traumatic-brain-injury/response/index.html).
```
