# Phase 361-370 Candidate Ranking After Sprain Maintenance

Status: complete.

Maintenance precondition:

Phase 352-360 passed before ranking. Knee/shoulder return text was cleaned. Elbow and foot strings still reliably trigger `elbow_or_foot_site_pending_split`.

Recommendation:

Open the elbow/foot sprain split next, starting with one narrow elbow draft. Do not build both elbow and foot in the same batch.

Ranking:

| Candidate | Rank | Frequency/usefulness | Narrowness | Source availability | Blocker clarity | Vague chief complaint leakage risk | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `elbow_sprain_xray_negative` | 1 | Common enough, and finishes the tracked sprain-family gap. | Narrow if adult elbow sprain/strain/injury, x-ray performed and negative, intact neurovascular exam. | MedlinePlus sprain/strain source covers general aftercare; elbow-specific fracture/occult injury cautions need source-first review. | Clear blockers: fracture, dislocation, open wound, tendon rupture concern, neurovascular compromise, septic joint, high-energy trauma, pediatric growth plate, elderly/osteoporotic risk, specialist plan. | Low to moderate if condition terms require elbow plus sprain/strain/injury plus negative x-ray context. | Build next as draft only. |
| `foot_sprain_xray_negative` | 2 | Common and useful, but more overlap with ankle pathway and inability-to-bear-weight logic. | Narrow only if foot site is explicit and ankle pathway is excluded. | General sprain/strain source is available; foot-specific fracture and Lisfranc-risk boundaries need source-first review. | Clear but more numerous blockers: ankle pathway, midfoot/Lisfranc concern, fracture, inability to bear weight, neurovascular compromise, high-energy trauma, open wound, pediatric/osteoporotic risk, specialist plan. | Moderate because foot/ankle wording can blur and lower-extremity weight-bearing language is sticky. | Do after elbow, or split into its own batch if elbow exposes shared sprain logic issues. |
| `skin_avulsion_or_abrasion_simple` | 3 | Useful, but no longer more urgent than the tracked sprain split. | Narrow if superficial wound, no closure, no infection, no deep structure risk. | Wound-care source base exists from prior laceration/suture work. | Good blockers, but wound family has broad complaint leakage history. | Moderate because "wound check" and vague injury complaints can drift. | Later. |
| `viral_syndrome_flu_like_illness` | 4 | Very common. | Hard to keep narrow without lab-confirmed or clinician-diagnosed frame. | CDC/MedlinePlus source support is strong. | Blockers are broad: pneumonia, sepsis, asthma/COPD, pregnancy, immunocompromise, dehydration, chest pain, meningitis concern. | High. | Later, after more broad-complaint stress depth. |
| `hypertension_no_emergency` | 5 | Useful. | Depends heavily on risk stratification and medication decisions. | Source support exists, but ED discharge boundary is clinician-dependent. | Blockers are numerous and context-heavy. | Moderate. | Defer. |
| `dizziness_nonspecific` | 6 | Common. | Not narrow enough for current ontology mode. | Source support does not solve risk stratification. | Dangerous misses dominate. | High. | Defer. |
| `syncope_low_risk_discharge` | 7 | Useful but high stakes. | Requires ECG/risk/comorbidity reasoning. | Source support exists but runtime would need deep structured context. | High-risk blockers are too broad for this stage. | High. | Defer. |

Boundary for the next batch:

Build one candidate only: `elbow_sprain_xray_negative`.

The next phase should be source-first and runtime-boundary-first. Patient-facing text comes only after elbow gates are clean. Foot stays explicitly excluded until an intentional foot split.
