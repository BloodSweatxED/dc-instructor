# Phase 153 Acute Otitis Media Source Plan

Status: complete.

Candidate: `acute_otitis_media_uncomplicated`.

Source cards:

- `cdc.ear_infection`
- `medlineplus.ear_infections`

Source-supported concepts:

- Acute otitis media is a middle-ear infection.
- Ear infection education can include pain, fever, hearing symptoms, and follow-up.
- Antibiotics are not automatic for every ear infection; treatment choice is clinician-directed.
- Severe, worsening, persistent, draining-ear, or hearing-loss symptoms need medical reassessment.

Source limitations:

- Sources support patient education, not ED disposition or risk stratification.
- Antibiotic selection, dosing, delayed prescribing, pediatric/adult differences, and follow-up interval need clinician-specific instructions.
- The ontology runtime must not infer absence of mastoiditis, perforation, tube, trauma, foreign body, hearing loss, facial weakness, or systemic illness from silence.

Boundary decision:

Build as draft only. Require clinician diagnosis plus structured absence of ear red flags before the draft can even reach the review fallback path.
