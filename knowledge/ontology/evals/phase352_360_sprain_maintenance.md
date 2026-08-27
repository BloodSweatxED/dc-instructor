# Phase 352-360 Sprain Maintenance

Status: complete.

Maintenance decision:

- Keep elbow and foot excluded from reviewed knee/shoulder output until they are intentionally split.
- Do not start a non-sprain expansion until the sprain-family loose ends are closed.

Item 1: knee/shoulder return precaution text

Replaced the weak knee/shoulder tail:

```text
symptoms that get worse instead of better
```

with:

```text
Fever, spreading redness or warmth, pus, or severe pain with movement.
```

This keeps the return precaution concrete and infection-focused.

Item 2: elbow/foot exclusion reliability

Clean tracked elbow and foot sprain strings still route to `sprain_strain_knee_or_shoulder_xray_negative` only for auditability, then stop before patient-facing ontology output with:

```text
unsafe_modifier_present: elbow_or_foot_site_pending_split
```

Verification:

```bash
python3 knowledge/ontology/evals/check_phase352_360_sprain_maintenance.py
python3 knowledge/ontology/evals/check_phase302_350_wrist_sprain_gate.py
python3 knowledge/ontology/evals/run_runtime_cases.py
node knowledge/ontology/evals/run_netlify_runtime_smoke.mjs
```

Decision:

Maintenance passes. Expansion can proceed to ranking only. No elbow or foot promotion happened in this phase.
