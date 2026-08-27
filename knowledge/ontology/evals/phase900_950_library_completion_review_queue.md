# Phase 900-950 Library Completion Draft Review Queue

Status: closed after clinician-owner approval and Phase 1001 promotion.

This cycle opened three source-supported draft phenotypes for high-frequency ED discharge coverage. Clinician-owner review on 2026-06-10 approved all three as narrow v1 phenotypes, and they were promoted into the reviewed runtime and exported to `library/`.

## Review Queue

| Phenotype | Decision Needed | Agent Recommendation | Main Safety Question | Review Sheet |
| --- | --- | --- | --- | --- |
| `influenza_like_illness_stable_supportive_care` | promoted | approved narrow v1 | High-risk hosts and antiviral cases remain hard blockers, not output modifiers. Runtime also blocks pregnancy/postpartum, pneumonia/hypoxia, unresolved dyspnea, PO intolerance, and chest pain. | `knowledge/ontology/review_sheets/influenza_like_illness_stable_supportive_care.md` |
| `asymptomatic_elevated_blood_pressure_no_end_organ_symptoms` | promoted | approved narrow v1 | Workflow dependency accepted because repeat measurement, documented clinician assessment, concrete follow-up, and medication-plan documentation are required safeguards. Runtime blocks crisis-threshold language, neuro symptoms, dyspnea/back pain, renal symptoms, pregnancy/postpartum, stimulant/cocaine context, renal-specialist pathways, secondary hypertension concern, poor follow-up, sepsis, and unstable vitals. | `knowledge/ontology/review_sheets/asymptomatic_elevated_blood_pressure_no_end_organ_symptoms.md` |
| `hemorrhoids_uncomplicated_no_heavy_bleeding` | promoted | approved narrow v1 | Blocker list accepted as sufficient: heavy bleeding, thrombosis/prolapse, anticoagulation, malignancy/IBD concern, pregnancy, abdominal pain, and related hard blockers. | `knowledge/ontology/review_sheets/hemorrhoids_uncomplicated_no_heavy_bleeding.md` |

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

Coverage now includes:

- clean draft matches that fall back with `phenotype_not_clinician_reviewed`
- missing required-context blocks
- flu unsafe modifier blocks for high-risk host, antiviral plan, pregnancy/postpartum, pneumonia/hypoxia, unresolved dyspnea, inability to tolerate oral fluids, and chest pain
- BP required-context blocks for missing repeat measurement, missing outpatient follow-up plan, and missing medication-plan documentation
- BP unsafe modifier blocks for crisis-threshold language, end-organ symptoms, chest pain, dyspnea/back pain, renal symptoms, pregnancy/postpartum, stimulant/cocaine context, renal-specialist pathways, secondary hypertension concern, poor follow-up, sepsis, and unstable vitals
- hemorrhoid unsafe modifier blocks for heavy bleeding, anticoagulated bleeding, anemia concern, thrombosis/irreducible prolapse, rectal mass or malignancy concern, IBD concern, abdominal pain plus GI bleeding, pregnancy, and perianal abscess or sepsis concern

## Gate State

Gate result after promotion:

- reviewed runtime clean: true
- phenotype expansion allowed: true
- active draft phenotypes: 0
- reviewed source gaps: 0
- draft source gaps: 0

## Recommendation

Continue building the reviewed discharge instruction library on autopilot. Use `bash knowledge/review.sh` inline for clinical uncertainty, keep source cards and runtime gates explicit, and keep moving rather than pausing for review gates unless a hard technical or patient-safety blocker prevents safe generation.
