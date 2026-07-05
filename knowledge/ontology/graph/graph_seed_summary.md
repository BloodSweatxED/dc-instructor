# DC Instructor Knowledge Graph Seed

Generated: deterministic_from_current_ontology_and_generator_batches

## Counts

- Nodes: 5704
- Edges: 11560

## Node Types

- `candidate_primitive`: 1099
- `exclusion`: 319
- `generator_case`: 50
- `generator_section`: 300
- `must_not_miss`: 359
- `phenotype`: 305
- `primitive`: 3140
- `safety_topic`: 9
- `source_card`: 123

## Edge Types

- `contains_candidate_primitive`: 1099
- `drafts_for_existing_phenotype`: 23
- `has_exclusion`: 481
- `has_generated_section`: 300
- `has_must_not_miss`: 1215
- `mentions_safety_topic`: 569
- `proposes_candidate_phenotype`: 27
- `requires_primitive`: 3113
- `supported_by_source`: 4733

## Use

This graph is a review artifact. Use it to find repeated candidate primitives, safety topics, unsupported phenotype candidates, and source-support gaps before promoting text into reviewed ontology primitives.

Canonical JSON:

```text
knowledge/ontology/graph/graph_seed.json
```

Cytoscape-compatible JSON:

```text
knowledge/ontology/graph/graph_seed.cyjs.json
```
