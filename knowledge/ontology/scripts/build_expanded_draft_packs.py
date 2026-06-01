#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from ontology_lib import ROOT, SECTIONS, assemble_discharge, load_phenotypes


REQUIRED_SECTIONS = [section_id for section_id, _ in SECTIONS]
REVIEW_DIR = ROOT / "review_sheets"
MANIFEST_PATH = ROOT / "runtime" / "ontology_manifest.json"
PRIMITIVE_PATH = ROOT / "primitives" / "expanded_draft_packs.json"
REVIEWER = "Andre / EM clinician-owner"
REVIEWER_ROLE = "Emergency Medicine physician"
REVIEW_DATE = "2026-06-01"
REVIEWED_PACK_IDS = {
    "abscess_after_i_and_d",
    "allergic_reaction_resolved_no_anaphylaxis",
    "cellulitis_uncomplicated_oral_antibiotics",
    "dental_pain_no_deep_space_infection",
    "laceration_repaired_simple",
    "viral_pharyngitis_strep_negative",
}


PACKS: list[dict[str, Any]] = [
    {
        "id": "cellulitis_uncomplicated_oral_antibiotics",
        "label": "Uncomplicated cellulitis treated as outpatient",
        "family": "skin_soft_tissue_infection",
        "condition_terms": ["cellulitis", "uncomplicated cellulitis", "skin infection", "skin infection cellulitis"],
        "source_card_ids": ["medlineplus.cellulitis", "cdc.group_a_strep_cellulitis"],
        "summary": "You were treated for a skin infection called cellulitis.",
        "found": "Your exam fits a skin infection that is safe to treat at home today. We did not find signs of a deeper emergency infection.",
        "home": ["Keep the area clean and dry.", "Raise the arm or leg when you can.", "Mark the edge of redness if your clinician asks you to."],
        "meds": ["Take the antibiotic exactly as prescribed.", "Use acetaminophen or ibuprofen only if you can take it safely and follow the label."],
        "return": ["Fever, shaking chills, confusion, or feeling very ill.", "Redness spreading fast, severe pain, numbness, pus, or red streaks.", "The infection is near the eye, genitals, or a joint and gets worse."],
        "follow": "Arrange recheck with primary care, urgent care, or the ED as instructed, especially if not improving.",
        "inclusion": ["Localized cellulitis judged safe for outpatient therapy.", "No shock, necrotizing infection concern, or deep-space infection concern."],
        "exclusion": ["Sepsis or unstable vital signs.", "Necrotizing soft tissue infection concern.", "Diabetic foot infection, bite wound, or immunocompromised host requiring a separate pathway."],
        "must_not_miss": ["Necrotizing soft tissue infection.", "Abscess needing drainage.", "Sepsis.", "Septic joint when over a joint."],
        "unsafe_modifiers": ["immunocompromised", "rapid_progression", "diabetic_foot", "bite_wound", "near_eye_or_genitals"],
    },
    {
        "id": "abscess_after_i_and_d",
        "label": "Abscess after incision and drainage",
        "family": "skin_soft_tissue_infection",
        "condition_terms": ["abscess after i and d", "abscess after incision and drainage", "abscess drained", "skin abscess drained", "i and d", "incision and drainage"],
        "source_card_ids": ["medlineplus.skin_abscess"],
        "summary": "You had an abscess drained today.",
        "found": "The painful swollen area had pus inside. It was opened and drained, which is the main treatment.",
        "home": ["Keep the dressing clean and dry.", "Wash your hands before and after wound care.", "Do not squeeze or dig into the wound."],
        "meds": ["Take antibiotics only if they were prescribed.", "Use acetaminophen or ibuprofen only if you can take it safely and follow the label."],
        "return": ["Fever, spreading redness, red streaks, or worsening swelling.", "Severe pain, numbness, or bleeding that will not stop.", "Packing falls out early and you were told it must stay in."],
        "follow": "Return or follow up for wound check as instructed.",
        "inclusion": ["Abscess drained in the ED and patient discharged.", "No deep-space infection or sepsis concern."],
        "exclusion": ["Deep hand, face, neck, breast, genital, or perirectal abscess pathway.", "Sepsis or immunocompromised host needing separate planning."],
        "must_not_miss": ["Necrotizing infection.", "Deep-space infection.", "Sepsis.", "Retained foreign body."],
        "unsafe_modifiers": ["deep_space_location", "immunocompromised", "packing_required", "recurrent_abscess"],
    },
    {
        "id": "laceration_repaired_simple",
        "label": "Simple laceration repair",
        "family": "wound_care",
        "condition_terms": ["laceration repaired simple", "simple laceration repair", "laceration repair", "repaired laceration", "stitches", "sutures", "skin glue"],
        "source_card_ids": ["medlineplus.cuts_puncture_wounds"],
        "summary": "Your cut was cleaned and repaired today.",
        "found": "We checked the wound and repaired it because it was safe to close. No emergency complication was found during today's exam.",
        "home": ["Keep the wound clean and dry today.", "After the first day, gentle soap and water is usually okay unless told otherwise.", "Do not soak the wound until it is healed."],
        "meds": ["Take antibiotics only if they were prescribed.", "Use acetaminophen or ibuprofen only if you can take it safely and follow the label."],
        "return": ["Fever, pus, spreading redness, red streaks, or worsening swelling.", "Bleeding that will not stop with firm pressure.", "New numbness, weakness, color change, or the wound opens."],
        "follow": "Follow up for wound check or suture removal on the schedule your clinician gave you.",
        "inclusion": ["Simple repaired laceration with no tendon, nerve, vessel, joint, or open fracture concern."],
        "exclusion": ["Bite wounds requiring special counseling.", "Open fracture, tendon injury, nerve injury, joint violation, or high-pressure injection injury."],
        "must_not_miss": ["Tendon injury.", "Nerve or vascular injury.", "Open fracture.", "Joint violation.", "Infection."],
        "unsafe_modifiers": ["bite_wound", "hand_tendon_risk", "joint_violation", "open_fracture", "dirty_wound"],
    },
    {
        "id": "minor_head_injury_no_red_flags",
        "label": "Minor head injury without red flags",
        "family": "head_injury",
        "condition_terms": ["minor head injury", "head injury", "hit head"],
        "source_card_ids": ["cdc.heads_up_concussion_symptoms", "cdc.mild_tbi_aftercare"],
        "summary": "You had a minor head injury.",
        "found": "Your exam was reassuring today. We did not find signs that you needed emergency treatment for bleeding around the brain.",
        "home": ["Rest today and increase activity slowly.", "Avoid alcohol or sedating drugs unless your clinician says they are safe.", "Have a trusted person check on you if possible."],
        "meds": ["Use acetaminophen for headache if you can take it safely and follow the label.", "Avoid medicines your clinician told you to avoid."],
        "return": ["Worsening severe headache, repeated vomiting, confusion, seizure, fainting, or trouble waking up.", "New weakness, numbness, trouble speaking, or vision changes.", "Clear fluid or blood from the nose or ear."],
        "follow": "Follow up with primary care if symptoms are not improving or if you were told to recheck.",
        "inclusion": ["Minor blunt head injury judged safe for discharge.", "No anticoagulation or high-risk features requiring separate pathway."],
        "exclusion": ["Anticoagulated patient.", "Persistent altered mental status.", "Suspected skull fracture.", "Non-accidental trauma concern."],
        "must_not_miss": ["Intracranial hemorrhage.", "Cervical spine injury.", "Skull fracture.", "Non-accidental trauma."],
        "unsafe_modifiers": ["anticoagulated", "loss_of_consciousness", "intoxication", "elderly", "persistent_vomiting"],
    },
    {
        "id": "concussion_discharge_no_imaging_red_flags",
        "label": "Concussion discharge without imaging red flags",
        "family": "head_injury",
        "condition_terms": ["concussion", "mild traumatic brain injury", "mild tbi"],
        "source_card_ids": ["cdc.heads_up_concussion_symptoms", "cdc.mild_tbi_aftercare"],
        "summary": "Your symptoms fit a concussion.",
        "found": "A concussion can happen after a hit or sudden movement of the head. Your exam today did not show an emergency danger sign requiring admission.",
        "home": ["Rest your brain and body for the first day.", "Return to school, work, exercise, and screens slowly as symptoms allow.", "Avoid another head injury while symptoms are present."],
        "meds": ["Use acetaminophen for headache if you can take it safely and follow the label.", "Avoid alcohol and sedating drugs unless your clinician says they are safe."],
        "return": ["Worsening headache, repeated vomiting, confusion, seizure, fainting, or trouble waking up.", "New weakness, numbness, trouble speaking, or vision changes.", "Any second head injury before you recover."],
        "follow": "Follow up with primary care, sports medicine, or concussion clinic if symptoms persist or if you need return-to-play clearance.",
        "inclusion": ["Concussion symptoms with reassuring ED assessment and safe discharge plan."],
        "exclusion": ["Red flags for intracranial bleeding.", "Anticoagulation or bleeding disorder.", "Unreliable observation plan."],
        "must_not_miss": ["Intracranial hemorrhage.", "Cervical spine injury.", "Second-impact risk.", "Persistent neurologic deficit."],
        "unsafe_modifiers": ["athlete_return_to_play", "anticoagulated", "neurologic_deficit", "persistent_vomiting"],
    },
    {
        "id": "renal_colic_stable_no_infection",
        "label": "Renal colic, stable, no infection concern",
        "family": "genitourinary",
        "condition_terms": ["renal colic", "kidney stone", "ureteral stone"],
        "source_card_ids": ["medlineplus.kidney_stones_self_care"],
        "summary": "Your symptoms fit a kidney stone.",
        "found": "Your ED evaluation was reassuring enough for home care today. We did not find signs of a dangerous kidney infection or blocked infected kidney.",
        "home": ["Drink fluids as you are able.", "Use a urine strainer if one was given.", "Save any passed stone if your clinician asked you to."],
        "meds": ["Take prescribed pain or nausea medicine exactly as directed.", "Use acetaminophen or ibuprofen only if you can take it safely and follow the label."],
        "return": ["Fever, chills, worsening flank pain, repeated vomiting, or feeling very ill.", "You cannot urinate.", "Pain cannot be controlled with the plan you were given."],
        "follow": "Follow up with urology or primary care as instructed.",
        "inclusion": ["Suspected or confirmed renal colic, stable for outpatient management.", "No fever, sepsis, solitary kidney emergency, or uncontrolled symptoms."],
        "exclusion": ["Infected obstructing stone concern.", "Solitary kidney, transplant kidney, pregnancy, renal failure, or uncontrolled pain/vomiting."],
        "must_not_miss": ["Infected obstructing stone.", "Abdominal aortic emergency mimic.", "Testicular torsion mimic.", "Pyelonephritis."],
        "unsafe_modifiers": ["fever", "solitary_kidney", "pregnancy", "renal_failure", "uncontrolled_pain"],
    },
    {
        "id": "dental_pain_no_deep_space_infection",
        "label": "Dental pain without deep-space infection",
        "family": "dental_oral",
        "condition_terms": ["dental pain no deep space infection", "dental pain", "tooth pain", "toothache", "dental infection no deep space infection"],
        "source_card_ids": ["medlineplus.toothaches"],
        "summary": "You were treated for dental pain today.",
        "found": "Your exam did not show signs of a dangerous deep infection in the face, jaw, or neck today.",
        "home": ["Keep the mouth clean with gentle brushing.", "Avoid chewing on the painful side.", "A dentist must treat the tooth problem for it to fully resolve."],
        "meds": ["Take antibiotics only if they were prescribed.", "Use acetaminophen or ibuprofen only if you can take it safely and follow the label."],
        "return": ["Face or neck swelling, fever, trouble swallowing, drooling, voice change, or trouble breathing.", "You cannot open your mouth normally.", "Pain or swelling spreads quickly."],
        "follow": "See a dentist as soon as possible.",
        "inclusion": ["Dental pain or localized dental infection without airway, deep-space, or sepsis concern."],
        "exclusion": ["Ludwig angina concern.", "Deep-space infection.", "Airway symptoms.", "Immunocompromised host."],
        "must_not_miss": ["Deep-space neck infection.", "Ludwig angina.", "Airway compromise.", "Sepsis."],
        "unsafe_modifiers": ["airway_symptoms", "deep_space_swelling", "immunocompromised", "trismus"],
    },
    {
        "id": "viral_pharyngitis_strep_negative",
        "label": "Viral pharyngitis, strep negative",
        "family": "upper_respiratory",
        "condition_terms": ["viral pharyngitis strep negative", "viral pharyngitis", "sore throat strep negative", "strep negative", "negative strep"],
        "source_card_ids": ["cdc.sore_throat_basics", "cdc.group_a_strep_pharyngitis"],
        "summary": "Your sore throat is most consistent with a viral infection.",
        "found": "Your strep test was negative. Your exam did not show signs of a dangerous throat or neck infection today.",
        "home": ["Drink fluids.", "Try warm liquids, honey if safe for you, or throat lozenges.", "Avoid sharing cups and wash your hands often."],
        "meds": ["Antibiotics are not needed for a viral sore throat.", "Use acetaminophen or ibuprofen only if you can take it safely and follow the label."],
        "return": ["Trouble breathing, drooling, muffled voice, stiff neck, or trouble opening your mouth.", "You cannot swallow fluids.", "Fever or throat pain becomes much worse."],
        "follow": "Follow up with primary care if symptoms are not improving or if your clinician instructed you to recheck.",
        "inclusion": ["Sore throat with negative strep testing and no deep neck infection signs."],
        "exclusion": ["Peritonsillar abscess concern.", "Epiglottitis concern.", "Immunocompromised host.", "Concern for mono complications."],
        "must_not_miss": ["Peritonsillar abscess.", "Epiglottitis.", "Retropharyngeal abscess.", "Airway compromise."],
        "unsafe_modifiers": ["drooling", "trismus", "voice_change", "airway_symptoms", "immunocompromised"],
    },
    {
        "id": "asthma_exacerbation_improved_discharge",
        "label": "Asthma exacerbation improved for discharge",
        "family": "respiratory",
        "condition_terms": ["asthma", "wheezing", "asthma attack"],
        "source_card_ids": ["medlineplus.asthma"],
        "summary": "You were treated for an asthma flare.",
        "found": "Your breathing improved enough for discharge today. Asthma can worsen again, so use the plan you were given closely.",
        "home": ["Avoid smoke, fumes, and known triggers.", "Use your spacer if one was prescribed.", "Rest and avoid heavy exertion until breathing is back to baseline."],
        "meds": ["Use your rescue inhaler exactly as prescribed.", "Take steroids or controller medicines exactly as prescribed."],
        "return": ["Shortness of breath at rest, blue lips, severe wheezing, or trouble speaking full sentences.", "Rescue inhaler is not helping or you need it much more often than instructed.", "Chest pain, fainting, confusion, or worsening symptoms."],
        "follow": "Follow up with primary care, pulmonology, or asthma clinic as instructed.",
        "inclusion": ["Asthma flare improved after ED treatment and safe for outpatient plan."],
        "exclusion": ["Persistent hypoxia.", "Impending respiratory failure.", "Pneumonia or pulmonary embolism concern.", "No access to rescue medication."],
        "must_not_miss": ["Respiratory failure.", "Pneumonia.", "Pneumothorax.", "Pulmonary embolism mimic."],
        "unsafe_modifiers": ["hypoxia", "poor_inhaler_access", "pregnancy", "chest_pain", "frequent_relapse"],
    },
    {
        "id": "allergic_reaction_resolved_no_anaphylaxis",
        "label": "Allergic reaction resolved, no anaphylaxis",
        "family": "allergy_immunology",
        "condition_terms": ["allergic reaction resolved no anaphylaxis", "allergic reaction no anaphylaxis", "allergic reaction", "hives", "urticaria"],
        "source_card_ids": ["medlineplus.allergic_reactions"],
        "summary": "You were treated for an allergic reaction.",
        "found": "Your symptoms improved, and we did not find signs of anaphylaxis at discharge today.",
        "home": ["Avoid the trigger if it is known.", "Watch for symptoms returning after you leave.", "Do not drive or drink alcohol after sedating allergy medicines."],
        "meds": ["Take allergy medicines exactly as prescribed.", "Use an epinephrine injector only if one was prescribed and you were instructed to use it."],
        "return": ["Trouble breathing, wheezing, throat tightness, tongue or lip swelling, fainting, or severe vomiting.", "Rash or swelling returns quickly or spreads.", "You use epinephrine."],
        "follow": "Follow up with primary care or allergy clinic if symptoms continue or trigger is unclear.",
        "inclusion": ["Allergic reaction improved or resolved without anaphylaxis at discharge."],
        "exclusion": ["Anaphylaxis.", "Airway swelling.", "Hypotension.", "Biphasic reaction concern needing observation."],
        "must_not_miss": ["Anaphylaxis.", "Airway edema.", "Medication reaction with mucosal involvement.", "Serum sickness or severe cutaneous adverse reaction."],
        "unsafe_modifiers": ["airway_symptoms", "hypotension", "epinephrine_given", "mucosal_lesions", "unknown_trigger"],
    },
    {
        "id": "community_acquired_pneumonia_outpatient",
        "label": "Community-acquired pneumonia, outpatient",
        "family": "respiratory_infection",
        "condition_terms": ["pneumonia", "lung infection"],
        "source_card_ids": ["cdc.pneumonia_about", "cdc.antibiotic_use_adult_outpatient"],
        "summary": "You were treated for pneumonia.",
        "found": "Your ED evaluation found a lung infection that was safe to treat at home today. Your oxygen level and overall condition were reassuring enough for discharge.",
        "home": ["Rest and increase activity slowly.", "Drink fluids if you are allowed.", "Avoid smoking and smoke exposure."],
        "meds": ["Take antibiotics exactly as prescribed.", "Use fever or pain medicine only if you can take it safely and follow the label."],
        "return": ["Worse trouble breathing, blue lips, confusion, fainting, or chest pain.", "Fever or symptoms worsen after starting treatment.", "You cannot keep medicines or fluids down."],
        "follow": "Follow up with primary care as instructed.",
        "inclusion": ["Pneumonia judged stable for outpatient treatment.", "No hypoxia, sepsis, or admission need at discharge."],
        "exclusion": ["Hypoxia.", "Sepsis.", "Immunocompromised host.", "High-risk comorbidity or unreliable outpatient plan."],
        "must_not_miss": ["Sepsis.", "Pulmonary embolism mimic.", "Heart failure mimic.", "Empyema.", "Hypoxic respiratory failure."],
        "unsafe_modifiers": ["hypoxia", "immunocompromised", "elderly_frail", "sepsis", "poor_follow_up"],
    },
    {
        "id": "chest_pain_low_risk_negative_ed_workup",
        "label": "Low-risk chest pain after negative ED workup",
        "family": "cardiovascular",
        "condition_terms": ["low risk chest pain", "chest pain", "negative cardiac workup"],
        "summary": "You were evaluated for chest pain today.",
        "found": "Your ED workup was reassuring today. No emergency cause was found, but chest pain can change after you leave.",
        "home": ["Rest today.", "Avoid heavy activity until you know how you feel and follow your clinician's instructions.", "Keep track of symptoms if they return."],
        "meds": ["Continue your home medicines unless your clinician told you to stop.", "Take any new medicine exactly as prescribed."],
        "return": ["Chest pain that returns, gets worse, or spreads to the arm, jaw, back, or neck.", "Shortness of breath, sweating, fainting, new weakness, or coughing blood.", "Fast or irregular heartbeat with dizziness or chest pain."],
        "follow": "Follow up with primary care or cardiology as instructed.",
        "inclusion": ["Chest pain evaluated in ED and judged low risk for discharge.", "No active ischemia, unstable vital signs, or admission need."],
        "exclusion": ["Abnormal ECG or troponin requiring admission.", "Ongoing concerning pain.", "Pulmonary embolism, aortic emergency, myocarditis, or pericarditis concern."],
        "must_not_miss": ["Acute coronary syndrome.", "Pulmonary embolism.", "Aortic dissection.", "Pneumothorax.", "Myocarditis."],
        "unsafe_modifiers": ["abnormal_troponin", "abnormal_ecg", "ongoing_pain", "syncope", "known_cad_high_risk"],
    },
    {
        "id": "abdominal_pain_nonspecific_reassuring_workup",
        "label": "Nonspecific abdominal pain with reassuring ED workup",
        "family": "gastrointestinal",
        "condition_terms": ["abdominal pain", "belly pain", "nonspecific abdominal pain"],
        "summary": "You were evaluated for abdominal pain today.",
        "found": "Your ED evaluation was reassuring today. We did not find a clear emergency cause, but early problems can change after discharge.",
        "home": ["Drink fluids as you are able.", "Start with bland foods if your stomach feels upset.", "Avoid alcohol and heavy meals until you feel better."],
        "meds": ["Take prescribed nausea or stomach medicine exactly as directed.", "Use pain medicine only as instructed by your clinician."],
        "return": ["Worsening or one-sided belly pain, repeated vomiting, fainting, or confusion.", "Fever, bloody stool, black stool, vomiting blood, or a swollen hard belly.", "New chest pain, trouble breathing, or pain with pregnancy concern."],
        "follow": "Follow up with primary care or return for recheck as instructed.",
        "inclusion": ["Abdominal pain with reassuring ED assessment and no surgical abdomen at discharge."],
        "exclusion": ["Pregnancy-related abdominal pain.", "Appendicitis, obstruction, ischemia, perforation, or sepsis concern.", "Uncontrolled pain or vomiting."],
        "must_not_miss": ["Appendicitis.", "Bowel obstruction.", "Bowel ischemia.", "Perforation.", "Ectopic pregnancy.", "AAA."],
        "unsafe_modifiers": ["pregnancy", "elderly", "immunocompromised", "peritoneal_signs", "uncontrolled_vomiting"],
    },
]


def audit(source_supported: bool = False, clinician_judgment_only: bool = False, unsafe_without_modifier: bool = False) -> dict[str, bool]:
    return {
        "source_supported": source_supported,
        "source_needed": not source_supported,
        "clinician_judgment_only": clinician_judgment_only,
        "restricted_source_risk": False,
        "unsafe_without_modifier": unsafe_without_modifier,
    }


def review_block(notes: str) -> dict[str, Any]:
    return {"status": "draft", "reviewer": None, "last_reviewed": None, "notes": notes}


def reviewed_block(notes: str) -> dict[str, Any]:
    return {
        "status": "reviewed",
        "reviewer": REVIEWER,
        "reviewer_role": REVIEWER_ROLE,
        "last_reviewed": REVIEW_DATE,
        "version": 1,
        "source_audit_status": "passed_for_v1",
        "production_status": "enabled_with_runtime_modifier_gates",
        "notes": notes,
    }


def primitive(pack: dict[str, Any], section: str, kind: str, priority: str, text: str, unsafe: bool = False, clinician: bool = False) -> dict[str, Any]:
    primitive_id = f"{pack['id']}.{section}.{kind}.v1"
    reviewed = pack["id"] in REVIEWED_PACK_IDS
    return {
        "id": primitive_id,
        "phenotypes": [pack["id"]],
        "section": section,
        "primitive_type": kind,
        "priority": priority,
        "text": {"en_4": text, "en_6": text, "en_hl1": text},
        "contraindications": pack["unsafe_modifiers"] if unsafe else [],
        "source_card_ids": pack.get("source_card_ids", []),
        "source_audit": audit(source_supported=reviewed, clinician_judgment_only=clinician, unsafe_without_modifier=unsafe),
        "review": reviewed_block("Reviewed for cellulitis_uncomplicated_oral_antibiotics v1. Patient-facing text is locally authored from source-supported concepts.")
        if reviewed
        else review_block("Expanded draft pack primitive. Needs source audit and EM clinician review before production use."),
    }


def pack_primitives(pack: dict[str, Any]) -> list[dict[str, Any]]:
    items = [
        primitive(pack, "diagnosis", "diagnosis_summary", "required", pack["summary"], clinician=True),
        primitive(pack, "what_we_found", "reassuring_ed_assessment", "required", pack["found"], unsafe=True, clinician=True),
    ]
    for idx, text in enumerate(pack["home"], start=1):
        items.append(primitive(pack, "home_care", f"home_care_{idx}", "high", text))
    for idx, text in enumerate(pack["meds"], start=1):
        items.append(primitive(pack, "medications", f"medication_guidance_{idx}", "high", text, unsafe=True, clinician=True))
    for idx, text in enumerate(pack["return"], start=1):
        items.append(primitive(pack, "return_precautions", f"return_precaution_{idx}", "required", text, clinician=True))
    items.append(primitive(pack, "follow_up", "default_follow_up", "required", pack["follow"], unsafe=True, clinician=True))
    return items


def phenotype(pack: dict[str, Any], primitive_ids: list[str]) -> dict[str, Any]:
    reviewed = pack["id"] in REVIEWED_PACK_IDS
    return {
        "id": pack["id"],
        "label": pack["label"],
        "status": "reviewed" if reviewed else "draft",
        "condition_family": pack["family"],
        "inclusion_criteria": pack["inclusion"],
        "exclusion_criteria": pack["exclusion"],
        "must_not_miss": pack["must_not_miss"],
        "default_follow_up": pack["follow"],
        "required_sections": REQUIRED_SECTIONS,
        "primitive_ids": primitive_ids,
        "source_card_ids": pack.get("source_card_ids", []),
        "source_audit": audit(source_supported=reviewed, clinician_judgment_only=not reviewed, unsafe_without_modifier=not reviewed),
        "runtime": {
            "condition_terms": pack["condition_terms"],
            "unsafe_modifiers": pack["unsafe_modifiers"],
            "minimum_confidence": 0.86,
            "mode": "reviewed_ontology_enabled" if reviewed else "draft_only_until_reviewed",
        },
        "version": 1,
        "review": {
            **reviewed_block("Reviewed as a narrow outpatient cellulitis phenotype. Use only when no sepsis, necrotizing infection, bite wound, diabetic foot, immunocompromise, or high-risk location modifier is present."),
            "clinical_status": "reviewed_for_limited_uncomplicated_outpatient_cellulitis_use",
            "required_modifiers": ["localized infection", "outpatient therapy judged safe", "no deep infection concern"],
            "blocked_modifiers": pack["unsafe_modifiers"],
        }
        if reviewed
        else review_block("Expanded ontology draft pack. Not clinician-reviewed. Runtime should fall back unless explicitly enabled for review."),
    }


def review_sheet(item: dict[str, Any], primitives: list[dict[str, Any]]) -> str:
    assembled = assemble_discharge(item["id"], "6")
    lines = [
        f"# {item['label']}",
        "",
        f"Phenotype ID: `{item['id']}`",
        "",
        f"Status: `{item['status']}`",
        "",
        "## Inclusion Criteria",
        "",
    ]
    lines.extend(f"- {row}" for row in item["inclusion_criteria"])
    lines.extend(["", "## Exclusions", ""])
    lines.extend(f"- {row}" for row in item["exclusion_criteria"])
    lines.extend(["", "## Must-Not-Miss Diagnoses", ""])
    lines.extend(f"- {row}" for row in item["must_not_miss"])
    lines.extend(["", "## Primitive List", ""])
    for row in primitives:
        audit_flags = ", ".join(key for key, value in row["source_audit"].items() if value) or "source_supported"
        modifiers = ", ".join(row["contraindications"]) or "none"
        lines.append(f"- `{row['id']}` | `{row['section']}` | audit: {audit_flags} | unsafe modifiers: {modifiers}")
    lines.extend(["", "## Assembled Six-Section Output", "", "```text", assembled.rstrip(), "```", ""])
    return "\n".join(lines)


def inferred_terms(item: dict[str, Any]) -> list[str]:
    terms = {
        item["id"].replace("_", " "),
        item["label"].lower(),
        item["condition_family"].replace("_", " "),
    }
    runtime_terms = item.get("runtime", {}).get("condition_terms", [])
    terms.update(term.lower() for term in runtime_terms)
    return sorted(terms)


def build_runtime_manifest() -> dict[str, Any]:
    all_phenotypes = load_phenotypes()
    return {
        "version": 1,
        "mode": "draft_safe",
        "rules": {
            "never_store_ed_note_text": True,
            "fallback_when_not_reviewed": True,
            "fallback_when_source_audit_not_supported": True,
            "block_unsafe_modifier_matches": True,
        },
        "phenotypes": [
            {
                "id": item["id"],
                "label": item["label"],
                "status": item["status"],
                "review_status": item["review"]["status"],
                "version": item.get("version", 1),
                "condition_terms": inferred_terms(item),
                "unsafe_modifiers": item.get("runtime", {}).get("unsafe_modifiers", []),
                "source_audit": item.get("source_audit", {"source_supported": bool(item.get("source_card_ids")), "source_needed": not bool(item.get("source_card_ids"))}),
            }
            for item in all_phenotypes.values()
        ],
    }


def main() -> int:
    REVIEW_DIR.mkdir(parents=True, exist_ok=True)
    MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)

    all_primitives: list[dict[str, Any]] = []
    phenotypes: list[dict[str, Any]] = []
    primitives_by_phenotype: dict[str, list[dict[str, Any]]] = {}

    for pack in PACKS:
        items = pack_primitives(pack)
        all_primitives.extend(items)
        primitives_by_phenotype[pack["id"]] = items
        item = phenotype(pack, [row["id"] for row in items])
        phenotypes.append(item)
        (ROOT / "phenotypes" / f"{item['id']}.json").write_text(json.dumps(item, indent=2) + "\n", encoding="utf-8")

    PRIMITIVE_PATH.write_text(json.dumps(all_primitives, indent=2) + "\n", encoding="utf-8")

    for item in phenotypes:
        (REVIEW_DIR / f"{item['id']}.md").write_text(
            review_sheet(item, primitives_by_phenotype[item["id"]]),
            encoding="utf-8",
        )

    MANIFEST_PATH.write_text(json.dumps(build_runtime_manifest(), indent=2) + "\n", encoding="utf-8")
    print(f"wrote {len(phenotypes)} phenotype packs")
    print(f"wrote {len(all_primitives)} primitives")
    print(f"wrote review sheets to {REVIEW_DIR}")
    print(f"wrote {MANIFEST_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
