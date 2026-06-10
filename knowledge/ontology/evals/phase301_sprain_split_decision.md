# Phase 301 Sprain Split Decision

Date: 2026-06-04

Status: complete.

## Decision

Do not promote the broad `sprain_strain_non_ankle_xray_negative` phenotype.

Retire the broad non-ankle sprain/strain draft to product-layer fallback only.

Promote a narrower reviewed v1:

- `sprain_strain_knee_or_shoulder_xray_negative`

Keep wrist separate and draft-only:

- `wrist_sprain_xray_negative`

Keep elbow and foot excluded pending split or separate clinician approval.

Ankle remains owned by `ankle_sprain_xray_negative`.

## Clinical Rationale

Knee and shoulder share enough discharge structure for a conservative shared v1 when x-ray is negative, neurovascular exam is intact, and high-risk orthopedic findings are absent.

Wrist is not safe inside the shared v1 because an initially negative x-ray does not reliably exclude occult scaphoid injury. The wrist draft requires explicit documentation that scaphoid or snuffbox tenderness is absent before it can even reach draft fallback behavior.

## Runtime Contract

Reviewed ontology mode:

- Clean knee sprain/strain with negative x-ray and intact neurovascular exam.
- Clean shoulder sprain/strain with negative x-ray and intact neurovascular exam.

Draft-only:

- Wrist sprain/strain with negative x-ray, intact neurovascular exam, and documented absence of scaphoid tenderness.

Blocked:

- Wrist without documented absence of scaphoid tenderness.
- Wrist with snuffbox/scaphoid tenderness.
- Wrist FOOSH or thumb-side wrist pain after fall.
- Knee acute hemarthrosis, tense effusion, or large effusion.
- Knee inability to bear weight.
- Elbow or foot sprain/strain pending split.
- Ankle pathway.
- No x-ray, fracture, dislocation, open wound/open fracture, high-energy trauma, crush injury, neurovascular compromise, suspected tendon/ligament rupture, compartment syndrome concern, septic joint/infection concern, pediatric growth plate pathway, elderly/osteoporotic high-risk pattern, or specialist-directed orthopedic plan.

## Patient-Facing Change

The reviewed knee/shoulder v1 includes a site-aware return precaution:

- For knee injuries, new inability to bear weight or put weight through the injured leg.

## Verification

Passed:

- `python3 knowledge/ontology/evals/check_phase251_300_sprain_boundary.py`
- `python3 knowledge/ontology/evals/check_phase216_220_promotion_readiness.py`
- `python3 knowledge/ontology/evals/check_phase222_250_promotion_release.py`
- `python3 knowledge/ontology/evals/check_phase202_215_cycle.py`
- `python3 knowledge/ontology/evals/run_runtime_cases.py`
- `node knowledge/ontology/evals/run_netlify_runtime_smoke.mjs`
- `python3 knowledge/ontology/evals/check_phase21_expansion_gate.py`
- `node knowledge/ontology/evals/check_product_tailoring_contract.mjs`
- `npm run build`
- `git diff --check`

## Current Gate

Reviewed runtime clean: true.

Reviewed source gaps: 0.

Draft source gaps: 0.

Active draft phenotype count: 1.

Active draft:

- `wrist_sprain_xray_negative`

Phenotype expansion allowed: false.

Graph: 2169 nodes / 3322 edges.
