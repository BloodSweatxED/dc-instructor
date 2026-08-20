# DC Instructor Ontology Graph

This folder is the first knowledge graph layer for the discharge ontology.

The graph is not the production runtime yet. It is a review and design artifact that makes the ontology inspectable:

```text
phenotype -> primitive -> source card
phenotype -> must-not-miss condition
phenotype -> exclusion criterion
generator case -> phenotype candidate
```

## Build

```bash
python3 knowledge/ontology/graph/build_seed_graph.py
```

This writes:

```text
knowledge/ontology/graph/graph_seed.json
```

## Node Types

- `phenotype`
- `primitive`
- `source_card`
- `must_not_miss`
- `exclusion`
- `generator_case`

## Edge Types

- `requires_primitive`
- `supported_by_source`
- `has_must_not_miss`
- `has_exclusion`
- `drafts_for_existing_phenotype`
- `proposes_candidate_phenotype`

## Why This Matters

The graph is the safety layer behind deterministic assembly.

It should eventually answer questions like:

- Which return precautions are required for this phenotype?
- Which primitives are unsafe if pregnancy, anticoagulation, immunocompromise, kidney disease, or abnormal vitals are present?
- Which source card supports each medication warning?
- Which generator outputs introduced claims that are not yet source-supported?
- Which unsupported phenotypes are ready for review because the generator produced useful primitive candidates?
