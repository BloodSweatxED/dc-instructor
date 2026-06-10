# Phase 20 False-Positive Pressure Table

These cases intentionally contain a candidate phenotype signal but must not enter ontology mode.

| Case | Candidate | Fallback | Exclusions | Case type |
| --- | --- | --- | --- | --- |
| `phase20_abscess_contradictory_note_blocks` | `abscess_after_i_and_d` | unsafe_modifier_present | `necrotizing_infection_concern`, `sepsis` | contradictory or vague |
| `phase20_allergy_contradictory_note_blocks` | `allergic_reaction_resolved_no_anaphylaxis` | unsafe_modifier_present | `airway_symptoms`, `hypotension` | contradictory or vague |
| `phase20_ankle_contradictory_note_blocks` | `ankle_sprain_xray_negative` | unsafe_modifier_present | `fracture_seen` | contradictory or vague |
| `phase20_asthma_contradictory_note_blocks` | `asthma_exacerbation_improved_discharge` | unsafe_modifier_present | `poor_inhaler_access` | contradictory or vague |
| `phase20_asthma_vague_chief_complaint_fallback` | `asthma_exacerbation_improved_discharge` | low_confidence | none | contradictory or vague |
| `phase20_cellulitis_contradictory_note_blocks` | `cellulitis_uncomplicated_oral_antibiotics` | unsafe_modifier_present | `necrotizing_infection_concern`, `rapid_progression` | contradictory or vague |
| `phase20_pneumonia_contradictory_note_blocks` | `community_acquired_pneumonia_outpatient` | unsafe_modifier_present | `hypoxia` | contradictory or vague |
| `phase20_concussion_contradictory_note_blocks` | `concussion_discharge_no_imaging_red_flags` | unsafe_modifier_present | `anticoagulated`, `neurologic_deficit` | contradictory or vague |
| `phase20_concussion_vague_chief_complaint_fallback` | `concussion_discharge_no_imaging_red_flags` | low_confidence | none | contradictory or vague |
| `phase20_dental_contradictory_note_blocks` | `dental_pain_no_deep_space_infection` | unsafe_modifier_present | `deep_space_swelling`, `trismus` | contradictory or vague |
| `phase20_gastro_contradictory_note_blocks` | `gastroenteritis_stable_hydrating` | unsafe_modifier_present | `gi_bleeding`, `unable_to_tolerate_oral_fluids` | contradictory or vague |
| `phase20_laceration_contradictory_note_blocks` | `laceration_repaired_simple` | unsafe_modifier_present | `bite_wound`, `hand_tendon_risk` | contradictory or vague |
| `phase20_lumbar_contradictory_note_blocks` | `lumbar_strain_no_red_flags` | unsafe_modifier_present | `cauda_equina_concern` | contradictory or vague |
| `phase20_minor_head_contradictory_note_blocks` | `minor_head_injury_no_red_flags` | unsafe_modifier_present | `anticoagulated`, `persistent_vomiting` | contradictory or vague |
| `phase20_renal_contradictory_note_blocks` | `renal_colic_stable_no_infection` | unsafe_modifier_present | `fever`, `vomiting_unable_to_take_meds` | contradictory or vague |
| `phase20_cystitis_contradictory_note_blocks` | `uncomplicated_cystitis_nonpregnant` | unsafe_modifier_present | `flank_pain`, `pregnancy`, `vomiting_unable_to_take_meds` | contradictory or vague |
| `phase20_pharyngitis_contradictory_note_blocks` | `viral_pharyngitis_strep_negative` | unsafe_modifier_present | `positive_strep_test` | contradictory or vague |
| `phase20_uri_contradictory_note_blocks` | `viral_uri_no_pneumonia` | unsafe_modifier_present | `bacterial_infection_suspected`, `pneumonia` | contradictory or vague |
| `phase20_med_sensitive_asthma_access_blocks` | `asthma_exacerbation_improved_discharge` | unsafe_modifier_present | `poor_inhaler_access` | medication-sensitive |
| `phase20_med_sensitive_cystitis_vomiting_blocks` | `uncomplicated_cystitis_nonpregnant` | unsafe_modifier_present | `vomiting_unable_to_take_meds` | medication-sensitive |
| `phase20_med_sensitive_gastro_recent_antibiotics_blocks` | `gastroenteritis_stable_hydrating` | unsafe_modifier_present | `c_diff_risk` | medication-sensitive |
| `phase20_med_sensitive_pneumonia_vomiting_blocks` | `community_acquired_pneumonia_outpatient` | unsafe_modifier_present | `vomiting_unable_to_take_meds` | medication-sensitive |
| `phase20_med_sensitive_renal_colic_vomiting_blocks` | `renal_colic_stable_no_infection` | unsafe_modifier_present | `vomiting_unable_to_take_meds` | medication-sensitive |
| `phase20_med_sensitive_uri_antibiotic_blocks` | `viral_uri_no_pneumonia` | unsafe_modifier_present | `antibiotic_prescribed`, `bacterial_infection_suspected` | medication-sensitive |
