#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

from ontology_lib import ROOT, load_phenotypes, read_json


MANIFEST_PATH = ROOT / "runtime" / "ontology_manifest.json"

EXCLUSION_RULES = {
    "airway_symptoms": ["trouble breathing", "throat swelling", "tongue swelling", "drooling", "stridor"],
    "abnormal_ecg": ["st elevation", "new ischemia", "abnormal ecg"],
    "abnormal_troponin": ["positive troponin", "elevated troponin"],
    "anticoagulated": ["warfarin", "eliquis", "apixaban", "xarelto", "rivaroxaban", "blood thinner"],
    "chest_pain": ["chest pain", "pressure in chest"],
    "deep_space_location": ["perirectal", "neck abscess", "hand abscess", "deep space"],
    "diabetic_foot": ["diabetic foot"],
    "elderly": ["elderly", "frail"],
    "fever": ["fever", "febrile", "chills"],
    "fracture_seen": ["fracture seen", "broken bone", "ankle fracture", "distal fibula fracture", "distal tibia fracture"],
    "hypotension": ["hypotension", "low blood pressure"],
    "hypoxia": ["hypoxic", "low oxygen", "oxygen saturation 90", "spo2 90", "spo2 89"],
    "immunocompromised": ["chemotherapy", "transplant", "immunocompromised", "neutropenia"],
    "intoxication": ["intoxicated", "etoh"],
    "loss_of_consciousness": ["loss of consciousness", "loc"],
    "near_eye_or_genitals": ["eye", "eyelid", "genital", "scrotum", "vulva"],
    "neurovascular_compromise": ["numb foot", "numb toes", "no pulse", "cold foot", "blue toes", "pale toes", "decreased sensation"],
    "no_xray_performed": ["no xray", "no x ray", "no imaging", "xray not done", "x ray not done"],
    "neurologic_deficit": ["weakness", "numbness", "aphasia", "slurred speech", "facial droop"],
    "ongoing_pain": ["ongoing pain", "persistent chest pain", "active chest pain"],
    "open_wound": ["open wound", "open fracture", "bone exposed", "laceration over ankle"],
    "peritoneal_signs": ["rebound", "guarding", "peritonitis"],
    "poor_follow_up": ["homeless", "unable to follow up", "no phone"],
    "pregnancy": ["pregnant", "pregnancy"],
    "rapid_progression": ["rapidly spreading", "rapid progression"],
    "sepsis": ["sepsis", "septic", "shock"],
    "solitary_kidney": ["solitary kidney", "transplant kidney"],
    "trismus": ["trismus", "cannot open mouth"],
    "uncontrolled_pain": ["uncontrolled pain", "intractable pain"],
    "uncontrolled_vomiting": ["intractable vomiting", "cannot keep down"],
    "unable_to_bear_weight": ["unable to bear weight", "cannot bear weight", "cannot walk at all"],
}

NEGATIVE_CONTEXT = ["no ", "denies ", "without "]


def norm(text: str) -> str:
    text = re.sub(r"[_-]+", " ", text.lower())
    return re.sub(r"\s+", " ", text).strip()


def term_score(text: str, terms: list[str]) -> tuple[float, list[str]]:
    matched = []
    for term in terms:
        normalized_term = norm(term)
        if normalized_term in text:
            matched.append(normalized_term)
    if not terms:
        return 0.0, matched
    return len(matched) / len(terms), matched


def has_non_negated(text: str, term: str) -> bool:
    idx = text.find(term)
    if idx < 0:
        return False
    window = text[max(0, idx - 16) : idx]
    return not any(marker in window for marker in NEGATIVE_CONTEXT)


def modifier_hits(text: str, unsafe_modifiers: list[str]) -> list[str]:
    hits = []
    for modifier in unsafe_modifiers:
        terms = EXCLUSION_RULES.get(modifier, [modifier.replace("_", " ")])
        if any(has_non_negated(text, term) for term in terms):
            hits.append(modifier)
    return sorted(set(hits))


def classify(condition: str, ed_note: str = "") -> dict[str, Any]:
    manifest = read_json(MANIFEST_PATH) if MANIFEST_PATH.exists() else {"phenotypes": []}
    text = norm(f"{condition} {ed_note}")
    scored = []
    for phenotype in manifest.get("phenotypes", []):
        score, matched = term_score(text, phenotype.get("condition_terms", []))
        if score <= 0:
            continue
        exclusions = modifier_hits(text, phenotype.get("unsafe_modifiers", []))
        exact_terms = {norm(phenotype["id"]), norm(phenotype["label"])}
        exact_match = any(term in text for term in exact_terms)
        base_confidence = 0.93 if exact_match else 0.55 + (0.35 * score)
        confidence = min(0.98, base_confidence - (0.15 if exclusions else 0.0))
        scored.append((confidence, phenotype, matched, exclusions))

    if not scored:
        return {
            "phenotype_id": None,
            "confidence": 0.0,
            "exclusions": [],
            "modifiers": [],
            "fallback_reason": "no_supported_phenotype_match",
        }

    confidence, phenotype, matched, exclusions = sorted(scored, key=lambda row: row[0], reverse=True)[0]
    fallback_reason = None
    if exclusions:
        fallback_reason = "unsafe_modifier_present"
    elif phenotype.get("status") != "reviewed" or phenotype.get("review_status") != "reviewed":
        fallback_reason = "phenotype_not_clinician_reviewed"
    elif phenotype.get("source_audit", {}).get("source_needed"):
        fallback_reason = "source_audit_not_passed"
    elif confidence < 0.86:
        fallback_reason = "low_confidence"

    return {
        "phenotype_id": phenotype["id"],
        "confidence": round(confidence, 3),
        "exclusions": exclusions,
        "modifiers": matched,
        "fallback_reason": fallback_reason,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Classify a condition into a draft ontology phenotype.")
    parser.add_argument("--condition", required=True)
    parser.add_argument("--ed-note", default="", help="Optional scrubbed note context. Not written to disk.")
    args = parser.parse_args()
    print(json.dumps(classify(args.condition, args.ed_note), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
