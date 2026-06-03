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
    "age_over_50_new_headache": ["new headache over 50", "age over 50", "older than 50 with new headache"],
    "anaphylaxis": ["anaphylaxis", "anaphylactic", "two system reaction"],
    "anticoagulated": ["warfarin", "eliquis", "apixaban", "xarelto", "rivaroxaban", "blood thinner"],
    "antibiotic_prescribed": ["antibiotic prescribed", "started antibiotics", "given antibiotics"],
    "antibiotic_prescribed_for_suspected_bacterial_infection": [
        "antibiotic prescribed for suspected bacterial infection",
        "antibiotics prescribed for bacterial infection",
        "started antibiotics for bacterial infection",
        "amoxicillin for bacterial bronchitis",
        "azithromycin for bacterial bronchitis",
        "bacterial bronchitis",
    ],
    "antibiotic_prescribed_for_sinusitis": [
        "antibiotic prescribed for sinusitis",
        "antibiotics prescribed for sinusitis",
        "amoxicillin for sinusitis",
        "amoxicillin clavulanate for sinusitis",
        "augmentin for sinusitis",
        "doxycycline for sinusitis",
    ],
    "athlete_return_to_play": ["return to play", "same day sports", "athlete", "game today", "practice today"],
    "biphasic_reaction_concern": ["biphasic", "recurrent reaction", "symptoms returned"],
    "chest_pain": ["chest pain", "pressure in chest"],
    "cardiac_or_pe_chest_pain_concern": [
        "cardiac chest pain",
        "pe concern",
        "pulmonary embolism concern",
        "pleuritic chest pain with pe concern",
        "acs concern",
        "acute coronary syndrome concern",
    ],
    "bacterial_infection_suspected": ["bacterial infection", "strep", "pneumonia", "sinusitis"],
    "bite_wound": ["bite wound", "dog bite", "cat bite", "human bite"],
    "bleeding_disorder": ["bleeding disorder", "hemophilia", "thrombocytopenia", "low platelets"],
    "c_diff_risk": ["c diff", "c. diff", "recent antibiotics", "clostridioides"],
    "cancer_red_flag": ["cancer", "malignancy", "weight loss", "night sweats"],
    "cauda_equina_concern": ["urinary retention", "bowel incontinence", "saddle anesthesia", "saddle numbness", "groin numbness"],
    "complicated_uti": ["complicated uti", "urinary obstruction", "urologic procedure"],
    "chronic_or_recurrent_sinusitis": [
        "chronic sinusitis",
        "recurrent sinusitis",
        "months of sinus symptoms",
        "multiple sinus infections this year",
    ],
    "contact_lens_use": ["contact lens", "contacts", "contact lenses"],
    "copd_or_asthma_exacerbation_pathway": [
        "copd exacerbation",
        "asthma exacerbation",
        "asthma flare",
        "wheezing requiring bronchodilators",
        "treated as asthma",
        "treated as copd",
    ],
    "deep_space_location": ["perirectal", "neck abscess", "hand abscess", "deep space", "orbital", "joint"],
    "deep_space_swelling": ["floor of mouth", "neck swelling", "jaw swelling", "facial swelling", "submandibular", "deep space"],
    "dental_or_facial_trauma_source": ["dental source", "tooth abscess", "facial trauma", "orbital fracture", "facial fracture"],
    "acute_glaucoma_mimic": ["acute glaucoma", "angle closure", "halos around lights", "fixed pupil", "mid dilated pupil"],
    "chemical_eye_exposure": ["chemical splash", "chemical exposure", "chemical burn", "acid in eye", "alkali in eye"],
    "corneal_ulcer_or_keratitis_concern": ["corneal ulcer", "keratitis", "corneal infiltrate", "white spot on cornea"],
    "eye_trauma_or_foreign_body": ["eye trauma", "foreign body", "metal in eye", "scratched eye", "corneal abrasion", "chemical splash"],
    "diabetic_foot": ["diabetic foot"],
    "dirty_wound": ["dirty wound", "contaminated wound", "soil", "rusty", "crush injury"],
    "drooling": ["drooling", "cannot handle secretions"],
    "elderly_frail": ["frail", "elderly", "nursing home"],
    "elderly": ["elderly", "frail"],
    "fever": ["fever", "febrile", "chills"],
    "flank_pain": ["flank pain", "cva tenderness", "side pain"],
    "focal_lung_findings_or_infiltrate": [
        "focal crackles",
        "focal rales",
        "focal lung findings",
        "localized crackles",
        "right lower lobe infiltrate",
        "left lower lobe infiltrate",
        "infiltrate",
        "consolidation",
    ],
    "fracture_or_trauma_concern": ["fall", "trauma", "crash", "fracture", "midline tenderness", "head trauma within 7 days"],
    "fracture_seen": ["fracture seen", "broken bone", "ankle fracture", "distal fibula fracture", "distal tibia fracture"],
    "facial_or_nasal_trauma": ["facial trauma", "nasal trauma", "nose injury", "hit in nose", "nasal fracture"],
    "gi_bleeding": ["bloody stool", "black stool", "blood in stool", "vomit blood", "coffee grounds"],
    "hemoptysis": ["coughing blood", "hemoptysis"],
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
    "meningitis_or_cns_infection_concern": ["meningitis", "stiff neck", "neck stiffness", "fever with headache", "encephalitis"],
    "mucosal_lesions": ["mucosal lesions", "mouth sores", "skin peeling", "target lesions"],
    "herpes_or_zoster_eye_concern": ["herpes eye", "zoster eye", "shingles near eye", "vesicles near eye", "dendritic lesion"],
    "near_eye_or_genitals": ["eye", "eyelid", "genital", "scrotum", "vulva"],
    "orbital_or_intracranial_sinusitis_concern": [
        "orbital cellulitis",
        "eye swelling",
        "swelling around the eye",
        "pain with eye movement",
        "vision change",
        "double vision",
        "confusion",
        "altered mental status",
        "meningitis",
        "severe headache with neurologic",
    ],
    "necrotizing_infection_concern": ["necrotizing", "pain out of proportion", "crepitus", "bullae"],
    "neurovascular_compromise": ["numb foot", "numb toes", "no pulse", "cold foot", "blue toes", "pale toes", "decreased sensation"],
    "no_xray_performed": ["no xray", "no x ray", "no imaging", "xray not done", "x ray not done"],
    "neurologic_deficit": ["weakness", "numbness", "aphasia", "slurred speech", "facial droop"],
    "new_neurologic_deficit": ["new weakness", "leg weakness", "foot drop", "new numbness", "numb leg"],
    "ongoing_pain": ["ongoing pain", "persistent chest pain", "active chest pain"],
    "open_wound": ["open wound", "open fracture", "bone exposed", "laceration over ankle"],
    "open_fracture": ["open fracture", "bone exposed"],
    "posterior_epistaxis_or_uncontrolled_bleeding": [
        "posterior epistaxis",
        "posterior nosebleed",
        "bleeding down throat",
        "continued bleeding",
        "bleeding would not stop",
        "uncontrolled nosebleed",
        "nasal packing",
        "rhino rocket",
    ],
    "packing_required": ["packing", "packed wound", "wick"],
    "peritonsillar_abscess_concern": ["peritonsillar abscess", "uvula deviation", "hot potato voice", "unilateral tonsil"],
    "periorbital_or_orbital_cellulitis_concern": ["periorbital cellulitis", "orbital cellulitis", "eyelid swelling", "pain with eye movement", "proptosis"],
    "photophobia": ["photophobia", "light sensitivity"],
    "peritoneal_signs": ["rebound", "guarding", "peritonitis"],
    "poor_follow_up": ["homeless", "unable to follow up", "poor follow up", "no phone"],
    "poor_inhaler_access": ["no inhaler", "lost inhaler", "cannot afford inhaler", "no rescue inhaler", "no access to inhaler"],
    "persistent_vomiting": ["persistent vomiting", "repeated vomiting", "vomiting repeatedly"],
    "pregnancy": ["is pregnant", "patient is pregnant", "pregnancy"],
    "pneumonia": ["pneumonia", "infiltrate", "consolidation"],
    "positive_strep_test": ["positive strep", "strep positive", "positive rapid strep"],
    "rapid_progression": ["rapidly spreading", "rapid progression"],
    "severe_eye_pain": ["severe eye pain", "significant eye pain", "deep eye pain"],
    "sepsis": ["sepsis", "septic", "shock"],
    "severe_dehydration": ["severe dehydration", "syncope", "very dry", "shock"],
    "severe_bacterial_sinusitis_features": [
        "fever 102",
        "fever 103",
        "high fever",
        "severe facial pain",
        "purulent nasal discharge for 4 days",
        "symptoms over 10 days",
        "symptoms for 10 days",
        "worsening after initial improvement",
        "double worsening",
    ],
    "epiglottitis_concern": ["epiglottitis", "tripod", "stridor"],
    "spinal_infection_concern": ["ivdu", "injection drug", "epidural abscess", "spinal infection", "fever with back pain"],
    "surgical_abdomen": ["appendicitis", "obstruction", "peritonitis", "surgical abdomen", "localized abdominal pain"],
    "solitary_kidney": ["solitary kidney", "transplant kidney"],
    "trismus": ["trismus", "cannot open mouth"],
    "hand_tendon_risk": ["tendon injury", "cannot extend", "cannot flex", "hand laceration", "finger laceration"],
    "mastoiditis_or_deep_ear_infection_concern": ["mastoiditis", "mastoid tenderness", "redness behind ear", "swelling behind ear", "protruding ear"],
    "malignant_otitis_externa_risk": ["malignant otitis externa", "diabetes", "diabetic", "immunocompromised", "skull base osteomyelitis"],
    "retained_foreign_body": ["foreign body", "glass retained", "splinter retained", "object stuck"],
    "ear_trauma_or_foreign_body": ["ear trauma", "foreign body in ear", "object in ear", "button battery", "cotton swab injury"],
    "tympanic_membrane_perforation_or_tube": ["perforated eardrum", "eardrum perforation", "ear tube", "tympanostomy tube"],
    "facial_weakness_or_neurologic_ear_sign": ["facial weakness", "facial droop", "cranial nerve deficit", "vertigo", "severe dizziness"],
    "acute_hearing_loss": ["sudden hearing loss", "acute hearing loss", "new hearing loss"],
    "renal_failure": ["renal failure", "kidney failure", "aki", "acute kidney injury", "creatinine elevated"],
    "respiratory_distress": ["respiratory distress", "tripoding", "unable to speak full sentences", "accessory muscle use"],
    "skull_fracture_concern": ["skull fracture", "basilar skull", "periorbital ecchymosis", "csf leak"],
    "syncope": ["syncope", "fainting", "passed out", "near syncope"],
    "altered_mental_status_not_resolved": [
        "altered mental status not fully resolved",
        "ams not resolved",
        "confusion not resolved",
        "persistent confusion",
    ],
    "ct_not_performed_with_headache_concern": [
        "ct not performed with documented concern",
        "ct not done with documented concern",
        "no ct with documented concern",
        "ct deferred despite concern",
    ],
    "first_lifetime_severe_headache": [
        "first lifetime headache",
        "first headache of this severity",
        "first headache this severe",
        "first severe headache",
    ],
    "thunderclap_or_sah_concern": [
        "thunderclap",
        "sudden severe headache reaches worst within seconds",
        "worst headache",
        "worst headache of life",
        "subarachnoid",
        "sah concern",
    ],
    "uncontrolled_pain": ["uncontrolled pain", "intractable pain"],
    "uncontrolled_vomiting": ["intractable vomiting", "cannot keep down"],
    "unable_to_bear_weight": ["unable to bear weight", "cannot bear weight", "cannot walk at all"],
    "unable_to_tolerate_oral_fluids": ["cannot keep fluids down", "unable to tolerate oral", "failed po challenge"],
    "unable_to_walk": ["unable to walk", "cannot walk", "nonambulatory"],
    "unstable_vitals": ["unstable vitals", "hypotension", "tachycardia", "toxic appearing"],
    "urinary_obstruction": ["urinary obstruction", "obstructing stone", "retention"],
    "unknown_trigger": ["unknown trigger", "unclear trigger", "trigger unclear"],
    "voice_change": ["voice change", "muffled voice", "hoarse voice", "hot potato voice"],
    "vision_change": ["vision change", "blurred vision", "vision loss", "decreased vision", "double vision"],
    "vomiting_unable_to_take_meds": ["vomiting", "cannot take pills", "cannot keep meds down"],
    "epinephrine_given": ["epinephrine given", "epi given", "epipen used", "used epipen", "received epinephrine"],
}

NEGATIVE_CONTEXT = ["no ", "denies ", "without "]
NEGATION_PATTERN = re.compile(r"(?:\bno|\bdenies|\bwithout)\s+$")
DIAGNOSTIC_NEGATION_PREFIX = re.compile(
    r"(?:\bno|\bdenies|\bwithout|\bruled out|\bnot consistent with)\s+(?:\w+\s+){0,4}$"
)
DIAGNOSTIC_NEGATION_SUFFIX = re.compile(
    r"^\s*(?:diagnosis|phenotype|documented|confirmed|suspected|evaluation)?\s*"
    r"(?:ruled out|not documented|not confirmed|not the final diagnosis|not final diagnosis)\b"
)


def norm(text: str) -> str:
    text = re.sub(r"[_-]+", " ", text.lower())
    return re.sub(r"\s+", " ", text).strip()


def term_score(text: str, terms: list[str]) -> tuple[float, list[str]]:
    matched = []
    for term in terms:
        normalized_term = norm(term)
        if has_affirmed_condition_term(text, normalized_term):
            matched.append(normalized_term)
    if not terms:
        return 0.0, matched
    return len(matched) / len(terms), matched


def has_affirmed_condition_term(text: str, term: str) -> bool:
    start = 0
    while True:
        idx = text.find(term, start)
        if idx < 0:
            return False
        before = text[max(0, idx - 48) : idx]
        after = text[idx + len(term) : idx + len(term) + 72]
        if DIAGNOSTIC_NEGATION_PREFIX.search(before) is None and DIAGNOSTIC_NEGATION_SUFFIX.search(after) is None:
            return True
        start = idx + len(term)


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


def missing_required_contexts(text: str, required_context: list[dict[str, Any]]) -> list[str]:
    missing = []
    for item in required_context:
        terms = [norm(term) for term in item.get("terms", [])]
        if terms and not any(has_non_negated(text, term) for term in terms):
            missing.append(item["id"])
    return sorted(set(missing))


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
        exact_terms.update(norm(term) for term in phenotype.get("high_confidence_terms", []))
        exact_match = any(term in text for term in exact_terms)
        base_confidence = 0.93 if exact_match else 0.55 + (0.35 * score)
        confidence = min(0.98, base_confidence - (0.15 if exclusions else 0.0))
        missing_context = missing_required_contexts(text, phenotype.get("required_context", []))
        scored.append((confidence, phenotype, matched, exclusions, missing_context))

    if not scored:
        return {
            "phenotype_id": None,
            "confidence": 0.0,
            "exclusions": [],
            "missing_required_context": [],
            "modifiers": [],
            "fallback_reason": "no_supported_phenotype_match",
        }

    confidence, phenotype, matched, exclusions, missing_context = sorted(scored, key=lambda row: row[0], reverse=True)[0]
    fallback_reason = None
    if exclusions:
        fallback_reason = "unsafe_modifier_present"
    elif missing_context:
        fallback_reason = "required_runtime_context_missing"
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
        "missing_required_context": missing_context,
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
