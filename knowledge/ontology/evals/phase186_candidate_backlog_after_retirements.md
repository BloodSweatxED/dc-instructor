# Phase 186 Candidate Backlog After Retirements

Status: complete.

Candidate backlog:

| Candidate | Recommendation | Reason |
| --- | --- | --- |
| `viral_syndrome_flu_like_illness` | consider later | Common, but broad symptom overlap is high. |
| `hypertension_no_emergency` | defer | Risk stratification and medication changes are clinician-dependent. |
| `medication_refill` | product-layer | Workflow more than clinical ontology. |
| `sprain_strain_non_ankle_xray_negative` | consider later | Safer if imaging/result context is explicit. |
| `skin_avulsion_or_abrasion_simple` | consider later | Could reuse wound sources, but needs boundary work. |
| `dizziness_nonspecific` | defer | Too dangerous for static ontology. |
| `syncope_low_risk_discharge` | defer | Requires risk stratification. |

Recommendation:

Next true candidate should be `sprain_strain_non_ankle_xray_negative` or `skin_avulsion_or_abrasion_simple`, not dizziness/syncope/chest pain.
