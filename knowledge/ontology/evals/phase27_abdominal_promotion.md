# Phase 27 Abdominal Promotion

Status: complete.

Phase 27 promotes `abdominal_pain_nonspecific_reassuring_workup` from narrow review candidate to reviewed runtime content after Phase 26 encoded the required runtime gate.

Promotion constraints:

- Use only for abdominal pain after reassuring ED evaluation.
- Require explicit clinician-directed recheck plan.
- Do not use as a catch-all fallback for unmatched abdominal pain.
- Keep `poor_follow_up`, frailty or elderly status, immunocompromise, pregnancy, fever, GI bleeding, peritoneal signs, sepsis, unstable vitals, and uncontrolled vomiting as blockers.
- Keep medication guidance passthrough-only and review-required.

Runtime outcome:

- Explicit abdominal recheck plan may enter ontology mode.
- Return precautions without clinician-directed recheck still falls back.
- Unreliable follow-up still falls back.

Verification:

- `python3 knowledge/ontology/evals/check_phase27_abdominal_promotion.py`
