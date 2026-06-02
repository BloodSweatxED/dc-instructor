#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from ontology_lib import assemble_discharge  # noqa: E402


STYLE_CHECKS = {
    "asthma_exacerbation_improved_discharge": {
        "required": [
            "You had an asthma flare-up",
            "You came to the ED",
            "breathing treatments",
            "opened your airways",
            "steroids",
            "breathing comfortably",
            "Rest for the next 1-2 days",
            "trigger your asthma",
            "controller inhaler",
            "rescue inhaler is not helping",
            "written asthma action plan",
            "within 3-5 days",
        ],
        "forbidden": [
            "Your breathing improved enough for discharge today.",
            "use the plan you were given closely",
        ],
    }
    ,
    "community_acquired_pneumonia_outpatient": {
        "required": ["You came to the ED", "oxygen level was safe", "Warm liquids", "full recovery can take 2-4 weeks"],
        "forbidden": ["Your ED evaluation found a lung infection that was safe to treat at home today.", "Drink fluids if you are allowed to", "reassuring enough"],
    },
    "minor_head_injury_no_red_flags": {
        "required": ["You came to the ED after hitting your head", "bleeding in or around the brain", "check on you tonight", "days to weeks"],
        "forbidden": ["Your exam was reassuring today. We did not find signs that you needed emergency treatment", "needed emergency treatment today", "Avoid medicines your clinician told you to avoid"],
    },
    "concussion_discharge_no_imaging_red_flags": {
        "required": ["You came to the ED after a head injury", "symptoms can change after you leave"],
        "forbidden": ["A concussion can happen after a hit or sudden movement of the head."],
    },
    "renal_colic_stable_no_infection": {
        "required": ["You came to the ED with flank pain", "pale yellow", "every urination", "within 1-2 weeks", "1-4 weeks"],
        "forbidden": ["Your ED evaluation was reassuring enough for home care today.", "Drink fluids as you are able", "reassuring enough"],
    },
    "cellulitis_uncomplicated_oral_antibiotics": {
        "required": ["You came to the ED for redness", "deeper emergency infection", "phone photo", "48-72 hours"],
        "forbidden": ["Your exam fits a skin infection that is safe to treat at home today.", "safe to treat at home today", "Use pain or fever medicine only if it is safe"],
    },
    "abscess_after_i_and_d": {
        "required": ["You came to the ED because the area was painful", "opened and drained"],
        "forbidden": ["The painful swollen area had pus inside."],
    },
    "dental_pain_no_deep_space_infection": {
        "required": ["You came to the ED for tooth or mouth pain", "The ED cannot fix the tooth permanently"],
        "forbidden": ["Your exam did not show signs of a dangerous deep infection"],
    },
    "laceration_repaired_simple": {
        "required": ["You came to the ED with a cut", "cleaned it, and repaired it"],
        "forbidden": ["We checked the wound and repaired it because it was safe to close."],
    },
    "viral_pharyngitis_strep_negative": {
        "required": ["You came to the ED for a sore throat", "strep test was negative"],
        "forbidden": ["Your strep test was negative. Your exam did not show signs"],
    },
    "allergic_reaction_resolved_no_anaphylaxis": {
        "required": ["You came to the ED with allergy symptoms", "did not find signs of anaphylaxis"],
        "forbidden": ["Your symptoms improved, and we did not find signs of anaphylaxis"],
    },
    "ankle_sprain_xray_negative": {
        "required": ["x-ray did not show a fracture", "good blood flow", "brace, wrap, or crutches"],
        "forbidden": [],
    },
    "lumbar_strain_no_red_flags": {
        "required": ["did not find signs of a dangerous nerve or spine problem", "Stay gently active"],
        "forbidden": [],
    },
    "viral_uri_no_pneumonia": {
        "required": ["viral upper respiratory infection", "breathing, oxygen level", "Antibiotics do not treat cold viruses"],
        "forbidden": [],
    },
    "uncomplicated_cystitis_nonpregnant": {
        "required": ["bladder infection", "did not find signs of a kidney infection", "urine culture"],
        "forbidden": [],
    },
    "gastroenteritis_stable_hydrating": {
        "required": ["gastroenteritis", "stable enough for discharge", "small sips often"],
        "forbidden": [],
    },
}


def main() -> int:
    failures: list[str] = []
    for phenotype_id, checks in STYLE_CHECKS.items():
        output = assemble_discharge(phenotype_id, "6")
        for phrase in checks["required"]:
            if phrase not in output:
                failures.append(f"{phenotype_id} missing style phrase: {phrase}")
        for phrase in checks["forbidden"]:
            if phrase in output:
                failures.append(f"{phenotype_id} still has stale phrase: {phrase}")
    if failures:
        for failure in failures:
            print(failure)
        return 1
    print("style baseline checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
