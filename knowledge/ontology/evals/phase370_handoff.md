# Phase 370 Handoff

Date: 2026-06-04

Status: sprain maintenance complete, next candidate ranked, no new draft opened.

Current state:

- `wrist_sprain_xray_negative` is reviewed.
- `sprain_strain_knee_or_shoulder_xray_negative` is reviewed.
- `sprain_strain_non_ankle_xray_negative` remains retired/product-layer fallback only.
- No active drafts are open.
- Elbow and foot remain excluded by `elbow_or_foot_site_pending_split`.

Completed in Phases 352-360:

- Replaced the weak knee/shoulder return-precaution tail with concrete infection language.
- Confirmed clean tracked elbow and foot sprain strings stop at `unsafe_modifier_present` with `elbow_or_foot_site_pending_split`.
- Kept elbow/foot out of patient-facing reviewed output.

Completed in Phases 361-370:

- Ranked next candidates after maintenance passed.
- Recommended opening the sprain-family split next, starting with `elbow_sprain_xray_negative` as one narrow draft.
- Kept `foot_sprain_xray_negative` second because foot/ankle boundary and weight-bearing logic are more leak-prone.

Verification:

```bash
python3 knowledge/ontology/scripts/build_expanded_draft_packs.py
python3 knowledge/ontology/scripts/promote_reviewed_phenotypes.py
python3 knowledge/ontology/graph/build_seed_graph.py
python3 knowledge/ontology/evals/check_phase352_360_sprain_maintenance.py
python3 knowledge/ontology/evals/check_phase302_350_wrist_sprain_gate.py
python3 knowledge/ontology/evals/run_runtime_cases.py
node knowledge/ontology/evals/run_netlify_runtime_smoke.mjs
npm run build
```

Next startup prompt:

Continue DC Instructor ontology work from Phase 370. Sprain maintenance is complete and the expansion gate is open with no active drafts. Open the elbow/foot sprain split as the next batch, but build only one narrow draft first: `elbow_sprain_xray_negative`. Start source-first and runtime-boundary-first. Keep foot excluded by `elbow_or_foot_site_pending_split` until an intentional foot split. Do not silently promote.
