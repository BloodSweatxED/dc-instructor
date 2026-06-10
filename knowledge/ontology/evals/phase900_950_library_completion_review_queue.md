# Phase 900-950 Library Completion Draft Review Queue

Status: complete.

This cycle opened three source-supported draft phenotypes for high-frequency ED discharge coverage. They are intentionally not exported to `library/` until clinician-owner review decides promote, revise, retire, split, or hold.

## Review Queue

| Phenotype | Decision Needed | Agent Recommendation | Main Safety Question | Review Sheet |
| --- | --- | --- | --- | --- |
| `influenza_like_illness_stable_supportive_care` | revise vs promote | revise, then promote narrow v1 if antiviral/high-risk boundaries are accepted | Should this draft block all high-risk flu hosts and all antiviral plans, or allow reviewed output modifiers? | `knowledge/ontology/review_sheets/influenza_like_illness_stable_supportive_care.md` |
| `asymptomatic_elevated_blood_pressure_no_end_organ_symptoms` | revise vs hold | hold or revise very narrowly | Is this too medicolegally workflow-dependent for static patient instructions, especially around BP >=180/120 and follow-up timing? | `knowledge/ontology/review_sheets/asymptomatic_elevated_blood_pressure_no_end_organ_symptoms.md` |
| `hemorrhoids_uncomplicated_no_heavy_bleeding` | revise vs promote | revise, then promote narrow v1 if bleeding/thrombosis boundaries are accepted | What exact rectal bleeding, thrombosis/prolapse, anticoagulation, age/cancer-risk, and abdominal-pain blockers are required? | `knowledge/ontology/review_sheets/hemorrhoids_uncomplicated_no_heavy_bleeding.md` |

## Source Support

- Flu-like illness: `medlineplus.flu`, `cdc.flu_taking_care`, `cdc.flu_treatment`
- Asymptomatic elevated blood pressure: `medlineplus.high_blood_pressure`, `aha.hypertensive_emergency`
- Hemorrhoids: `medlineplus.hemorrhoids`, `niddk.hemorrhoids_treatment`

## Clinician Review Helper Used

Ran `bash knowledge/review.sh --json` for:

- influenza-like illness boundaries
- asymptomatic elevated blood pressure boundaries
- hemorrhoids red flags

All three helper runs returned moderate confidence but with off-topic retrieved local MedlinePlus context. The answers were treated as boundary prompts, not promotion authority. The actual source cards use condition-specific official public sources.

## Runtime Coverage

Added `knowledge/ontology/evals/phase900_950_library_completion_draft_runtime_cases.json`.

Coverage includes:

- clean draft matches that fall back with `phenotype_not_clinician_reviewed`
- missing required-context blocks
- unsafe modifier blocks for high-risk flu, antiviral plan, BP symptoms, pregnancy, heavy hemorrhoid bleeding, and perianal abscess concern

## Gate State

Expected gate result after this cycle:

- reviewed runtime clean: true
- phenotype expansion allowed: false
- active draft phenotypes: 3
- reviewed source gaps: 0
- draft source gaps: 0

## Recommendation

Do not add these to `library/` yet.

Best next clinician review order:

1. `hemorrhoids_uncomplicated_no_heavy_bleeding`
2. `influenza_like_illness_stable_supportive_care`
3. `asymptomatic_elevated_blood_pressure_no_end_organ_symptoms`

Rationale: hemorrhoids and flu are likely promotable as narrow v1 phenotypes after boundary tightening. Asymptomatic elevated BP may be better kept as a workflow/follow-up product layer unless the phenotype is made extremely narrow.
