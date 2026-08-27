# Phase 250 Handoff

Date: 2026-06-03

Status: completed through Phase 250.

Repo source of truth:

`/Users/andre/Desktop/Claude Projects/dc-instructor`

## Current State

Promoted and reviewed ontology enabled:

- `skin_avulsion_or_abrasion_simple`
- `acute_otitis_media_uncomplicated`
- `suture_removal_or_wound_check_no_infection`

Still draft-only:

- `sprain_strain_non_ankle_xray_negative`

Reviewed runtime clean: true.

Reviewed source gaps: 0.

Draft source gaps: 0.

Active draft phenotype count: 1.

Phenotype expansion allowed: false.

## New Phase 223-250 Artifacts

- `knowledge/ontology/evals/check_phase222_250_promotion_release.py`
- `knowledge/ontology/evals/phase223_250_promotion_release_review.md`
- `knowledge/ontology/evals/phase250_handoff.md`

## Key Decision

Output modifiers are metadata and review-banner content only.

They do not silently rewrite patient-facing instructions.

## Remaining Review Question

`sprain_strain_non_ankle_xray_negative` remains draft-only because elbow and foot clean cases still match at low confidence.

The next clinician/product decision is whether to split by site or keep elbow and foot excluded from v1.

## Verification

Passed:

- `python3 knowledge/ontology/evals/check_phase222_250_promotion_release.py`
- `python3 knowledge/ontology/evals/check_phase216_220_promotion_readiness.py`
- `python3 knowledge/ontology/evals/check_phase202_215_cycle.py`
- `python3 knowledge/ontology/evals/run_runtime_cases.py`
- `node knowledge/ontology/evals/run_netlify_runtime_smoke.mjs`
- `python3 knowledge/ontology/evals/check_phase21_expansion_gate.py`
- `node knowledge/ontology/evals/check_product_tailoring_contract.mjs`
- `npm run build`
- `git diff --check`

## Startup Prompt

Continue DC Instructor ontology work from Phase 250. Use `/Users/andre/Desktop/Claude Projects/dc-instructor` as the repo source of truth and `/Users/andre/Desktop/Vaults/Life/11-DC instructor` for vault handoffs. Preserve the Phase 222 promotion decision: skin avulsion/abrasion, acute otitis media, and suture/wound-check are reviewed ontology enabled; sprain/strain non-ankle xray negative remains draft-only. Keep output modifiers as metadata plus review-banner notes only. Do not silently alter patient-facing text. Before any sprain/strain promotion, resolve the elbow and foot low-confidence concern by splitting site-specific phenotypes or excluding those sites from v1.
