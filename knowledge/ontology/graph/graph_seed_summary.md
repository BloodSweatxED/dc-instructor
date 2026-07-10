# DC Instructor Knowledge Graph Seed

Generated: deterministic_from_current_ontology_and_generator_batches

## Counts

- Nodes: 6190
- Edges: 12959

## Node Types

- `candidate_primitive`: 1099
- `exclusion`: 321
- `generator_case`: 50
- `generator_section`: 300
- `must_not_miss`: 363
- `phenotype`: 345
- `primitive`: 3580
- `safety_topic`: 9
- `source_card`: 123

## Edge Types

- `contains_candidate_primitive`: 1099
- `drafts_for_existing_phenotype`: 23
- `has_exclusion`: 521
- `has_generated_section`: 300
- `has_must_not_miss`: 1375
- `mentions_safety_topic`: 569
- `proposes_candidate_phenotype`: 27
- `requires_primitive`: 3553
- `supported_by_source`: 5492

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
