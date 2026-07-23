# Phase 461-480 Candidate Selection

Status: complete.

Gate precondition:

Phase 452-460 was rerun from a clean sequence before drafting:

- `build_expanded_draft_packs.py`
- `promote_reviewed_phenotypes.py`
- `run_runtime_cases.py`
- `build_phase21_expansion_gate.py`
- `check_phase21_expansion_gate.py`
- `build_seed_graph.py`
- `run_netlify_runtime_smoke.mjs`
- `check_product_tailoring_contract.mjs`
- `check_product_prompt_policy.mjs`
- `npm run build`
- `git diff --check`

Gate result before drafting:

- `reviewed_runtime_clean: true`
- `phenotype_expansion_allowed: true`
- `reviewed_source_gap_count: 0`
- `draft_source_gap_count: 0`
- `active_draft_phenotype_count: 0`

Candidate comparison:

| Candidate | Source coverage | Overlap risk | Decision |
| --- | --- | --- | --- |
| `foot_sprain_xray_negative` | Stronger. MedlinePlus has direct foot sprain aftercare plus general sprain/strain coverage. | Moderate. Needs ankle pathway, Lisfranc or midfoot concern, inability to bear weight, diabetic foot, vascular disease, and high-risk trauma blockers. | Selected for this cycle. |
| `acute_elbow_sprain_xray_negative` | Weaker. General sprain/strain support exists, but elbow-specific discharge boundaries would lean on fracture, dislocation, instability, and tendon sources rather than a direct elbow sprain aftercare source. | Moderate. Needs separation from reviewed elbow overuse and from acute elbow instability, tendon rupture, dislocation, and pediatric fracture pathways. | Defer until after foot review. |

Recommendation:

Build exactly one draft: `foot_sprain_xray_negative`.

Rationale:

Foot has cleaner public patient-education source support today. The overlap risk is real but controllable with explicit foot terms and strict blockers. Acute traumatic elbow sprain should come next only after this foot draft is reviewed, revised, promoted, or retired.

