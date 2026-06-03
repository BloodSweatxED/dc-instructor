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
        "home": ["Rest today and increase activity slowly.", "Avoid alcohol or sedating drugs unless your clinician says they are safe.", "Have a trusted person check on you if possible.", "Limit screens, loud environments, and strenuous activity if they worsen symptoms."],
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
        "home": ["Drink fluids as you are able.", "Use a urine strainer if one was given.", "Save any passed stone if your clinician asked you to.", "Avoid dehydration until follow-up."],
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
        "summary": "You had an asthma flare-up that made it hard to breathe.",
        "found": "You came to the ED because your asthma got worse. We gave you breathing treatments that opened your airways and steroids to calm lung swelling. After treatment, you were breathing comfortably on your own and were safe to go home.",
        "home": ["Rest for the next 1-2 days and avoid hard exercise until your breathing feels normal.", "Stay away from things that trigger your asthma, like smoke, strong smells, cold air, dust, mold, pet dander, humidity, or exercise in cold air.", "Always use a spacer with your rescue inhaler if you have one. It gets more medicine into your lungs.", "Start activity slowly as your breathing improves.", "If you have a peak flow meter, use it to track your breathing at home.", "Wash your hands and avoid sick contacts when you can."],
        "meds": ["Use your rescue inhaler as prescribed.", "If you have a controller inhaler, keep taking it even when you feel better. It helps prevent the next flare.", "Take the steroid course if one was prescribed.", "Do not wait at home if your rescue inhaler is not helping."],
        "return": ["You need your inhaler more often than instructed.", "Your breathing gets worse or you feel short of breath at rest.", "You cannot speak in full sentences because of shortness of breath.", "Your lips or fingernails turn blue or gray.", "You have chest pain, confusion, fainting, or severe sleepiness."],
        "follow": "See your primary care doctor or asthma clinician within 3-5 days, or sooner if symptoms are not improving. If you do not have a written asthma action plan, ask for one at follow-up.",
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
        "home": ["Rest and increase activity slowly.", "Drink fluids if you are allowed.", "Use warm liquids or steam if they help cough or mucus.", "Avoid smoking and smoke exposure."],
        "meds": ["Take antibiotics exactly as prescribed.", "Use fever or pain medicine only if you can take it safely and follow the label."],
        "return": ["Worse trouble breathing, blue lips, confusion, fainting, or chest pain.", "Fever or symptoms worsen after starting treatment.", "You cannot keep medicines or fluids down."],
        "follow": "Follow up with primary care as instructed.",
        "inclusion": ["Pneumonia judged stable for outpatient treatment.", "No hypoxia, sepsis, or admission need at discharge."],
        "exclusion": ["Hypoxia.", "Sepsis.", "Immunocompromised host.", "High-risk comorbidity or unreliable outpatient plan."],
        "must_not_miss": ["Sepsis.", "Pulmonary embolism mimic.", "Heart failure mimic.", "Empyema.", "Hypoxic respiratory failure."],
        "unsafe_modifiers": ["hypoxia", "immunocompromised", "elderly_frail", "sepsis", "poor_follow_up"],
    },
    {
        "id": "acute_bronchitis_no_pneumonia",
        "label": "Acute bronchitis or chest cold without pneumonia concern",
        "family": "respiratory_infection",
        "condition_terms": [
            "acute bronchitis",
            "acute bronchitis no pneumonia",
            "chest cold",
            "viral bronchitis",
            "bronchitis without pneumonia concern",
        ],
        "source_card_ids": [
            "cdc.acute_bronchitis",
            "medlineplus.acute_bronchitis",
            "cdc.antibiotic_use_adult_outpatient",
        ],
        "status": "needs_review",
        "review_status": "needs_review",
        "source_supported": True,
        "source_audit_notes": "CDC and MedlinePlus support acute bronchitis and chest cold framing, viral predominance, supportive care, and escalation for worsening breathing symptoms. CDC outpatient guidance supports keeping pneumonia concern, abnormal vital signs, and focal lung findings outside uncomplicated bronchitis.",
        "review_notes": "Phase 31 draft only. Narrow runtime recognition is allowed for review stress testing, but patient-facing output must not run in ontology mode until EM clinician review promotes it.",
        "summary": "Your symptoms fit acute bronchitis, also called a chest cold.",
        "found": "Your ED evaluation did not show a pneumonia concern that needed a separate treatment plan today.",
        "home": [
            "Rest as needed and increase activity slowly as breathing feels comfortable.",
            "Drink fluids if you are allowed to and use warm liquids or humidified air if they ease cough.",
            "Avoid smoke and strong fumes while your airways are irritated.",
        ],
        "meds": [
            "Antibiotics do not help most acute bronchitis cases unless your clinician found a bacterial infection.",
            "Use only the medicines your clinician prescribed or said are safe for you.",
        ],
        "return": [
            "Trouble breathing, shortness of breath at rest, blue lips, confusion, fainting, or severe weakness.",
            "Chest pain concerning for the heart or blood clot, coughing blood, or symptoms that feel much worse.",
            "Fever, worsening cough, or new pneumonia concern after discharge.",
        ],
        "follow": "Follow up with primary care as instructed, especially if symptoms are not improving or you have higher-risk lung or immune problems.",
        "inclusion": [
            "Adult with cough or chest cold symptoms.",
            "Clinician diagnosis or discharge impression is acute bronchitis, chest cold, or viral bronchitis.",
            "No pneumonia diagnosis or focal pneumonia concern documented at discharge.",
            "Oxygenation and work of breathing acceptable for discharge.",
            "No unstable vital signs, sepsis concern, or admission need.",
        ],
        "exclusion": [
            "Hypoxia, respiratory distress, unstable vital signs, sepsis concern, or admission need.",
            "Pneumonia diagnosis, infiltrate, consolidation, focal lung findings, or unresolved focal pneumonia concern.",
            "COPD or asthma exacerbation requiring a disease-specific pathway.",
            "Immunocompromised or frail elderly patient requiring individualized planning.",
            "Hemoptysis or chest pain concerning for cardiac disease or pulmonary embolism.",
            "Antibiotics prescribed for suspected bacterial infection.",
        ],
        "must_not_miss": [
            "Pneumonia.",
            "Hypoxic respiratory failure.",
            "Asthma or COPD exacerbation.",
            "Pulmonary embolism.",
            "Acute coronary syndrome.",
            "Sepsis.",
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
        "high_confidence_terms": [
            "acute bronchitis",
            "acute bronchitis no pneumonia",
            "chest cold",
            "viral bronchitis",
        ],
    },
    {
        "id": "acute_sinusitis_supportive_care",
        "label": "Acute sinusitis supportive care without antibiotic plan",
        "family": "upper_respiratory",
        "condition_terms": [
            "acute sinusitis supportive care",
            "sinus infection supportive care",
            "acute sinusitis",
            "sinus infection",
            "rhinosinusitis supportive care",
        ],
        "source_card_ids": [
            "cdc.sinus_infection",
            "medlineplus.sinusitis",
            "cdc.antibiotic_use_adult_outpatient",
        ],
        "status": "needs_review",
        "review_status": "needs_review",
        "source_supported": True,
        "source_audit_notes": "CDC and MedlinePlus support sinusitis framing, symptom-based diagnosis, supportive care, and seeking care for severe or concerning symptoms. CDC outpatient guidance supports that most rhinosinusitis is viral, that antibiotics may not help many cases, and that bacterial-feature or antibiotic decisions require clinician judgment.",
        "review_notes": "Phase 38 draft only. Supportive-care sinusitis has a narrower runtime boundary than broad sinus symptoms, but antibiotic/watchful-waiting decisions still require clinician review before promotion.",
        "summary": "Your symptoms fit acute sinusitis, also called a sinus infection.",
        "found": "Your clinician did not document an emergency sinus complication or a need for an antibiotic plan in these discharge instructions.",
        "home": [
            "Drink fluids if you are allowed to and rest as needed.",
            "Use saline spray or humidified air if it helps congestion.",
            "A warm compress over the sore sinus area may help pressure.",
        ],
        "meds": [
            "Use only the medicines your clinician prescribed or said are safe for you.",
            "Do not start leftover antibiotics unless your clinician tells you to.",
        ],
        "return": [
            "Trouble breathing, confusion, fainting, stiff neck, severe headache, or feeling very ill.",
            "Swelling around the eye, vision changes, double vision, or pain with eye movement.",
            "Fever, worsening facial pain, or symptoms that get much worse after initially improving.",
        ],
        "follow": "Follow up with primary care or ENT as instructed, especially if symptoms are not improving or keep coming back.",
        "inclusion": [
            "Adult with clinician diagnosis or discharge impression of acute sinusitis, sinus infection, or acute rhinosinusitis.",
            "Supportive-care discharge plan without clinician-entered antibiotic instructions.",
            "No orbital, intracranial, dental, facial trauma, sepsis, or airway emergency concern.",
            "No chronic or recurrent sinusitis pathway.",
        ],
        "exclusion": [
            "Antibiotics prescribed for sinusitis or suspected bacterial sinus infection.",
            "Severe bacterial sinusitis features requiring clinician-specific antibiotic or watchful-waiting decision.",
            "Orbital or intracranial complication concern, including eye swelling, vision change, severe headache with neurologic symptoms, meningitis concern, or altered mental status.",
            "Dental source, facial trauma, immunocompromise, sepsis, unstable vital signs, pregnancy, or frail elderly patient requiring individualized planning.",
            "Chronic, recurrent, fungal, post-surgical, or ENT-directed sinusitis pathway.",
        ],
        "must_not_miss": [
            "Orbital cellulitis.",
            "Intracranial infection.",
            "Meningitis.",
            "Dental abscess.",
            "Sepsis.",
            "Facial trauma.",
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
        "high_confidence_terms": [
            "acute sinusitis supportive care",
            "sinus infection supportive care",
        ],
    },
    {
        "id": "conjunctivitis_uncomplicated_no_contact_lens",
        "label": "Uncomplicated conjunctivitis without contact lens or red flags",
        "family": "eye",
        "condition_terms": [
            "conjunctivitis uncomplicated",
            "pink eye uncomplicated",
            "conjunctivitis no contact lens",
            "pink eye no contact lens",
        ],
        "source_card_ids": [
            "cdc.conjunctivitis",
            "medlineplus.conjunctivitis",
        ],
        "status": "retired",
        "review_status": "retired",
        "source_supported": True,
        "source_audit_notes": "CDC and MedlinePlus support conjunctivitis framing, hygiene and spread prevention, common symptoms, and escalation for pain, light sensitivity, blurred vision, intense redness, contact lens use, or worsening symptoms.",
        "runtime_mode": "retired_product_layer_fallback_only",
        "review_notes": "Phase 54 retired this draft to product-layer fallback. Eye complaints remain too high-risk for static ontology mode without explicit clinician review of contact-lens, corneal, chemical, glaucoma, trauma, vision, photophobia, herpes/zoster, cellulitis, immunocompromise, and pregnancy boundaries.",
        "summary": "Your symptoms fit conjunctivitis, also called pink eye.",
        "found": "Your clinician did not document contact lens risk, eye injury, vision loss, or another eye emergency in these discharge instructions.",
        "home": [
            "Wash your hands often and avoid touching or rubbing the eye.",
            "Do not share towels, pillowcases, makeup, or eye drops.",
            "Use a clean warm or cool compress if your clinician said it is safe.",
        ],
        "meds": [
            "Use only the eye drops or medicines your clinician prescribed or said are safe for you.",
            "Do not use contact lenses until your clinician says it is safe.",
        ],
        "return": [
            "Eye pain, light sensitivity, vision changes, or worsening redness.",
            "Swelling around the eye, trouble moving the eye, fever, or feeling very ill.",
            "Symptoms get worse, do not improve as expected, or you were exposed to chemicals or an eye injury."
        ],
        "follow": "Follow up with primary care, urgent care, or an eye clinician as instructed.",
        "inclusion": [
            "Adult with clinician diagnosis or discharge impression of conjunctivitis or pink eye.",
            "No contact lens use documented.",
            "No eye trauma, foreign body, chemical exposure, corneal ulcer or keratitis concern, acute glaucoma mimic, severe pain, photophobia, vision change, herpes/zoster concern, or orbital/periorbital cellulitis concern.",
        ],
        "exclusion": [
            "Contact lens use.",
            "Eye trauma, foreign body, chemical exposure, corneal abrasion, corneal ulcer, or keratitis concern.",
            "Severe eye pain, photophobia, vision change, proptosis, pain with eye movement, or periorbital/orbital cellulitis concern.",
            "Herpes or zoster eye concern.",
            "Immunocompromised host, pregnancy, infant/pediatric pathway, or specialist-directed ophthalmology plan.",
        ],
        "must_not_miss": [
            "Keratitis or corneal ulcer.",
            "Corneal abrasion or foreign body.",
            "Acute glaucoma.",
            "Uveitis or iritis.",
            "Herpes or zoster eye disease.",
            "Orbital cellulitis.",
        ],
        "unsafe_modifiers": [
            "contact_lens_use",
            "chemical_eye_exposure",
            "corneal_ulcer_or_keratitis_concern",
            "acute_glaucoma_mimic",
            "eye_trauma_or_foreign_body",
            "severe_eye_pain",
            "photophobia",
            "vision_change",
            "herpes_or_zoster_eye_concern",
            "periorbital_or_orbital_cellulitis_concern",
            "immunocompromised",
            "pregnancy",
        ],
        "high_confidence_terms": [
            "conjunctivitis uncomplicated",
            "pink eye uncomplicated",
            "conjunctivitis no contact lens",
            "pink eye no contact lens",
        ],
    },
    {
        "id": "otitis_externa_no_mastoiditis",
        "label": "Uncomplicated otitis externa without mastoiditis concern",
        "family": "ear",
        "condition_terms": [
            "otitis externa uncomplicated",
            "swimmer's ear uncomplicated",
            "swimmers ear uncomplicated",
            "otitis externa no mastoiditis",
        ],
        "source_card_ids": [
            "cdc.swimmers_ear",
            "medlineplus.swimmers_ear",
        ],
        "status": "retired",
        "review_status": "retired",
        "source_supported": True,
        "source_audit_notes": "CDC and MedlinePlus support swimmer's ear/otitis externa framing, ear-canal infection symptoms, drying/prevention concepts, treatment with clinician-directed drops, and escalation for fever, symptoms behind the ear, severe symptoms, or worsening illness.",
        "runtime_mode": "retired_product_layer_fallback_only",
        "review_notes": "Phase 64 retired this draft to product-layer fallback. Do not use broad ear pain or ear drainage as standalone runtime terms. Keep mastoiditis, malignant otitis externa risk, perforation/tube, ear trauma/foreign body, acute hearing loss, facial weakness, and systemic illness outside ontology mode unless later reviewed.",
        "summary": "Your symptoms fit otitis externa, also called swimmer's ear.",
        "found": "Your clinician did not document mastoiditis concern, a deep ear infection, eardrum rupture, or another ear emergency in these discharge instructions.",
        "home": [
            "Keep the ear dry unless your clinician told you something different.",
            "Do not put cotton swabs, earbuds, or other objects into the ear canal.",
            "Avoid swimming until your clinician says it is safe.",
        ],
        "meds": [
            "Use ear drops only as prescribed.",
            "Use acetaminophen or ibuprofen only if you can take it safely and follow the label.",
        ],
        "return": [
            "Fever, worsening pain, severe headache, confusion, or feeling very ill.",
            "Redness, swelling, or pain behind the ear, or the ear starts sticking out.",
            "New hearing loss, dizziness, facial weakness, or drainage that gets worse.",
        ],
        "follow": "Follow up with primary care, urgent care, or an ear clinician as instructed.",
        "inclusion": [
            "Adult with clinician diagnosis or discharge impression of uncomplicated otitis externa or swimmer's ear.",
            "No mastoiditis, malignant otitis externa, middle-ear complication, ear trauma, foreign body, acute hearing loss, facial weakness, or systemic illness concern documented.",
        ],
        "exclusion": [
            "Mastoiditis, deep ear infection, skull base osteomyelitis, or malignant otitis externa concern.",
            "Diabetes, immunocompromised host, severe systemic illness, unstable vital signs, or fever needing separate planning.",
            "Perforated eardrum, tympanostomy tube, ear trauma, ear foreign body, acute hearing loss, vertigo, facial weakness, or specialist-directed ENT plan.",
        ],
        "must_not_miss": [
            "Mastoiditis.",
            "Malignant otitis externa.",
            "Skull base osteomyelitis.",
            "Perforated tympanic membrane.",
            "Ear foreign body.",
            "Sudden sensorineural hearing loss.",
        ],
        "unsafe_modifiers": [
            "mastoiditis_or_deep_ear_infection_concern",
            "malignant_otitis_externa_risk",
            "immunocompromised",
            "fever",
            "unstable_vitals",
            "tympanic_membrane_perforation_or_tube",
            "ear_trauma_or_foreign_body",
            "acute_hearing_loss",
            "facial_weakness_or_neurologic_ear_sign",
        ],
        "high_confidence_terms": [
            "otitis externa uncomplicated",
            "swimmer's ear uncomplicated",
            "swimmers ear uncomplicated",
            "otitis externa no mastoiditis",
        ],
    },
    {
        "id": "epistaxis_resolved_no_posterior_bleed",
        "label": "Resolved nosebleed without posterior bleed concern",
        "family": "ent",
        "condition_terms": [
            "epistaxis resolved",
            "nosebleed resolved",
            "resolved nosebleed no posterior bleed",
            "epistaxis resolved no posterior bleed",
        ],
        "source_card_ids": [
            "medlineplus.nosebleed",
            "aao_hns.nosebleed_guideline",
        ],
        "status": "retired",
        "review_status": "retired",
        "source_supported": True,
        "source_audit_notes": "MedlinePlus supports nosebleed first-aid concepts and when to seek care. AAO-HNS supports clinician-facing epistaxis guideline concepts, but ED discharge risk stratification still requires local clinician review.",
        "runtime_mode": "retired_product_layer_fallback_only",
        "review_notes": "Phase 70 retired this draft to product-layer fallback. Do not use broad bleeding or nasal complaint terms. Keep posterior bleeding, continued bleeding, anticoagulation, bleeding disorder, facial/nasal trauma, airway symptoms, unstable vitals, and anemia/syncope concern outside ontology mode unless later reviewed.",
        "summary": "You were treated for a nosebleed that stopped.",
        "found": "Your clinician did not document ongoing bleeding, posterior nosebleed concern, major trauma, or another emergency bleeding problem in these discharge instructions.",
        "home": [
            "Do not blow or pick your nose today.",
            "Keep your head above your heart when resting.",
            "Use the nasal moisture plan your clinician recommended if one was given.",
        ],
        "meds": [
            "Use only nasal sprays or medicines your clinician prescribed or said are safe.",
            "Do not stop blood thinners unless the clinician who prescribes them tells you to.",
        ],
        "return": [
            "Bleeding starts again and will not stop with firm pressure.",
            "Blood runs down your throat, you vomit blood, or you have trouble breathing.",
            "You feel faint, weak, confused, have chest pain, or bleeding follows an injury.",
        ],
        "follow": "Follow up with primary care or ENT as instructed, especially if nosebleeds keep happening.",
        "inclusion": [
            "Adult with clinician diagnosis or discharge impression of epistaxis or nosebleed that resolved before discharge.",
            "No posterior bleed concern, active bleeding, facial trauma, anticoagulation complication, bleeding disorder, airway issue, or unstable vital signs documented.",
        ],
        "exclusion": [
            "Posterior epistaxis, ongoing bleeding, packing requiring specific plan, or recurrent severe bleed.",
            "Anticoagulation complication, bleeding disorder, anemia/syncope concern, unstable vital signs, or airway symptoms.",
            "Facial or nasal trauma, suspected fracture, or specialist-directed ENT plan.",
        ],
        "must_not_miss": [
            "Posterior epistaxis.",
            "Hemorrhagic shock.",
            "Facial fracture.",
            "Airway compromise.",
            "Coagulopathy or anticoagulation complication.",
        ],
        "unsafe_modifiers": [
            "posterior_epistaxis_or_uncontrolled_bleeding",
            "anticoagulated",
            "bleeding_disorder",
            "facial_or_nasal_trauma",
            "airway_symptoms",
            "unstable_vitals",
            "syncope",
        ],
        "high_confidence_terms": [
            "epistaxis resolved",
            "nosebleed resolved",
            "epistaxis resolved no posterior bleed",
        ],
    },
    {
        "id": "migraine_improved_discharge",
        "label": "Migraine improved after ED treatment",
        "family": "headache",
        "condition_terms": [
            "migraine improved discharge",
            "migraine improved",
            "migraine headache improved",
            "migraine discharged",
        ],
        "source_card_ids": [
            "medlineplus.migraine",
            "ninds.headache",
        ],
        "status": "needs_review",
        "review_status": "needs_review",
        "source_supported": True,
        "source_audit_notes": "MedlinePlus supports migraine symptom and treatment concepts. NINDS headache education supports secondary-headache warning concepts, including post-traumatic headache and systemic or neurologic concern. ED discharge risk stratification requires clinician review.",
        "review_notes": "Phase 84 clinician review status: revise, not ready for promotion. Require structured improvement and structured red-flag absence before any later promotion. Do not infer red-flag absence from missing documentation.",
        "summary": "Your clinician diagnosed your headache as a migraine. Your symptoms improved with treatment.",
        "found": "Your ED team treated your migraine and confirmed that you were improved enough to go home with this plan.",
        "home": [
            "Rest in a quiet, dark place if symptoms return.",
            "Drink more fluids if you can and avoid triggers you already know affect you.",
            "Limit screen time, bright light, noise, and heavy mental stimulation while you are recovering.",
            "Use stress reduction techniques that work for you, such as slow breathing, quiet rest, or gentle stretching.",
            "Avoid driving or operating heavy machinery until you feel fully alert and your thinking is clear.",
            "Most people feel better within one to two days. Fatigue and trouble concentrating can last up to 48 hours after a migraine resolves.",
            "Keep a headache log. Write down or record on your phone when headaches start, how long they last, how severe they are, and any symptoms that come with them. Bring this log to your follow-up visit.",
        ],
        "meds": [
            "Use only the headache medicines your clinician prescribed or said are safe for you.",
            "Do not take extra doses or mix medicines unless your clinician told you to.",
        ],
        "return": [
            "A sudden, severe headache that reaches its worst point within seconds, or feels like the worst headache of your life; headache after injury; fainting; confusion; seizure; or trouble staying awake.",
            "New weakness, numbness, trouble speaking, vision loss, trouble walking, fever, or stiff neck.",
            "Vomiting that will not stop, headache that is much worse or different than usual, or symptoms that do not improve as expected.",
        ],
        "follow": "Follow up with primary care or a headache clinician as instructed, especially if headaches are new, changing, or frequent.",
        "inclusion": [
            "Adult with clinician diagnosis or discharge impression of migraine that improved after ED treatment.",
            "Structured confirmation of clinical improvement after ED treatment is present.",
            "Structured confirmation that headache red flags are absent is present.",
        ],
        "exclusion": [
            "Sudden, severe headache that reaches its worst point within seconds, worst headache of life, subarachnoid hemorrhage concern, stroke/TIA concern, unresolved neurologic deficit, seizure, or altered mental status not fully resolved at discharge.",
            "Fever with headache, neck stiffness, meningitis/encephalitis concern, pregnancy, immunocompromise, head trauma within 7 days, age over 50 with new headache pattern, or unstable vital signs.",
            "Uncontrolled vomiting at discharge, specialist-directed neurology plan, headache not improved enough for discharge, first-lifetime headache of this severity, or CT not performed when documented concern exists.",
        ],
        "must_not_miss": [
            "Subarachnoid hemorrhage.",
            "Stroke or TIA.",
            "Meningitis or encephalitis.",
            "Intracranial mass or elevated intracranial pressure.",
            "Cerebral venous thrombosis.",
            "Pre-eclampsia in pregnancy.",
        ],
        "unsafe_modifiers": [
            "thunderclap_or_sah_concern",
            "neurologic_deficit",
            "meningitis_or_cns_infection_concern",
            "fracture_or_trauma_concern",
            "pregnancy",
            "immunocompromised",
            "age_over_50_new_headache",
            "uncontrolled_vomiting",
            "unstable_vitals",
            "altered_mental_status_not_resolved",
            "first_lifetime_severe_headache",
            "ct_not_performed_with_headache_concern",
        ],
        "high_confidence_terms": [
            "migraine improved discharge",
            "migraine improved",
            "migraine headache improved",
        ],
    },
    {
        "id": "chest_pain_low_risk_negative_ed_workup",
        "label": "Low-risk chest pain after negative ED workup",
        "family": "cardiovascular",
        "condition_terms": ["low risk chest pain", "chest pain", "negative cardiac workup"],
        "status": "retired",
        "review_status": "retired",
        "source_card_ids": ["aha.chest_pain_warning_signs"],
        "source_supported": True,
        "source_audit_notes": "AHA supports chest pain warning-sign education, but not static low-risk ED risk stratification. This draft is retired from ontology expansion and should remain product-layer fallback unless later rebuilt as a narrower reviewed phenotype.",
        "runtime_mode": "retired_product_layer_fallback_only",
        "review_notes": "Phase 22 retired this broad static ontology draft. Chest pain risk stratification depends on ECG, troponin, protocol, local follow-up, and clinician judgment; use product-layer fallback unless rebuilt as a narrower source-supported phenotype.",
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
        "label": "Abdominal pain recheck after reassuring ED evaluation",
        "family": "gastrointestinal",
        "condition_terms": ["abdominal pain recheck", "abdominal pain reassuring evaluation", "belly pain recheck", "nonspecific abdominal pain"],
        "source_card_ids": ["medlineplus.abdominal_pain", "medlineplus.abdominal_pain_ency"],
        "status": "needs_review",
        "review_status": "needs_review",
        "source_supported": True,
        "source_audit_notes": "MedlinePlus supports general abdominal pain framing, cautious home care, and conservative return precautions. Phase 23 narrows this to recheck and return-precaution guidance after a reassuring ED evaluation; it still requires clinician review before runtime use.",
        "review_notes": "Phase 25 clinician feedback applied. Narrowed abdominal pain draft is approved as a review candidate only, with runtime gates still required and no promotion yet.",
        "summary": "You were evaluated for abdominal pain today.",
        "found": "We did not find an emergency cause that needed surgery or admission, but abdominal pain can change after you leave.",
        "home": ["Use the food and fluid plan your clinician gave you.", "Start with small sips and light foods if your stomach feels upset.", "Do not ignore symptoms that are getting worse just because today's evaluation was reassuring."],
        "meds": ["Take prescribed nausea or stomach medicine exactly as directed.", "Use pain medicine only as instructed by your clinician. Do not take extra doses to cover worsening pain."],
        "return": ["Worsening, severe, or one-sided belly pain.", "Repeated vomiting, fainting, confusion, fever, bloody stool, black stool, or vomiting blood.", "A swollen hard belly, pain going to the shoulder or back, or any pregnancy concern."],
        "follow": "Return for recheck as your clinician instructed.",
        "inclusion": [
            "Abdominal pain evaluated in the ED with a reassuring exam and workup at discharge.",
            "No current surgical abdomen, unstable vital signs, or admission need.",
            "Patient discharged with explicit clinician-directed recheck plan.",
        ],
        "exclusion": [
            "Pregnancy or pregnancy concern.",
            "Localized or worsening pain concerning for appendicitis, obstruction, ischemia, perforation, or other surgical abdomen.",
            "Uncontrolled pain, repeated vomiting, fever, GI bleeding, sepsis concern, frailty, immunocompromise, or unreliable follow-up."
        ],
        "must_not_miss": ["Appendicitis.", "Bowel obstruction.", "Bowel ischemia.", "Perforation.", "Ectopic pregnancy.", "AAA.", "Sepsis."],
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
    source_supported = reviewed or bool(pack.get("source_supported"))
    review_status = pack.get("review_status", "draft")
    return {
        "id": primitive_id,
        "phenotypes": [pack["id"]],
        "section": section,
        "primitive_type": kind,
        "priority": priority,
        "text": {"en_4": text, "en_6": text, "en_hl1": text},
        "contraindications": pack["unsafe_modifiers"] if unsafe else [],
        "source_card_ids": pack.get("source_card_ids", []),
        "source_audit": {
            **audit(source_supported=source_supported, clinician_judgment_only=clinician, unsafe_without_modifier=unsafe),
            **({"notes": pack["source_audit_notes"]} if pack.get("source_audit_notes") else {}),
        },
        "review": reviewed_block("Reviewed for cellulitis_uncomplicated_oral_antibiotics v1. Patient-facing text is locally authored from source-supported concepts.")
        if reviewed
        else {**review_block(pack.get("review_notes", "Expanded draft pack primitive. Needs source audit and EM clinician review before production use.")), "status": review_status},
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
    source_supported = reviewed or bool(pack.get("source_supported"))
    status = "reviewed" if reviewed else pack.get("status", "draft")
    review_status = "reviewed" if reviewed else pack.get("review_status", "draft")
    return {
        "id": pack["id"],
        "label": pack["label"],
        "status": status,
        "condition_family": pack["family"],
        "inclusion_criteria": pack["inclusion"],
        "exclusion_criteria": pack["exclusion"],
        "must_not_miss": pack["must_not_miss"],
        "default_follow_up": pack["follow"],
        "required_sections": REQUIRED_SECTIONS,
        "primitive_ids": primitive_ids,
        "source_card_ids": pack.get("source_card_ids", []),
        "source_audit": {
            **audit(source_supported=source_supported, clinician_judgment_only=not reviewed, unsafe_without_modifier=not reviewed),
            **({"notes": pack["source_audit_notes"]} if pack.get("source_audit_notes") else {}),
        },
        "runtime": {
            "condition_terms": pack["condition_terms"],
            "unsafe_modifiers": pack["unsafe_modifiers"],
            **({"required_context": pack["required_context"]} if pack.get("required_context") else {}),
            **({"high_confidence_terms": pack["high_confidence_terms"]} if pack.get("high_confidence_terms") else {}),
            "minimum_confidence": 0.86,
            "mode": "reviewed_ontology_enabled" if reviewed else pack.get("runtime_mode", "draft_only_until_reviewed"),
        },
        "version": 1,
        "review": {
            **reviewed_block("Reviewed as a narrow outpatient cellulitis phenotype. Use only when no sepsis, necrotizing infection, bite wound, diabetic foot, immunocompromise, or high-risk location modifier is present."),
            "clinical_status": "reviewed_for_limited_uncomplicated_outpatient_cellulitis_use",
            "required_modifiers": ["localized infection", "outpatient therapy judged safe", "no deep infection concern"],
            "blocked_modifiers": pack["unsafe_modifiers"],
        }
        if reviewed
        else {**review_block(pack.get("review_notes", "Expanded ontology draft pack. Not clinician-reviewed. Runtime should fall back unless explicitly enabled for review.")), "status": review_status},
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
    }
    family_term = item["condition_family"].replace("_", " ")
    if len(family_term.split()) > 1:
        terms.add(family_term)
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
                "required_context": item.get("runtime", {}).get("required_context", []),
                "high_confidence_terms": item.get("runtime", {}).get("high_confidence_terms", []),
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
