#!/usr/bin/env python3
"""
Clinician review automation for DC Instructor.

Retrieves MedlinePlus context for a clinical question and returns a grounded answer
via the Anthropic API. Used standalone or called by batch_review.py.

Usage:
    python clinician_review.py "When should a patient return to the ED for chest pain?"
    python clinician_review.py --question "..." --condition "chest pain" --context "ED note..."
    python clinician_review.py --question "..." --json
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import UTC, datetime
from pathlib import Path

import requests
from dotenv import load_dotenv

sys.path.insert(0, str(Path(__file__).parent))
from ingest_medlineplus import (
    DEFAULT_DB_PATH,
    DEFAULT_EMBED_MODEL,
    V1_COLLECTION,
    get_collection,
    intent_adjusted_distance,
)

ANTHROPIC_URL = "https://api.anthropic.com/v1/messages"
DEFAULT_MODEL = "claude-sonnet-4-6"
LOW_CONFIDENCE_THRESHOLD = 0.55

SYSTEM = """You are a board-certified Emergency Medicine clinician answering a specific clinical question to improve patient discharge instructions.

Use the retrieved MedlinePlus context and standard EM practice. If retrieved context is thin or off-topic, say so and give conservative standard guidance — do not fabricate specifics. Be concise and actionable. Write at a clinician level (not patient level). Begin directly with the answer."""


def load_env() -> None:
    for candidate in [Path(".env"), Path(__file__).parent.parent / ".env"]:
        if candidate.exists():
            load_dotenv(candidate)
            return


def retrieve(query: str, db_path: Path, collection: str, embed_model: str, top_k: int) -> list[dict]:
    try:
        col = get_collection(db_path, collection, embed_model)
    except Exception:
        return []

    count = col.count()
    if count == 0:
        return []

    n_results = min(max(top_k * 8, 24), count)
    results = col.query(query_texts=[query], n_results=n_results)
    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]
    distances = results.get("distances", [[]])[0]

    rows = []
    for doc, meta, dist in zip(documents, metadatas, distances):
        text = doc.split("\n\n", 1)[-1]
        row = {
            "topic": meta["topic"],
            "section": meta["section"],
            "section_type": meta.get("section_type"),
            "resource_title": meta.get("resource_title"),
            "url": meta["url"],
            "distance": dist,
            "text": text,
        }
        row["adjusted_distance"] = intent_adjusted_distance(query, row)
        rows.append(row)

    rows.sort(key=lambda r: (r["adjusted_distance"], r["distance"]))

    deduped, seen = [], set()
    for row in rows:
        key = (row["url"], row["section"], row["text"][:80])
        if key in seen:
            continue
        seen.add(key)
        deduped.append(row)
        if len(deduped) == top_k:
            break

    return [{**r, "rank": i + 1} for i, r in enumerate(deduped)]


def build_prompt(question: str, condition: str | None, context: str | None, sources: list[dict]) -> str:
    parts = [f"QUESTION:\n{question}"]
    if condition:
        parts.append(f"CONDITION:\n{condition}")
    if context:
        parts.append(f"CLINICAL CONTEXT:\n{context}")

    if sources:
        blocks = []
        for s in sources:
            section_label = s.get("section_type") or s["section"]
            blocks.append(
                f"[SOURCE {s['rank']}]\nTopic: {s['topic']}\nSection: {section_label}\n"
                f"URL: {s['url']}\nText: {s['text']}"
            )
        parts.append("RETRIEVED MEDLINEPLUS CONTEXT:\n" + "\n\n".join(blocks))
    else:
        parts.append(
            "RETRIEVED CONTEXT:\nNo relevant MedlinePlus context found. "
            "Use conservative standard EM guidance and note the limitation."
        )

    return "\n\n".join(parts)


def call_api(api_key: str, model: str, prompt: str, max_tokens: int) -> str:
    resp = requests.post(
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
            "system": SYSTEM,
            "messages": [{"role": "user", "content": prompt}],
        },
    )
    if not resp.ok:
        raise RuntimeError(f"Anthropic {resp.status_code}: {resp.text[:400]}")
    payload = resp.json()
    return "".join(
        item.get("text", "") for item in payload.get("content", []) if item.get("type") == "text"
    ).strip()


def review_question(
    question: str,
    *,
    condition: str | None = None,
    context: str | None = None,
    db_path: Path = DEFAULT_DB_PATH,
    collection: str = V1_COLLECTION,
    embed_model: str = DEFAULT_EMBED_MODEL,
    model: str = DEFAULT_MODEL,
    top_k: int = 5,
    max_tokens: int = 800,
    api_key: str | None = None,
) -> dict:
    load_env()
    api_key = api_key or os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key:
        raise RuntimeError("ANTHROPIC_API_KEY required — set in .env or environment")

    sources = retrieve(question, db_path, collection, embed_model, top_k)

    avg_dist = sum(s["adjusted_distance"] for s in sources) / len(sources) if sources else 1.0
    if not sources:
        confidence = "low"
    elif avg_dist > LOW_CONFIDENCE_THRESHOLD:
        confidence = "low"
    elif avg_dist > 0.38:
        confidence = "moderate"
    else:
        confidence = "high"

    prompt = build_prompt(question, condition, context, sources)
    answer = call_api(api_key, model, prompt, max_tokens)

    return {
        "question": question,
        "condition": condition,
        "answer": answer,
        "confidence": confidence,
        "avg_distance": round(avg_dist, 4),
        "sources": [
            {
                "rank": s["rank"],
                "topic": s["topic"],
                "section": s.get("section_type") or s["section"],
                "url": s["url"],
            }
            for s in sources
        ],
        "model": model,
        "reviewed_at": datetime.now(UTC).replace(microsecond=0).isoformat(),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Answer a clinical question using RAG + Anthropic API")
    parser.add_argument("question", nargs="?", help="Clinical question (positional)")
    parser.add_argument("--question", "-q", dest="question_flag", help="Clinical question (flag)")
    parser.add_argument("--condition", "-c", help="Condition name for context")
    parser.add_argument("--context", help="ED note or clinical context")
    parser.add_argument("--model", default=DEFAULT_MODEL, help="Anthropic model ID")
    parser.add_argument("--top-k", type=int, default=5, help="Retrieval top-k chunks")
    parser.add_argument("--json", action="store_true", dest="output_json", help="Output JSON")
    args = parser.parse_args()

    question = args.question or args.question_flag
    if not question:
        parser.error("Question required (positional or --question)")

    result = review_question(
        question,
        condition=args.condition,
        context=args.context,
        model=args.model,
        top_k=args.top_k,
    )

    if args.output_json:
        print(json.dumps(result, indent=2))
    else:
        conf_icon = {"high": "✅", "moderate": "⚠️", "low": "❌"}.get(result["confidence"], "?")
        print(f"\nQ: {result['question']}")
        print(f"Confidence: {conf_icon} {result['confidence']} (avg_dist={result['avg_distance']})")
        if result["sources"]:
            topics = ", ".join(dict.fromkeys(s["topic"] for s in result["sources"][:3]))
            print(f"Sources: {topics}")
        print(f"\nA: {result['answer']}\n")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)
