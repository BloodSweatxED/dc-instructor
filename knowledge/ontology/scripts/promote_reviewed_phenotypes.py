#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from ontology_lib import ROOT, assemble_discharge, load_primitives, read_json
from build_expanded_draft_packs import MANIFEST_PATH, build_runtime_manifest


REVIEWER = "Andre / EM clinician-owner"
REVIEWER_ROLE = "Emergency Medicine physician"
REVIEW_DATE = "2026-06-01"
REVIEW_DIR = ROOT / "review_sheets"

PROMOTIONS: dict[str, dict[str, Any]] = {
    "abscess_after_i_and_d": {
        "primitive_file": ROOT / "primitives" / "expanded_draft_packs.json",
        "condition_terms": ["abscess after i and d", "abscess after incision and drainage", "abscess drained", "skin abscess drained", "i and d", "incision and drainage"],
        "unsafe_modifiers": ["deep_space_location", "immunocompromised", "packing_required", "recurrent_abscess", "sepsis", "necrotizing_infection_concern"],
        "source_audit_notes": "MedlinePlus supports skin abscess symptoms, pus drainage, fever or chills, and need to seek care for new symptoms after treatment.",
        "clinical_status": "reviewed_for_limited_abscess_after_ed_drainage_use",
        "required_modifiers": ["abscess drained", "safe discharge plan", "no deep-space location", "no sepsis"],
    },
    "allergic_reaction_resolved_no_anaphylaxis": {
        "primitive_file": ROOT / "primitives" / "expanded_draft_packs.json",
        "condition_terms": ["allergic reaction resolved no anaphylaxis", "allergic reaction no anaphylaxis", "allergic reaction", "hives", "urticaria"],
        "unsafe_modifiers": ["airway_symptoms", "hypotension", "epinephrine_given", "mucosal_lesions", "unknown_trigger", "anaphylaxis", "biphasic_reaction_concern"],
        "source_audit_notes": "MedlinePlus supports allergic reaction symptoms, anaphylaxis danger signs, epinephrine planning, and emergency escalation for airway or severe systemic symptoms.",
        "clinical_status": "reviewed_for_limited_resolved_allergic_reaction_without_anaphylaxis_use",
        "required_modifiers": ["symptoms improved or resolved", "no anaphylaxis", "no airway swelling", "no hypotension"],
    },
    "lumbar_strain_no_red_flags": {
        "primitive_file": ROOT / "primitives" / "back_pain.json",
        "condition_terms": [
            "lumbar strain no red flags",
            "lumbar strain",
            "low back strain",
            "mechanical low back pain",
            "acute low back pain",
            "back pain no red flags",
        ],
        "unsafe_modifiers": [
            "cauda_equina_concern",
            "spinal_infection_concern",
            "fracture_or_trauma_concern",
            "cancer_red_flag",
            "fever",
            "new_neurologic_deficit",
            "pregnancy",
            "unable_to_walk",
        ],
        "source_audit_notes": "MedlinePlus supports conservative low-back-pain care and red flags. WikEM supports ED phenotype boundaries and must-not-miss framing only.",
        "clinical_status": "reviewed_for_limited_mechanical_low_back_pain_without_red_flags_use",
        "required_modifiers": ["no cauda equina concern", "no spinal infection concern", "no major trauma or fracture concern", "ambulatory or safe mobility plan"],
    },
    "viral_uri_no_pneumonia": {
        "primitive_file": ROOT / "primitives" / "viral_uri.json",
        "condition_terms": [
            "viral uri no pneumonia",
            "viral upper respiratory infection",
            "viral uri",
            "common cold",
            "cold symptoms",
            "uri no pneumonia",
        ],
        "unsafe_modifiers": [
            "pneumonia",
            "hypoxia",
            "respiratory_distress",
            "unstable_vitals",
            "immunocompromised",
            "sepsis",
            "chest_pain",
            "antibiotic_prescribed",
            "bacterial_infection_suspected",
        ],
        "source_audit_notes": "MedlinePlus supports viral URI supportive care and escalation symptoms. AHRQ supports antibiotic stewardship for uncomplicated viral URI.",
        "clinical_status": "reviewed_for_limited_viral_uri_without_pneumonia_use",
        "required_modifiers": ["comfortable breathing", "acceptable oxygen level", "no pneumonia concern", "no antibiotic prescribed"],
    },
    "uncomplicated_cystitis_nonpregnant": {
        "primitive_file": ROOT / "primitives" / "cystitis.json",
        "condition_terms": [
            "uncomplicated cystitis nonpregnant",
            "uncomplicated cystitis",
            "bladder infection",
            "uti",
            "urinary tract infection",
            "cystitis",
        ],
        "unsafe_modifiers": [
            "pregnancy",
            "male_patient",
            "pyelonephritis",
            "fever",
            "flank_pain",
            "sepsis",
            "vomiting_unable_to_take_meds",
            "complicated_uti",
            "kidney_transplant",
            "urinary_obstruction",
            "indwelling_catheter",
            "no_antibiotic_prescribed",
        ],
        "source_audit_notes": "CDC and MedlinePlus support UTI framing, antibiotic treatment when clinically indicated, hydration, and pyelonephritis or sepsis return precautions.",
        "clinical_status": "reviewed_for_limited_nonpregnant_uncomplicated_cystitis_use",
        "required_modifiers": ["not pregnant", "lower urinary symptoms", "no fever or flank pain", "oral antibiotics prescribed"],
    },
    "gastroenteritis_stable_hydrating": {
        "primitive_file": ROOT / "primitives" / "gastroenteritis.json",
        "condition_terms": [
            "gastroenteritis stable hydrating",
            "gastroenteritis",
            "stomach virus",
            "vomiting diarrhea",
            "nausea vomiting diarrhea",
            "diarrhea vomiting",
        ],
        "unsafe_modifiers": [
            "surgical_abdomen",
            "sepsis",
            "gi_bleeding",
            "severe_dehydration",
            "unable_to_tolerate_oral_fluids",
            "unstable_vitals",
            "pregnancy",
            "immunocompromised",
            "elderly_frail",
            "c_diff_risk",
        ],
        "source_audit_notes": "MedlinePlus supports oral rehydration, gradual diet advancement, hygiene, and return precautions for dehydration, blood in stool, fever, and severe abdominal pain.",
        "clinical_status": "reviewed_for_limited_stable_gastroenteritis_able_to_hydrate_use",
        "required_modifiers": ["stable for discharge", "can continue oral hydration", "no surgical abdomen", "no GI bleeding"],
    },
    "cellulitis_uncomplicated_oral_antibiotics": {
        "primitive_file": ROOT / "primitives" / "expanded_draft_packs.json",
        "condition_terms": ["cellulitis", "uncomplicated cellulitis", "skin infection", "skin infection cellulitis"],
        "unsafe_modifiers": ["immunocompromised", "rapid_progression", "diabetic_foot", "bite_wound", "near_eye_or_genitals", "sepsis", "necrotizing_infection_concern", "deep_space_location"],
        "source_audit_notes": "MedlinePlus and CDC support cellulitis treatment framing, antibiotic use when clinically indicated, and escalation for worsening or severe infection.",
        "clinical_status": "reviewed_for_limited_uncomplicated_outpatient_cellulitis_use",
        "required_modifiers": ["localized infection", "outpatient antibiotics prescribed", "no sepsis", "no necrotizing infection concern", "no high-risk location"],
    },
    "dental_pain_no_deep_space_infection": {
        "primitive_file": ROOT / "primitives" / "expanded_draft_packs.json",
        "condition_terms": ["dental pain no deep space infection", "dental pain", "tooth pain", "toothache", "dental infection no deep space infection"],
        "unsafe_modifiers": ["airway_symptoms", "deep_space_swelling", "immunocompromised", "trismus", "fever", "sepsis", "ludwig_angina_concern"],
        "source_audit_notes": "MedlinePlus supports dental pain causes, need for dental evaluation, and urgent escalation for swelling, fever, trouble swallowing, or trouble breathing.",
        "clinical_status": "reviewed_for_limited_dental_pain_without_deep_space_infection_use",
        "required_modifiers": ["no airway symptoms", "no deep-space swelling", "dental follow-up needed"],
    },
    "laceration_repaired_simple": {
        "primitive_file": ROOT / "primitives" / "expanded_draft_packs.json",
        "condition_terms": ["laceration repaired simple", "simple laceration repair", "laceration repair", "repaired laceration", "stitches", "sutures", "skin glue"],
        "unsafe_modifiers": ["bite_wound", "hand_tendon_risk", "joint_violation", "open_fracture", "dirty_wound", "neurovascular_compromise", "retained_foreign_body"],
        "source_audit_notes": "MedlinePlus supports laceration framing, wound infection signs, higher-risk wounds, and deeper structure concerns for tendons, nerves, vessels, or bone.",
        "clinical_status": "reviewed_for_limited_simple_repaired_laceration_use",
        "required_modifiers": ["simple repaired wound", "no tendon nerve vessel joint or open fracture concern", "wound care plan given"],
    },
    "viral_pharyngitis_strep_negative": {
        "primitive_file": ROOT / "primitives" / "expanded_draft_packs.json",
        "condition_terms": ["viral pharyngitis strep negative", "viral pharyngitis", "sore throat strep negative", "strep negative", "negative strep"],
        "unsafe_modifiers": ["drooling", "trismus", "voice_change", "airway_symptoms", "immunocompromised", "peritonsillar_abscess_concern", "epiglottitis_concern", "mono_complication_concern", "positive_strep_test", "antibiotic_prescribed"],
        "source_audit_notes": "CDC supports viral sore throat antibiotic stewardship and group A strep testing distinctions, including not treating viral pharyngitis with antibiotics.",
        "clinical_status": "reviewed_for_limited_strep_negative_viral_pharyngitis_use",
        "required_modifiers": ["negative strep evaluation", "no deep neck infection signs", "no antibiotic prescribed"],
    },
}


def reviewed_block(notes: str, extra: dict[str, Any] | None = None) -> dict[str, Any]:
    block = {
        "status": "reviewed",
        "reviewer": REVIEWER,
        "reviewer_role": REVIEWER_ROLE,
        "last_reviewed": REVIEW_DATE,
        "version": 1,
        "source_audit_status": "passed_for_v1",
        "production_status": "enabled_with_runtime_modifier_gates",
        "notes": notes,
    }
    if extra:
        block.update(extra)
    return block


def source_audit(notes: str, clinician: bool = False, unsafe: bool = False) -> dict[str, Any]:
    return {
        "source_supported": True,
        "source_needed": False,
        "clinician_judgment_only": clinician,
        "restricted_source_risk": False,
        "unsafe_without_modifier": unsafe,
        "notes": notes,
    }


def write_json(path: Path, data: Any) -> None:
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def promote_phenotype(phenotype_id: str, config: dict[str, Any]) -> None:
    path = ROOT / "phenotypes" / f"{phenotype_id}.json"
    item = read_json(path)
    item["status"] = "reviewed"
    item["source_audit"] = source_audit(config["source_audit_notes"])
    item["runtime"] = {
        "condition_terms": config["condition_terms"],
        "unsafe_modifiers": config["unsafe_modifiers"],
        "minimum_confidence": 0.86,
        "mode": "reviewed_ontology_enabled",
    }
    item["version"] = 1
    item["review"] = reviewed_block(
        f"Reviewed as a narrow production ontology phenotype. {config['source_audit_notes']}",
        {
            "clinical_status": config["clinical_status"],
            "required_modifiers": config["required_modifiers"],
            "blocked_modifiers": config["unsafe_modifiers"],
        },
    )
    write_json(path, item)


def promote_primitives(phenotype_id: str, config: dict[str, Any]) -> None:
    path = config["primitive_file"]
    rows = read_json(path)
    for row in rows:
        if phenotype_id not in row.get("phenotypes", []):
            continue
        clinician = row["section"] in {"diagnosis", "what_we_found", "follow_up"}
        unsafe = bool(row.get("contraindications"))
        row["source_audit"] = source_audit(config["source_audit_notes"], clinician=clinician, unsafe=unsafe)
        row["review"] = reviewed_block(
            f"Reviewed for {phenotype_id} v1. Patient-facing text is locally authored from source-supported concepts."
        )
    write_json(path, rows)


def review_packet(phenotype_id: str, config: dict[str, Any]) -> str:
    phenotype = read_json(ROOT / "phenotypes" / f"{phenotype_id}.json")
    primitives = load_primitives()
    selected = [primitives[primitive_id] for primitive_id in phenotype["primitive_ids"]]
    lines = [
        f"# {phenotype['label']} V1 Review Packet",
        "",
        f"Phenotype ID: `{phenotype_id}`",
        "",
        f"Clinical status: {phenotype['review']['clinical_status']}.",
        "",
        "Production status: enabled with runtime modifier gates.",
        "",
        f"Reviewer: {REVIEWER}.",
        "",
        f"Review date: {REVIEW_DATE}.",
        "",
        "## Inclusion Criteria",
        "",
    ]
    lines.extend(f"- {row}" for row in phenotype["inclusion_criteria"])
    lines.extend(["", "## Exclusions", ""])
    lines.extend(f"- {row}" for row in phenotype["exclusion_criteria"])
    lines.extend(["", "## Must-Not-Miss Diagnoses", ""])
    lines.extend(f"- {row}" for row in phenotype["must_not_miss"])
    lines.extend(["", "## Source Audit", ""])
    for source_id in phenotype.get("source_card_ids", []):
        lines.append(f"- `{source_id}` supports this phenotype's reviewed concepts.")
    lines.append(f"- {config['source_audit_notes']}")
    lines.append("- Patient-facing text is locally authored. No WikEM prose is copied.")
    lines.extend(["", "## Blocked Modifiers", ""])
    lines.extend(f"- `{row}`" for row in config["unsafe_modifiers"])
    lines.extend(["", "## Primitive List", ""])
    for row in selected:
        flags = ", ".join(key for key, value in row.get("source_audit", {}).items() if value is True) or "source_supported"
        lines.append(f"- `{row['id']}` | `{row['section']}` | audit: {flags}")
    lines.extend(["", "## Patient-Facing Output", "", "```text", assemble_discharge(phenotype_id, "6").rstrip(), "```", ""])
    return "\n".join(lines)


def main() -> int:
    REVIEW_DIR.mkdir(parents=True, exist_ok=True)
    for phenotype_id, config in PROMOTIONS.items():
        promote_phenotype(phenotype_id, config)
        promote_primitives(phenotype_id, config)
        (REVIEW_DIR / f"{phenotype_id}_v1_review_packet.md").write_text(
            review_packet(phenotype_id, config),
            encoding="utf-8",
        )
        print(f"promoted {phenotype_id}")
    write_json(MANIFEST_PATH, build_runtime_manifest())
    print(f"wrote {MANIFEST_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
