#!/usr/bin/env python3
"""
Local RAG smoke test for DC Instructor.

Retrieves MedlinePlus v1 chunks, builds a grounded discharge-instruction prompt,
and optionally calls Anthropic using ANTHROPIC_API_KEY from the environment or
repo .env file.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import requests
from dotenv import load_dotenv

from ingest_medlineplus import (
    DEFAULT_DB_PATH,
    DEFAULT_EMBED_MODEL,
    V1_COLLECTION,
    get_collection,
    intent_adjusted_distance,
)


DEFAULT_OUTPUT_PATH = Path("knowledge/evals/rag_smoke_backpain_v1.json")
ANTHROPIC_URL = "https://api.anthropic.com/v1/messages"
DEFAULT_MODEL = "claude-sonnet-4-5"


@dataclass(frozen=True)
class SmokeCase:
    id: str
    condition: str
    reading_level: str
    language: str
    ed_note: str
    retrieval_query: str


SMOKE_CASES = [
    SmokeCase(
        id="lumbar_strain",
        condition="lumbar strain",
        reading_level="6th Grade",
        language="English",
        ed_note=(
            "Adult with atraumatic low back pain after lifting boxes. Normal lower-extremity "
            "strength and sensation. No fever. No bowel or bladder symptoms. No saddle anesthesia. "
            "Able to walk. Treated with ibuprofen and acetaminophen."
        ),
        retrieval_query="lumbar strain low back pain home care activity medicine return precautions",
    ),
    SmokeCase(
        id="sciatica",
        condition="sciatica",
        reading_level="6th Grade",
        language="English",
        ed_note=(
            "Adult with low back pain radiating down the right leg. Positive straight leg raise. "
            "No weakness. No urinary retention. No fever. Discharged with NSAID plan and PCP follow-up."
        ),
        retrieval_query="sciatica discharge instructions numbness weakness home care return precautions",
    ),
    SmokeCase(
        id="atraumatic_back_pain",
        condition="atraumatic low back pain",
        reading_level="4th Grade",
        language="English",
        ed_note=(
            "Adult with two days of lower back pain. No trauma. No neurologic deficits. No red flags. "
            "Vitals normal. No imaging indicated today."
        ),
        retrieval_query="atraumatic acute low back pain discharge instructions home care return precautions",
    ),
    SmokeCase(
        id="back_pain_red_flags",
        condition="back pain with return precautions",
        reading_level="6th Grade",
        language="English",
        ed_note=(
            "Adult evaluated for back pain. Exam reassuring today. Needs clear return precautions for "
            "weakness, numbness, fever, trauma, bowel or bladder changes, and worsening pain."
        ),
        retrieval_query="back pain red flags bowel bladder weakness fever trauma return precautions",
    ),
    SmokeCase(
        id="neck_strain",
        condition="neck strain",
        reading_level="6th Grade",
        language="English",
        ed_note=(
            "Adult with neck pain after sleeping awkwardly. No trauma. No arm weakness or numbness. "
            "Full range of motion with discomfort. Discharged with conservative care."
        ),
        retrieval_query="neck strain neck spasm home care conservative treatment return precautions",
    ),
    SmokeCase(
        id="ankle_sprain",
        condition="ankle sprain",
        reading_level="6th Grade",
        language="English",
        ed_note=(
            "Adult twisted ankle while walking. X-ray negative for fracture. Mild swelling. "
            "Neurovascularly intact. Discharged with brace, rest, ice, elevation, and PCP follow-up."
        ),
        retrieval_query="ankle sprain aftercare RICE rest ice elevation follow up return precautions",
    ),
    SmokeCase(
        id="herniated_disk",
        condition="herniated disk",
        reading_level="8th Grade",
        language="English",
        ed_note=(
            "Adult with known herniated disk and recurrent back pain. No new weakness. No bowel or "
            "bladder symptoms. Pain improved with medication. Outpatient follow-up advised."
        ),
        retrieval_query="herniated disk discharge instructions home care follow up weakness bowel bladder precautions",
    ),
    SmokeCase(
        id="chronic_back_flare",
        condition="chronic low back pain flare",
        reading_level="6th Grade",
        language="English",
        ed_note=(
            "Adult with flare of chronic low back pain. No trauma. No fever. No neurologic deficits. "
            "Discussed activity as tolerated, heat, NSAIDs if safe, and outpatient follow-up."
        ),
        retrieval_query="chronic low back pain flare activity heat medicine home care follow up",
    ),
    SmokeCase(
        id="return_to_work",
        condition="return to work after back pain",
        reading_level="6th Grade",
        language="English",
        ed_note=(
            "Adult with improving back pain asking when to return to work. Job involves lifting. "
            "Exam reassuring. Needs lifting precautions and gradual return guidance."
        ),
        retrieval_query="return to work after back pain lifting precautions gradual activity home care",
    ),
    SmokeCase(
        id="heat_vs_ice",
        condition="heat versus ice for back pain",
        reading_level="4th Grade",
        language="English",
        ed_note=(
            "Adult with acute low back pain and no red flags. Asked whether to use ice or heat at home."
        ),
        retrieval_query="acute low back pain ice heat home care instructions",
    ),
]


def utc_now_iso() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat()


def strip_retrieval_context(document: str) -> str:
    return document.split("\n\n", 1)[-1]


def retrieve_context(
    *,
    query: str,
    db_path: Path,
    collection_name: str,
    embed_model: str,
    top_k: int,
) -> list[dict[str, Any]]:
    collection = get_collection(db_path, collection_name, embed_model)
    if collection.count() == 0:
        raise RuntimeError(f"Collection {collection_name!r} is empty. Run ingest-v1 first.")

    candidate_count = max(top_k * 8, 24)
    results = collection.query(query_texts=[query], n_results=candidate_count)
    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]
    distances = results.get("distances", [[]])[0]

    rows: list[dict[str, Any]] = []
    for document, metadata, distance in zip(documents, metadatas, distances, strict=False):
        source_text = strip_retrieval_context(document)
        row = {
            "topic": metadata["topic"],
            "section": metadata["section"],
            "section_type": metadata.get("section_type"),
            "resource_title": metadata.get("resource_title"),
            "url": metadata["url"],
            "fk_grade": metadata["fk_grade"],
            "reading_level": metadata["reading_level"],
            "distance": distance,
            "text": source_text,
            "preview": source_text[:260],
        }
        row["adjusted_distance"] = intent_adjusted_distance(query, row)
        rows.append(row)

    rows.sort(key=lambda item: (item["adjusted_distance"], item["distance"]))
    deduped = []
    seen = set()
    for row in rows:
        key = (row["url"], row["section"], row["preview"][:80])
        if key in seen:
            continue
        seen.add(key)
        deduped.append(row)
        if len(deduped) == top_k:
            break

    return [{**row, "rank": rank} for rank, row in enumerate(deduped, start=1)]


def build_user_prompt(case: SmokeCase, sources: list[dict[str, Any]]) -> str:
    source_blocks = []
    for source in sources:
        source_blocks.append(
            "\n".join(
                [
                    f"[SOURCE {source['rank']}]",
                    f"Topic: {source['topic']}",
                    f"Resource: {source.get('resource_title') or source['section']}",
                    f"Section type: {source.get('section_type') or source['section']}",
                    f"URL: {source['url']}",
                    f"Text: {source['text']}",
                ]
            )
        )

    return f"""CONDITION:
{case.condition}

READING LEVEL:
{case.reading_level}

LANGUAGE:
{case.language}

ED NOTE CONTEXT, PHI REDACTED:
{case.ed_note}

RETRIEVED MEDLINEPLUS CONTEXT:
{chr(10).join(source_blocks)}

Write patient discharge instructions using the retrieved context as grounding. Do not quote sources verbatim unless the wording is ordinary medical phrasing. Do not invent facts not supported by the ED note or retrieved context."""


def system_prompt() -> str:
    return """You are a board-certified Emergency Medicine clinician writing discharge instructions for a patient you evaluated.

Use only the ED note context and retrieved MedlinePlus context as grounding. If the retrieved context is incomplete, write conservative general instructions and avoid unsupported details.

Output plain text only. Do not use Markdown. Do not use # headings. Do not use bold text. Begin directly with DIAGNOSIS:.

Output exactly these section headers, in this exact order:

DIAGNOSIS:
WHAT WE FOUND:
WHAT TO DO AT HOME:
MEDICATIONS:
RETURN TO ED IF:
FOLLOW UP:

Rules:
- Write directly to the patient using "you".
- Keep the language at the requested reading level.
- Include concrete return precautions.
- Do not mention vector databases, retrieval, RAG, or internal source IDs in the patient-facing output.
- Do not include a preamble or closing note."""


def load_environment() -> None:
    repo_env = Path(".env")
    if repo_env.exists():
        load_dotenv(repo_env)


def call_anthropic(*, api_key: str, model: str, user_prompt: str, max_tokens: int) -> str:
    response = requests.post(
        ANTHROPIC_URL,
        timeout=90,
        headers={
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json",
        },
        json={
            "model": model,
            "max_tokens": max_tokens,
            "system": system_prompt(),
            "messages": [{"role": "user", "content": user_prompt}],
        },
    )
    if not response.ok:
        raise RuntimeError(f"Anthropic error {response.status_code}: {response.text[:500]}")

    payload = response.json()
    return "".join(
        item.get("text", "")
        for item in payload.get("content", [])
        if item.get("type") == "text"
    ).strip()


def selected_cases(args: argparse.Namespace) -> list[SmokeCase]:
    if args.all:
        return SMOKE_CASES
    if args.case:
        case_by_id = {case.id: case for case in SMOKE_CASES}
        missing = [case_id for case_id in args.case if case_id not in case_by_id]
        if missing:
            raise RuntimeError(f"Unknown smoke case id: {', '.join(missing)}")
        return [case_by_id[case_id] for case_id in args.case]
    return [SMOKE_CASES[0]]


def run(args: argparse.Namespace) -> None:
    load_environment()
    cases = selected_cases(args)
    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    should_generate = not args.no_generate
    if should_generate and not api_key:
        raise RuntimeError("ANTHROPIC_API_KEY missing. Use --no-generate for retrieval-only smoke tests.")

    run_rows = {
        "tested_at": utc_now_iso(),
        "collection": args.collection,
        "db_path": str(args.db_path),
        "embedding_model": args.embed_model,
        "generation_model": args.model if should_generate else None,
        "generated": should_generate,
        "cases": [],
    }

    for case in cases:
        sources = retrieve_context(
            query=case.retrieval_query,
            db_path=args.db_path,
            collection_name=args.collection,
            embed_model=args.embed_model,
            top_k=args.top_k,
        )
        prompt = build_user_prompt(case, sources)
        output = None
        if should_generate:
            output = call_anthropic(
                api_key=api_key,
                model=args.model,
                user_prompt=prompt,
                max_tokens=args.max_tokens,
            )

        print(f"\n=== {case.id}: {case.condition} ===")
        for source in sources:
            print(
                f"[{source['rank']}] {source['topic']} | {source.get('section_type') or source['section']} "
                f"| {source.get('resource_title') or source['section']} | {source['url']}"
            )
        if output:
            print("\n" + output[:1800])

        run_rows["cases"].append(
            {
                "id": case.id,
                "condition": case.condition,
                "reading_level": case.reading_level,
                "language": case.language,
                "ed_note": case.ed_note,
                "retrieval_query": case.retrieval_query,
                "sources": sources,
                "prompt": prompt if args.include_prompts else None,
                "output": output,
            }
        )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(run_rows, indent=2) + "\n", encoding="utf-8")
    print(f"\nSmoke test output: {args.output}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run local DC Instructor RAG smoke tests")
    parser.add_argument("--db-path", type=Path, default=DEFAULT_DB_PATH)
    parser.add_argument("--collection", default=V1_COLLECTION)
    parser.add_argument("--embed-model", default=DEFAULT_EMBED_MODEL)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT_PATH)
    parser.add_argument("--top-k", type=int, default=5)
    parser.add_argument("--max-tokens", type=int, default=2200)
    parser.add_argument("--case", action="append", help="Smoke case id. Can be repeated.")
    parser.add_argument("--all", action="store_true", help="Run all smoke cases.")
    parser.add_argument("--no-generate", action="store_true", help="Retrieve and write prompts only.")
    parser.add_argument("--include-prompts", action="store_true", help="Include full prompts in output JSON.")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    run(args)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise
