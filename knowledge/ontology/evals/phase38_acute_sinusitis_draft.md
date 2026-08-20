# Phase 38 Acute Sinusitis Draft

Phase 38 creates `acute_sinusitis_supportive_care` as a narrow draft phenotype only.

Runtime may recognize the phenotype for review stress testing, but must fall back because it is not clinician-reviewed. This is intentional.

Runtime expectations:

- Clean supportive-care acute sinusitis matches but falls back with `phenotype_not_clinician_reviewed`.
- Antibiotic-prescribed sinusitis blocks.
- Severe bacterial-feature language blocks.
- Orbital or intracranial concern blocks.
- Vague congestion does not match.

Guardrails:

- Do not promote sinusitis yet.
- Do not add broad congestion, facial pain, or cold symptoms as standalone terms.
- Do not infer antibiotic instructions.
- Do not use sinusitis as a catch-all URI fallback.
