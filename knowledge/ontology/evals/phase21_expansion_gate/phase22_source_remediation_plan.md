# Phase 22 Source Remediation Plan

Goal: close or retire draft source gaps and active draft phenotypes before any phenotype expansion.

Current active draft targets: phenotype `asymptomatic_elevated_blood_pressure_no_end_organ_symptoms`, phenotype `hemorrhoids_uncomplicated_no_heavy_bleeding`, phenotype `influenza_like_illness_stable_supportive_care`.

Recommended sequence:

1. `chest_pain_low_risk_negative_ed_workup` is retired as static ontology content. Keep chest pain in product-layer fallback unless it is rebuilt later as a much narrower reviewed phenotype.
2. Decide whether `abdominal_pain_nonspecific_reassuring_workup` is worth preserving as a narrow reviewed phenotype, or should stay product-only/LLM fallback because it is too broad for static ontology mode.
3. If abdominal pain is preserved, narrow boundaries before editing patient-facing primitives.
4. Generate a clinician review packet only after source cards exist and the phenotype boundaries are narrowed.
5. Keep active phenotypes draft until source audit, runtime contradiction cases, medication policy, and clinician review pass.

Recommendation: abdominal pain can be considered only if narrowed to a very explicit recheck/return-precaution phenotype.
