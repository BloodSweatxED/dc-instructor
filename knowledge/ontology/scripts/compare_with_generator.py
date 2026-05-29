#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from ontology_lib import SECTIONS, assemble_discharge, read_json, ROOT


DEFAULT_CASES = ROOT / "evals" / "ontology_vs_generator_cases.json"
DEFAULT_JSON = ROOT / "evals" / "ontology_vs_generator_latest.json"
DEFAULT_MD = ROOT / "evals" / "ontology_vs_generator_latest.md"


def extract_sections(text: str) -> dict[str, str]:
    headers = [header for _, header in SECTIONS]
    sections: dict[str, list[str]] = {}
    current: str | None = None
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if line in headers:
            current = line
            sections[current] = []
            continue
        if current:
            sections[current].append(raw_line.rstrip())
    return {header: "\n".join(lines).strip() for header, lines in sections.items()}


def section_summary(text: str) -> dict[str, Any]:
    sections = extract_sections(text)
    summary: dict[str, Any] = {}
    for _, header in SECTIONS:
        body = sections.get(header, "")
        bullets = [line for line in body.splitlines() if line.lstrip().startswith("-")]
        summary[header] = {
            "present": bool(body),
            "chars": len(body),
            "bullets": len(bullets),
        }
    return summary


def post_generator(generator_url: str, case: dict[str, Any], timeout: int) -> str:
    payload = {
        "condition": case["condition"],
        "edNoteScrubbed": case.get("ed_note_scrubbed", ""),
        "readingLevel": case.get("reading_level", "6th Grade"),
        "language": case.get("language", "English"),
        "hasImage": False,
    }
    request = urllib.request.Request(
        generator_url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"content-type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        body = response.read().decode("utf-8")

    chunks = []
    for line in body.splitlines():
        if not line.strip():
            continue
        event = json.loads(line)
        if event.get("type") == "chunk":
            chunks.append(event.get("text", ""))
    return "".join(chunks)


def build_review_md(result: dict[str, Any]) -> str:
    lines = [
        "# Ontology vs Current Generator Review",
        "",
        f"Generated: {result['generated_at']}",
        "",
        "Use this file for clinician review. The ontology side is deterministic. The generator side is present only when `--generator-url` was used.",
        "",
    ]
    for case in result["cases"]:
        lines.extend(
            [
                f"## {case['id']}",
                "",
                f"- Phenotype: `{case['phenotype']}`",
                f"- Condition: {case['condition']}",
                f"- Generator called: {case['generator_called']}",
                "",
                "### Section Summary",
                "",
                "| Section | Ontology chars | Ontology bullets | Generator chars | Generator bullets |",
                "| --- | ---: | ---: | ---: | ---: |",
            ]
        )
        for _, header in SECTIONS:
            ontology = case["ontology_summary"][header]
            generator = case.get("generator_summary", {}).get(header, {})
            lines.append(
                "| {section} | {ontology_chars} | {ontology_bullets} | {generator_chars} | {generator_bullets} |".format(
                    section=header,
                    ontology_chars=ontology["chars"],
                    ontology_bullets=ontology["bullets"],
                    generator_chars=generator.get("chars", ""),
                    generator_bullets=generator.get("bullets", ""),
                )
            )
        lines.extend(["", "### Ontology Output", "", "```text", case["ontology_output"].strip(), "```", ""])
        if case.get("generator_output"):
            lines.extend(["### Generator Output", "", "```text", case["generator_output"].strip(), "```", ""])
        elif case.get("generator_error"):
            lines.extend(["### Generator Error", "", "```text", case["generator_error"], "```", ""])
        else:
            lines.extend(["### Generator Output", "", "Not generated in this run.", ""])
    return "\n".join(lines).rstrip() + "\n"


def run(args: argparse.Namespace) -> dict[str, Any]:
    cases = read_json(Path(args.cases))
    results = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "generator_url": args.generator_url,
        "cases": [],
    }

    for case in cases:
        ontology_output = assemble_discharge(case["phenotype"], case.get("ontology_reading_level", "6"))
        item: dict[str, Any] = {
            "id": case["id"],
            "phenotype": case["phenotype"],
            "condition": case["condition"],
            "generator_called": bool(args.generator_url),
            "ontology_output": ontology_output,
            "ontology_summary": section_summary(ontology_output),
        }
        if args.generator_url:
            try:
                generator_output = post_generator(args.generator_url, case, args.timeout)
                item["generator_output"] = generator_output
                item["generator_summary"] = section_summary(generator_output)
            except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, OSError) as exc:
                item["generator_error"] = str(exc)
        results["cases"].append(item)
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description="Compare deterministic ontology output against the current generator.")
    parser.add_argument("--cases", default=str(DEFAULT_CASES), help="Case JSON file.")
    parser.add_argument("--json-out", default=str(DEFAULT_JSON), help="JSON output path.")
    parser.add_argument("--md-out", default=str(DEFAULT_MD), help="Markdown review output path.")
    parser.add_argument(
        "--generator-url",
        default="",
        help="Optional Netlify function URL, such as http://localhost:8888/.netlify/functions/generate. Omit for ontology-only review files.",
    )
    parser.add_argument("--timeout", type=int, default=120, help="Generator request timeout in seconds.")
    args = parser.parse_args()

    result = run(args)
    json_out = Path(args.json_out)
    md_out = Path(args.md_out)
    json_out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    md_out.write_text(build_review_md(result), encoding="utf-8")
    print(f"wrote {json_out}")
    print(f"wrote {md_out}")
    if args.generator_url and any("generator_error" in case for case in result["cases"]):
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
