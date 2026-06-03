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
    "asthma_exacerbation_improved_discharge": {
        "primitive_file": ROOT / "primitives" / "expanded_draft_packs.json",
        "condition_terms": ["asthma exacerbation improved discharge", "asthma flare improved", "asthma", "wheezing", "asthma attack"],
        "unsafe_modifiers": ["hypoxia", "poor_inhaler_access", "pregnancy", "chest_pain", "frequent_relapse", "respiratory_distress"],
        "source_audit_notes": "MedlinePlus supports asthma symptoms, flare-up framing, trigger avoidance, prescribed inhaler use, and escalation for severe or life-threatening attacks.",
        "clinical_status": "reviewed_for_limited_improved_asthma_exacerbation_discharge_use",
        "required_modifiers": ["breathing improved after ED treatment", "safe outpatient plan", "rescue medication access", "no persistent hypoxia"],
    },
    "community_acquired_pneumonia_outpatient": {
        "primitive_file": ROOT / "primitives" / "expanded_draft_packs.json",
        "condition_terms": ["community acquired pneumonia outpatient", "pneumonia outpatient", "community acquired pneumonia", "pneumonia", "lung infection"],
        "unsafe_modifiers": ["hypoxia", "immunocompromised", "elderly_frail", "sepsis", "poor_follow_up", "respiratory_distress", "vomiting_unable_to_take_meds"],
        "source_audit_notes": "CDC supports pneumonia symptom framing, higher-risk host factors, and outpatient antibiotic-stewardship distinctions. Dosing and regimen selection remain outside the ontology until medication policy exists.",
        "clinical_status": "reviewed_for_limited_outpatient_community_acquired_pneumonia_use",
        "required_modifiers": ["pneumonia diagnosed by clinician", "stable for outpatient treatment", "acceptable oxygen level", "antibiotics prescribed"],
    },
    "acute_bronchitis_no_pneumonia": {
        "primitive_file": ROOT / "primitives" / "expanded_draft_packs.json",
        "condition_terms": [
            "acute bronchitis",
            "acute bronchitis no pneumonia",
            "chest cold",
            "viral bronchitis",
            "bronchitis without pneumonia concern",
        ],
        "unsafe_modifiers": [
            "hypoxia",
            "respiratory_distress",
            "pneumonia",
            "focal_lung_findings_or_infiltrate",
            "copd_or_asthma_exacerbation_pathway",
            "immunocompromised",
            "elderly_frail",
            "hemoptysis",
            "cardiac_or_pe_chest_pain_concern",
            "sepsis",
            "unstable_vitals",
            "antibiotic_prescribed_for_suspected_bacterial_infection",
        ],
        "high_confidence_terms": ["acute bronchitis", "acute bronchitis no pneumonia", "chest cold", "viral bronchitis"],
        "source_audit_notes": "CDC and MedlinePlus support acute bronchitis and chest cold framing, viral predominance, supportive care, and escalation for worsening breathing symptoms. CDC outpatient guidance supports keeping pneumonia concern, abnormal vital signs, and focal lung findings outside uncomplicated bronchitis.",
        "clinical_status": "reviewed_for_limited_acute_bronchitis_without_pneumonia_concern_use",
        "required_modifiers": [
            "adult with clinician diagnosis of acute bronchitis, chest cold, or viral bronchitis",
            "no pneumonia diagnosis or focal pneumonia concern",
            "acceptable oxygenation",
            "comfortable work of breathing",
            "no antibiotics prescribed for suspected bacterial infection",
        ],
    },
    "acute_sinusitis_supportive_care": {
        "primitive_file": ROOT / "primitives" / "expanded_draft_packs.json",
        "condition_terms": [
            "acute sinusitis supportive care",
            "sinus infection supportive care",
            "acute sinusitis",
            "sinus infection",
            "rhinosinusitis supportive care",
        ],
        "unsafe_modifiers": [
            "antibiotic_prescribed_for_sinusitis",
            "severe_bacterial_sinusitis_features",
            "orbital_or_intracranial_sinusitis_concern",
            "dental_or_facial_trauma_source",
            "immunocompromised",
            "elderly_frail",
            "pregnancy",
            "sepsis",
            "unstable_vitals",
            "chronic_or_recurrent_sinusitis",
        ],
        "high_confidence_terms": ["acute sinusitis supportive care", "sinus infection supportive care"],
        "source_audit_notes": "CDC and MedlinePlus support sinusitis framing, symptom-based diagnosis, supportive care, and seeking care for severe or concerning symptoms. CDC outpatient guidance supports that most rhinosinusitis is viral, that antibiotics may not help many cases, and that bacterial-feature or antibiotic decisions require clinician judgment.",
        "clinical_status": "reviewed_for_limited_acute_sinusitis_supportive_care_without_antibiotic_plan_use",
        "required_modifiers": [
            "adult with clinician diagnosis of acute sinusitis, sinus infection, or acute rhinosinusitis",
            "supportive-care plan without antibiotic instructions",
            "no severe bacterial sinusitis features",
            "no orbital or intracranial complication concern",
            "no dental source, facial trauma, sepsis, or individualized high-risk host pathway",
        ],
    },
    "concussion_discharge_no_imaging_red_flags": {
        "primitive_file": ROOT / "primitives" / "expanded_draft_packs.json",
        "condition_terms": ["concussion discharge no imaging red flags", "concussion", "mild traumatic brain injury", "mild tbi"],
        "unsafe_modifiers": ["athlete_return_to_play", "anticoagulated", "neurologic_deficit", "persistent_vomiting", "loss_of_consciousness", "intoxication"],
        "source_audit_notes": "CDC HEADS UP and CDC mild TBI guidance support danger signs, gradual return to activity, and clinician-directed return-to-school, work, driving, or play planning.",
        "clinical_status": "reviewed_for_limited_concussion_without_imaging_red_flags_use",
        "required_modifiers": ["reassuring neurologic assessment", "no imaging red flags documented", "safe observation plan", "no anticoagulation"],
    },
    "minor_head_injury_no_red_flags": {
        "primitive_file": ROOT / "primitives" / "expanded_draft_packs.json",
        "condition_terms": ["minor head injury no red flags", "minor head injury", "head injury", "hit head"],
        "unsafe_modifiers": ["anticoagulated", "loss_of_consciousness", "intoxication", "elderly", "persistent_vomiting", "neurologic_deficit", "skull_fracture_concern"],
        "source_audit_notes": "CDC concussion guidance supports delayed symptoms, emergency danger signs, and gradual activity return after minor head trauma or possible concussion.",
        "clinical_status": "reviewed_for_limited_minor_head_injury_without_red_flags_use",
        "required_modifiers": ["minor blunt head injury", "reassuring ED assessment", "no anticoagulation", "no neurologic deficit"],
    },
    "renal_colic_stable_no_infection": {
        "primitive_file": ROOT / "primitives" / "expanded_draft_packs.json",
        "condition_terms": ["renal colic stable no infection", "renal colic", "kidney stone", "ureteral stone"],
        "unsafe_modifiers": ["fever", "solitary_kidney", "pregnancy", "renal_failure", "uncontrolled_pain", "vomiting_unable_to_take_meds", "urinary_obstruction", "sepsis"],
        "source_audit_notes": "MedlinePlus supports kidney stone self-care, hydration, urine straining when instructed, and escalation for fever, chills, vomiting, severe pain, cloudy urine, or urinary symptoms.",
        "clinical_status": "reviewed_for_limited_stable_renal_colic_without_infection_use",
        "required_modifiers": ["suspected or confirmed renal colic", "stable for outpatient management", "no fever or sepsis", "symptoms controlled enough for discharge"],
    },
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
    "abdominal_pain_nonspecific_reassuring_workup": {
        "primitive_file": ROOT / "primitives" / "expanded_draft_packs.json",
        "condition_terms": ["abdominal pain recheck", "abdominal pain reassuring evaluation", "belly pain recheck", "nonspecific abdominal pain"],
        "unsafe_modifiers": ["pregnancy", "elderly", "immunocompromised", "poor_follow_up", "peritoneal_signs", "uncontrolled_vomiting", "fever", "gi_bleeding", "sepsis", "unstable_vitals"],
        "required_context": [
            {
                "id": "clinician_directed_recheck_plan",
                "terms": [
                    "explicit recheck",
                    "return for recheck",
                    "recheck as instructed",
                    "clinician instructed recheck",
                    "clinician directed recheck",
                    "clinician-directed recheck",
                    "follow up for recheck as instructed",
                    "ed recheck as instructed",
                ],
            }
        ],
        "high_confidence_terms": ["abdominal pain recheck"],
        "source_audit_notes": "MedlinePlus supports general abdominal pain framing, cautious home care, and conservative return precautions. This reviewed phenotype is limited to clinician-directed abdominal pain recheck after a reassuring ED evaluation.",
        "clinical_status": "reviewed_for_limited_abdominal_pain_recheck_after_reassuring_ed_evaluation_use",
        "required_modifiers": ["reassuring ED evaluation", "clinician-directed recheck plan", "no surgical abdomen concern", "reliable follow-up"],
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
        **({"required_context": config["required_context"]} if config.get("required_context") else {}),
        **({"high_confidence_terms": config["high_confidence_terms"]} if config.get("high_confidence_terms") else {}),
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
    if phenotype_id == "abdominal_pain_nonspecific_reassuring_workup":
        lines.extend(
            [
                "",
                "## Prior Clinician Decisions Preserved",
                "",
                "- Approve as a narrow review candidate.",
                "- Do not use it as a catch-all fallback for unmatched abdominal pain.",
                "- Medication lines are acceptable as passthrough-only and remain review-required.",
                "- Runtime requires clinician-directed recheck. If the clinician did not give a recheck plan, this phenotype should not fire.",
            ]
        )
    if phenotype_id == "acute_bronchitis_no_pneumonia":
        lines.extend(
            [
                "",
                "## Prior Clinician Decisions Preserved",
                "",
                "- Approve only as a narrow acute bronchitis or chest cold phenotype without pneumonia concern.",
                "- Do not use broad cough as a standalone runtime term.",
                "- Do not use acute bronchitis as a catch-all respiratory fallback.",
                "- Do not infer antibiotic instructions. Medication text is limited to stewardship framing and clinician-entered medicine instructions.",
                "- Runtime must block pneumonia concern, hypoxia, respiratory distress, COPD or asthma pathway, frailty, immunocompromise, hemoptysis, PE or cardiac chest-pain concern, sepsis, unstable vitals, and antibiotics prescribed for suspected bacterial infection.",
            ]
        )
    if phenotype_id == "acute_sinusitis_supportive_care":
        lines.extend(
            [
                "",
                "## Prior Clinician Decisions Preserved",
                "",
                "- Approve only as a narrow supportive-care sinusitis phenotype without an antibiotic plan.",
                "- Do not say antibiotics are never needed.",
                "- Do not use broad congestion, facial pain, or cold symptoms as standalone runtime terms.",
                "- Do not use sinusitis as a catch-all URI fallback.",
                "- Runtime must block antibiotics prescribed for sinusitis, severe bacterial-feature language, orbital or intracranial concern, dental source, facial trauma, immunocompromise, frailty, pregnancy, sepsis, unstable vitals, and chronic or recurrent sinusitis.",
            ]
        )
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
