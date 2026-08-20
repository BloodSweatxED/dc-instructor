# Phase 602-650 Reviewed Wound Runtime Stress

Status: complete.

Starting point:

- Phase 601 promoted `elbow_sprain_acute_traumatic_xray_negative`.
- Phase 21 gate was open.
- Active draft queue was empty.

Decision:

Use this macrocycle for maintenance, not a new draft.

Rationale:

- The sprain-family elbow and foot split work had just closed.
- `skin_avulsion_or_abrasion_simple` was already reviewed and ontology enabled.
- Wound-family broad-chief-complaint leakage and modifier/blocker boundaries remained useful to harden.

Runtime stress added:

- Clean simple abrasion with diabetes remains reviewed output and surfaces `diabetes_general_risk`.
- Clean simple skin tear with PVD remains reviewed output and surfaces `peripheral_vascular_disease`.
- Clean delayed skin avulsion remains reviewed output and surfaces `delayed_wound_presentation`.
- Bite wound, diabetic foot wound, retained foreign body concern, hand tendon risk, and immunocompromised host block.
- Broad `skin abrasion` without clinician diagnosis does not match.
- Missing wound-cleaned-and-dressed context blocks.

Files added:

- `knowledge/ontology/evals/phase602_650_wound_reviewed_stress_runtime_cases.json`
- `knowledge/ontology/evals/check_phase602_650_wound_reviewed_stress.py`

Files updated:

- `knowledge/ontology/evals/run_netlify_runtime_smoke.mjs`
- Generated runtime results, gate artifacts, graph artifacts, manifest, primitives, and review sheets after serial regeneration.

Review queue:

| ID | Phase | Phenotype | Review Type | Decision Needed | Agent Recommendation | Blocked Action | Safe Work Continued |
|---|---:|---|---|---|---|---|---|
| none | 602-650 | n/a | n/a | n/a | n/a | n/a | reviewed wound runtime hardening |

Verification:

- `knowledge/.venv/bin/python knowledge/ontology/scripts/build_expanded_draft_packs.py`
- `knowledge/.venv/bin/python knowledge/ontology/scripts/promote_reviewed_phenotypes.py`
- `knowledge/.venv/bin/python knowledge/ontology/evals/run_runtime_cases.py`
- `knowledge/.venv/bin/python knowledge/ontology/evals/build_phase21_expansion_gate.py`
- `knowledge/.venv/bin/python knowledge/ontology/evals/check_phase21_expansion_gate.py`
- `knowledge/.venv/bin/python knowledge/ontology/evals/check_phase602_650_wound_reviewed_stress.py`
- `knowledge/.venv/bin/python knowledge/ontology/evals/check_phase352_360_sprain_maintenance.py`
- `knowledge/.venv/bin/python knowledge/ontology/evals/check_phase532_550_elbow_acute_traumatic_draft.py`
- `knowledge/.venv/bin/python knowledge/ontology/evals/check_phase551_600_elbow_review_queue.py`
- `node knowledge/ontology/evals/run_netlify_runtime_smoke.mjs`
- `node knowledge/ontology/evals/check_product_tailoring_contract.mjs`
- `node knowledge/ontology/evals/check_product_prompt_policy.mjs`
- `knowledge/.venv/bin/python knowledge/ontology/graph/build_seed_graph.py`
- `npm run build`
- `git diff --check`

Notes:

- An initial invalid verification attempt ran generator and promotion in parallel. That tripped a transient JSON read error in the generator.
- Primitive JSON files were checked afterward and none were empty or invalid.
- The generation path was rerun serially and passed.

Gate state after macrocycle:

- Reviewed runtime clean: true
- Phenotype expansion allowed: true
- Reviewed source gaps: 0
- Draft source gaps: 0
- Active draft phenotypes: 0
- Runtime cases: 447

Graph count:

- Nodes: 2244
- Edges: 3542
- Phenotype nodes: 61
- Primitive nodes: 434
- Candidate primitive nodes: 1099
- Source card nodes: 49

Next recommendation:

Run another 50-phase macrocycle. Candidate ranking is safe now that gate remains open.

Recommended next lane:

1. Rank the next non-sprain, non-wound candidate with source support.
2. Prefer source audit and runtime-boundary-first work.
3. Do not promote any new candidate without explicit clinician approval.
