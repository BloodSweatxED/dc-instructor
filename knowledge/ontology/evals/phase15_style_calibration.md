# Phase 15 Style Calibration

Status: complete for current reviewed ontology library.

Reviewed phenotypes covered: 16.

## What Changed

Phase 15 added a reproducible DC Instructor voice overlay:

```text
knowledge/ontology/style/apply_style_calibration.py
```

The overlay runs after source-backed draft generation and reviewed phenotype promotion. It keeps the source-audited ontology structure, but rewrites expanded reviewed pack primitives toward the live DC Instructor style:

- ED-course narrative.
- Practical home actions.
- Direct return precautions.
- Less generic source-card prose.
- No invented medication dosing.

The style baseline check now covers all 16 reviewed phenotypes:

```text
knowledge/ontology/evals/check_style_baseline.py
```

## Product Boundary

The ED discharge-instruction knowledge base should remain reusable open-source infrastructure.

`dcinstructor.com` is the tailoring product. It uses the reusable knowledge base, LLM calls, graph/vector/RAG support, clinician-entered medications, reading level, language, and local instructions to create patient-specific output.

## Next Gates

Do not expand phenotype count until these are explicit:

- Medication policy for clinician-provided doses.
- Follow-up interval policy.
- Product-layer tailoring contract between ontology output and live LLM output.
