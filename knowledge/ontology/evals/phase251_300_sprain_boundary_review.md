# Phase 251-300 Sprain Boundary Review

Date: 2026-06-04

Status: complete.

## Decision

`sprain_strain_non_ankle_xray_negative` remains draft-only.

Elbow and foot are excluded from the current v1 boundary pending a site-specific split or separate clinician approval.

Knee, wrist, and shoulder remain the only clean high-confidence draft sites for this phenotype.

## Phase Log

| Phase | Result |
| --- | --- |
| 251 | Phase 250 handoff rechecked. |
| 252 | Sprain/strain draft inspected against runtime manifest. |
| 253 | Conservative boundary selected: exclude elbow and foot from v1 instead of broadening. |
| 254 | Generator source updated in `build_expanded_draft_packs.py`. |
| 255 | Python runtime exclusion rule added. |
| 256 | Netlify runtime exclusion rule added. |
| 257 | Sprain phenotype regenerated from source. |
| 258 | Manifest regenerated. |
| 259 | Review sheet regenerated. |
| 260 | Graph rebuilt. |
| 261 | Phase 217 sprain site stress cases updated. |
| 262 | Phase 222-250 release check updated for explicit site exclusion. |
| 263 | Netlify smoke expanded to include Phase 217 sprain site cases. |
| 264 | Phase 251-300 boundary checker added. |
| 265 | Promotion script rerun after generation to restore reviewed phenotype state. |
| 266 | Graph rebuilt after promotion restoration. |
| 267 | Expansion gate verified: one active draft remains. |
| 268 | Knee clean case verified high confidence and draft-only. |
| 269 | Wrist clean case verified high confidence and draft-only. |
| 270 | Shoulder clean case verified high confidence and draft-only. |
| 271 | Elbow clean case verified explicit site exclusion. |
| 272 | Foot clean case verified explicit site exclusion. |
| 273 | Missing x-ray sprain case preserved. |
| 274 | Scaphoid wrist blocker preserved. |
| 275 | Unable-to-bear-weight blocker preserved. |
| 276 | Compartment signal blocker preserved. |
| 277 | Elderly osteoporotic MSK blocker preserved. |
| 278 | Output modifier metadata contract rechecked. |
| 279 | Review banner wiring rechecked. |
| 280 | `generate.js` metadata handoff rechecked. |
| 281 | Python/Netlify parity rechecked for Phase 217 cases. |
| 282 | Phase 216-220 promotion-readiness check passed. |
| 283 | Phase 222-250 promotion-release check passed. |
| 284 | Phase 202-215 cycle check passed. |
| 285 | Broad Python runtime cases passed. |
| 286 | Netlify runtime smoke passed. |
| 287 | Expansion gate passed. |
| 288 | Product tailoring contract passed. |
| 289 | Vite build passed. |
| 290 | `git diff --check` passed. |
| 291 | Graph counts unchanged at 2133 nodes / 3212 edges. |
| 292 | Reviewed source gap count remained zero. |
| 293 | Draft source gap count remained zero. |
| 294 | Active draft count remained one. |
| 295 | RAG smoke artifacts preserved out of scope. |
| 296 | No new phenotype expansion performed. |
| 297 | Promotion blocked pending clinician owner decision. |
| 298 | Phase 300 handoff prepared. |
| 299 | Beyond-300 continuation boundary documented. |
| 300 | Phase 251-300 complete. |

## Current Runtime Behavior

Allowed draft sites:

- `knee sprain xray negative`
- `wrist sprain xray negative`
- `shoulder sprain xray negative`

Excluded pending split:

- `elbow sprain xray negative`
- `foot sprain xray negative`

Elbow and foot still route to the held draft for auditability, but the fallback reason is now `unsafe_modifier_present` with exclusion `elbow_or_foot_site_pending_split`.

## Verification

Passed:

- `python3 knowledge/ontology/evals/check_phase251_300_sprain_boundary.py`
- `python3 knowledge/ontology/evals/check_phase216_220_promotion_readiness.py`
- `python3 knowledge/ontology/evals/check_phase222_250_promotion_release.py`
- `python3 knowledge/ontology/evals/check_phase202_215_cycle.py`
- `python3 knowledge/ontology/evals/run_runtime_cases.py`
- `node knowledge/ontology/evals/run_netlify_runtime_smoke.mjs`
- `python3 knowledge/ontology/evals/check_phase21_expansion_gate.py`
- `node knowledge/ontology/evals/check_product_tailoring_contract.mjs`
- `npm run build`
- `git diff --check`

## Remaining Decision

Do not promote `sprain_strain_non_ankle_xray_negative` until the clinician owner chooses one path:

1. Promote a narrower knee/wrist/shoulder v1.
2. Split elbow and foot into site-specific variants.
3. Keep elbow and foot excluded indefinitely from v1.
