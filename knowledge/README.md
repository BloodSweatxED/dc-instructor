# DC Instructor Knowledge Base

Local MedlinePlus vector database pipeline for DC Instructor.

This builds small back-pain collections from MedlinePlus Health Topic XML. The Chroma database stays local. The code, manifests, and retrieval evals are committed so the database can be rebuilt and audited.

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

This writes:

```text
knowledge/evals/medline_backpain_v0_retrieval.json
knowledge/evals/medline_backpain_v1_sections_retrieval.json
knowledge/evals/medline_backpain_v0_vs_v1.json
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
