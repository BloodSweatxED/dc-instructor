#!/usr/bin/env python3
"""
Batch clinician review processor for DC Instructor.

Reads the review queue, answers up to BATCH_SIZE pending questions using RAG,
and writes a markdown summary for review. Progress never stops for the queue —
Codex enqueues and continues; this script handles the answers.

Usage:
    python batch_review.py                              # process next 5 pending
    python batch_review.py --batch-size 3              # process next 3
    python batch_review.py --status                    # show queue status
    python batch_review.py --enqueue "question..."     # add to queue and exit
    python batch_review.py --enqueue "..." --condition "chest pain" --source "session-abc"
"""

from __future__ import annotations

import argparse
import json
import sys
import uuid
from datetime import UTC, datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from clinician_review import load_env, review_question
from ingest_medlineplus import DEFAULT_DB_PATH, DEFAULT_EMBED_MODEL, V1_COLLECTION

QUEUE_PATH = Path("knowledge/review_queue.jsonl")
OUTPUT_DIR = Path("knowledge/review_output")
DEFAULT_BATCH_SIZE = 5
DEFAULT_MODEL = "claude-sonnet-4-6"

CONF_ICON = {"high": "✅", "moderate": "⚠️", "low": "❌"}


def utc_now() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat()


# --- Queue I/O ---

def load_queue() -> list[dict]:
    if not QUEUE_PATH.exists():
        return []
    items = []
    for line in QUEUE_PATH.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            try:
                items.append(json.loads(line))
            except json.JSONDecodeError:
                pass
    return items


def save_queue(items: list[dict]) -> None:
    QUEUE_PATH.parent.mkdir(parents=True, exist_ok=True)
    QUEUE_PATH.write_text(
        "\n".join(json.dumps(item) for item in items) + "\n",
        encoding="utf-8",
    )


def enqueue(question: str, *, condition: str | None = None, context: str | None = None, source: str | None = None) -> str:
    items = load_queue()
    item_id = str(uuid.uuid4())[:8]
    items.append({
        "id": item_id,
        "question": question,
        "condition": condition,
        "context": context,
        "source": source,
        "status": "pending",
        "created_at": utc_now(),
        "answer": None,
        "sources": None,
        "confidence": None,
        "reviewed_at": None,
        "error": None,
    })
    save_queue(items)
    return item_id


# --- Output ---

def next_batch_num(date_str: str) -> int:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    existing = list(OUTPUT_DIR.glob(f"{date_str}_batch*.md"))
    return len(existing) + 1


def format_md(batch_num: int, date_str: str, items: list[dict], results: list[dict]) -> str:
    lines = [
        f"# DC Instructor — Clinician Review Batch {batch_num} ({date_str})",
        "",
        f"**{len(items)} question(s) answered.** Scan each; note any that look wrong.**",
        "",
        "Confidence: ✅ high (strong source match) | ⚠️ moderate | ❌ low (thin/no retrieval — treat as general guidance)",
        "",
        "---",
        "",
    ]

    for i, (item, result) in enumerate(zip(items, results), start=1):
        conf = result.get("confidence", "low")
        icon = CONF_ICON.get(conf, "?")
        lines += [f"## {i}. {item['question']}", ""]
        if item.get("condition"):
            lines.append(f"**Condition:** {item['condition']}  ")
        if item.get("source"):
            lines.append(f"**Source:** {item['source']}  ")
        lines += [
            f"**Confidence:** {icon} {conf}  ",
            f"**Item ID:** `{item['id']}`",
            "",
            "**Answer:**",
            "",
            result.get("answer") or "_No answer generated — see error_",
            "",
        ]
        if result.get("sources"):
            source_lines = [
                f"- [{s['topic']} — {s['section']}]({s['url']})"
                for s in result["sources"][:3]
            ]
            lines += ["**Sources:**", ""] + source_lines + [""]
        if result.get("error"):
            lines += [f"> ⚠️ Error: {result['error']}", ""]
        lines += ["---", ""]

    return "\n".join(lines)


# --- Batch run ---

def run_batch(batch_size: int, model: str) -> None:
    items = load_queue()
    pending = [item for item in items if item.get("status") == "pending"]

    if not pending:
        print("Queue is empty — nothing to process.")
        return

    batch = pending[:batch_size]
    remaining = len(pending) - len(batch)
    print(f"Processing {len(batch)} of {len(pending)} pending items...")

    results = []
    for item in batch:
        print(f"  [{item['id']}] {item['question'][:80]}...")
        try:
            result = review_question(
                item["question"],
                condition=item.get("condition"),
                context=item.get("context"),
                model=model,
            )
            item.update({
                "status": "processed",
                "answer": result["answer"],
                "sources": result["sources"],
                "confidence": result["confidence"],
                "reviewed_at": result["reviewed_at"],
                "error": None,
            })
            results.append(result)
            icon = CONF_ICON.get(result["confidence"], "?")
            print(f"    → {icon} {result['confidence']}")
        except Exception as exc:
            item["status"] = "error"
            item["error"] = str(exc)
            results.append({"answer": None, "confidence": "low", "sources": [], "error": str(exc)})
            print(f"    → ERROR: {exc}", file=sys.stderr)

    save_queue(items)

    date_str = datetime.now(UTC).strftime("%Y-%m-%d")
    batch_num = next_batch_num(date_str)
    output_path = OUTPUT_DIR / f"{date_str}_batch{batch_num:02d}.md"
    output_path.write_text(format_md(batch_num, date_str, batch, results), encoding="utf-8")

    print(f"\nReview output → {output_path}")
    if remaining:
        print(f"{remaining} items still pending — run again to process next batch.")


# --- Status ---

def show_status() -> None:
    items = load_queue()
    if not items:
        print("Queue is empty.")
        return

    by_status: dict[str, list] = {}
    for item in items:
        by_status.setdefault(item.get("status", "unknown"), []).append(item)

    pending = by_status.get("pending", [])
    processed = by_status.get("processed", [])
    errors = by_status.get("error", [])

    print(f"Queue: {len(items)} total | {len(pending)} pending | {len(processed)} processed | {len(errors)} error(s)")
    if pending:
        print("\nNext pending:")
        for item in pending[:5]:
            print(f"  [{item['id']}] {item['question'][:80]}")
    if errors:
        print("\nErrors:")
        for item in errors:
            print(f"  [{item['id']}] {item.get('error', '?')[:80]}")


# --- CLI ---

def main() -> None:
    parser = argparse.ArgumentParser(description="Batch clinician review processor")
    parser.add_argument("--enqueue", "-e", metavar="QUESTION", help="Add question to queue and exit")
    parser.add_argument("--condition", "-c", help="Condition name (used with --enqueue)")
    parser.add_argument("--context", help="Clinical context / ED note (used with --enqueue)")
    parser.add_argument("--source", help="Source label, e.g. Codex session ID (used with --enqueue)")
    parser.add_argument("--batch-size", type=int, default=DEFAULT_BATCH_SIZE, help=f"Items per run (default {DEFAULT_BATCH_SIZE})")
    parser.add_argument("--model", default=DEFAULT_MODEL, help="Anthropic model ID")
    parser.add_argument("--status", action="store_true", help="Show queue status and exit")
    args = parser.parse_args()

    load_env()

    if args.status:
        show_status()
        return

    if args.enqueue:
        item_id = enqueue(
            args.enqueue,
            condition=args.condition,
            context=args.context,
            source=args.source,
        )
        print(f"Enqueued [{item_id}]: {args.enqueue[:80]}")
        return

    run_batch(args.batch_size, args.model)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)
