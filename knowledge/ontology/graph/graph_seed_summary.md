# DC Instructor Knowledge Graph Seed

Generated: deterministic_from_current_ontology_and_generator_batches

## Counts

- Nodes: 2067
- Edges: 3055

## Node Types

- `candidate_primitive`: 1099
- `exclusion`: 94
- `generator_case`: 50
- `generator_section`: 300
- `must_not_miss`: 96
- `phenotype`: 54
- `primitive`: 324
- `safety_topic`: 9
- `source_card`: 41

## Edge Types

- `contains_candidate_primitive`: 1099
- `drafts_for_existing_phenotype`: 21
- `has_exclusion`: 97
- `has_generated_section`: 300
- `has_must_not_miss`: 124
- `mentions_safety_topic`: 569
- `proposes_candidate_phenotype`: 29
- `requires_primitive`: 297
- `supported_by_source`: 519

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
