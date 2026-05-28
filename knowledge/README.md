# DC Instructor Knowledge Base

Local MedlinePlus vector database pipeline for DC Instructor.

This first pass builds a small back-pain collection from MedlinePlus Health Topic XML. The Chroma database stays local. The code, manifest, and retrieval evals are committed so the database can be rebuilt and audited.

## What Gets Ingested

Collection: `medlineplus_backpain_v0`

Topics:

- Back Pain
- Sciatica
- Herniated Disk
- Neck Injuries and Disorders
- Spine Injuries and Disorders
- Sprains and Strains

Source: latest MedlinePlus Health Topic XML from `https://medlineplus.gov/xml.html`.

The pipeline uses the `full-summary` field from XML only. It does not scrape individual topic pages in v0.

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

Default local DB path:

```text
knowledge/db/dc_medline_db
```

That directory is ignored by git.

## Run Retrieval Sanity Test

```bash
python knowledge/ingest_medlineplus.py test
```

This writes:

```text
knowledge/evals/medline_backpain_v0_retrieval.json
```

## Optional Overrides

```bash
python knowledge/ingest_medlineplus.py ingest \
  --db-path knowledge/db/dc_medline_db \
  --collection medlineplus_backpain_v0
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
