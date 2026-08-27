# DC Instructor Knowledge Base

Local MedlinePlus vector database pipeline for DC Instructor.

This builds small back-pain collections from MedlinePlus Health Topic XML. The Chroma database stays local. The code, manifests, and retrieval evals are committed so the database can be rebuilt and audited.

## Ontology Layer

The `knowledge/ontology` folder is the first primitive-centered ED discharge instruction layer.

It starts with five supported draft phenotypes:

- `lumbar_strain_no_red_flags`
- `ankle_sprain_xray_negative`
- `viral_uri_no_pneumonia`
- `uncomplicated_cystitis_nonpregnant`
- `gastroenteritis_stable_hydrating`

Validate it:

```bash
python3 knowledge/ontology/scripts/validate_ontology.py
```

Assemble a deterministic discharge instruction from primitives:

```bash
python3 knowledge/ontology/scripts/assemble_discharge.py --phenotype lumbar_strain_no_red_flags --reading-level 6
python3 knowledge/ontology/scripts/assemble_discharge.py --phenotype ankle_sprain_xray_negative --reading-level 6
python3 knowledge/ontology/scripts/assemble_discharge.py --phenotype viral_uri_no_pneumonia --reading-level 6
python3 knowledge/ontology/scripts/assemble_discharge.py --phenotype uncomplicated_cystitis_nonpregnant --reading-level 6
python3 knowledge/ontology/scripts/assemble_discharge.py --phenotype gastroenteritis_stable_hydrating --reading-level 6
```

Generate side-by-side ontology review files for the first five phenotypes:

```bash
python3 knowledge/ontology/scripts/compare_with_generator.py
```

To include output from a local Netlify generator:

```bash
python3 knowledge/ontology/scripts/compare_with_generator.py --generator-url http://localhost:8888/.netlify/functions/generate
```

Generate the 15-case draft-output batch using the same prompt scaffold as the app:

```bash
node knowledge/ontology/scripts/generate_batch_outputs.mjs
node knowledge/ontology/scripts/generate_batch_outputs.mjs --fill-vault-note
```

Generate the second 35-case draft-output batch:

```bash
node knowledge/ontology/scripts/generate_batch_outputs.mjs \
  --title "Generator Batch 02 Outputs" \
  --cases knowledge/ontology/evals/generator_batch_02_cases.json \
  --json-out knowledge/ontology/evals/generator_batch_02_outputs.json \
  --md-out knowledge/ontology/evals/generator_batch_02_outputs.md
```

Build the seed ontology graph:

```bash
python3 knowledge/ontology/graph/build_seed_graph.py
```

The ontology layer is meant to become the governed product core:

```text
condition + ED note -> phenotype -> reviewed primitives -> six-section discharge instructions
```

The MedlinePlus and WikEM source cards support primitive review and phenotype design. They are not treated as copy/paste source text.

## What Gets Ingested

Collections:

- `medlineplus_backpain_v0`: XML `full-summary` only.
- `medlineplus_backpain_v1_sections`: XML summaries plus linked MedlinePlus page sections.

Topics:

- Back Pain
- Sciatica
- Herniated Disk
- Neck Injuries and Disorders
- Spine Injuries and Disorders
- Sprains and Strains

Source: latest MedlinePlus Health Topic XML from `https://medlineplus.gov/xml.html`.

The v0 pipeline uses the `full-summary` field from XML only.

The v1 pipeline keeps the same topic allowlist, then fetches linked MedlinePlus-owned resources, extracts article sections, classifies section types, and stores source metadata for retrieval evaluation.

V1 also adds a small deterministic reranker for ED-style test queries. It retrieves a wider vector candidate pool, then boosts section types that match intent, such as `when_to_seek_care` for return precautions and `self_care` for home-care queries.

## Setup

```bash
cd "/Users/andre/Desktop/Claude Projects/dc-instructor"
python3 -m venv knowledge/.venv
source knowledge/.venv/bin/activate
pip install -r knowledge/requirements.txt
```

## Build The Local DB

```bash
python knowledge/ingest_medlineplus.py ingest
```

Build the richer section-level collection:

```bash
python knowledge/ingest_medlineplus.py ingest-v1
```

Default local DB path:

```text
knowledge/db/dc_medline_db
```

That directory is ignored by git.

## Run Retrieval Sanity Test

```bash
python knowledge/ingest_medlineplus.py test
```

Run the richer v1 test:

```bash
python knowledge/ingest_medlineplus.py test-v1
```

Compare v0 vs v1 retrieval:

```bash
python knowledge/ingest_medlineplus.py compare
```

Run the local RAG smoke test against one case:

```bash
python knowledge/rag_smoke_test.py
```

Run all smoke cases:

```bash
python knowledge/rag_smoke_test.py --all
```

The current smoke-test bridge writes the v3 prompt/retrieval artifact by default:

```text
knowledge/evals/rag_smoke_backpain_v3.json
```

Run retrieval-only without calling the LLM:

```bash
python knowledge/rag_smoke_test.py --all --no-generate
```

This writes:

```text
knowledge/evals/medline_backpain_v0_retrieval.json
knowledge/evals/medline_backpain_v1_sections_retrieval.json
knowledge/evals/medline_backpain_v0_vs_v1.json
knowledge/evals/rag_smoke_backpain_v1.json
knowledge/evals/rag_smoke_backpain_v2.json
knowledge/evals/rag_smoke_backpain_v3.json
knowledge/evals/rag_smoke_review_backpain_v1.md
knowledge/evals/rag_smoke_review_backpain_v2.md
knowledge/evals/rag_smoke_review_backpain_v3.md
```

## Optional Overrides

```bash
python knowledge/ingest_medlineplus.py ingest \
  --db-path knowledge/db/dc_medline_db \
  --collection medlineplus_backpain_v0

python knowledge/ingest_medlineplus.py ingest-v1 \
  --db-path knowledge/db/dc_medline_db \
  --collection medlineplus_backpain_v1_sections
```

Use `--xml-url` to pin a specific MedlinePlus XML file for exact reruns.

## Committed vs Local

Committed:

- Pipeline code
- Python requirements
- Manifest
- Retrieval eval JSON

Local only:

- Chroma database files
- Downloaded raw XML cache
- Python virtual environment
- Local model/package caches
