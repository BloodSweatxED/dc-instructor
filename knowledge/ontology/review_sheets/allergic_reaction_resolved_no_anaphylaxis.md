# Allergic reaction resolved, no anaphylaxis

Phenotype ID: `allergic_reaction_resolved_no_anaphylaxis`

Status: `draft`

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

## Primitive List

- `allergic_reaction_resolved_no_anaphylaxis.diagnosis.diagnosis_summary.v1` | `diagnosis` | audit: source_needed, clinician_judgment_only | unsafe modifiers: none
- `allergic_reaction_resolved_no_anaphylaxis.what_we_found.reassuring_ed_assessment.v1` | `what_we_found` | audit: source_needed, clinician_judgment_only, unsafe_without_modifier | unsafe modifiers: airway_symptoms, hypotension, epinephrine_given, mucosal_lesions, unknown_trigger
- `allergic_reaction_resolved_no_anaphylaxis.home_care.home_care_1.v1` | `home_care` | audit: source_needed | unsafe modifiers: none
- `allergic_reaction_resolved_no_anaphylaxis.home_care.home_care_2.v1` | `home_care` | audit: source_needed | unsafe modifiers: none
- `allergic_reaction_resolved_no_anaphylaxis.home_care.home_care_3.v1` | `home_care` | audit: source_needed | unsafe modifiers: none
- `allergic_reaction_resolved_no_anaphylaxis.medications.medication_guidance_1.v1` | `medications` | audit: source_needed, clinician_judgment_only, unsafe_without_modifier | unsafe modifiers: airway_symptoms, hypotension, epinephrine_given, mucosal_lesions, unknown_trigger
- `allergic_reaction_resolved_no_anaphylaxis.medications.medication_guidance_2.v1` | `medications` | audit: source_needed, clinician_judgment_only, unsafe_without_modifier | unsafe modifiers: airway_symptoms, hypotension, epinephrine_given, mucosal_lesions, unknown_trigger
- `allergic_reaction_resolved_no_anaphylaxis.return_precautions.return_precaution_1.v1` | `return_precautions` | audit: source_needed, clinician_judgment_only | unsafe modifiers: none
- `allergic_reaction_resolved_no_anaphylaxis.return_precautions.return_precaution_2.v1` | `return_precautions` | audit: source_needed, clinician_judgment_only | unsafe modifiers: none
- `allergic_reaction_resolved_no_anaphylaxis.return_precautions.return_precaution_3.v1` | `return_precautions` | audit: source_needed, clinician_judgment_only | unsafe modifiers: none
- `allergic_reaction_resolved_no_anaphylaxis.follow_up.default_follow_up.v1` | `follow_up` | audit: source_needed, clinician_judgment_only, unsafe_without_modifier | unsafe modifiers: airway_symptoms, hypotension, epinephrine_given, mucosal_lesions, unknown_trigger

## Assembled Six-Section Output

```text
DIAGNOSIS:
You were treated for an allergic reaction.

WHAT WE FOUND:
Your symptoms improved, and we did not find signs of anaphylaxis at discharge today.

WHAT TO DO AT HOME:
- Avoid the trigger if it is known.
- Watch for symptoms returning after you leave.
- Do not drive or drink alcohol after sedating allergy medicines.

MEDICATIONS:
- Take allergy medicines exactly as prescribed.
- Use an epinephrine injector only if one was prescribed and you were instructed to use it.

RETURN TO ED IF:
- Trouble breathing, wheezing, throat tightness, tongue or lip swelling, fainting, or severe vomiting.
- Rash or swelling returns quickly or spreads.
- You use epinephrine.

FOLLOW UP:
Follow up with primary care or allergy clinic if symptoms continue or trigger is unclear.
```
