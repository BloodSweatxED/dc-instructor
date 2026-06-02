# DC Instructor Ontology Style Guide

The live DC Instructor tool is the style baseline. Source cards support claims, but they should not set the voice.

## Voice Target

Patient-facing output should sound like an ED clinician translating the visit, not a health library article.

Use:

- Short sentences.
- Plain words.
- Concrete home actions.
- ED-course narrative when it helps: why the patient came in, what was checked or treated, what improved, and why home care is reasonable.
- Direct return precautions.

Avoid:

- Generic source-card phrasing.
- Long disease education.
- Repeating "as prescribed" in every medication line.
- Unsupported certainty about tests, imaging, or diagnoses.
- Medication dosing unless the medication-policy layer allows clinician-provided dose extraction.

## Section Pattern

`DIAGNOSIS` should name the problem in patient language.

`WHAT WE FOUND` should usually include the ED arc:

1. You came in because symptoms got worse.
2. We checked or treated the relevant problem.
3. You improved or your exam was reassuring.
4. This is why home care is reasonable today.

`WHAT TO DO AT HOME` should be practical. Prefer actions the patient can do tonight.

`MEDICATIONS` should be useful but governed. Until medication policy is built, use clinician-provided medication names only when explicitly supported by the note/runtime layer. Static ontology primitives should avoid inventing dose, duration, route, or frequency.

`RETURN TO ED IF` should sound like ED return precautions, not a textbook symptom list.

`FOLLOW UP` should be actionable, but local-policy-dependent intervals need clinician review before broad rollout.

## Phase 14.5 Rule

Before expanding phenotype count, each reviewed phenotype should have at least one golden-output comparison against the live DC Instructor tool or a clinician-authored target.

## Product Boundary

The reviewed ontology, graph, vector/RAG support, source cards, and evals should stay reusable as an open-source ED discharge-instruction knowledge base.

DC Instructor itself is the product layer. It tailors the reusable knowledge base to the actual ED note, clinician-entered medications, reading level, language, local follow-up instructions, and interface.

Do not make the open-source layer a copy of `dcinstructor.com`. Make it the clinical substrate that `dcinstructor.com` can tailor.
