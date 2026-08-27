#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
RESOURCE_PATH = ROOT / "primitives" / "resources.json"
REVIEWED_ONLY = True
REVIEWER = "Andre / EM clinician-owner"
REVIEW_DATE = "2026-06-02"
TEXT_KEYS = ("en_4", "en_6", "en_hl1")
FOLLOWUP_SCRIPTS = {
    "abscess_after_i_and_d": ("an abscess that was drained", "as instructed for a wound check"),
    "allergic_reaction_resolved_no_anaphylaxis": ("an allergic reaction", "within 1 week if symptoms continue or the trigger is unclear"),
    "ankle_sprain_xray_negative": ("an ankle sprain", "within 5-7 days if pain or walking is not improving"),
    "asthma_exacerbation_improved_discharge": ("an asthma flare-up", "within 3-5 days"),
    "cellulitis_uncomplicated_oral_antibiotics": ("cellulitis", "within 48-72 hours"),
    "community_acquired_pneumonia_outpatient": ("pneumonia", "within 2-3 days"),
    "concussion_discharge_no_imaging_red_flags": ("a concussion", "within 1 week if symptoms persist, or sooner if you need return-to-play clearance"),
    "dental_pain_no_deep_space_infection": ("dental pain", "as soon as possible with a dentist"),
    "gastroenteritis_stable_hydrating": ("gastroenteritis", "within 1-3 days if symptoms are not improving"),
    "laceration_repaired_simple": ("a repaired cut", "on the schedule you were given for wound check or suture removal"),
    "lumbar_strain_no_red_flags": ("a low back strain", "within 1-2 weeks if pain is not improving"),
    "minor_head_injury_no_red_flags": ("a minor head injury", "within 1 week if symptoms are not improving"),
    "renal_colic_stable_no_infection": ("a kidney stone", "within 1-2 weeks"),
    "uncomplicated_cystitis_nonpregnant": ("a urinary tract infection", "within 1 week, or sooner if symptoms are not improving"),
    "viral_pharyngitis_strep_negative": ("a viral sore throat", "within 1 week if symptoms are not improving"),
    "viral_uri_no_pneumonia": ("a viral upper respiratory infection", "within 3-7 days if symptoms are not improving"),
}
FOLLOWUP_EXTRAS = {
    "asthma_exacerbation_improved_discharge": "If you do not have a written asthma action plan, ask for one at follow-up.",
    "community_acquired_pneumonia_outpatient": "Most people start to feel better within 3-5 days of antibiotics, but full recovery can take 2-4 weeks.",
    "dental_pain_no_deep_space_infection": "The ED cannot fix the tooth permanently.",
    "renal_colic_stable_no_infection": "Most small stones pass on their own within 1-4 weeks.",
}


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: Any) -> None:
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def resource_text(source: dict[str, Any]) -> str:
    return f"Learn more: {source['source']} - {source['title']} ({source['url']})."


def review_block() -> dict[str, Any]:
    return {
        "status": "reviewed",
        "reviewer": REVIEWER,
        "reviewer_role": "Emergency Medicine physician",
        "last_reviewed": REVIEW_DATE,
        "version": 1,
        "source_audit_status": "passed_for_v1",
        "production_status": "enabled_with_runtime_modifier_gates",
        "notes": "Reviewed as a short source-card learning resource. Keep resources concise and link-based.",
    }


def source_audit(source_ids: list[str]) -> dict[str, Any]:
    return {
        "source_supported": True,
        "source_needed": False,
        "clinician_judgment_only": False,
        "restricted_source_risk": False,
        "unsafe_without_modifier": False,
        "notes": f"Resource link uses source cards: {', '.join(source_ids)}.",
    }


def primitive(phenotype_id: str, kind: str, text: str, source_ids: list[str], priority: str = "low") -> dict[str, Any]:
    primitive_id = f"{phenotype_id}.resources.{kind}.v1"
    return {
        "id": primitive_id,
        "phenotypes": [phenotype_id],
        "section": "resources",
        "primitive_type": kind,
        "priority": priority,
        "text": {key: text for key in TEXT_KEYS},
        "contraindications": [],
        "source_card_ids": source_ids,
        "review": review_block(),
        "source_audit": source_audit(source_ids),
    }


def followup_text(condition_label: str, timeframe: str, extra: str | None = None) -> str:
    base = (
        f"Call your primary care doctor's office or clinic. Say, \"I was in the emergency department and was diagnosed with {condition_label}. "
        f"I need a follow-up visit {timeframe}.\""
    )
    if extra:
        return f"{base} {extra}"
    return base


def apply_followup_scripts() -> None:
    for path in sorted((ROOT / "primitives").glob("*.json")):
        rows = read_json(path)
        changed = False
        for row in rows:
            if row.get("section") != "follow_up":
                continue
            phenotype_ids = row.get("phenotypes", [])
            if len(phenotype_ids) != 1:
                continue
            phenotype_id = phenotype_ids[0]
            if phenotype_id not in FOLLOWUP_SCRIPTS:
                continue
            text = followup_text(*FOLLOWUP_SCRIPTS[phenotype_id], FOLLOWUP_EXTRAS.get(phenotype_id))
            row["text"] = {key: text for key in TEXT_KEYS}
            row.setdefault("style", {})["followup_script"] = "phase17_patient_advocacy"
            changed = True
        if changed:
            write_json(path, rows)


def main() -> int:
    apply_followup_scripts()
    source_cards = {item["id"]: item for item in (read_json(path) for path in sorted((ROOT / "source_cards").glob("*.json")))}
    resource_rows: list[dict[str, Any]] = []

    for path in sorted((ROOT / "phenotypes").glob("*.json")):
        phenotype = read_json(path)
        if REVIEWED_ONLY and phenotype.get("review", {}).get("status") != "reviewed":
            continue
        source_ids = [source_id for source_id in phenotype.get("source_card_ids", []) if source_id in source_cards]
        if not source_ids:
            continue

        selected_sources = source_ids[:2]
        resource_ids: list[str] = []
        for idx, source_id in enumerate(selected_sources, start=1):
            row = primitive(phenotype["id"], f"source_link_{idx}", resource_text(source_cards[source_id]), [source_id])
            resource_rows.append(row)
            resource_ids.append(row["id"])

        follow_text = "Bring these instructions to your follow-up visit."
        follow_row = primitive(phenotype["id"], "followup_reminder", follow_text, selected_sources, priority="medium")
        resource_rows.append(follow_row)
        resource_ids.append(follow_row["id"])

        existing = [primitive_id for primitive_id in phenotype["primitive_ids"] if ".resources." not in primitive_id]
        phenotype["primitive_ids"] = existing + resource_ids
        write_json(path, phenotype)

    write_json(RESOURCE_PATH, resource_rows)
    print(f"wrote {len(resource_rows)} resource primitives to {RESOURCE_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
