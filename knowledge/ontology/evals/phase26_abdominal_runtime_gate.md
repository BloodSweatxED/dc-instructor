# Phase 26 Abdominal Runtime Gate

Status: complete.

Phase 26 encodes the clinician feedback from Phase 25 as runtime behavior before any abdominal pain promotion.

Implemented:

- Added `clinician_directed_recheck_plan` as required runtime context for `abdominal_pain_nonspecific_reassuring_workup`.
- Added `poor_follow_up` as an abdominal hard blocker to match the clinician decision that unreliable follow-up breaks this phenotype.
- Added runtime cases for reassuring abdominal pain without a recheck plan and for unreliable follow-up.
- Kept abdominal pain as `needs_review`; explicit recheck cases still fall back because the phenotype is not promoted.

Runtime decision:

- A note with abdominal pain and reassuring ED evaluation but return precautions only is not enough.
- A note must include an explicit clinician-directed recheck plan before this phenotype can clear the runtime context gate.
- Even with a recheck plan, frailty, immunocompromise, pregnancy, fever, GI bleeding, peritoneal signs, sepsis, unstable vitals, uncontrolled vomiting, or unreliable follow-up block the phenotype.

Verification:

- `python3 knowledge/ontology/evals/check_phase26_abdominal_runtime_gate.py`
- `python3 knowledge/ontology/evals/check_phase23_abdominal_narrowing.py`
- `python3 knowledge/ontology/evals/run_runtime_cases.py`
- `node knowledge/ontology/evals/run_netlify_runtime_smoke.mjs`
