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


ANTHROPIC_URL = "https://api.anthropic.com/v1/messages"
DEFAULT_MODEL = "claude-sonnet-4-5"
PROMPT_VERSION = "backpain_rag_prompt_v3"
RETRIEVAL_VERSION = "backpain_retrieval_v3"
CURRENT_OUTPUT_PATH = Path("knowledge/evals/rag_smoke_backpain_v3.json")


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


def case_terms(case: SmokeCase) -> str:
    return f"{case.id} {case.condition} {case.retrieval_query}".lower()


def case_adjusted_distance(case: SmokeCase, row: dict[str, Any]) -> float:
    adjusted = intent_adjusted_distance(case.retrieval_query, row)
    terms = case_terms(case)
    text = row["text"].lower()
    topic = row["topic"].lower()
    title = (row.get("resource_title") or "").lower()
    section_type = row.get("section_type") or ""

    if "sciatica" in terms:
        if topic == "sciatica" or "sciatica" in title:
            adjusted -= 0.18
        if "back pain - returning to work" in title:
            adjusted += 0.40
        if "piriformis syndrome" in title:
            adjusted += 0.08
        if any(term in text for term in ["urinate", "blood in your urine", "redness or swelling"]):
            adjusted += 0.10

    if "neck_strain" in terms or "neck strain" in terms:
        if topic == "neck injuries and disorders":
            adjusted -= 0.16
        if "cervical spondylosis" in title:
            adjusted += 0.18
        if any(term in text for term in ["chest pain", "shortness of breath", "difficulty swallowing"]):
            adjusted += 0.12

    if "ankle_sprain" in terms:
        if "ankle sprain" in title:
            adjusted -= 0.22
        elif "foot sprain" in title:
            adjusted += 0.05
        else:
            adjusted += 0.35

    if "return_to_work" in terms:
        if "returning to work" in title:
            adjusted -= 0.24
        if section_type == "when_to_seek_care":
            adjusted += 0.18

    if "herniated" in terms:
        if topic == "herniated disk" or "herniated disk" in title:
            adjusted -= 0.16
        if section_type == "self_care":
            adjusted -= 0.08
        if "sacroiliac joint" in title or "returning to work" in title:
            adjusted += 0.18

    if "chronic_back_flare" in terms:
        if "low back pain - chronic" in title:
            adjusted -= 0.18
        if section_type == "self_care":
            adjusted -= 0.08
        if "sacroiliac joint" in title:
            adjusted += 0.08
        if "returning to work" in title:
            adjusted += 0.16

    if "heat_vs_ice" in terms:
        if "low back pain - acute" in title:
            adjusted -= 0.20
        if "heat" in text and "ice" in text:
            adjusted -= 0.18
        if "sacroiliac joint" in title:
            adjusted += 0.24

    if "atraumatic_back_pain" in terms or "lumbar_strain" in terms:
        if "low back pain - acute" in title:
            adjusted -= 0.28
        if "taking care of your back at home" in title:
            adjusted -= 0.20
        if "sacroiliac joint" in title:
            adjusted += 0.24
        if "returning to work" in title:
            adjusted += 0.16

    if "back_pain_red_flags" in terms:
        if "low back pain - acute" in title:
            adjusted -= 0.18
        if topic == "spine injuries and disorders":
            adjusted += 0.10

    return adjusted


def allowed_topics_for(case: SmokeCase) -> set[str]:
    terms = case_terms(case)
    if "sciatica" in terms:
        return {"Sciatica"}
    if "neck_strain" in terms or "neck strain" in terms:
        return {"Neck Injuries and Disorders"}
    if "ankle_sprain" in terms:
        return {"Sprains and Strains"}
    if "herniated" in terms:
        return {"Herniated Disk", "Back Pain"}
    if "lumbar_strain" in terms or "atraumatic_back_pain" in terms or "heat_vs_ice" in terms:
        return {"Back Pain"}
    return {"Back Pain", "Sciatica", "Herniated Disk", "Spine Injuries and Disorders"}


def is_compatible_source(case: SmokeCase, row: dict[str, Any]) -> bool:
    terms = case_terms(case)
    title = (row.get("resource_title") or "").lower()

    if "ankle_sprain" in terms:
        return any(term in title for term in ["ankle sprain", "foot sprain"])

    if "heat_vs_ice" in terms:
        return any(
            term in title
            for term in [
                "low back pain - acute",
                "sacroiliac joint pain",
                "taking care of your back",
            ]
        )

    if "lumbar_strain" in terms:
        return any(
            term in title
            for term in [
                "low back pain - acute",
                "taking care of your back at home",
                "back pain - when you see the doctor",
            ]
        )

    if "atraumatic_back_pain" in terms:
        return any(
            term in title
            for term in [
                "low back pain - acute",
                "taking care of your back at home",
                "back pain - when you see the doctor",
            ]
        )

    if "chronic_back_flare" in terms:
        return not any(term in title for term in ["returning to work"])

    if "herniated" in terms:
        return not any(term in title for term in ["sacroiliac joint pain"])

    return True


def required_section_types(case: SmokeCase) -> list[str]:
    terms = case_terms(case)
    required = []
    if any(term in terms for term in ["home", "aftercare", "activity", "heat", "ice", "return to work"]):
        required.append("self_care")
    if any(term in terms for term in ["return precautions", "red flags", "weakness", "bowel", "bladder"]):
        required.append("when_to_seek_care")
    if "return_to_work" in terms:
        required = ["self_care"]
    return required


def select_diverse_sources(
    rows: list[dict[str, Any]],
    *,
    case: SmokeCase,
    top_k: int,
) -> list[dict[str, Any]]:
    selected: list[dict[str, Any]] = []
    seen_chunks: set[tuple[str, str, str]] = set()
    url_counts: dict[str, int] = {}
    max_per_url = 2

    def can_add(row: dict[str, Any]) -> bool:
        key = (row["url"], row["section"], row["preview"][:80])
        if key in seen_chunks:
            return False
        if url_counts.get(row["url"], 0) >= max_per_url:
            return False
        return True

    def add(row: dict[str, Any]) -> None:
        key = (row["url"], row["section"], row["preview"][:80])
        seen_chunks.add(key)
        url_counts[row["url"]] = url_counts.get(row["url"], 0) + 1
        selected.append(row)

    for section_type in required_section_types(case):
        match = next(
            (
                row
                for row in rows
                if row.get("section_type") == section_type and can_add(row)
            ),
            None,
        )
        if match:
            add(match)

    for row in rows:
        if len(selected) == top_k:
            break
        if can_add(row):
            add(row)

    return [{**row, "rank": rank} for rank, row in enumerate(selected, start=1)]


def retrieve_context(
    *,
    case: SmokeCase,
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
    allowed_topics = allowed_topics_for(case)
    for document, metadata, distance in zip(documents, metadatas, distances, strict=False):
        if metadata["topic"] not in allowed_topics:
            continue
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
        row["adjusted_distance"] = case_adjusted_distance(case, row)
        if not is_compatible_source(case, row):
            continue
        rows.append(row)

    rows.sort(key=lambda item: (item["adjusted_distance"], item["distance"]))
    return select_diverse_sources(rows, case=case, top_k=top_k)


def case_specific_prompt_rules(case: SmokeCase) -> str:
    terms = case_terms(case)
    rules = [
        "Do not turn every MedlinePlus provider-contact item into an ED return precaution.",
        "Separate emergency return advice from routine follow-up advice.",
        "Do not mention sedating medication precautions unless the ED note says a sedating medication was prescribed or given.",
        "Do not include exact numeric medication doses unless the ED note provides them.",
        "Do not say a medication is safe for most people. Use safety-specific wording instead.",
    ]

    if case.reading_level.startswith("4th"):
        rules.extend(
            [
                "Use very short sentences.",
                "Prefer plain words like pee, poop, bottom, and private area when clinically acceptable.",
                "Avoid words like neurologic, incontinence, saddle anesthesia, and radiculopathy.",
            ]
        )

    if "sciatica" in terms:
        rules.extend(
            [
                "For sciatica, ED return precautions should focus on new weakness, numbness in the groin or buttocks, trouble controlling pee or poop, fever, inability to walk, or severe worsening pain.",
                "Do not list burning with urination, blood in urine, back redness, night pain, or unexplained weight loss as ED return triggers unless the ED note supports them.",
            ]
        )

    if "neck_strain" in terms or "neck strain" in terms:
        rules.extend(
            [
                "For atraumatic neck strain after sleeping awkwardly, avoid alarm-heavy cardiopulmonary, swallowing, or breathing precautions unless the ED note supports them.",
                "Focus ED return precautions on new arm weakness or numbness, fever with severe stiff neck, major trauma, severe worsening pain, or trouble walking.",
            ]
        )

    if "return_to_work" in terms:
        rules.extend(
            [
                "Give practical lifting precautions and gradual return guidance.",
                "Do not tell the patient to negotiate medical restrictions directly with a boss. Say to follow the work note or discuss restrictions with their clinician.",
            ]
        )

    if "heat_vs_ice" in terms:
        rules.append("Answer the heat-versus-ice question directly before adding general back-pain advice.")

    if "lumbar_strain" in terms:
        rules.extend(
            [
                "For lumbar strain home care, include practical first-line advice: stay gently active, avoid bed rest, avoid heavy lifting or twisting for a few days, use ice for the first 1 to 2 days, try heat after that if it helps, and use pillow positioning for sleep comfort.",
                "Do not recommend chiropractic care, massage therapy, acupuncture, injections, or specialist care in WHAT TO DO AT HOME for uncomplicated lumbar strain.",
                "Mention physical therapy only in FOLLOW UP if pain is not improving or lasts several weeks.",
            ]
        )

    if "atraumatic_back_pain" in terms:
        rules.append("For uncomplicated atraumatic low back pain, favor concrete home care over referrals: gentle activity, short walks, ice then heat, sleep positioning, and avoiding heavy lifting briefly.")

    if any(
        term in terms
        for term in ["lumbar_strain", "atraumatic_back_pain", "heat_vs_ice"]
    ):
        rules.extend(
            [
                "For routine low back pain with a reassuring ED exam, ED return precautions should focus on new weakness, numbness in the groin or buttocks, trouble controlling pee or poop, fever, major trauma, inability to walk, or severe worsening pain.",
                "Do not list burning with urination, blood in urine, night pain, redness, or unexplained weight loss as ED return triggers unless the ED note supports them.",
            ]
        )

    if any(term in terms for term in ["atraumatic_back_pain", "heat_vs_ice", "sciatica"]):
        rules.extend(
            [
                "If suggesting ibuprofen, naproxen, or another NSAID, include a short safety warning about kidney disease, stomach ulcers or bleeding, blood thinners, and being told to avoid NSAIDs.",
                "Mention acetaminophen as a separate option when appropriate.",
            ]
        )

    return "\n".join(f"- {rule}" for rule in rules)


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

CASE-SPECIFIC RULES:
{case_specific_prompt_rules(case)}

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
- Keep routine musculoskeletal return precautions focused. Prefer 5 to 7 high-yield ED return triggers unless the case is specifically a red-flag teaching case.
- Do not promote routine primary-care follow-up symptoms into emergency department return symptoms.
- In MEDICATIONS, name common OTC options when the ED note supports them. Keep NSAID cautions short and concrete.
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
        "prompt_version": PROMPT_VERSION,
        "retrieval_version": RETRIEVAL_VERSION,
        "generated": should_generate,
        "cases": [],
    }

    for case in cases:
        sources = retrieve_context(
            case=case,
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
                "prompt_version": PROMPT_VERSION,
                "retrieval_version": RETRIEVAL_VERSION,
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
    parser.add_argument("--output", type=Path, default=CURRENT_OUTPUT_PATH)
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
