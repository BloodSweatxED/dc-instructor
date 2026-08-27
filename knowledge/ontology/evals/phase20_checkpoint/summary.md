# Phase 20 Runtime Depth Checkpoint

Reviewed runtime-enabled phenotypes: 16.
Phase 20 runtime cases: 40.
Contradictory-note cases: 16.
Vague-chief-complaint cases: 16.
Medication-sensitive cases: 6.
Ontology-mode clean passes in Phase 20: 0.
Unsafe-modifier fallbacks in Phase 20: 22.
Low-confidence fallbacks in Phase 20: 2.
No-match fallbacks in Phase 20: 16.

Checkpoint read: Phase 20 is a depth gate, not a phenotype-expansion phase. The classifier should keep ambiguous or contradictory notes out of ontology mode even when a reviewed phenotype is nearby.

Low-confidence behavior is now allowlisted. New low-confidence candidates should fail `check_low_confidence_near_misses.py` until reviewed.

Next recommended move: use this checkpoint as the gate before adding new phenotypes or expanding patient-facing content.
