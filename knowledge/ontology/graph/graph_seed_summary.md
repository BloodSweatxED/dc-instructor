# DC Instructor Knowledge Graph Seed

Generated: deterministic_from_current_ontology_and_generator_batches

## Counts

- Nodes: 4698
- Edges: 8744

## Node Types

- `candidate_primitive`: 1099
- `exclusion`: 307
- `generator_case`: 50
- `generator_section`: 300
- `must_not_miss`: 326
- `phenotype`: 225
- `primitive`: 2259
- `safety_topic`: 9
- `source_card`: 123

## Edge Types

- `contains_candidate_primitive`: 1099
- `drafts_for_existing_phenotype`: 23
- `has_exclusion`: 401
- `has_generated_section`: 300
- `has_must_not_miss`: 892
- `mentions_safety_topic`: 569
- `proposes_candidate_phenotype`: 27
- `requires_primitive`: 2232
- `supported_by_source`: 3201

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
