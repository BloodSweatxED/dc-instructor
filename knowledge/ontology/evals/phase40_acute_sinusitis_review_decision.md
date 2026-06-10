# Phase 40 Acute Sinusitis Review Decision

Decision: do not promote `acute_sinusitis_supportive_care` yet.

Reason:

The draft is useful and source-supported, but the antibiotic boundary is clinically sensitive. It needs clinician review before runtime ontology mode because acute bacterial sinusitis, watchful waiting, antibiotic prescribing, recurrent disease, dental source, and orbital complications can be too close for a first-pass static phenotype.

Current state:

- Draft phenotype exists.
- Runtime blockers exist.
- Phase 38 and Phase 39 runtime cases exist.
- Source cards exist.
- Patient-facing draft is available in the review sheet.
- Expansion gate should remain closed with one active draft.

Promotion requirements:

- Explicit clinician approval of supportive-care wording.
- Explicit decision about whether watchful waiting belongs inside this phenotype or remains outside.
- Phase 20 contradictory and vague-chief-complaint coverage before any promotion.
- Netlify parity remains passing.
