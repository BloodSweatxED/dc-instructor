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
    "anaphylaxis": ["anaphylaxis", "anaphylactic", "two system reaction"],
    "anticoagulated": ["warfarin", "eliquis", "apixaban", "xarelto", "rivaroxaban", "blood thinner"],
    "antibiotic_prescribed": ["antibiotic prescribed", "started antibiotics", "given antibiotics"],
    "athlete_return_to_play": ["return to play", "same day sports", "athlete", "game today", "practice today"],
    "biphasic_reaction_concern": ["biphasic", "recurrent reaction", "symptoms returned"],
    "chest_pain": ["chest pain", "pressure in chest"],
    "bacterial_infection_suspected": ["bacterial infection", "strep", "pneumonia", "sinusitis"],
    "bite_wound": ["bite wound", "dog bite", "cat bite", "human bite"],
    "c_diff_risk": ["c diff", "c. diff", "recent antibiotics", "clostridioides"],
    "cancer_red_flag": ["cancer", "malignancy", "weight loss", "night sweats"],
    "cauda_equina_concern": ["urinary retention", "bowel incontinence", "saddle anesthesia", "saddle numbness", "groin numbness"],
    "complicated_uti": ["complicated uti", "urinary obstruction", "urologic procedure"],
    "deep_space_location": ["perirectal", "neck abscess", "hand abscess", "deep space", "orbital", "joint"],
    "deep_space_swelling": ["floor of mouth", "neck swelling", "jaw swelling", "facial swelling", "submandibular", "deep space"],
    "diabetic_foot": ["diabetic foot"],
    "dirty_wound": ["dirty wound", "contaminated wound", "soil", "rusty", "crush injury"],
    "drooling": ["drooling", "cannot handle secretions"],
    "elderly_frail": ["frail", "elderly", "nursing home"],
    "elderly": ["elderly", "frail"],
    "fever": ["fever", "febrile", "chills"],
    "flank_pain": ["flank pain", "cva tenderness", "side pain"],
    "fracture_or_trauma_concern": ["fall", "trauma", "crash", "fracture", "midline tenderness"],
    "fracture_seen": ["fracture seen", "broken bone", "ankle fracture", "distal fibula fracture", "distal tibia fracture"],
    "gi_bleeding": ["bloody stool", "black stool", "blood in stool", "vomit blood", "coffee grounds"],
    "hypotension": ["hypotension", "low blood pressure"],
    "hypoxia": ["hypoxic", "low oxygen", "oxygen saturation 90", "spo2 90", "spo2 89"],
    "immunocompromised": ["chemotherapy", "transplant", "immunocompromised", "neutropenia"],
    "indwelling_catheter": ["foley", "catheter"],
    "joint_violation": ["joint violation", "joint capsule", "traumatic arthrotomy", "over joint"],
    "intoxication": ["intoxicated", "etoh"],
    "kidney_transplant": ["kidney transplant", "renal transplant"],
    "loss_of_consciousness": ["loss of consciousness", "loc"],
    "male_patient": ["male patient", "man with uti", "male with uti"],
    "mono_complication_concern": ["mono", "splenomegaly", "left upper quadrant pain"],
    "mucosal_lesions": ["mucosal lesions", "mouth sores", "skin peeling", "target lesions"],
    "near_eye_or_genitals": ["eye", "eyelid", "genital", "scrotum", "vulva"],
    "necrotizing_infection_concern": ["necrotizing", "pain out of proportion", "crepitus", "bullae"],
    "neurovascular_compromise": ["numb foot", "numb toes", "no pulse", "cold foot", "blue toes", "pale toes", "decreased sensation"],
    "no_xray_performed": ["no xray", "no x ray", "no imaging", "xray not done", "x ray not done"],
    "neurologic_deficit": ["weakness", "numbness", "aphasia", "slurred speech", "facial droop"],
    "new_neurologic_deficit": ["new weakness", "leg weakness", "foot drop", "new numbness", "numb leg"],
    "ongoing_pain": ["ongoing pain", "persistent chest pain", "active chest pain"],
    "open_wound": ["open wound", "open fracture", "bone exposed", "laceration over ankle"],
    "open_fracture": ["open fracture", "bone exposed"],
    "packing_required": ["packing", "packed wound", "wick"],
    "peritonsillar_abscess_concern": ["peritonsillar abscess", "uvula deviation", "hot potato voice", "unilateral tonsil"],
    "peritoneal_signs": ["rebound", "guarding", "peritonitis"],
    "poor_follow_up": ["homeless", "unable to follow up", "poor follow up", "no phone"],
    "poor_inhaler_access": ["no inhaler", "lost inhaler", "cannot afford inhaler", "no rescue inhaler", "no access to inhaler"],
    "persistent_vomiting": ["persistent vomiting", "repeated vomiting", "vomiting repeatedly"],
    "pregnancy": ["is pregnant", "patient is pregnant", "pregnancy"],
    "pneumonia": ["pneumonia", "infiltrate", "consolidation"],
    "positive_strep_test": ["positive strep", "strep positive", "positive rapid strep"],
    "rapid_progression": ["rapidly spreading", "rapid progression"],
    "sepsis": ["sepsis", "septic", "shock"],
    "severe_dehydration": ["severe dehydration", "syncope", "very dry", "shock"],
    "epiglottitis_concern": ["epiglottitis", "tripod", "stridor"],
    "spinal_infection_concern": ["ivdu", "injection drug", "epidural abscess", "spinal infection", "fever with back pain"],
    "surgical_abdomen": ["appendicitis", "obstruction", "peritonitis", "surgical abdomen", "localized abdominal pain"],
    "solitary_kidney": ["solitary kidney", "transplant kidney"],
    "trismus": ["trismus", "cannot open mouth"],
    "hand_tendon_risk": ["tendon injury", "cannot extend", "cannot flex", "hand laceration", "finger laceration"],
    "retained_foreign_body": ["foreign body", "glass retained", "splinter retained", "object stuck"],
    "renal_failure": ["renal failure", "kidney failure", "aki", "acute kidney injury", "creatinine elevated"],
    "respiratory_distress": ["respiratory distress", "tripoding", "unable to speak full sentences", "accessory muscle use"],
    "skull_fracture_concern": ["skull fracture", "basilar skull", "periorbital ecchymosis", "csf leak"],
    "uncontrolled_pain": ["uncontrolled pain", "intractable pain"],
    "uncontrolled_vomiting": ["intractable vomiting", "cannot keep down"],
    "unable_to_bear_weight": ["unable to bear weight", "cannot bear weight", "cannot walk at all"],
    "unable_to_tolerate_oral_fluids": ["cannot keep fluids down", "unable to tolerate oral", "failed po challenge"],
    "unable_to_walk": ["unable to walk", "cannot walk", "nonambulatory"],
    "unstable_vitals": ["unstable vitals", "hypotension", "tachycardia", "toxic appearing"],
    "urinary_obstruction": ["urinary obstruction", "obstructing stone", "retention"],
    "unknown_trigger": ["unknown trigger", "unclear trigger", "trigger unclear"],
    "voice_change": ["voice change", "muffled voice", "hoarse voice", "hot potato voice"],
    "vomiting_unable_to_take_meds": ["vomiting", "cannot take pills", "cannot keep meds down"],
    "epinephrine_given": ["epinephrine given", "epi given", "epipen used", "used epipen", "received epinephrine"],
}

NEGATIVE_CONTEXT = ["no ", "denies ", "without "]
NEGATION_PATTERN = re.compile(r"(?:\bno|\bdenies|\bwithout)\s+$")


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
    start = 0
    while True:
        idx = text.find(term, start)
        if idx < 0:
            return False
        window = text[max(0, idx - 16) : idx]
        if NEGATION_PATTERN.search(window) is None:
            return True
        start = idx + len(term)


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
