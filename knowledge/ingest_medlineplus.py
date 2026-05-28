#!/usr/bin/env python3
"""
MedlinePlus ingestion pipeline for DC Instructor.

Builds a local Chroma vector database from a small, reproducible back-pain
subset of MedlinePlus Health Topic XML. Generated DB files are intentionally
local-only; the manifest and retrieval evals are safe to commit.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any
from urllib.parse import urlparse
import xml.etree.ElementTree as ET

import chromadb
import requests
import textstat
from bs4 import BeautifulSoup
from chromadb.utils import embedding_functions


PIPELINE_VERSION = "medline_backpain_v0"
MEDLINE_XML_INDEX_PAGE = "https://medlineplus.gov/xml.html"
DEFAULT_COLLECTION = "medlineplus_backpain_v0"
DEFAULT_EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
DEFAULT_DB_PATH = Path("knowledge/db/dc_medline_db")
DEFAULT_MANIFEST_PATH = Path("knowledge/manifests/medline_backpain_v0.json")
DEFAULT_EVAL_PATH = Path("knowledge/evals/medline_backpain_v0_retrieval.json")
RAW_DIR = Path("knowledge/data/raw")

ALLOWED_TOPICS = [
    "Back Pain",
    "Sciatica",
    "Herniated Disk",
    "Neck Injuries and Disorders",
    "Spine Injuries and Disorders",
    "Sprains and Strains",
]

TEST_QUERIES = [
    "home care after lumbar strain",
    "ice or heat for back pain",
    "when to return to the ED for back pain",
    "sciatica numbness weakness instructions",
    "herniated disk follow up",
]

CHUNK_SIZE_WORDS = 150
CHUNK_OVERLAP_SENTENCES = 2


@dataclass(frozen=True)
class Topic:
    title: str
    url: str
    topic_id: str
    language: str
    groups: list[str]
    mesh: list[str]
    also_called: list[str]
    full_summary_html: str


def utc_now_iso() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat()


def content_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def stable_chunk_id(topic_url: str, section: str, chunk_index: int, text: str) -> str:
    raw = f"{topic_url}|{section}|{chunk_index}|{text}"
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()[:24]


def clean_text(text: str) -> str:
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def html_to_text(html: str) -> str:
    soup = BeautifulSoup(html, "lxml")
    for tag in soup(["script", "style"]):
        tag.decompose()
    return clean_text(soup.get_text(separator=" "))


def sentence_split(text: str) -> list[str]:
    sentences = re.split(r"(?<=[.!?])\s+", text)
    return [sentence.strip() for sentence in sentences if len(sentence.split()) > 3]


def reading_level_label(grade: float) -> str:
    if grade <= 6:
        return "basic"
    if grade <= 9:
        return "intermediate"
    return "advanced"


def flesch_kincaid_grade(text: str) -> float:
    try:
        return round(float(textstat.flesch_kincaid_grade(text)), 1)
    except Exception:
        return -1.0


def chunk_text(text: str) -> list[dict[str, Any]]:
    sentences = sentence_split(text)
    chunks: list[dict[str, Any]] = []
    current: list[str] = []
    word_count = 0

    for sentence in sentences:
        current.append(sentence)
        word_count += len(sentence.split())

        if word_count >= CHUNK_SIZE_WORDS:
            chunk = clean_text(" ".join(current))
            grade = flesch_kincaid_grade(chunk)
            chunks.append(
                {
                    "text": chunk,
                    "fk_grade": grade,
                    "reading_level": reading_level_label(grade),
                    "word_count": word_count,
                }
            )
            current = current[-CHUNK_OVERLAP_SENTENCES:]
            word_count = sum(len(item.split()) for item in current)

    if current and word_count > 20:
        chunk = clean_text(" ".join(current))
        grade = flesch_kincaid_grade(chunk)
        chunks.append(
            {
                "text": chunk,
                "fk_grade": grade,
                "reading_level": reading_level_label(grade),
                "word_count": word_count,
            }
        )

    return chunks


def discover_latest_xml_url(index_page: str = MEDLINE_XML_INDEX_PAGE) -> str:
    response = requests.get(index_page, timeout=30)
    response.raise_for_status()

    urls = sorted(
        set(
            re.findall(
                r"https://medlineplus\.gov/xml/mplus_topics_\d{4}-\d{2}-\d{2}\.xml",
                response.text,
            )
        ),
        reverse=True,
    )
    if not urls:
        raise RuntimeError(f"No MedlinePlus health topic XML URLs found at {index_page}")
    return urls[0]


def raw_xml_path(xml_url: str) -> Path:
    name = Path(urlparse(xml_url).path).name
    return RAW_DIR / name


def download_xml(xml_url: str) -> bytes:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    path = raw_xml_path(xml_url)
    if path.exists():
        return path.read_bytes()

    response = requests.get(xml_url, timeout=60)
    response.raise_for_status()
    path.write_bytes(response.content)
    return response.content


def parse_topics(xml_bytes: bytes) -> tuple[list[Topic], str]:
    root = ET.fromstring(xml_bytes)
    source_date_generated = root.attrib.get("date-generated", "")
    topics: list[Topic] = []

    for item in root.findall(".//health-topic"):
        topic = Topic(
            title=item.attrib.get("title", ""),
            url=item.attrib.get("url", ""),
            topic_id=item.attrib.get("id", ""),
            language=item.attrib.get("language", ""),
            groups=[group.text or "" for group in item.findall("./group") if group.text],
            mesh=[
                descriptor.text or ""
                for descriptor in item.findall("./mesh-heading/descriptor")
                if descriptor.text
            ],
            also_called=[
                alias.text or "" for alias in item.findall("./also-called") if alias.text
            ],
            full_summary_html=item.findtext("./full-summary") or "",
        )
        topics.append(topic)

    return topics, source_date_generated


def allowed_english_topics(topics: list[Topic]) -> list[Topic]:
    allowed = set(ALLOWED_TOPICS)
    return [
        topic
        for topic in topics
        if topic.language == "English" and topic.title in allowed and topic.full_summary_html
    ]


def build_records(
    topics: list[Topic],
    *,
    source_xml_url: str,
    source_date_generated: str,
    ingested_at: str,
) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []

    for topic in topics:
        text = html_to_text(topic.full_summary_html)
        if not text:
            continue

        for chunk_index, chunk in enumerate(chunk_text(text)):
            chunk_hash = content_hash(chunk["text"])
            records.append(
                {
                    "id": stable_chunk_id(topic.url, "full_summary", chunk_index, chunk["text"]),
                    "document": chunk["text"],
                    "metadata": {
                        "topic": topic.title,
                        "topic_id": topic.topic_id,
                        "section": "full_summary",
                        "url": topic.url,
                        "mesh": json.dumps(topic.mesh),
                        "groups": json.dumps(topic.groups),
                        "also_called": json.dumps(topic.also_called),
                        "language": "en",
                        "fk_grade": chunk["fk_grade"],
                        "reading_level": chunk["reading_level"],
                        "word_count": chunk["word_count"],
                        "content_hash": chunk_hash,
                        "source_xml_url": source_xml_url,
                        "source_date_generated": source_date_generated,
                        "ingested_at": ingested_at,
                        "pipeline_version": PIPELINE_VERSION,
                    },
                }
            )

    return records


def embedding_function(model_name: str):
    return embedding_functions.SentenceTransformerEmbeddingFunction(model_name=model_name)


def get_collection(db_path: Path, collection_name: str, model_name: str):
    client = chromadb.PersistentClient(path=str(db_path))
    return client.get_or_create_collection(
        name=collection_name,
        embedding_function=embedding_function(model_name),
        metadata={"hnsw:space": "cosine"},
    )


def write_manifest(
    path: Path,
    *,
    source_xml_url: str,
    source_date_generated: str,
    ingested_at: str,
    db_path: Path,
    collection_name: str,
    embed_model: str,
    topics: list[Topic],
    records: list[dict[str, Any]],
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    manifest = {
        "pipeline_version": PIPELINE_VERSION,
        "source": "MedlinePlus Health Topic XML",
        "source_xml_url": source_xml_url,
        "source_date_generated": source_date_generated,
        "ingested_at": ingested_at,
        "db_path": str(db_path),
        "collection": collection_name,
        "embedding_model": embed_model,
        "allowed_topics": ALLOWED_TOPICS,
        "topics_ingested": [topic.title for topic in topics],
        "topic_count": len(topics),
        "chunk_count": len(records),
        "chunk_hashes": [record["metadata"]["content_hash"] for record in records],
    }
    path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


def ingest(args: argparse.Namespace) -> None:
    source_xml_url = args.xml_url or discover_latest_xml_url()
    ingested_at = utc_now_iso()

    print(f"Source XML: {source_xml_url}")
    xml_bytes = download_xml(source_xml_url)
    all_topics, source_date_generated = parse_topics(xml_bytes)
    topics = allowed_english_topics(all_topics)
    records = build_records(
        topics,
        source_xml_url=source_xml_url,
        source_date_generated=source_date_generated,
        ingested_at=ingested_at,
    )

    missing = sorted(set(ALLOWED_TOPICS) - {topic.title for topic in topics})
    if missing:
        raise RuntimeError(f"Missing expected MedlinePlus topics: {', '.join(missing)}")
    if not records:
        raise RuntimeError("No chunks generated; refusing to create an empty collection.")

    collection = get_collection(args.db_path, args.collection, args.embed_model)

    for start in range(0, len(records), args.batch_size):
        batch = records[start : start + args.batch_size]
        collection.upsert(
            ids=[record["id"] for record in batch],
            documents=[record["document"] for record in batch],
            metadatas=[record["metadata"] for record in batch],
        )
        print(f"Upserted {start + len(batch)} / {len(records)} chunks")

    write_manifest(
        args.manifest_path,
        source_xml_url=source_xml_url,
        source_date_generated=source_date_generated,
        ingested_at=ingested_at,
        db_path=args.db_path,
        collection_name=args.collection,
        embed_model=args.embed_model,
        topics=topics,
        records=records,
    )

    print(f"Collection count: {collection.count()}")
    print(f"Manifest: {args.manifest_path}")


def test_retrieval(args: argparse.Namespace) -> None:
    collection = get_collection(args.db_path, args.collection, args.embed_model)
    if collection.count() == 0:
        raise RuntimeError(f"Collection {args.collection!r} is empty. Run ingest first.")

    eval_rows = {
        "pipeline_version": PIPELINE_VERSION,
        "tested_at": utc_now_iso(),
        "db_path": str(args.db_path),
        "collection": args.collection,
        "embedding_model": args.embed_model,
        "queries": [],
    }

    required_metadata = {
        "topic",
        "section",
        "url",
        "mesh",
        "groups",
        "source_xml_url",
        "source_date_generated",
        "content_hash",
        "reading_level",
        "fk_grade",
    }

    for query in TEST_QUERIES:
        results = collection.query(query_texts=[query], n_results=args.n_results)
        docs = results.get("documents", [[]])[0]
        metadatas = results.get("metadatas", [[]])[0]
        distances = results.get("distances", [[]])[0]

        rows = []
        print(f"\nQuery: {query}")
        for rank, (doc, metadata, distance) in enumerate(
            zip(docs, metadatas, distances, strict=False),
            start=1,
        ):
            missing = sorted(required_metadata - set(metadata.keys()))
            if missing:
                raise RuntimeError(
                    f"Result for query {query!r} is missing metadata: {', '.join(missing)}"
                )

            row = {
                "rank": rank,
                "topic": metadata["topic"],
                "section": metadata["section"],
                "url": metadata["url"],
                "fk_grade": metadata["fk_grade"],
                "reading_level": metadata["reading_level"],
                "distance": distance,
                "preview": doc[:220],
            }
            rows.append(row)
            print(
                f"  [{rank}] {row['topic']} | {row['reading_level']} "
                f"| FK {row['fk_grade']} | distance {distance:.4f}"
            )
            print(f"      {row['preview']}...")

        eval_rows["queries"].append({"query": query, "results": rows})

    args.eval_path.parent.mkdir(parents=True, exist_ok=True)
    args.eval_path.write_text(json.dumps(eval_rows, indent=2) + "\n", encoding="utf-8")
    print(f"\nRetrieval eval: {args.eval_path}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="DC Instructor MedlinePlus ingestion")
    subparsers = parser.add_subparsers(dest="command", required=True)

    def add_common(subparser: argparse.ArgumentParser) -> None:
        subparser.add_argument("--db-path", type=Path, default=DEFAULT_DB_PATH)
        subparser.add_argument("--collection", default=DEFAULT_COLLECTION)
        subparser.add_argument("--embed-model", default=DEFAULT_EMBED_MODEL)

    ingest_parser = subparsers.add_parser("ingest", help="Build/update local Chroma DB")
    add_common(ingest_parser)
    ingest_parser.add_argument("--xml-url", default=None)
    ingest_parser.add_argument("--manifest-path", type=Path, default=DEFAULT_MANIFEST_PATH)
    ingest_parser.add_argument("--batch-size", type=int, default=100)
    ingest_parser.set_defaults(func=ingest)

    test_parser = subparsers.add_parser("test", help="Run retrieval sanity test")
    add_common(test_parser)
    test_parser.add_argument("--eval-path", type=Path, default=DEFAULT_EVAL_PATH)
    test_parser.add_argument("--n-results", type=int, default=3)
    test_parser.set_defaults(func=test_retrieval)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
