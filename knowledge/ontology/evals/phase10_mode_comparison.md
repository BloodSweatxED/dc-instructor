# Phase 10 Mode Comparison

Compares current generator output, ontology assembly, and the current clinician-review target state.

| Phenotype | Classifier | Generator risks | Ontology risks | Source support | Review |
| --- | --- | --- | --- | --- | --- |
| `abdominal_pain_nonspecific_reassuring_workup` | 0.93 / phenotype_not_clinician_reviewed | red_flags_missing=False; med=3; certainty=0 | red_flags_missing=False; med=0; certainty=0 | needed=False | needs_review |
| `abscess_after_i_and_d` | 0.93 / ontology | red_flags_missing=False; med=3; certainty=0 | red_flags_missing=False; med=0; certainty=0 | needed=False | reviewed |
| `allergic_reaction_resolved_no_anaphylaxis` | 0.93 / ontology | red_flags_missing=False; med=2; certainty=0 | red_flags_missing=False; med=0; certainty=0 | needed=False | reviewed |
| `ankle_sprain_xray_negative` | 0.93 / ontology | red_flags_missing=False; med=3; certainty=0 | red_flags_missing=False; med=0; certainty=0 | needed=False | reviewed |
| `asthma_exacerbation_improved_discharge` | 0.93 / ontology | red_flags_missing=False; med=2; certainty=0 | red_flags_missing=False; med=0; certainty=0 | needed=False | reviewed |
| `cellulitis_uncomplicated_oral_antibiotics` | 0.93 / ontology | red_flags_missing=False; med=2; certainty=0 | red_flags_missing=False; med=0; certainty=0 | needed=False | reviewed |
| `chest_pain_low_risk_negative_ed_workup` | 0.93 / phenotype_not_clinician_reviewed | red_flags_missing=False; med=3; certainty=1 | red_flags_missing=False; med=0; certainty=0 | needed=False | retired |
| `community_acquired_pneumonia_outpatient` | 0.93 / ontology | red_flags_missing=False; med=3; certainty=0 | red_flags_missing=False; med=0; certainty=0 | needed=False | reviewed |
| `concussion_discharge_no_imaging_red_flags` | 0.93 / ontology | red_flags_missing=False; med=2; certainty=0 | red_flags_missing=False; med=0; certainty=0 | needed=False | reviewed |
| `dental_pain_no_deep_space_infection` | 0.93 / ontology | red_flags_missing=False; med=3; certainty=0 | red_flags_missing=False; med=0; certainty=0 | needed=False | reviewed |
| `gastroenteritis_stable_hydrating` | 0.93 / ontology | red_flags_missing=False; med=3; certainty=0 | red_flags_missing=False; med=0; certainty=0 | needed=False | reviewed |
| `laceration_repaired_simple` | 0.93 / ontology | red_flags_missing=False; med=2; certainty=0 | red_flags_missing=False; med=0; certainty=0 | needed=False | reviewed |
| `lumbar_strain_no_red_flags` | 0.93 / ontology | red_flags_missing=False; med=2; certainty=0 | red_flags_missing=False; med=0; certainty=0 | needed=False | reviewed |
| `minor_head_injury_no_red_flags` | 0.93 / ontology | red_flags_missing=False; med=2; certainty=1 | red_flags_missing=False; med=0; certainty=0 | needed=False | reviewed |
| `renal_colic_stable_no_infection` | 0.93 / ontology | red_flags_missing=False; med=3; certainty=0 | red_flags_missing=False; med=0; certainty=0 | needed=False | reviewed |
| `uncomplicated_cystitis_nonpregnant` | 0.93 / ontology | red_flags_missing=False; med=3; certainty=1 | red_flags_missing=False; med=0; certainty=0 | needed=False | reviewed |
| `viral_pharyngitis_strep_negative` | 0.93 / ontology | red_flags_missing=False; med=3; certainty=0 | red_flags_missing=False; med=0; certainty=0 | needed=False | reviewed |
| `viral_uri_no_pneumonia` | 0.93 / ontology | red_flags_missing=False; med=3; certainty=0 | red_flags_missing=False; med=0; certainty=0 | needed=False | reviewed |

## Production Gates

- Source audit must pass before ontology mode can be used.
- Clinician review status must be `reviewed` for phenotype and primitives.
- Unsafe modifier matches force generator fallback.
- The classifier accepts scrubbed ED-note context only and writes no note text.
- Runtime emits `ontology_mode`, `phenotype_id`, `ontology_confidence`, and `fallback_reason` metadata.
