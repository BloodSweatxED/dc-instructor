# Phase 20 Low-Confidence Near-Miss Audit

Low-confidence fallback is allowed only when the candidate match is intentional symptom-only or chief-complaint-only behavior. Ruled-out diagnoses and absent final diagnoses should become `no_supported_phenotype_match` instead.

| Case | Candidate | Confidence | Rationale |
| --- | --- | --- | --- |
| `phase14_asthma_near_miss_copd_fallback` | `asthma_exacerbation_improved_discharge` | 0.6 | COPD wheezing may share asthma terms but must not enter ontology mode |
| `phase14_asthma_vague_wheeze_fallback` | `asthma_exacerbation_improved_discharge` | 0.6 | symptom-only wheezing remains near asthma but below ontology threshold |
| `phase14_low_confidence_hit_head` | `minor_head_injury_no_red_flags` | 0.62 | hit-head triage language remains near minor head injury but lacks final diagnosis |
| `phase14_low_confidence_kidney_stone` | `renal_colic_stable_no_infection` | 0.608 | possible stone language remains near renal colic but lacks final diagnosis |
| `phase14_low_confidence_lung_infection` | `community_acquired_pneumonia_outpatient` | 0.6 | possible lung infection remains near pneumonia but lacks discharge phenotype |
| `phase14_vague_rash_fallback` | `allergic_reaction_resolved_no_anaphylaxis` | 0.6 | rash with allergy language remains near allergy but below ontology threshold |
| `phase20_asthma_vague_chief_complaint_fallback` | `asthma_exacerbation_improved_discharge` | 0.6 | symptom-only wheezing remains near asthma but below ontology threshold |
| `phase20_concussion_vague_chief_complaint_fallback` | `concussion_discharge_no_imaging_red_flags` | 0.608 | chief complaint names concussion but lacks red-flag and imaging review |
