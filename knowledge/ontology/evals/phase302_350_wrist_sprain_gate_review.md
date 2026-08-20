# Phase 302-350 Wrist Sprain Gate Review

Date: 2026-06-04

Status: complete.

## Decision

Keep `wrist_sprain_xray_negative` draft-only.

No new phenotype batch starts while wrist remains the only active draft.

## Rationale

The wrist split has a safe draft shape, but clinician-owner review returned a revise decision on the patient-facing text and blocker semantics. The requested revision is applied, and wrist remains draft-only pending re-review:

- Clean wrist sprain/strain/injury with negative x-ray, intact neurovascular exam, and no scaphoid/snuffbox tenderness routes to draft fallback only.
- Missing no-scaphoid documentation blocks by required context.
- Scaphoid tenderness, snuffbox tenderness, FOOSH plus radial/thumb-side pain or grip deficit, fracture, no imaging, tendon risk, pediatric growth plate risk, documented osteoporotic or fragility-fracture risk, and specialist-directed orthopedic plan block through unsafe modifiers.
- FOOSH alone with a clean scaphoid exam no longer blocks.
- Age-language alone no longer triggers the osteoporotic-risk blocker.
- Mallet finger and jersey finger pathways now trigger `hand_tendon_risk`.
- Knee and shoulder reviewed ontology mode remains unchanged.

## Clinician-Review Revision Applied

Updated patient-facing text:

- `WHAT WE FOUND` now explains the scaphoid screen as specific wrist areas checked for deeper injury, without using chart-language anatomy.
- `WHAT TO DO AT HOME` now adds a 3 to 5 day improvement check.
- The thumb-side return precaution now uses lay symptom language.
- The fever/infection return precaution no longer ends with vague "symptoms that get worse instead of better" language.
- `FOLLOW UP` is now non-contingent at 5 to 7 days and explains possible occult fracture on first x-ray.

## Runtime Fixture

New fixture:

- `knowledge/ontology/evals/phase302_350_wrist_sprain_runtime_cases.json`

Coverage:

- 23 Phase 302-324 cases.
- Python broad runtime auto-includes the fixture.
- Netlify smoke now includes the fixture.

## Gate

Reviewed runtime clean: true.

Reviewed source gaps: 0.

Draft source gaps: 0.

Active draft phenotype count: 1.

Active draft:

- `wrist_sprain_xray_negative`

Phenotype expansion allowed: false.

## Clinical Holding Point

Wrist can be promoted only after clinician review of:

- revised patient-facing text,
- explicit no-scaphoid/snuffbox requirement,
- compound FOOSH/scaphoid-risk blocker behavior,
- osteoporotic-risk and hand-tendon-risk blocker behavior.
