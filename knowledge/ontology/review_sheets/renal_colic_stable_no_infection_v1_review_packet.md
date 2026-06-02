# Renal colic, stable, no infection concern V1 Review Packet

Phenotype ID: `renal_colic_stable_no_infection`

Clinical status: reviewed_for_limited_stable_renal_colic_without_infection_use.

Production status: enabled with runtime modifier gates.

Reviewer: Andre / EM clinician-owner.

Review date: 2026-06-01.

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

## Source Audit

- `medlineplus.kidney_stones_self_care` supports this phenotype's reviewed concepts.
- MedlinePlus supports kidney stone self-care, hydration, urine straining when instructed, and escalation for fever, chills, vomiting, severe pain, cloudy urine, or urinary symptoms.
- Patient-facing text is locally authored. No WikEM prose is copied.

## Blocked Modifiers

- `fever`
- `solitary_kidney`
- `pregnancy`
- `renal_failure`
- `uncontrolled_pain`
- `vomiting_unable_to_take_meds`
- `urinary_obstruction`
- `sepsis`

## Primitive List

- `renal_colic_stable_no_infection.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only
- `renal_colic_stable_no_infection.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier
- `renal_colic_stable_no_infection.home_care.home_care_1.v1` | `home_care` | audit: source_supported
- `renal_colic_stable_no_infection.home_care.home_care_2.v1` | `home_care` | audit: source_supported
- `renal_colic_stable_no_infection.home_care.home_care_3.v1` | `home_care` | audit: source_supported
- `renal_colic_stable_no_infection.home_care.home_care_4.v1` | `home_care` | audit: source_supported
- `renal_colic_stable_no_infection.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, unsafe_without_modifier
- `renal_colic_stable_no_infection.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, unsafe_without_modifier
- `renal_colic_stable_no_infection.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported
- `renal_colic_stable_no_infection.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported
- `renal_colic_stable_no_infection.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported
- `renal_colic_stable_no_infection.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier

## Patient-Facing Output

```text
DIAGNOSIS:
Your symptoms fit a kidney stone.

WHAT WE FOUND:
You came to the ED with flank pain or symptoms that fit a kidney stone. We did not find signs of infection or a dangerous blockage.

WHAT TO DO AT HOME:
- Drink plenty of fluids. Aim for urine that is pale yellow. This helps flush the stone through.
- Use a urine strainer with every urination, including at night, if one was given.
- Save any passed stone if your clinician asked you to.
- Until you follow up, limit salt and animal protein, and avoid getting dehydrated.

MEDICATIONS:
- Take prescribed pain or nausea medicine only as directed.
- If tamsulosin was prescribed, it relaxes the ureter and may help the stone pass.

RETURN TO ED IF:
- Come back for fever, chills, worsening flank pain, repeated vomiting, or feeling very ill.
- Come back if you cannot urinate.
- Come back if pain cannot be controlled with the plan you were given.

FOLLOW UP:
Follow up with urology or primary care within 1-2 weeks. Most small stones pass on their own within 1-4 weeks.
```
