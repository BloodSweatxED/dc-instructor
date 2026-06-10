# Open-Source Knowledge Base Boundary

DC Instructor has two related but separate layers.

## Reusable Open-Source Layer

The ED discharge-instruction knowledge base should be reusable.

This includes:

- Phenotype definitions.
- Source cards.
- Reviewed primitives.
- Runtime safety gates.
- Vector, graph, and RAG support artifacts.
- Review packets.
- Evaluation cases.

This layer should work as open infrastructure for ED discharge-instruction generation. It should help other projects assemble safe, source-audited, emergency-medicine-specific discharge instructions without copying the DC Instructor product.

## DC Instructor Product Layer

`dcinstructor.com` is the tailoring product.

The product takes the reusable knowledge base and adapts it to:

- The actual ED note.
- Medications and doses the clinician entered.
- Reading level.
- Language.
- Local follow-up instructions.
- The patient-facing tone and layout.

The product can use an LLM, vector retrieval, graph retrieval, and deterministic ontology assembly together. The knowledge base is the reusable clinical substrate. DC Instructor is the workflow that turns it into a patient-specific discharge instruction.

## Design Rule

Do not let the reusable knowledge base become a generic public-health article store.

The knowledge base should preserve ED reasoning, source audit, must-not-miss boundaries, and practical discharge actions. The product layer should personalize and format that material for the patient in front of the clinician.
