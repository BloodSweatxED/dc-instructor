# DC Instructor Knowledge Graph Seed

Generated: deterministic_from_current_ontology_and_generator_batches

## Counts

- Nodes: 2086
- Edges: 3097

## Node Types

- `candidate_primitive`: 1099
- `exclusion`: 97
- `generator_case`: 50
- `generator_section`: 300
- `must_not_miss`: 99
- `phenotype`: 55
- `primitive`: 335
- `safety_topic`: 9
- `source_card`: 42

## Edge Types

- `contains_candidate_primitive`: 1099
- `drafts_for_existing_phenotype`: 21
- `has_exclusion`: 100
- `has_generated_section`: 300
- `has_must_not_miss`: 130
- `mentions_safety_topic`: 569
- `proposes_candidate_phenotype`: 29
- `requires_primitive`: 308
- `supported_by_source`: 541

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
