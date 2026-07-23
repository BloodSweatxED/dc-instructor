# Phase 152 Candidate Ranking After Phase 151

Status: complete.

The Phase 151 gate is open: reviewed runtime clean, source gaps zero, active draft count zero, and broad chief complaints do not trigger ontology phenotypes.

Recommendation: build `acute_otitis_media_uncomplicated` next as draft only.

Why this candidate:

- Common ED discharge problem.
- Clear CDC and MedlinePlus source support for middle-ear infection education and antibiotic-stewardship framing.
- Safer boundary than dizziness, syncope, palpitations, low-risk chest pain, or nonspecific headache.
- Runtime can require clinician diagnosis and structured absence of ear red flags.
- Main risks are visible and controllable: mastoiditis, perforation or tube, otitis externa, ear trauma or foreign body, acute hearing loss, facial weakness, immunocompromise, severe systemic illness, chronic/recurrent infection, and specialist-directed ENT plans.

Candidates considered:

| Candidate | Recommendation | Reason |
| --- | --- | --- |
| `acute_otitis_media_uncomplicated` | first | Best mix of frequency, source support, and runtime boundary clarity. |
| `suture_removal_or_wound_check_no_infection` | second | Operationally safe, but source support is thinner and overlaps existing laceration content. |
| `viral_syndrome_flu_like_illness` | later | Common, but broad chief-complaint bleed risk is high without a very narrow diagnosis context. |
| `hypertension_no_emergency` | later | Useful, but risks overstepping medication and risk-stratification decisions. |
| `medication_refill` | defer | Product workflow more than clinical ontology. |
| `dizziness_nonspecific` | defer | Too high-risk and context-dependent for static ontology. |
| `syncope_low_risk_discharge` | defer | Requires risk stratification, ECG interpretation, comorbidities, and local follow-up. |
| `chest_pain_low_risk_negative_ed_workup` | defer | Already retired as static ontology content. |

Decision:

Proceed to source plan and draft boundaries for `acute_otitis_media_uncomplicated`. Do not promote without explicit clinician review.
