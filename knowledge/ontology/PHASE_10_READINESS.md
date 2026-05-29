# DC Instructor Ontology Phase 10 Readiness

Status: draft infrastructure complete. No expanded phenotype is production-ready until source audit and EM clinician review pass.

## What Exists

- Primitive harvest:
  - `knowledge/ontology/harvest/build_primitive_harvest.py`
  - `knowledge/ontology/harvest/primitive_candidates.json`
  - `knowledge/ontology/harvest/primitive_clusters.json`
  - `knowledge/ontology/harvest/primitive_review.md`
  - `knowledge/ontology/harvest/source_gaps.md`
- Expanded draft packs:
  - 13 new phenotype JSON files in `knowledge/ontology/phenotypes/`
  - Shared primitive file: `knowledge/ontology/primitives/expanded_draft_packs.json`
  - Regenerator: `knowledge/ontology/scripts/build_expanded_draft_packs.py`
- Clinician review surface:
  - One Markdown sheet per expanded phenotype in `knowledge/ontology/review_sheets/`
  - Each sheet includes inclusion criteria, exclusions, must-not-miss diagnoses, primitive audit flags, unsafe modifiers, and assembled six-section output.
- Classifier prototype:
  - `knowledge/ontology/scripts/classify_phenotype.py`
  - Output fields: `phenotype_id`, `confidence`, `exclusions`, `modifiers`, `fallback_reason`.
- Runtime integration:
  - `netlify/functions/ontology-runtime.js`
  - `netlify/functions/generate.js`
  - The app displays generator fallback vs reviewed ontology mode in the output panel.
- Evaluation:
  - `knowledge/ontology/evals/compare_modes.py`
  - `knowledge/ontology/evals/phase10_mode_comparison.json`
  - `knowledge/ontology/evals/phase10_mode_comparison.md`
- Visualization:
  - `knowledge/ontology/graph/graph_seed.json`
  - `knowledge/ontology/graph/graph_seed.cyjs.json`
  - Cytoscape-compatible export is the primary graph view.

## Runtime Gates

Ontology mode is blocked unless all are true:

- Phenotype classifier confidence is high enough.
- Phenotype review status is `reviewed`.
- Source audit does not require additional support.
- Unsafe modifier terms are absent from the scrubbed ED-note context.
- The assembler can produce all six required sections.

If any gate fails, runtime uses the existing generator path and emits metadata:

- `ontology_mode`
- `phenotype_id`
- `ontology_confidence`
- `fallback_reason`

The ED note is used only as scrubbed context for classification and generation. It is not written to disk or logged by the ontology runtime.

## Current Clinical State

The expanded packs are intentionally conservative:

- Medication doses are not included in draft ontology primitives.
- Negative imaging and diagnostic certainty are treated as unsafe without chart-specific modifiers.
- Exact follow-up intervals are not hard-coded unless clinician review adds them.
- WikEM remains phenotype and must-not-miss support only, not patient-facing prose.

## Verification Commands

```bash
python3 knowledge/ontology/scripts/validate_ontology.py
python3 knowledge/ontology/graph/build_seed_graph.py
python3 knowledge/ontology/harvest/build_primitive_harvest.py
python3 knowledge/ontology/scripts/build_expanded_draft_packs.py
python3 knowledge/ontology/scripts/classify_phenotype.py --condition "cellulitis skin infection"
python3 knowledge/ontology/evals/compare_modes.py
npm run build
```
