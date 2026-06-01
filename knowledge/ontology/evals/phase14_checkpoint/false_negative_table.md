# Phase 14 False-Negative Table

These are no-match fallbacks. In the current policy, false negatives are acceptable if they avoid unsafe ontology mode.

| Case | Input condition | Expected behavior |
| --- | --- | --- |
| `vague_ankle_pain_fallback` | ankle pain | generator fallback |
| `phase14_minor_head_vague_fallback` | headache | generator fallback |
| `phase14_renal_colic_vague_fallback` | flank pain | generator fallback |
| `lumbar_vague_fallback` | back pain | generator fallback |
| `viral_uri_vague_fallback` | cough | generator fallback |
| `cystitis_vague_fallback` | dysuria | generator fallback |
| `gastro_vague_fallback` | nausea | generator fallback |
| `cellulitis_vague_fallback` | rash | generator fallback |
| `abscess_vague_fallback` | skin bump | generator fallback |
| `laceration_vague_fallback` | wound | generator fallback |
| `dental_vague_fallback` | mouth pain | generator fallback |
| `allergy_vague_fallback` | itching | generator fallback |
