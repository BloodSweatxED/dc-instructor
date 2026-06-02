#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PRIMITIVE_PATH = ROOT / "primitives" / "expanded_draft_packs.json"
TEXT_KEYS = ("en_4", "en_6", "en_hl1")


OVERRIDES: dict[str, str] = {
    "abscess_after_i_and_d.diagnosis.diagnosis_summary.v1": "You had an abscess, which is a pocket of pus under the skin.",
    "abscess_after_i_and_d.what_we_found.reassuring_ed_assessment.v1": "You came to the ED because the area was painful and swollen. We opened and drained the abscess, which is the main treatment. You were safe to go home with wound care instructions.",
    "abscess_after_i_and_d.home_care.home_care_1.v1": "Keep the dressing clean and dry today.",
    "abscess_after_i_and_d.home_care.home_care_2.v1": "Wash your hands before and after touching the wound.",
    "abscess_after_i_and_d.home_care.home_care_3.v1": "Do not squeeze, dig into, or try to drain the wound again at home.",
    "abscess_after_i_and_d.medications.medication_guidance_1.v1": "Take antibiotics only if they were prescribed.",
    "abscess_after_i_and_d.medications.medication_guidance_2.v1": "Use pain medicine only if it is safe for you and follow the label or your clinician's instructions.",
    "abscess_after_i_and_d.return_precautions.return_precaution_1.v1": "Come back for fever, spreading redness, red streaks, worsening swelling, or feeling very sick.",
    "abscess_after_i_and_d.return_precautions.return_precaution_2.v1": "Come back for severe pain, numbness, bleeding that will not stop, or pus building back up.",
    "abscess_after_i_and_d.return_precautions.return_precaution_3.v1": "Come back if packing falls out early and you were told it needed to stay in.",
    "abscess_after_i_and_d.follow_up.default_follow_up.v1": "Return or follow up for a wound check as instructed.",

    "allergic_reaction_resolved_no_anaphylaxis.diagnosis.diagnosis_summary.v1": "You were treated for an allergic reaction.",
    "allergic_reaction_resolved_no_anaphylaxis.what_we_found.reassuring_ed_assessment.v1": "You came to the ED with allergy symptoms. The symptoms improved, and we did not find signs of anaphylaxis when you were ready for discharge.",
    "allergic_reaction_resolved_no_anaphylaxis.home_care.home_care_1.v1": "Avoid the trigger if you know what caused the reaction.",
    "allergic_reaction_resolved_no_anaphylaxis.home_care.home_care_2.v1": "Watch for symptoms coming back after you leave.",
    "allergic_reaction_resolved_no_anaphylaxis.home_care.home_care_3.v1": "Do not drive, drink alcohol, or take other sedating medicines after sedating allergy medicine unless your clinician says it is safe.",
    "allergic_reaction_resolved_no_anaphylaxis.medications.medication_guidance_1.v1": "Take allergy medicines as prescribed or as directed on the label.",
    "allergic_reaction_resolved_no_anaphylaxis.medications.medication_guidance_2.v1": "Use an epinephrine injector only if one was prescribed and you were told when to use it.",
    "allergic_reaction_resolved_no_anaphylaxis.return_precautions.return_precaution_1.v1": "Come back right away for trouble breathing, wheezing, throat tightness, tongue or lip swelling, fainting, or severe vomiting.",
    "allergic_reaction_resolved_no_anaphylaxis.return_precautions.return_precaution_2.v1": "Come back if rash or swelling returns quickly or spreads.",
    "allergic_reaction_resolved_no_anaphylaxis.return_precautions.return_precaution_3.v1": "Come back right away if you use epinephrine.",
    "allergic_reaction_resolved_no_anaphylaxis.follow_up.default_follow_up.v1": "Follow up with primary care or an allergy clinician if symptoms continue or the trigger is unclear.",

    "cellulitis_uncomplicated_oral_antibiotics.diagnosis.diagnosis_summary.v1": "You were treated for cellulitis, which is a skin infection.",
    "cellulitis_uncomplicated_oral_antibiotics.what_we_found.reassuring_ed_assessment.v1": "You came to the ED for redness, pain, or swelling of the skin. Your exam fit cellulitis that was safe to treat at home today. We did not find signs of a deeper emergency infection.",
    "cellulitis_uncomplicated_oral_antibiotics.home_care.home_care_1.v1": "Keep the area clean and dry.",
    "cellulitis_uncomplicated_oral_antibiotics.home_care.home_care_2.v1": "Raise the arm or leg when you can to help swelling.",
    "cellulitis_uncomplicated_oral_antibiotics.home_care.home_care_3.v1": "Mark the edge of the redness if your clinician asked you to, so you can tell if it is spreading.",
    "cellulitis_uncomplicated_oral_antibiotics.medications.medication_guidance_1.v1": "Take the antibiotic as prescribed. Do not stop early unless a clinician or pharmacist tells you to.",
    "cellulitis_uncomplicated_oral_antibiotics.medications.medication_guidance_2.v1": "Use pain or fever medicine only if it is safe for you and follow the label.",
    "cellulitis_uncomplicated_oral_antibiotics.return_precautions.return_precaution_1.v1": "Come back for fever, shaking chills, confusion, or feeling very sick.",
    "cellulitis_uncomplicated_oral_antibiotics.return_precautions.return_precaution_2.v1": "Come back if redness spreads fast, pain becomes severe, you notice numbness, pus, or red streaks.",
    "cellulitis_uncomplicated_oral_antibiotics.return_precautions.return_precaution_3.v1": "Come back if the infection is near the eye, genitals, or a joint and gets worse.",
    "cellulitis_uncomplicated_oral_antibiotics.follow_up.default_follow_up.v1": "Arrange a recheck with primary care, urgent care, or the ED as instructed, especially if it is not improving.",

    "community_acquired_pneumonia_outpatient.diagnosis.diagnosis_summary.v1": "You were treated for pneumonia, which is an infection in the lungs.",
    "community_acquired_pneumonia_outpatient.what_we_found.reassuring_ed_assessment.v1": "You came to the ED with symptoms of a lung infection. Your oxygen level and overall condition were reassuring enough to treat this at home today.",
    "community_acquired_pneumonia_outpatient.home_care.home_care_1.v1": "Rest and increase activity slowly as your breathing and energy improve.",
    "community_acquired_pneumonia_outpatient.home_care.home_care_2.v1": "Drink fluids if you are allowed to.",
    "community_acquired_pneumonia_outpatient.home_care.home_care_3.v1": "Avoid smoking, vaping, and smoke exposure while your lungs recover.",
    "community_acquired_pneumonia_outpatient.medications.medication_guidance_1.v1": "Take antibiotics as prescribed. Do not skip doses or stop early unless a clinician or pharmacist tells you to.",
    "community_acquired_pneumonia_outpatient.medications.medication_guidance_2.v1": "Use fever or pain medicine only if it is safe for you and follow the label.",
    "community_acquired_pneumonia_outpatient.return_precautions.return_precaution_1.v1": "Come back for worse trouble breathing, blue lips, confusion, fainting, or chest pain.",
    "community_acquired_pneumonia_outpatient.return_precautions.return_precaution_2.v1": "Come back if fever or symptoms get worse after starting treatment.",
    "community_acquired_pneumonia_outpatient.return_precautions.return_precaution_3.v1": "Come back if you cannot keep medicines or fluids down.",
    "community_acquired_pneumonia_outpatient.follow_up.default_follow_up.v1": "See your primary care doctor or clinic within 2-3 days, or sooner if symptoms are not improving.",

    "concussion_discharge_no_imaging_red_flags.diagnosis.diagnosis_summary.v1": "Your symptoms fit a concussion.",
    "concussion_discharge_no_imaging_red_flags.what_we_found.reassuring_ed_assessment.v1": "You came to the ED after a head injury. Your exam did not show an emergency danger sign requiring admission today, but concussion symptoms can change after you leave.",
    "concussion_discharge_no_imaging_red_flags.home_care.home_care_1.v1": "Rest your brain and body for the first day.",
    "concussion_discharge_no_imaging_red_flags.home_care.home_care_2.v1": "Return to school, work, screens, and exercise slowly as symptoms allow.",
    "concussion_discharge_no_imaging_red_flags.home_care.home_care_3.v1": "Avoid another head injury while symptoms are present.",
    "concussion_discharge_no_imaging_red_flags.medications.medication_guidance_1.v1": "Use acetaminophen for headache only if it is safe for you and follow the label.",
    "concussion_discharge_no_imaging_red_flags.medications.medication_guidance_2.v1": "Avoid alcohol, sedating drugs, and driving until you know you are thinking clearly and your clinician says it is safe.",
    "concussion_discharge_no_imaging_red_flags.return_precautions.return_precaution_1.v1": "Come back right away for worsening headache, repeated vomiting, confusion, seizure, fainting, or trouble waking up.",
    "concussion_discharge_no_imaging_red_flags.return_precautions.return_precaution_2.v1": "Come back for new weakness, numbness, trouble speaking, or vision changes.",
    "concussion_discharge_no_imaging_red_flags.return_precautions.return_precaution_3.v1": "Come back after any second head injury before you recover.",
    "concussion_discharge_no_imaging_red_flags.follow_up.default_follow_up.v1": "Follow up with primary care, sports medicine, or a concussion clinic if symptoms persist or if you need return-to-play clearance.",

    "dental_pain_no_deep_space_infection.diagnosis.diagnosis_summary.v1": "You were treated for dental pain today.",
    "dental_pain_no_deep_space_infection.what_we_found.reassuring_ed_assessment.v1": "You came to the ED for tooth or mouth pain. We did not see signs of a dangerous deep infection in the face, jaw, or neck today.",
    "dental_pain_no_deep_space_infection.home_care.home_care_1.v1": "Keep your mouth clean with gentle brushing.",
    "dental_pain_no_deep_space_infection.home_care.home_care_2.v1": "Avoid chewing on the painful side.",
    "dental_pain_no_deep_space_infection.home_care.home_care_3.v1": "A dentist needs to treat the tooth problem for it to fully resolve.",
    "dental_pain_no_deep_space_infection.medications.medication_guidance_1.v1": "Take antibiotics only if they were prescribed.",
    "dental_pain_no_deep_space_infection.medications.medication_guidance_2.v1": "Use pain medicine only if it is safe for you and follow the label or your clinician's instructions.",
    "dental_pain_no_deep_space_infection.return_precautions.return_precaution_1.v1": "Come back right away for face or neck swelling, fever, trouble swallowing, drooling, voice change, or trouble breathing.",
    "dental_pain_no_deep_space_infection.return_precautions.return_precaution_2.v1": "Come back if you cannot open your mouth normally.",
    "dental_pain_no_deep_space_infection.return_precautions.return_precaution_3.v1": "Come back if pain or swelling spreads quickly.",
    "dental_pain_no_deep_space_infection.follow_up.default_follow_up.v1": "See a dentist as soon as possible. The ED cannot fix the tooth permanently.",

    "laceration_repaired_simple.diagnosis.diagnosis_summary.v1": "Your cut was cleaned and repaired today.",
    "laceration_repaired_simple.what_we_found.reassuring_ed_assessment.v1": "You came to the ED with a cut. We checked the wound, cleaned it, and repaired it because it was safe to close. We did not find signs of tendon, nerve, blood vessel, joint, or bone injury today.",
    "laceration_repaired_simple.home_care.home_care_1.v1": "Keep the wound clean and dry today.",
    "laceration_repaired_simple.home_care.home_care_2.v1": "After the first day, gentle soap and water is usually okay unless you were told otherwise.",
    "laceration_repaired_simple.home_care.home_care_3.v1": "Do not soak the wound until it is healed.",
    "laceration_repaired_simple.medications.medication_guidance_1.v1": "Take antibiotics only if they were prescribed.",
    "laceration_repaired_simple.medications.medication_guidance_2.v1": "Use pain medicine only if it is safe for you and follow the label.",
    "laceration_repaired_simple.return_precautions.return_precaution_1.v1": "Come back for fever, pus, spreading redness, red streaks, or worsening swelling.",
    "laceration_repaired_simple.return_precautions.return_precaution_2.v1": "Come back for bleeding that will not stop with firm pressure.",
    "laceration_repaired_simple.return_precautions.return_precaution_3.v1": "Come back for new numbness, weakness, color change, or if the wound opens.",
    "laceration_repaired_simple.follow_up.default_follow_up.v1": "Follow up for wound check or suture removal on the schedule your clinician gave you.",

    "minor_head_injury_no_red_flags.diagnosis.diagnosis_summary.v1": "You had a minor head injury.",
    "minor_head_injury_no_red_flags.what_we_found.reassuring_ed_assessment.v1": "You came to the ED after hitting your head. Your exam was reassuring. We did not find signs of bleeding around the brain that needed emergency treatment today.",
    "minor_head_injury_no_red_flags.home_care.home_care_1.v1": "Rest today and increase activity slowly.",
    "minor_head_injury_no_red_flags.home_care.home_care_2.v1": "Avoid alcohol or sedating drugs unless your clinician says they are safe.",
    "minor_head_injury_no_red_flags.home_care.home_care_3.v1": "Have a trusted person check on you if possible.",
    "minor_head_injury_no_red_flags.medications.medication_guidance_1.v1": "Use acetaminophen for headache only if it is safe for you and follow the label.",
    "minor_head_injury_no_red_flags.medications.medication_guidance_2.v1": "Avoid medicines your clinician told you to avoid.",
    "minor_head_injury_no_red_flags.return_precautions.return_precaution_1.v1": "Come back right away for worsening severe headache, repeated vomiting, confusion, seizure, fainting, or trouble waking up.",
    "minor_head_injury_no_red_flags.return_precautions.return_precaution_2.v1": "Come back for new weakness, numbness, trouble speaking, or vision changes.",
    "minor_head_injury_no_red_flags.return_precautions.return_precaution_3.v1": "Come back for clear fluid or blood from the nose or ear.",
    "minor_head_injury_no_red_flags.follow_up.default_follow_up.v1": "Follow up with primary care if symptoms are not improving or if you were told to recheck.",

    "renal_colic_stable_no_infection.diagnosis.diagnosis_summary.v1": "Your symptoms fit a kidney stone.",
    "renal_colic_stable_no_infection.what_we_found.reassuring_ed_assessment.v1": "You came to the ED with flank pain or symptoms that fit a kidney stone. Your evaluation was reassuring enough for home care today. We did not find signs of a dangerous kidney infection or blocked infected kidney.",
    "renal_colic_stable_no_infection.home_care.home_care_1.v1": "Drink fluids as you are able.",
    "renal_colic_stable_no_infection.home_care.home_care_2.v1": "Use a urine strainer if one was given.",
    "renal_colic_stable_no_infection.home_care.home_care_3.v1": "Save any passed stone if your clinician asked you to.",
    "renal_colic_stable_no_infection.medications.medication_guidance_1.v1": "Take prescribed pain or nausea medicine only as directed.",
    "renal_colic_stable_no_infection.medications.medication_guidance_2.v1": "Use acetaminophen or ibuprofen only if it is safe for you and follow the label or your clinician's instructions.",
    "renal_colic_stable_no_infection.return_precautions.return_precaution_1.v1": "Come back for fever, chills, worsening flank pain, repeated vomiting, or feeling very ill.",
    "renal_colic_stable_no_infection.return_precautions.return_precaution_2.v1": "Come back if you cannot urinate.",
    "renal_colic_stable_no_infection.return_precautions.return_precaution_3.v1": "Come back if pain cannot be controlled with the plan you were given.",
    "renal_colic_stable_no_infection.follow_up.default_follow_up.v1": "Follow up with urology or primary care as instructed.",

    "viral_pharyngitis_strep_negative.diagnosis.diagnosis_summary.v1": "Your sore throat is most consistent with a viral infection.",
    "viral_pharyngitis_strep_negative.what_we_found.reassuring_ed_assessment.v1": "You came to the ED for a sore throat. Your strep test was negative, and your exam did not show signs of a dangerous throat or neck infection today.",
    "viral_pharyngitis_strep_negative.home_care.home_care_1.v1": "Drink fluids.",
    "viral_pharyngitis_strep_negative.home_care.home_care_2.v1": "Try warm liquids, honey if safe for you, or throat lozenges.",
    "viral_pharyngitis_strep_negative.home_care.home_care_3.v1": "Avoid sharing cups and wash your hands often.",
    "viral_pharyngitis_strep_negative.medications.medication_guidance_1.v1": "Antibiotics are not needed for a viral sore throat.",
    "viral_pharyngitis_strep_negative.medications.medication_guidance_2.v1": "Use acetaminophen or ibuprofen only if it is safe for you and follow the label.",
    "viral_pharyngitis_strep_negative.return_precautions.return_precaution_1.v1": "Come back right away for trouble breathing, drooling, muffled voice, stiff neck, or trouble opening your mouth.",
    "viral_pharyngitis_strep_negative.return_precautions.return_precaution_2.v1": "Come back if you cannot swallow fluids.",
    "viral_pharyngitis_strep_negative.return_precautions.return_precaution_3.v1": "Come back if fever or throat pain becomes much worse.",
    "viral_pharyngitis_strep_negative.follow_up.default_follow_up.v1": "Follow up with primary care if symptoms are not improving or if your clinician instructed you to recheck.",
}


def main() -> int:
    rows = json.loads(PRIMITIVE_PATH.read_text(encoding="utf-8"))
    found: set[str] = set()
    for row in rows:
        primitive_id = row.get("id")
        if primitive_id not in OVERRIDES:
            continue
        for key in TEXT_KEYS:
            row["text"][key] = OVERRIDES[primitive_id]
        row.setdefault("style", {})["calibration"] = "phase15_dc_instructor_voice"
        found.add(primitive_id)
    missing = sorted(set(OVERRIDES) - found)
    if missing:
        for primitive_id in missing:
            print(f"missing style override target: {primitive_id}")
        return 1
    PRIMITIVE_PATH.write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")
    print(f"applied {len(found)} style overrides")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
