#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from ontology_lib import ROOT, SECTIONS, load_primitives, read_json  # noqa: E402


HARVEST_DIR = ROOT / "harvest"
GRAPH_PATH = ROOT / "graph" / "graph_seed.json"
BATCH_OUTPUTS = [
    ROOT / "evals" / "generator_batch_01_outputs.json",
    ROOT / "evals" / "generator_batch_02_outputs.json",
]
SECTION_IDS = [section_id for section_id, _ in SECTIONS]
OUTPUT_CANDIDATES = HARVEST_DIR / "primitive_candidates.json"
OUTPUT_CLUSTERS = HARVEST_DIR / "primitive_clusters.json"
OUTPUT_REVIEW = HARVEST_DIR / "primitive_review.md"
OUTPUT_GAPS = HARVEST_DIR / "source_gaps.md"


FLAG_RULES = {
    "medication_dosing": [
        r"\b\d+\s?(mg|mcg|g|ml|units?)\b",
        r"\bevery\s+\d+\s*(hours?|hrs?)\b",
        r"\b\d+\s*(times|x)\s+(a|per)\s+day\b",
    ],
    "unsupported_diagnosis_certainty": [
        r"\bthis is\b",
        r"\bthis was\b",
        r"\byou have\b",
        r"\byou do not have\b",
    ],
    "negative_imaging_claim": [
        r"\bx-?ray (showed|was|did not|does not)\b",
        r"\bct (showed|was|did not|does not)\b",
        r"\bultrasound (showed|was|did not|does not)\b",
        r"\bno (fracture|pneumonia|bleeding|blood clot)\b",
    ],
    "exact_follow_up_interval": [
        r"\bwithin\s+\d+[\-\s]?\d*\s+(days?|weeks?)\b",
        r"\bin\s+\d+[\-\s]?\d*\s+(days?|weeks?)\b",
        r"\b\d+[\-\s]?\d*\s+(days?|weeks?)\b",
    ],
    "return_to_work_claim": [
        r"\bwork\b",
        r"\bschool\b",
        r"\bstrenuous activity\b",
        r"\bheavy exercise\b",
    ],
    "source_needed": [
        r"\bantibiotic\b",
        r"\bsteroid\b",
        r"\bepipen\b",
        r"\bfollow-up\b",
        r"\brepeat\b",
        r"\bcleared completely\b",
    ],
}

SAFETY_TOPICS = {
    "dehydration": ["dehydrat", "urine", "urinated", "keep down", "dizzy", "lightheaded"],
    "respiratory_distress": ["shortness of breath", "trouble breathing", "blue", "wheezing"],
    "neurologic_red_flag": ["weakness", "numb", "confusion", "seizure", "speech", "vision"],
    "cardiac_red_flag": ["chest pain", "pressure", "jaw", "arm", "faint", "palpitations"],
    "infection_progression": ["fever", "pus", "redness", "swelling", "streaking", "worse"],
    "anaphylaxis": ["throat", "tongue", "lip", "hives", "wheezing", "faint"],
    "medication_safety": ["side effect", "blood thinner", "kidney", "liver", "allergic", "avoid"],
    "pregnancy_modifier": ["pregnant", "pregnancy"],
}


@dataclass
class Candidate:
    id: str
    section: str
    text: str
    case_id: str
    source_file: str
    repeat_count: int
    flags: list[str]
    safety_topics: list[str]
    source_audit: dict[str, bool]


def clean_line(line: str) -> str:
    line = re.sub(r"^#{1,6}\s*", "", line.strip())
    line = re.sub(r"^\*\*(.*?)\*\*$", r"\1", line)
    line = re.sub(r"^\*\*(.*?):\*\*$", r"\1:", line)
    line = re.sub(r"^[\-*•]\s*", "", line)
    return line.strip()


def normalize(text: str) -> str:
    text = text.lower()
    text = re.sub(r"\b\d+\b", "#", text)
    text = re.sub(r"[^a-z0-9#]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def short_slug(text: str) -> str:
    value = re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")
    return value[:72] or "candidate"


def flag_text(text: str) -> list[str]:
    lowered = text.lower()
    flags: list[str] = []
    for name, patterns in FLAG_RULES.items():
        if any(re.search(pattern, lowered) for pattern in patterns):
            flags.append(name)
    return sorted(flags)


def topic_links(text: str) -> list[str]:
    lowered = text.lower()
    return sorted(topic for topic, terms in SAFETY_TOPICS.items() if any(term in lowered for term in terms))


def source_audit_for(flags: list[str], safety_topics: list[str], text: str) -> dict[str, bool]:
    lowered = text.lower()
    source_needed = bool(flags) or bool(safety_topics)
    restricted_source_risk = "wikem" in lowered or "uptodate" in lowered or "epocrates" in lowered
    clinician_judgment_only = any(flag in flags for flag in ["negative_imaging_claim", "return_to_work_claim"])
    unsafe_without_modifier = any(
        flag in flags
        for flag in ["medication_dosing", "unsupported_diagnosis_certainty", "negative_imaging_claim", "exact_follow_up_interval"]
    )
    return {
        "source_supported": False,
        "source_needed": source_needed,
        "clinician_judgment_only": clinician_judgment_only,
        "restricted_source_risk": restricted_source_risk,
        "unsafe_without_modifier": unsafe_without_modifier,
    }


def extract_batch_candidates() -> list[dict[str, str]]:
    section_headers = {header: section_id for section_id, header in SECTIONS}
    rows: list[dict[str, str]] = []
    for path in BATCH_OUTPUTS:
        data = read_json(path)
        for case in data.get("cases", []):
            current: str | None = None
            for raw_line in (case.get("output") or "").splitlines():
                cleaned = clean_line(raw_line)
                upper = cleaned.upper()
                if not upper.endswith(":"):
                    upper = f"{upper}:"
                if upper in section_headers:
                    current = section_headers[upper]
                    continue
                if current and len(cleaned) >= 12:
                    statements = re.split(r"(?<=\.)\s+", cleaned) if len(cleaned) > 220 else [cleaned]
                    for statement in statements:
                        statement = statement.strip()
                        if len(statement) >= 12:
                            rows.append(
                                {
                                    "section": current,
                                    "text": statement,
                                    "case_id": case["id"],
                                    "source_file": str(path.relative_to(ROOT)),
                                }
                            )
    return rows


def graph_candidate_rows() -> list[dict[str, str]]:
    if not GRAPH_PATH.exists():
        return []
    graph = read_json(GRAPH_PATH)
    rows: list[dict[str, str]] = []
    for node in graph.get("nodes", []):
        if node.get("type") != "candidate_primitive":
            continue
        rows.append(
            {
                "section": node.get("section", "unknown"),
                "text": node.get("text", ""),
                "case_id": node.get("case_id", ""),
                "source_file": "graph/graph_seed.json",
            }
        )
    return rows


def build_candidates() -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    existing_text = {normalize(item["text"]["en_6"]): primitive_id for primitive_id, item in load_primitives().items()}
    raw_rows = graph_candidate_rows() or extract_batch_candidates()
    repeat_counter: dict[str, int] = defaultdict(int)
    for row in raw_rows:
        repeat_counter[f"{row['section']}::{normalize(row['text'])}"] += 1

    candidates: list[Candidate] = []
    seen: set[str] = set()
    for row in raw_rows:
        key = f"{row['section']}::{normalize(row['text'])}"
        if key in seen:
            continue
        seen.add(key)
        flags = flag_text(row["text"])
        safety_topics = topic_links(row["text"])
        normalized = normalize(row["text"])
        audit = source_audit_for(flags, safety_topics, row["text"])
        if normalized in existing_text:
            audit["source_supported"] = True
            audit["source_needed"] = False
        candidate_id = f"{row['section']}.{short_slug(row['text'])}"
        candidates.append(
            Candidate(
                id=candidate_id,
                section=row["section"],
                text=row["text"],
                case_id=row["case_id"],
                source_file=row["source_file"],
                repeat_count=repeat_counter[key],
                flags=flags,
                safety_topics=safety_topics,
                source_audit=audit,
            )
        )

    candidates.sort(key=lambda item: (SECTION_IDS.index(item.section) if item.section in SECTION_IDS else 99, -item.repeat_count, item.id))

    clusters_by_section: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for section in SECTION_IDS:
        section_items = [item for item in candidates if item.section == section]
        topic_groups: dict[str, list[Candidate]] = defaultdict(list)
        for item in section_items:
            cluster_key = item.safety_topics[0] if item.safety_topics else item.flags[0] if item.flags else "general"
            topic_groups[cluster_key].append(item)
        for cluster_key, items in sorted(topic_groups.items()):
            clusters_by_section[section].append(
                {
                    "cluster_id": f"{section}.{cluster_key}",
                    "section": section,
                    "rank": sum(item.repeat_count for item in items),
                    "candidate_count": len(items),
                    "safety_topics": sorted({topic for item in items for topic in item.safety_topics}),
                    "flags": sorted({flag for item in items for flag in item.flags}),
                    "representative_text": items[0].text,
                    "candidate_ids": [item.id for item in items],
                }
            )

    return [item.__dict__ for item in candidates], [cluster for section in SECTION_IDS for cluster in clusters_by_section[section]]


def review_markdown(candidates: list[dict[str, Any]], clusters: list[dict[str, Any]]) -> str:
    lines = [
        "# Primitive Candidate Review",
        "",
        "Status: harvest artifact only. No candidate is promoted to reviewed ontology text by this file.",
        "",
        "## Highest Repeats And Risks",
        "",
    ]
    risky = sorted(candidates, key=lambda item: (-item["repeat_count"], len(item["flags"]) * -1, item["id"]))[:60]
    for item in risky:
        flags = ", ".join(item["flags"]) or "none"
        topics = ", ".join(item["safety_topics"]) or "none"
        lines.append(f"- `{item['section']}` x{item['repeat_count']} [{flags}] [{topics}] {item['text']}")
    lines.extend(["", "## Clusters By Section", ""])
    for section in SECTION_IDS:
        lines.append(f"### {section}")
        section_clusters = [cluster for cluster in clusters if cluster["section"] == section]
        for cluster in sorted(section_clusters, key=lambda item: (-item["rank"], item["cluster_id"])):
            lines.append(
                f"- `{cluster['cluster_id']}` rank {cluster['rank']}: {cluster['representative_text']}"
            )
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def gaps_markdown(candidates: list[dict[str, Any]]) -> str:
    lines = [
        "# Source Gaps",
        "",
        "These candidate primitives need source support, clinician judgment boundaries, or unsafe-modifier handling before promotion.",
        "",
    ]
    for section in SECTION_IDS:
        section_items = [
            item
            for item in candidates
            if item["section"] == section and any(item["source_audit"].values())
        ]
        if not section_items:
            continue
        lines.append(f"## {section}")
        for item in sorted(section_items, key=lambda row: (-row["repeat_count"], row["id"]))[:40]:
            audit = ", ".join(key for key, value in item["source_audit"].items() if value) or "none"
            lines.append(f"- `{item['id']}` x{item['repeat_count']} audit: {audit}. Text: {item['text']}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    HARVEST_DIR.mkdir(parents=True, exist_ok=True)
    candidates, clusters = build_candidates()
    OUTPUT_CANDIDATES.write_text(json.dumps(candidates, indent=2) + "\n", encoding="utf-8")
    OUTPUT_CLUSTERS.write_text(json.dumps(clusters, indent=2) + "\n", encoding="utf-8")
    OUTPUT_REVIEW.write_text(review_markdown(candidates, clusters), encoding="utf-8")
    OUTPUT_GAPS.write_text(gaps_markdown(candidates), encoding="utf-8")
    print(f"wrote {OUTPUT_CANDIDATES}")
    print(f"wrote {OUTPUT_CLUSTERS}")
    print(f"wrote {OUTPUT_REVIEW}")
    print(f"wrote {OUTPUT_GAPS}")
    print(f"candidates: {len(candidates)}")
    print(f"clusters: {len(clusters)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
