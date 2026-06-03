# Phase 82 Migraine Retirement

Decision: retire `migraine_improved_discharge` to product-layer fallback only.

Runtime mode: `retired_product_layer_fallback_only`.

Reason:

- No explicit clinician approval exists for ontology-mode use.
- Secondary-headache boundaries are clinically high-stakes.
- The existing draft is useful for review and product-layer fallback, but not for autonomous ontology selection.
- Retirement reopens phenotype expansion without lowering the review bar.

Guardrails preserved:

- No broad headache fallback.
- No broad severe headache fallback.
- Sudden, severe headache reaching worst point within seconds or worst headache of life, neurologic deficit, meningitis or CNS infection concern, fever with headache, neck stiffness, head trauma within 7 days, pregnancy, immunocompromise, age over 50 with new headache pattern, uncontrolled vomiting at discharge, altered mental status not fully resolved, unstable vitals, first-lifetime headache of this severity, and CT not performed with documented concern remain blockers.
