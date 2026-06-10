# Phase 84 Migraine Clinician Feedback

Target phenotype: `migraine_improved_discharge`.

Status: revise. Not ready for promotion pathway.

Clinician decisions:

- Secondary-headache exclusion must be handled at runtime through structured input confirmation, not inferred from documentation absence.
- Absolute runtime blockers are non-negotiable and should not be modifier-toggled or clinician-overrideable.
- Absolute blockers: sudden severe headache reaching worst point within seconds, worst headache of life, age over 50 with new headache pattern, pregnancy, immunocompromise, fever with headache, neck stiffness, unresolved neurologic deficit, head trauma within 7 days, altered mental status not fully resolved at discharge, unstable vitals, and uncontrolled vomiting at discharge.
- Soft blockers requiring explicit clinician override: first-lifetime headache of this severity, and CT not performed with documented concern.
- The word "thunderclap" should not appear in patient-facing text.
- Replace "fits a migraine pattern" with clinician-diagnosis language.
- Remove negative-documentation language from What We Found.
- Require two structured confirmations before any later promotion: documented ED improvement and structured absence of red flags.
- Remove base vision language. Put migraine-with-aura language behind a conditional branch if built later.

Patient-facing revisions made:

- Diagnosis now says: "Your clinician diagnosed your headache as a migraine. Your symptoms improved with treatment."
- What We Found no longer says red flags were absent because they were not documented.
- Home care now includes quiet dark room rest, increased fluids, limited screen/mental stimulation, stress reduction, no driving/heavy machinery until alert and thinking clearly, expected recovery timeline, and headache log instructions.
- Return precautions now spell out sudden severe headache language without using "thunderclap."

Promotion requirement:

Do not promote this phenotype until the runtime has structured improvement confirmation, structured red-flag absence, hard blockers, and an explicit clinician-override path for soft blockers if those soft blockers are allowed to pass.
