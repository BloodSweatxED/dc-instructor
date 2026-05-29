# Phase 10 Mode Comparison

Compares current generator output, ontology assembly, and the current clinician-review target state.

| Phenotype | Classifier | Generator risks | Ontology risks | Source support | Review |
| --- | --- | --- | --- | --- | --- |
| `abdominal_pain_nonspecific_reassuring_workup` | 0.93 / phenotype_not_clinician_reviewed | red_flags_missing=False; med=3; certainty=0 | red_flags_missing=False; med=0; certainty=0 | needed=True | draft |
| `abscess_after_i_and_d` | 0.93 / phenotype_not_clinician_reviewed | red_flags_missing=False; med=3; certainty=0 | red_flags_missing=False; med=0; certainty=0 | needed=True | draft |
| `allergic_reaction_resolved_no_anaphylaxis` | 0.93 / phenotype_not_clinician_reviewed | red_flags_missing=False; med=2; certainty=0 | red_flags_missing=False; med=0; certainty=0 | needed=True | draft |
| `ankle_sprain_xray_negative` | 0.93 / ontology | red_flags_missing=False; med=3; certainty=0 | red_flags_missing=False; med=0; certainty=0 | needed=False | reviewed |
| `asthma_exacerbation_improved_discharge` | 0.93 / phenotype_not_clinician_reviewed | red_flags_missing=False; med=2; certainty=0 | red_flags_missing=False; med=0; certainty=0 | needed=True | draft |
| `cellulitis_uncomplicated_oral_antibiotics` | 0.93 / phenotype_not_clinician_reviewed | red_flags_missing=False; med=2; certainty=0 | red_flags_missing=False; med=0; certainty=0 | needed=True | draft |
| `chest_pain_low_risk_negative_ed_workup` | 0.93 / phenotype_not_clinician_reviewed | red_flags_missing=False; med=3; certainty=1 | red_flags_missing=False; med=0; certainty=0 | needed=True | draft |
| `community_acquired_pneumonia_outpatient` | 0.93 / phenotype_not_clinician_reviewed | red_flags_missing=False; med=3; certainty=0 | red_flags_missing=False; med=0; certainty=0 | needed=True | draft |
| `concussion_discharge_no_imaging_red_flags` | 0.93 / phenotype_not_clinician_reviewed | red_flags_missing=False; med=2; certainty=0 | red_flags_missing=False; med=0; certainty=0 | needed=True | draft |
| `dental_pain_no_deep_space_infection` | 0.93 / phenotype_not_clinician_reviewed | red_flags_missing=False; med=3; certainty=0 | red_flags_missing=False; med=0; certainty=0 | needed=True | draft |
| `gastroenteritis_stable_hydrating` | 0.93 / phenotype_not_clinician_reviewed | red_flags_missing=False; med=3; certainty=0 | red_flags_missing=False; med=0; certainty=0 | needed=False | draft |
| `laceration_repaired_simple` | 0.93 / phenotype_not_clinician_reviewed | red_flags_missing=False; med=2; certainty=0 | red_flags_missing=False; med=0; certainty=0 | needed=True | draft |
| `lumbar_strain_no_red_flags` | 0.93 / phenotype_not_clinician_reviewed | red_flags_missing=False; med=2; certainty=0 | red_flags_missing=False; med=0; certainty=0 | needed=False | draft |
| `minor_head_injury_no_red_flags` | 0.93 / phenotype_not_clinician_reviewed | red_flags_missing=False; med=2; certainty=1 | red_flags_missing=False; med=0; certainty=0 | needed=True | draft |
| `renal_colic_stable_no_infection` | 0.93 / phenotype_not_clinician_reviewed | red_flags_missing=False; med=3; certainty=0 | red_flags_missing=False; med=0; certainty=0 | needed=True | draft |
| `uncomplicated_cystitis_nonpregnant` | 0.93 / phenotype_not_clinician_reviewed | red_flags_missing=False; med=3; certainty=1 | red_flags_missing=False; med=0; certainty=0 | needed=False | draft |
| `viral_pharyngitis_strep_negative` | 0.93 / phenotype_not_clinician_reviewed | red_flags_missing=False; med=3; certainty=0 | red_flags_missing=False; med=0; certainty=0 | needed=True | draft |
| `viral_uri_no_pneumonia` | 0.93 / phenotype_not_clinician_reviewed | red_flags_missing=False; med=3; certainty=0 | red_flags_missing=False; med=0; certainty=0 | needed=False | draft |

## Production Gates

- Source audit must pass before ontology mode can be used.
- Clinician review status must be `reviewed` for phenotype and primitives.
- Unsafe modifier matches force generator fallback.
- The classifier accepts scrubbed ED-note context only and writes no note text.
- Runtime emits `ontology_mode`, `phenotype_id`, `ontology_confidence`, and `fallback_reason` metadata.
