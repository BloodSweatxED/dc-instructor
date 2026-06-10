# Phase 18 Product Tailoring Contract

Status: approved for implementation.

## Product Boundary

DCInstructor.com is the tailoring product. It uses the reusable knowledge base, LLM calls, graph/vector/RAG support, clinician-entered medications, reading level, language, and local instructions to create patient-specific output.

The reusable knowledge base is the governed clinical substrate. It should be reusable outside DCInstructor.com as an open-source feature: reviewed phenotypes, reviewed primitives, source cards, graph exports, runtime gates, and evaluation cases.

## What The Ontology May Do

- Provide reviewed baseline discharge content for narrow phenotypes.
- Include source-card IDs and review metadata.
- Use general medication language without doses, routes, frequencies, or durations.
- Fall back when unsafe modifiers, vague chief complaints, contradictions, missing support, or low confidence are present.

## What The Product Layer May Do

- Tailor voice, reading level, language, and local phrasing.
- Use clinician-entered ED note context after PHI redaction.
- Pass through medication details only when explicitly present in the clinician-entered note.
- Add local follow-up scripts and additional learning resources.
- Use the LLM when ontology mode is blocked or when the case is not yet reviewed.

## What The Product Layer Must Not Do

- Infer a medication, dose, route, frequency, or duration from a diagnosis alone.
- Complete missing medication details from a vague note such as "start antibiotics."
- Weaken ontology fallback gates.
- Present draft ontology content as reviewed.
- Hide medication and follow-up review requirements from the clinician.

## Current Implementation

- `netlify/functions/generate.js` enforces passthrough-only medication prompting.
- `netlify/functions/generate.js` emits medication provenance metadata for the UI.
- `src/components/OutputPanel.jsx` displays medication provenance next to mode metadata.
- `netlify/functions/ontology-runtime.js` emits source-card IDs used by reviewed ontology output.

## Phase 20 Direction

Phase 20 should deepen this boundary instead of expanding content:

- Build a false-positive and false-negative table for runtime gating.
- Add contradictory-note and vague-chief-complaint cases for every reviewed phenotype.
- Add line-level or section-level provenance in the product UI if medication review still feels too coarse.
- Keep source-card and graph/RAG artifacts reusable outside DCInstructor.com.
