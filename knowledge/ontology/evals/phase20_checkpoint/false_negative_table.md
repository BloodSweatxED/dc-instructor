# Phase 20 False-Negative Pressure Table

These vague-chief-complaint cases should fall back unless the classifier has enough reviewed-phenotype signal.

| Case | Input condition | Candidate | Fallback |
| --- | --- | --- | --- |
| `phase20_abscess_vague_chief_complaint_fallback` | skin problem | none | no_supported_phenotype_match |
| `phase20_allergy_vague_chief_complaint_fallback` | rash | none | no_supported_phenotype_match |
| `phase20_ankle_vague_chief_complaint_fallback` | ankle pain | none | no_supported_phenotype_match |
| `phase20_asthma_vague_chief_complaint_fallback` | wheezing | `asthma_exacerbation_improved_discharge` | low_confidence |
| `phase20_cellulitis_vague_chief_complaint_fallback` | rash | none | no_supported_phenotype_match |
| `phase20_pneumonia_vague_chief_complaint_fallback` | cough | none | no_supported_phenotype_match |
| `phase20_concussion_vague_chief_complaint_fallback` | concussion | `concussion_discharge_no_imaging_red_flags` | low_confidence |
| `phase20_dental_vague_chief_complaint_fallback` | mouth pain | none | no_supported_phenotype_match |
| `phase20_gastro_vague_chief_complaint_fallback` | nausea | none | no_supported_phenotype_match |
| `phase20_laceration_vague_chief_complaint_fallback` | wound | none | no_supported_phenotype_match |
| `phase20_lumbar_vague_chief_complaint_fallback` | back pain | none | no_supported_phenotype_match |
| `phase20_minor_head_vague_chief_complaint_fallback` | headache | none | no_supported_phenotype_match |
| `phase20_renal_vague_chief_complaint_fallback` | flank pain | none | no_supported_phenotype_match |
| `phase20_cystitis_vague_chief_complaint_fallback` | dysuria | none | no_supported_phenotype_match |
| `phase20_pharyngitis_vague_chief_complaint_fallback` | sore throat | none | no_supported_phenotype_match |
| `phase20_uri_vague_chief_complaint_fallback` | cough | none | no_supported_phenotype_match |
