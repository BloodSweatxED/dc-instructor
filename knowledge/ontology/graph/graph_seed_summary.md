# DC Instructor Knowledge Graph Seed

Generated: deterministic_from_current_ontology_and_generator_batches

## Counts

- Nodes: 1862
- Edges: 2607

## Node Types

- `candidate_primitive`: 1099
- `exclusion`: 66
- `generator_case`: 50
- `generator_section`: 300
- `must_not_miss`: 68
- `phenotype`: 50
- `primitive`: 196
- `safety_topic`: 9
- `source_card`: 24

## Edge Types

- `contains_candidate_primitive`: 1099
- `drafts_for_existing_phenotype`: 18
- `has_exclusion`: 68
- `has_generated_section`: 300
- `has_must_not_miss`: 82
- `mentions_safety_topic`: 569
- `proposes_candidate_phenotype`: 32
- `requires_primitive`: 196
- `supported_by_source`: 243

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
