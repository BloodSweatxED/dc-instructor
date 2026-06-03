# DC Instructor Knowledge Graph Seed

Generated: deterministic_from_current_ontology_and_generator_batches

## Counts

- Nodes: 2133
- Edges: 3212

## Node Types

- `candidate_primitive`: 1099
- `exclusion`: 103
- `generator_case`: 50
- `generator_section`: 300
- `must_not_miss`: 109
- `phenotype`: 57
- `primitive`: 362
- `safety_topic`: 9
- `source_card`: 44

## Edge Types

- `contains_candidate_primitive`: 1099
- `drafts_for_existing_phenotype`: 21
- `has_exclusion`: 106
- `has_generated_section`: 300
- `has_must_not_miss`: 146
- `mentions_safety_topic`: 569
- `proposes_candidate_phenotype`: 29
- `requires_primitive`: 335
- `supported_by_source`: 607

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
