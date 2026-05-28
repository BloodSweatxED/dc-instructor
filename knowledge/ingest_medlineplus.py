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
V1_PIPELINE_VERSION = "medline_backpain_v1_sections"
MEDLINE_XML_INDEX_PAGE = "https://medlineplus.gov/xml.html"
DEFAULT_COLLECTION = "medlineplus_backpain_v0"
V1_COLLECTION = "medlineplus_backpain_v1_sections"
DEFAULT_EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
DEFAULT_DB_PATH = Path("knowledge/db/dc_medline_db")
DEFAULT_MANIFEST_PATH = Path("knowledge/manifests/medline_backpain_v0.json")
V1_MANIFEST_PATH = Path("knowledge/manifests/medline_backpain_v1_sections.json")
DEFAULT_EVAL_PATH = Path("knowledge/evals/medline_backpain_v0_retrieval.json")
V1_EVAL_PATH = Path("knowledge/evals/medline_backpain_v1_sections_retrieval.json")
COMPARE_EVAL_PATH = Path("knowledge/evals/medline_backpain_v0_vs_v1.json")
RAW_DIR = Path("knowledge/data/raw")
CACHE_DIR = Path("knowledge/data/cache")

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

V1_TEST_QUERIES = [
    *TEST_QUERIES,
    "back pain red flags bowel bladder weakness",
    "lumbar strain discharge instructions",
    "sciatica return precautions",
    "neck strain home care",
    "sprain strain RICE instructions",
]

CHUNK_SIZE_WORDS = 150
CHUNK_OVERLAP_SENTENCES = 2
REQUEST_TIMEOUT_SEC = 25
USER_AGENT = "DC-Instructor-App/1.0"

SKIPPED_SECTION_HEADINGS = {
    "alternative names",
    "images",
    "references",
    "review date",
    "related medlineplus health topics",
    "browse the encyclopedia",
}

RESOURCE_INCLUDE_CATEGORIES = {
    "diagnosis and tests",
    "encyclopedia",
    "living with",
    "patient handouts",
    "prevention and risk factors",
    "specifics",
    "start here",
    "summary",
    "symptoms",
    "treatments and therapies",
}

EXCLUDED_RESOURCE_TITLE_TERMS = {
    "ct scan",
    "diskitis",
    "disk replacement",
    "diskectomy",
    "electromyography",
    "foraminotomy",
    "fusion",
    "mri",
    "myelography",
    "spinal cord stimulation",
    "surgery",
    "x-ray",
}

TOPIC_RETRIEVAL_TERMS = {
    "Back Pain": "low back pain lumbar strain back strain acute back pain home care heat ice activity return precautions",
    "Sciatica": "sciatic pain radiculopathy leg numbness leg weakness tingling return precautions",
    "Herniated Disk": "herniated disc slipped disk radiculopathy nerve pain numbness weakness follow up",
    "Neck Injuries and Disorders": "neck pain neck strain neck spasm cervical strain home care",
    "Spine Injuries and Disorders": "spine injury spinal pain back injury red flags bowel bladder weakness",
    "Sprains and Strains": "sprain strain RICE rest ice compression elevation aftercare home care",
}


@dataclass(frozen=True)
class SiteResource:
    title: str
    url: str
    information_category: str
    organization: str
    standard_description: str


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
    sites: list[SiteResource]


def utc_now_iso() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat()


def content_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def stable_chunk_id(topic_url: str, section: str, chunk_index: int, text: str) -> str:
    raw = f"{topic_url}|{section}|{chunk_index}|{text}"
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()[:24]


def stable_resource_chunk_id(
    topic_url: str,
    resource_url: str,
    section: str,
    chunk_index: int,
    text: str,
) -> str:
    raw = f"{topic_url}|{resource_url}|{section}|{chunk_index}|{text}"
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()[:24]


def clean_text(text: str) -> str:
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def html_to_text(html: str) -> str:
    soup = BeautifulSoup(html, "lxml")
    for tag in soup(["script", "style"]):
        tag.decompose()
    return clean_text(soup.get_text(separator=" "))


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "_", text)
    return text.strip("_") or "section"


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
        sites = []
        for site in item.findall("./site"):
            sites.append(
                SiteResource(
                    title=site.attrib.get("title", ""),
                    url=site.attrib.get("url", ""),
                    information_category=site.findtext("./information-category") or "",
                    organization=site.findtext("./organization") or "",
                    standard_description=site.findtext("./standard-description") or "",
                )
            )

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
            sites=sites,
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


def should_fetch_resource(resource: SiteResource) -> bool:
    if not resource.url:
        return False

    parsed = urlparse(resource.url)
    if parsed.netloc != "medlineplus.gov":
        return False
    if parsed.path.endswith(".pdf"):
        return False
    if parsed.path.startswith("/spanish/"):
        return False
    if not (parsed.path.startswith("/ency/") or re.fullmatch(r"/[a-z0-9]+\.html", parsed.path)):
        return False

    category = resource.information_category.lower()
    if category and category not in RESOURCE_INCLUDE_CATEGORIES:
        return False

    title = resource.title.lower()
    if "clinicaltrials.gov" in title or "journal articles" in title:
        return False
    if any(term in title for term in EXCLUDED_RESOURCE_TITLE_TERMS):
        return False

    return True


def cache_path_for_url(url: str) -> Path:
    suffix = hashlib.sha256(url.encode("utf-8")).hexdigest()[:16]
    return CACHE_DIR / f"{suffix}.html"


def fetch_resource_html(url: str) -> str:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    cache_path = cache_path_for_url(url)
    if cache_path.exists():
        return cache_path.read_text(encoding="utf-8")

    response = requests.get(url, timeout=REQUEST_TIMEOUT_SEC, headers={"User-Agent": USER_AGENT})
    response.raise_for_status()
    if "text/html" not in response.headers.get("content-type", ""):
        return ""

    cache_path.write_text(response.text, encoding="utf-8")
    return response.text


def section_type_for(heading: str, resource_title: str) -> str:
    haystack = f"{heading} {resource_title}".lower()
    if any(term in haystack for term in ["when to call", "when to contact", "seek care", "doctor", "emergency", "red flag"]):
        return "when_to_seek_care"
    if any(term in haystack for term in ["home care", "self-care", "aftercare", "returning to work", "living with"]):
        return "self_care"
    if any(term in haystack for term in ["symptom", "warning sign"]):
        return "symptoms"
    if any(term in haystack for term in ["cause", "risk"]):
        return "causes"
    if any(term in haystack for term in ["exam", "test", "diagnos", "mri", "ct scan"]):
        return "diagnosis"
    if any(term in haystack for term in ["treat", "therapy", "medicine", "surgery", "exercise", "stretch", "rice"]):
        return "treatment"
    if any(term in haystack for term in ["prevent"]):
        return "prevention"
    if any(term in haystack for term in ["follow", "rehab"]):
        return "follow_up"
    return "overview"


def retrieval_document(
    *,
    topic: str,
    resource_title: str,
    section_heading: str,
    section_type: str,
    text: str,
) -> str:
    terms = TOPIC_RETRIEVAL_TERMS.get(topic, "")
    context = (
        f"Topic: {topic}. Resource: {resource_title}. Section: {section_heading}. "
        f"Section type: {section_type}. Retrieval terms: {terms}."
    )
    return f"{context}\n\n{text}"


def intent_adjusted_distance(query: str, row: dict[str, Any]) -> float:
    query_lower = query.lower()
    adjusted = float(row["distance"])
    section_type = row.get("section_type") or ""
    resource_title = (row.get("resource_title") or "").lower()

    if any(term in query_lower for term in ["red flag", "return", "ed", "emergency", "precaution", "bowel", "bladder"]):
        if section_type == "when_to_seek_care":
            adjusted -= 0.18
        elif section_type in {"symptoms", "overview"}:
            adjusted -= 0.04

    if any(term in query_lower for term in ["home", "aftercare", "discharge", "strain", "sprain"]):
        if section_type in {"self_care", "treatment"}:
            adjusted -= 0.14
        if any(term in resource_title for term in ["acute", "aftercare", "self care", "returning to work", "strains", "sprains"]):
            adjusted -= 0.08
        if section_type == "diagnosis":
            adjusted += 0.12

    if any(term in query_lower for term in ["ice", "heat", "rice"]):
        if section_type in {"self_care", "treatment"}:
            adjusted -= 0.16

    if "follow" in query_lower:
        if section_type in {"follow_up", "treatment", "overview"}:
            adjusted -= 0.08
        if section_type == "when_to_seek_care":
            adjusted += 0.08

    return adjusted


def normalize_heading(heading: str) -> str:
    heading = clean_text(heading)
    heading = re.sub(r"\s+\d{1,2}/\d{1,2}/\d{4}$", "", heading)
    return heading


def is_skipped_heading(heading: str) -> bool:
    normalized = normalize_heading(heading).lower()
    return any(normalized == skipped or normalized.startswith(f"{skipped} ") for skipped in SKIPPED_SECTION_HEADINGS)


def extract_sections_from_html(html: str) -> list[dict[str, str]]:
    soup = BeautifulSoup(html, "lxml")
    article = soup.find("article") or soup.find(id="mplus-content")
    if not article:
        return []

    for tag in article(["script", "style", "nav", "aside", "form", "button"]):
        tag.decompose()

    title = article.find("h1")
    page_title = normalize_heading(title.get_text(" ", strip=True)) if title else "overview"
    sections: list[dict[str, str]] = []
    section_nodes = article.find_all("section")
    headings = article.find_all(["h2", "h3"])

    if section_nodes:
        intro_parts: list[str] = []
        for sibling in title.find_next_siblings() if title else article.children:
            if getattr(sibling, "name", None) == "section":
                break
            text = clean_text(sibling.get_text(" ", strip=True)) if hasattr(sibling, "get_text") else clean_text(str(sibling))
            if text and "enable JavaScript" not in text:
                intro_parts.append(text)
        intro = clean_text(" ".join(intro_parts))
        if len(intro.split()) >= 25:
            sections.append({"heading": "Overview", "text": intro})

        for section in section_nodes:
            heading = section.find(["h2", "h3"])
            if not heading:
                continue
            heading_text = normalize_heading(heading.get_text(" ", strip=True))
            if not heading_text or is_skipped_heading(heading_text):
                continue
            heading.extract()
            text = clean_text(section.get_text(" ", strip=True))
            text = re.sub(r"^\s*Collapse Section\s*", "", text)
            if len(text.split()) >= 25:
                sections.append({"heading": heading_text, "text": text})
        return sections

    if not headings:
        text = clean_text(article.get_text(" ", strip=True))
        return [{"heading": page_title, "text": text}] if len(text.split()) >= 25 else []

    intro_parts: list[str] = []
    for sibling in title.find_next_siblings() if title else article.children:
        if getattr(sibling, "name", None) in {"h2", "h3"}:
            break
        text = clean_text(sibling.get_text(" ", strip=True)) if hasattr(sibling, "get_text") else clean_text(str(sibling))
        if text:
            intro_parts.append(text)
    intro = clean_text(" ".join(intro_parts))
    if len(intro.split()) >= 25:
        sections.append({"heading": "Overview", "text": intro})

    for heading in headings:
        heading_text = normalize_heading(heading.get_text(" ", strip=True))
        if not heading_text or is_skipped_heading(heading_text):
            continue

        parts: list[str] = []
        for sibling in heading.find_next_siblings():
            if getattr(sibling, "name", None) in {"h2", "h3"}:
                break
            text = clean_text(sibling.get_text(" ", strip=True)) if hasattr(sibling, "get_text") else clean_text(str(sibling))
            if text:
                parts.append(text)

        text = clean_text(" ".join(parts))
        if len(text.split()) >= 25:
            sections.append({"heading": heading_text, "text": text})

    return sections


def build_v1_records(
    topics: list[Topic],
    *,
    source_xml_url: str,
    source_date_generated: str,
    ingested_at: str,
    max_resources_per_topic: int,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    records: list[dict[str, Any]] = []
    resources_seen: list[dict[str, Any]] = []

    for topic in topics:
        topic_summary_text = html_to_text(topic.full_summary_html)
        for chunk_index, chunk in enumerate(chunk_text(topic_summary_text)):
            chunk_hash = content_hash(chunk["text"])
            records.append(
                {
                    "id": stable_resource_chunk_id(topic.url, topic.url, "full_summary", chunk_index, chunk["text"]),
                    "document": retrieval_document(
                        topic=topic.title,
                        resource_title=topic.title,
                        section_heading="full_summary",
                        section_type="overview",
                        text=chunk["text"],
                    ),
                    "metadata": {
                        "topic": topic.title,
                        "topic_id": topic.topic_id,
                        "section": "full_summary",
                        "section_type": "overview",
                        "url": topic.url,
                        "parent_topic_url": topic.url,
                        "resource_title": topic.title,
                        "resource_url": topic.url,
                        "resource_org": "MedlinePlus",
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
                        "pipeline_version": V1_PIPELINE_VERSION,
                    },
                }
            )

        fetched_count = 0
        deduped_urls: set[str] = set()
        for resource in topic.sites:
            if fetched_count >= max_resources_per_topic:
                break
            if resource.url in deduped_urls or not should_fetch_resource(resource):
                continue
            deduped_urls.add(resource.url)

            try:
                html = fetch_resource_html(resource.url)
                sections = extract_sections_from_html(html)
            except Exception as exc:
                resources_seen.append(
                    {
                        "topic": topic.title,
                        "resource_title": resource.title,
                        "resource_url": resource.url,
                        "status": "fetch_failed",
                        "error": str(exc)[:300],
                    }
                )
                continue

            if not sections:
                resources_seen.append(
                    {
                        "topic": topic.title,
                        "resource_title": resource.title,
                        "resource_url": resource.url,
                        "status": "no_sections",
                    }
                )
                continue

            fetched_count += 1
            resources_seen.append(
                {
                    "topic": topic.title,
                    "resource_title": resource.title,
                    "resource_url": resource.url,
                    "information_category": resource.information_category,
                    "organization": resource.organization or resource.standard_description or "MedlinePlus",
                    "section_count": len(sections),
                    "status": "ingested",
                }
            )

            for section in sections:
                section_name = slugify(section["heading"])
                section_type = section_type_for(section["heading"], resource.title)
                for chunk_index, chunk in enumerate(chunk_text(section["text"])):
                    chunk_hash = content_hash(chunk["text"])
                    records.append(
                        {
                            "id": stable_resource_chunk_id(
                                topic.url,
                                resource.url,
                                section_name,
                                chunk_index,
                                chunk["text"],
                            ),
                            "document": retrieval_document(
                                topic=topic.title,
                                resource_title=resource.title,
                                section_heading=section["heading"],
                                section_type=section_type,
                                text=chunk["text"],
                            ),
                            "metadata": {
                                "topic": topic.title,
                                "topic_id": topic.topic_id,
                                "section": section_name,
                                "section_type": section_type,
                                "url": resource.url,
                                "parent_topic_url": topic.url,
                                "resource_title": resource.title,
                                "resource_url": resource.url,
                                "resource_org": resource.organization or resource.standard_description or "MedlinePlus",
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
                                "pipeline_version": V1_PIPELINE_VERSION,
                            },
                        }
                    )

    return records, resources_seen


def embedding_function(model_name: str):
    return embedding_functions.SentenceTransformerEmbeddingFunction(model_name=model_name)


def get_collection(db_path: Path, collection_name: str, model_name: str):
    client = chromadb.PersistentClient(path=str(db_path))
    return client.get_or_create_collection(
        name=collection_name,
        embedding_function=embedding_function(model_name),
        metadata={"hnsw:space": "cosine"},
    )


def reset_collection(db_path: Path, collection_name: str) -> None:
    client = chromadb.PersistentClient(path=str(db_path))
    try:
        client.delete_collection(collection_name)
        print(f"Reset collection: {collection_name}")
    except Exception:
        pass


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


def write_v1_manifest(
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
    resources: list[dict[str, Any]],
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    ingested_resources = [resource for resource in resources if resource.get("status") == "ingested"]
    section_types = sorted({record["metadata"].get("section_type", "") for record in records})
    manifest = {
        "pipeline_version": V1_PIPELINE_VERSION,
        "source": "MedlinePlus Health Topic XML plus linked MedlinePlus pages",
        "source_xml_url": source_xml_url,
        "source_date_generated": source_date_generated,
        "ingested_at": ingested_at,
        "db_path": str(db_path),
        "collection": collection_name,
        "embedding_model": embed_model,
        "allowed_topics": ALLOWED_TOPICS,
        "topics_ingested": [topic.title for topic in topics],
        "topic_count": len(topics),
        "resource_count": len(ingested_resources),
        "chunk_count": len(records),
        "section_types": section_types,
        "resources": ingested_resources,
        "skipped_or_failed_resources": [
            resource for resource in resources if resource.get("status") != "ingested"
        ],
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

    reset_collection(args.db_path, args.collection)
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


def ingest_v1(args: argparse.Namespace) -> None:
    source_xml_url = args.xml_url or discover_latest_xml_url()
    ingested_at = utc_now_iso()

    print(f"Source XML: {source_xml_url}")
    xml_bytes = download_xml(source_xml_url)
    all_topics, source_date_generated = parse_topics(xml_bytes)
    topics = allowed_english_topics(all_topics)
    records, resources = build_v1_records(
        topics,
        source_xml_url=source_xml_url,
        source_date_generated=source_date_generated,
        ingested_at=ingested_at,
        max_resources_per_topic=args.max_resources_per_topic,
    )

    missing = sorted(set(ALLOWED_TOPICS) - {topic.title for topic in topics})
    if missing:
        raise RuntimeError(f"Missing expected MedlinePlus topics: {', '.join(missing)}")
    if not records:
        raise RuntimeError("No chunks generated; refusing to create an empty collection.")

    reset_collection(args.db_path, args.collection)
    collection = get_collection(args.db_path, args.collection, args.embed_model)

    for start in range(0, len(records), args.batch_size):
        batch = records[start : start + args.batch_size]
        collection.upsert(
            ids=[record["id"] for record in batch],
            documents=[record["document"] for record in batch],
            metadatas=[record["metadata"] for record in batch],
        )
        print(f"Upserted {start + len(batch)} / {len(records)} chunks")

    write_v1_manifest(
        args.manifest_path,
        source_xml_url=source_xml_url,
        source_date_generated=source_date_generated,
        ingested_at=ingested_at,
        db_path=args.db_path,
        collection_name=args.collection,
        embed_model=args.embed_model,
        topics=topics,
        records=records,
        resources=resources,
    )

    print(f"Collection count: {collection.count()}")
    print(f"Resources ingested: {sum(1 for resource in resources if resource.get('status') == 'ingested')}")
    print(f"Manifest: {args.manifest_path}")


def query_collection(
    *,
    collection_name: str,
    db_path: Path,
    embed_model: str,
    queries: list[str],
    n_results: int,
) -> list[dict[str, Any]]:
    collection = get_collection(db_path, collection_name, embed_model)
    if collection.count() == 0:
        raise RuntimeError(f"Collection {collection_name!r} is empty. Run ingest first.")

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
    rows_by_query: list[dict[str, Any]] = []

    candidate_count = max(n_results * 8, 24)

    for query in queries:
        results = collection.query(query_texts=[query], n_results=candidate_count)
        docs = results.get("documents", [[]])[0]
        metadatas = results.get("metadatas", [[]])[0]
        distances = results.get("distances", [[]])[0]

        rows = []
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
                    "section_type": metadata.get("section_type"),
                    "resource_title": metadata.get("resource_title"),
                    "url": metadata["url"],
                    "fk_grade": metadata["fk_grade"],
                    "reading_level": metadata["reading_level"],
                    "distance": distance,
                    "preview": doc.split("\n\n", 1)[-1][:220],
                }
            row["adjusted_distance"] = intent_adjusted_distance(query, row)
            rows.append(row)

        rows.sort(key=lambda item: (item["adjusted_distance"], item["distance"]))
        rows = [{**row, "rank": rank} for rank, row in enumerate(rows[:n_results], start=1)]

        rows_by_query.append({"query": query, "results": rows})

    return rows_by_query


def test_retrieval(args: argparse.Namespace) -> None:
    eval_rows = {
        "pipeline_version": PIPELINE_VERSION,
        "tested_at": utc_now_iso(),
        "db_path": str(args.db_path),
        "collection": args.collection,
        "embedding_model": args.embed_model,
        "queries": [],
    }
    eval_rows["queries"] = query_collection(
        collection_name=args.collection,
        db_path=args.db_path,
        embed_model=args.embed_model,
        queries=TEST_QUERIES,
        n_results=args.n_results,
    )

    for query_row in eval_rows["queries"]:
        print(f"\nQuery: {query_row['query']}")
        for row in query_row["results"]:
            print(
                f"  [{row['rank']}] {row['topic']} | {row['reading_level']} "
                f"| FK {row['fk_grade']} | distance {row['distance']:.4f}"
            )
            print(f"      {row['preview']}...")

    args.eval_path.parent.mkdir(parents=True, exist_ok=True)
    args.eval_path.write_text(json.dumps(eval_rows, indent=2) + "\n", encoding="utf-8")
    print(f"\nRetrieval eval: {args.eval_path}")


def test_retrieval_v1(args: argparse.Namespace) -> None:
    eval_rows = {
        "pipeline_version": V1_PIPELINE_VERSION,
        "tested_at": utc_now_iso(),
        "db_path": str(args.db_path),
        "collection": args.collection,
        "embedding_model": args.embed_model,
        "queries": query_collection(
            collection_name=args.collection,
            db_path=args.db_path,
            embed_model=args.embed_model,
            queries=V1_TEST_QUERIES,
            n_results=args.n_results,
        ),
    }

    for query_row in eval_rows["queries"]:
        print(f"\nQuery: {query_row['query']}")
        for row in query_row["results"]:
            label = row["resource_title"] or row["section"]
            print(
                f"  [{row['rank']}] {row['topic']} | {row.get('section_type') or row['section']} "
                f"| {label} | distance {row['distance']:.4f}"
            )
            print(f"      {row['preview']}...")

    args.eval_path.parent.mkdir(parents=True, exist_ok=True)
    args.eval_path.write_text(json.dumps(eval_rows, indent=2) + "\n", encoding="utf-8")
    print(f"\nRetrieval eval: {args.eval_path}")


def compare_retrieval(args: argparse.Namespace) -> None:
    compared_at = utc_now_iso()
    v0_rows = query_collection(
        collection_name=args.v0_collection,
        db_path=args.db_path,
        embed_model=args.embed_model,
        queries=V1_TEST_QUERIES,
        n_results=args.n_results,
    )
    v1_rows = query_collection(
        collection_name=args.v1_collection,
        db_path=args.db_path,
        embed_model=args.embed_model,
        queries=V1_TEST_QUERIES,
        n_results=args.n_results,
    )

    comparison = {
        "compared_at": compared_at,
        "db_path": str(args.db_path),
        "embedding_model": args.embed_model,
        "v0_collection": args.v0_collection,
        "v1_collection": args.v1_collection,
        "queries": [
            {
                "query": v0_row["query"],
                "v0_results": v0_row["results"],
                "v1_results": v1_row["results"],
            }
            for v0_row, v1_row in zip(v0_rows, v1_rows, strict=True)
        ],
    }

    for row in comparison["queries"]:
        print(f"\nQuery: {row['query']}")
        v0_top = row["v0_results"][0]
        v1_top = row["v1_results"][0]
        print(f"  v0 top: {v0_top['topic']} | {v0_top['section']} | {v0_top['distance']:.4f}")
        print(
            f"  v1 top: {v1_top['topic']} | {v1_top.get('section_type') or v1_top['section']} "
            f"| {v1_top.get('resource_title') or v1_top['section']} | {v1_top['distance']:.4f}"
        )

    args.eval_path.parent.mkdir(parents=True, exist_ok=True)
    args.eval_path.write_text(json.dumps(comparison, indent=2) + "\n", encoding="utf-8")
    print(f"\nComparison eval: {args.eval_path}")


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

    ingest_v1_parser = subparsers.add_parser(
        "ingest-v1",
        help="Build/update richer section-level local Chroma DB",
    )
    add_common(ingest_v1_parser)
    ingest_v1_parser.set_defaults(collection=V1_COLLECTION)
    ingest_v1_parser.add_argument("--xml-url", default=None)
    ingest_v1_parser.add_argument("--manifest-path", type=Path, default=V1_MANIFEST_PATH)
    ingest_v1_parser.add_argument("--batch-size", type=int, default=100)
    ingest_v1_parser.add_argument("--max-resources-per-topic", type=int, default=12)
    ingest_v1_parser.set_defaults(func=ingest_v1)

    test_v1_parser = subparsers.add_parser("test-v1", help="Run v1 retrieval sanity test")
    add_common(test_v1_parser)
    test_v1_parser.set_defaults(collection=V1_COLLECTION)
    test_v1_parser.add_argument("--eval-path", type=Path, default=V1_EVAL_PATH)
    test_v1_parser.add_argument("--n-results", type=int, default=3)
    test_v1_parser.set_defaults(func=test_retrieval_v1)

    compare_parser = subparsers.add_parser("compare", help="Compare v0 and v1 retrieval")
    compare_parser.add_argument("--db-path", type=Path, default=DEFAULT_DB_PATH)
    compare_parser.add_argument("--embed-model", default=DEFAULT_EMBED_MODEL)
    compare_parser.add_argument("--v0-collection", default=DEFAULT_COLLECTION)
    compare_parser.add_argument("--v1-collection", default=V1_COLLECTION)
    compare_parser.add_argument("--eval-path", type=Path, default=COMPARE_EVAL_PATH)
    compare_parser.add_argument("--n-results", type=int, default=3)
    compare_parser.set_defaults(func=compare_retrieval)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
