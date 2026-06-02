#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from ontology_lib import load_phenotypes, load_primitives, load_source_cards, read_json  # noqa: E402


ROOT = Path(__file__).resolve().parents[1]
GRAPH_DIR = ROOT / "graph"
OUTPUT = GRAPH_DIR / "graph_seed.json"
CYTOSCAPE_OUTPUT = GRAPH_DIR / "graph_seed.cyjs.json"
SUMMARY_OUTPUT = GRAPH_DIR / "graph_seed_summary.md"
BATCH_OUTPUTS = [
    ROOT / "evals" / "generator_batch_01_outputs.json",
    ROOT / "evals" / "generator_batch_02_outputs.json",
]
SECTION_HEADERS = {
    "DIAGNOSIS:": "diagnosis",
    "WHAT WE FOUND:": "what_we_found",
    "WHAT TO DO AT HOME:": "home_care",
    "MEDICATIONS:": "medications",
    "RETURN TO ED IF:": "return_precautions",
    "FOLLOW UP:": "follow_up",
    "RESOURCES:": "resources",
}
TOPIC_RULES = {
    "dehydration": ["dehydrat", "urinat", "urine", "keep down", "fluids", "dizzy", "lightheaded"],
    "gi_bleed": ["blood in your stool", "bloody", "black, tarry", "coffee grounds", "vomit blood"],
    "respiratory_distress": ["trouble breathing", "shortness of breath", "blue lips", "wheezing", "oxygen"],
    "neuro_deficit": ["weakness", "numb", "confusion", "seizure", "trouble speaking", "vision changes"],
    "sepsis_or_systemic_infection": ["fever", "chills", "very sick", "confusion", "racing heart"],
    "medication_safety": ["do not take", "avoid", "side effect", "allergic", "blood thinner", "kidney", "liver"],
    "wound_infection": ["redness", "pus", "drainage", "streaking", "swelling", "warm"],
    "anaphylaxis": ["throat", "tongue", "lip", "swelling", "hives", "wheezing", "faint"],
    "cardiac_red_flag": ["chest pain", "pressure", "jaw", "arm", "faint", "palpitations"],
    "pregnancy_modifier": ["pregnant", "pregnancy"],
}


def slug(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "_", value).strip("_")
    return value[:96] or "item"


def add_node(nodes: dict[str, dict[str, Any]], node_id: str, node_type: str, label: str, **props: Any) -> None:
    if node_id in nodes:
        nodes[node_id].update({k: v for k, v in props.items() if v not in (None, "", [])})
        return
    nodes[node_id] = {"id": node_id, "type": node_type, "label": label, **props}


def add_edge(edges: list[dict[str, Any]], source: str, edge_type: str, target: str, **props: Any) -> None:
    item = {"source": source, "type": edge_type, "target": target, **props}
    if item not in edges:
        edges.append(item)


def clean_line(line: str) -> str:
    line = line.strip()
    line = re.sub(r"^#{1,6}\s*", "", line)
    line = re.sub(r"^\*\*(.*?)\*\*$", r"\1", line)
    line = re.sub(r"^\*\*(.*?):\*\*$", r"\1:", line)
    line = re.sub(r"^[\-*•]\s*", "", line)
    return line.strip()


def normalize_header(line: str) -> str | None:
    cleaned = clean_line(line).upper()
    if not cleaned.endswith(":"):
        cleaned = f"{cleaned}:"
    return SECTION_HEADERS.get(cleaned)


def extract_sections(output: str) -> dict[str, list[str]]:
    sections: dict[str, list[str]] = {section_id: [] for section_id in SECTION_HEADERS.values()}
    current: str | None = None
    for raw_line in output.splitlines():
        header = normalize_header(raw_line)
        if header:
            current = header
            continue
        if not current:
            continue
        line = clean_line(raw_line)
        if line:
            sections[current].append(line)
    return sections


def candidate_statements(lines: list[str]) -> list[str]:
    statements: list[str] = []
    for line in lines:
        if len(line) > 220 and ". " in line:
            statements.extend(part.strip() for part in re.split(r"(?<=\.)\s+", line) if part.strip())
        else:
            statements.append(line)
    return [item for item in statements if len(item) >= 12]


def topic_matches(text: str) -> list[str]:
    lowered = text.lower()
    matches = []
    for topic, terms in TOPIC_RULES.items():
        if any(term in lowered for term in terms):
            matches.append(topic)
    return matches


def load_generator_cases() -> list[dict[str, Any]]:
    cases: list[dict[str, Any]] = []
    for path in BATCH_OUTPUTS:
        if not path.exists():
            continue
        data = read_json(path)
        for item in data.get("cases", []):
            item = dict(item)
            item["batch_file"] = str(path.relative_to(ROOT))
            cases.append(item)
    return cases


def build_graph() -> dict[str, Any]:
    phenotypes = load_phenotypes()
    primitives = load_primitives()
    source_cards = load_source_cards()
    generator_cases = load_generator_cases()
    nodes: dict[str, dict[str, Any]] = {}
    edges: list[dict[str, Any]] = []

    for source_id, source in source_cards.items():
        node_id = f"source_card:{source_id}"
        add_node(
            nodes,
            node_id,
            "source_card",
            source["title"],
            source=source["source"],
            url=source["url"],
            use_policy=source["use_policy"],
            source_type=source["source_type"],
        )

    for primitive_id, primitive in primitives.items():
        node_id = f"primitive:{primitive_id}"
        add_node(
            nodes,
            node_id,
            "primitive",
            primitive_id,
            section=primitive["section"],
            primitive_type=primitive["primitive_type"],
            priority=primitive["priority"],
            review_status=primitive["review"]["status"],
        )
        for source_id in primitive["source_card_ids"]:
            add_edge(edges, node_id, "supported_by_source", f"source_card:{source_id}")

    for phenotype_id, phenotype in phenotypes.items():
        node_id = f"phenotype:{phenotype_id}"
        add_node(
            nodes,
            node_id,
            "phenotype",
            phenotype["label"],
            status=phenotype["status"],
            condition_family=phenotype["condition_family"],
            review_status=phenotype["review"]["status"],
        )
        for primitive_id in phenotype["primitive_ids"]:
            add_edge(edges, node_id, "requires_primitive", f"primitive:{primitive_id}")
        for item in phenotype["must_not_miss"]:
            target = f"must_not_miss:{slug(item)}"
            add_node(nodes, target, "must_not_miss", item)
            add_edge(edges, node_id, "has_must_not_miss", target)
        for item in phenotype["exclusion_criteria"]:
            target = f"exclusion:{slug(item)}"
            add_node(nodes, target, "exclusion", item)
            add_edge(edges, node_id, "has_exclusion", target)

    for item in generator_cases:
        case_id = item["id"]
        node_id = f"generator_case:{case_id}"
        output = item.get("output") or ""
        add_node(
            nodes,
            node_id,
            "generator_case",
            case_id,
            condition=item["condition"],
            reading_level=item.get("reading_level"),
            language=item.get("language"),
            output_chars=len(output),
            batch_file=item.get("batch_file"),
        )
        if case_id in phenotypes:
            add_edge(edges, node_id, "drafts_for_existing_phenotype", f"phenotype:{case_id}")
        else:
            candidate = f"phenotype_candidate:{case_id}"
            add_node(nodes, candidate, "phenotype", case_id, status="candidate_from_generator_batch")
            add_edge(edges, node_id, "proposes_candidate_phenotype", candidate)

        sections = extract_sections(output)
        for section_id, lines in sections.items():
            if not lines:
                continue
            section_node = f"generator_section:{case_id}.{section_id}"
            add_node(
                nodes,
                section_node,
                "generator_section",
                f"{case_id} {section_id}",
                case_id=case_id,
                section=section_id,
                line_count=len(lines),
            )
            add_edge(edges, node_id, "has_generated_section", section_node)
            for position, statement in enumerate(candidate_statements(lines), start=1):
                primitive_node = f"candidate_primitive:{case_id}.{section_id}.{position}"
                add_node(
                    nodes,
                    primitive_node,
                    "candidate_primitive",
                    statement[:120],
                    case_id=case_id,
                    section=section_id,
                    text=statement,
                    review_status="unreviewed_generator_candidate",
                )
                add_edge(edges, section_node, "contains_candidate_primitive", primitive_node, order=position)
                for topic in topic_matches(statement):
                    topic_node = f"safety_topic:{topic}"
                    add_node(nodes, topic_node, "safety_topic", topic.replace("_", " "))
                    add_edge(edges, primitive_node, "mentions_safety_topic", topic_node)

    return {
        "generated_at": "deterministic_from_current_ontology_and_generator_batches",
        "node_count": len(nodes),
        "edge_count": len(edges),
        "nodes": sorted(nodes.values(), key=lambda item: (item["type"], item["id"])),
        "edges": sorted(edges, key=lambda item: (item["source"], item["type"], item["target"])),
    }


def cytoscape_export(graph: dict[str, Any]) -> dict[str, Any]:
    elements = []
    for node in graph["nodes"]:
        elements.append({"data": node})
    for idx, edge in enumerate(graph["edges"], start=1):
        elements.append({"data": {"id": f"edge:{idx}", **edge}})
    return {"elements": elements}


def summary_markdown(graph: dict[str, Any]) -> str:
    node_counts: dict[str, int] = {}
    edge_counts: dict[str, int] = {}
    for node in graph["nodes"]:
        node_counts[node["type"]] = node_counts.get(node["type"], 0) + 1
    for edge in graph["edges"]:
        edge_counts[edge["type"]] = edge_counts.get(edge["type"], 0) + 1

    lines = [
        "# DC Instructor Knowledge Graph Seed",
        "",
        f"Generated: {graph['generated_at']}",
        "",
        "## Counts",
        "",
        f"- Nodes: {graph['node_count']}",
        f"- Edges: {graph['edge_count']}",
        "",
        "## Node Types",
        "",
    ]
    for key, value in sorted(node_counts.items()):
        lines.append(f"- `{key}`: {value}")
    lines.extend(["", "## Edge Types", ""])
    for key, value in sorted(edge_counts.items()):
        lines.append(f"- `{key}`: {value}")
    lines.extend(
        [
            "",
            "## Use",
            "",
            "This graph is a review artifact. Use it to find repeated candidate primitives, safety topics, unsupported phenotype candidates, and source-support gaps before promoting text into reviewed ontology primitives.",
            "",
            "Canonical JSON:",
            "",
            "```text",
            "knowledge/ontology/graph/graph_seed.json",
            "```",
            "",
            "Cytoscape-compatible JSON:",
            "",
            "```text",
            "knowledge/ontology/graph/graph_seed.cyjs.json",
            "```",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> int:
    graph = build_graph()
    OUTPUT.write_text(json.dumps(graph, indent=2) + "\n", encoding="utf-8")
    CYTOSCAPE_OUTPUT.write_text(json.dumps(cytoscape_export(graph), indent=2) + "\n", encoding="utf-8")
    SUMMARY_OUTPUT.write_text(summary_markdown(graph), encoding="utf-8")
    print(f"wrote {OUTPUT}")
    print(f"wrote {CYTOSCAPE_OUTPUT}")
    print(f"wrote {SUMMARY_OUTPUT}")
    print(f"nodes: {graph['node_count']}")
    print(f"edges: {graph['edge_count']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
