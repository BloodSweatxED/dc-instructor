# DC Instructor Knowledge Graph Seed

Generated: deterministic_from_current_ontology_and_generator_batches

## Counts

- Nodes: 1615
- Edges: 2179

## Node Types

- `candidate_primitive`: 1099
- `exclusion`: 26
- `generator_case`: 50
- `generator_section`: 300
- `must_not_miss`: 23
- `phenotype`: 50
- `primitive`: 48
- `safety_topic`: 9
- `source_card`: 10

## Edge Types

- `contains_candidate_primitive`: 1099
- `drafts_for_existing_phenotype`: 5
- `has_exclusion`: 26
- `has_generated_section`: 300
- `has_must_not_miss`: 25
- `mentions_safety_topic`: 569
- `proposes_candidate_phenotype`: 45
- `requires_primitive`: 48
- `supported_by_source`: 62

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
