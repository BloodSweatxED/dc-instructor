# Phase 351 Wrist Sprain Promotion

Date: 2026-06-04

Status: promoted after clinician-owner approval.

## Approval

Clinician-owner approval:

```text
I approve `wrist_sprain_xray_negative` for reviewed ontology mode with the current required context, blocker behavior, and patient-facing output.
```

## Decision

Promote `wrist_sprain_xray_negative` to reviewed ontology mode.

Keep these adjacent sprain decisions unchanged:

- `sprain_strain_non_ankle_xray_negative` remains retired.
- `sprain_strain_knee_or_shoulder_xray_negative` remains reviewed and enabled.
- `ankle_sprain_xray_negative` remains unchanged.
- Elbow and foot remain excluded pending split.

## Runtime Contract

Reviewed ontology mode requires:

- Wrist site documented.
- X-ray performed and negative.
- Intact neurovascular exam.
- Explicit no scaphoid or no snuffbox tenderness documentation.

Reviewed ontology mode blocks:

- Scaphoid or snuffbox tenderness.
- FOOSH plus scaphoid-risk signal.
- No x-ray performed.
- Fracture seen.
- Dislocation.
- Open wound or open fracture.
- High-energy trauma or crush injury.
- Neurovascular compromise.
- Tendon or ligament rupture concern.
- Compartment syndrome concern.
- Septic joint or infection concern.
- Pediatric growth plate pathway.
- Osteoporotic or fragility-fracture risk.
- Hand tendon risk.
- Specialist-directed orthopedic plan.

## Maintenance Items Logged Before Closure

Tracked in:

- `knowledge/ontology/evals/phase351_sprain_maintenance_items.md`

Items:

- Replace the weak knee/shoulder infection return-precaution tail during the next sprain maintenance pass.
- Before opening the next phenotype batch, confirm elbow and foot strings still reliably trigger `elbow_or_foot_site_pending_split`.

## Verification

Passed:

- `python3 knowledge/ontology/evals/check_phase302_350_wrist_sprain_gate.py`
- `python3 knowledge/ontology/evals/check_phase251_300_sprain_boundary.py`
- `python3 knowledge/ontology/evals/check_phase216_220_promotion_readiness.py`
- `python3 knowledge/ontology/evals/check_phase202_215_cycle.py`
- `python3 knowledge/ontology/evals/check_phase222_250_promotion_release.py`
- `python3 knowledge/ontology/evals/run_runtime_cases.py`
- `node knowledge/ontology/evals/run_netlify_runtime_smoke.mjs`
- `python3 knowledge/ontology/evals/build_phase21_expansion_gate.py`
- `python3 knowledge/ontology/evals/check_phase21_expansion_gate.py`
- `node knowledge/ontology/evals/check_product_tailoring_contract.mjs`
- `npm run build`
- `git diff --check`

Current gate:

- Reviewed runtime clean: true.
- Reviewed source gaps: 0.
- Draft source gaps: 0.
- Active draft phenotype count: 0.
- Phenotype expansion allowed: true.
- Phase 20 contradictory-note coverage: 24 of 24 reviewed phenotypes.
