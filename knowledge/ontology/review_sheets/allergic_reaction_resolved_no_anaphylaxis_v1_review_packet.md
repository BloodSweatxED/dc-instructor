# Allergic reaction resolved, no anaphylaxis V1 Review Packet

Phenotype ID: `allergic_reaction_resolved_no_anaphylaxis`

Clinical status: reviewed_for_limited_resolved_allergic_reaction_without_anaphylaxis_use.

Production status: enabled with runtime modifier gates.

Reviewer: Andre / EM clinician-owner.

Review date: 2026-06-01.

## Inclusion Criteria

- Allergic reaction improved or resolved without anaphylaxis at discharge.

## Exclusions

- Anaphylaxis.
- Airway swelling.
- Hypotension.
- Biphasic reaction concern needing observation.

## Must-Not-Miss Diagnoses

- Anaphylaxis.
- Airway edema.
- Medication reaction with mucosal involvement.
- Serum sickness or severe cutaneous adverse reaction.

## Source Audit

- `medlineplus.allergic_reactions` supports this phenotype's reviewed concepts.
- MedlinePlus supports allergic reaction symptoms, anaphylaxis danger signs, epinephrine planning, and emergency escalation for airway or severe systemic symptoms.
- Patient-facing text is locally authored. No WikEM prose is copied.

## Blocked Modifiers

- `airway_symptoms`
- `hypotension`
- `epinephrine_given`
- `mucosal_lesions`
- `unknown_trigger`
- `anaphylaxis`
- `biphasic_reaction_concern`

## Primitive List

- `allergic_reaction_resolved_no_anaphylaxis.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_supported, clinician_judgment_only
- `allergic_reaction_resolved_no_anaphylaxis.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier
- `allergic_reaction_resolved_no_anaphylaxis.home_care.home_care_1.v1` | `home_care` | audit: source_supported
- `allergic_reaction_resolved_no_anaphylaxis.home_care.home_care_2.v1` | `home_care` | audit: source_supported
- `allergic_reaction_resolved_no_anaphylaxis.home_care.home_care_3.v1` | `home_care` | audit: source_supported
- `allergic_reaction_resolved_no_anaphylaxis.medications.medication_guidance_1.v1` | `medications` | audit: source_supported, unsafe_without_modifier
- `allergic_reaction_resolved_no_anaphylaxis.medications.medication_guidance_2.v1` | `medications` | audit: source_supported, unsafe_without_modifier
- `allergic_reaction_resolved_no_anaphylaxis.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_supported
- `allergic_reaction_resolved_no_anaphylaxis.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_supported
- `allergic_reaction_resolved_no_anaphylaxis.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_supported
- `allergic_reaction_resolved_no_anaphylaxis.follow_up.default_follow_up.v1` | `follow_up` | audit: source_supported, clinician_judgment_only, unsafe_without_modifier
- `allergic_reaction_resolved_no_anaphylaxis.resources.source_link_1.v1` | `resources` | audit: source_supported
- `allergic_reaction_resolved_no_anaphylaxis.resources.followup_reminder.v1` | `resources` | audit: source_supported

## Patient-Facing Output

```text
DIAGNOSIS:
You were treated for an allergic reaction.

WHAT WE FOUND:
You came to the ED with allergy symptoms. The symptoms improved, and we did not find signs of anaphylaxis when you were ready for discharge.

WHAT TO DO AT HOME:
- Avoid the trigger if you know what caused the reaction.
- Watch for symptoms coming back after you leave.
- Do not drive, drink alcohol, or take other sedating medicines after sedating allergy medicine unless your clinician says it is safe.

MEDICATIONS:
- Take allergy medicines as prescribed or as directed on the label.
- Use an epinephrine injector only if one was prescribed and you were told when to use it.

RETURN TO ED IF:
- Come back right away for trouble breathing, wheezing, throat tightness, tongue or lip swelling, fainting, or severe vomiting.
- Come back if rash or swelling returns quickly or spreads.
- Come back right away if you use epinephrine.

FOLLOW UP:
Call your primary care doctor's office or clinic. Say, "I was in the emergency department and was diagnosed with an allergic reaction. I need a follow-up visit within 1 week if symptoms continue or the trigger is unclear."

RESOURCES:
- Bring these instructions to your follow-up visit.
- Learn more: MedlinePlus - Allergic reactions (https://medlineplus.gov/ency/article/000005.htm).
```
