# Phase 223-250 Promotion Release Review

Date: 2026-06-03

Source decision: Phase 222 promotion decision, based on Phase 221 revision review.

Status after Phase 250: promotion release audit passed with one active hold.

## Promoted To Reviewed Ontology Mode

These phenotypes are reviewed and runtime enabled:

- `skin_avulsion_or_abrasion_simple`
- `acute_otitis_media_uncomplicated`
- `suture_removal_or_wound_check_no_infection`

`sprain_strain_non_ankle_xray_negative` remains draft-only.

## Phase Log

| Phase | Result |
| --- | --- |
| 223 | Promotion decision encoded from clinician review. |
| 224 | Output modifier disposition checked against phenotype runtime metadata. |
| 225 | Python runtime propagation checked. |
| 226 | Netlify runtime propagation checked. |
| 227 | Review banner delivery checked in `OutputPanel.jsx`. |
| 228 | `generate.js` metadata handoff checked. |
| 229 | Skin avulsion blocker/modifier boundary checked. |
| 230 | Acute otitis media blocker/modifier boundary checked. |
| 231 | Suture/wound-check blocker/modifier boundary checked. |
| 232 | Suture/wound-check required-context gate checked. |
| 233 | Sprain/strain hold confirmed. |
| 234 | Sprain elbow/foot low-confidence concern preserved. |
| 235 | Manifest parity checked. |
| 236 | Graph count integrity checked. |
| 237 | Expansion gate checked. |
| 238 | Reviewed source gap count checked. |
| 239 | Draft source gap count checked. |
| 240 | Broad Python runtime cases passed. |
| 241 | Netlify runtime smoke passed. |
| 242 | Prior Phase 202-215 cycle check passed. |
| 243 | Prior Phase 216-220 promotion-readiness check passed. |
| 244 | Product tailoring contract check passed. |
| 245 | Build passed. |
| 246 | `git diff --check` passed. |
| 247 | Dirty worktree reviewed, unrelated RAG smoke artifacts preserved. |
| 248 | Review concerns compiled for clinician follow-up. |
| 249 | Vault handoff prepared. |
| 250 | Release audit complete. |

## Output Modifier Delivery

Output modifiers are returned in ontology metadata as `output_modifiers`.

They are displayed in the review banner.

They do not silently alter patient-facing text.

The clinician must review the modifier note before using the output.

## Modifier And Blocker Disposition

`skin_avulsion_or_abrasion_simple`

- True runtime blockers preserved: immunocompromise, bite wound, dirty wound, infection concern, repair need, retained foreign body or deep-structure concern, diabetic foot, and other specialist or pediatric pathways.
- Output modifiers: diabetes general risk, peripheral vascular disease, anticoagulation, delayed clean-wound presentation.

`acute_otitis_media_uncomplicated`

- True runtime blockers preserved: immunocompromise, mastoiditis or deep infection concern, meningitis or CNS concern, venous sinus thrombosis concern, tube or perforation pathway, acute hearing loss, facial weakness or neurologic ear sign, pediatric pathway, recurrent or chronic pathway, unstable vitals, ENT-directed plan.
- Watchful-waiting unreliable follow-up remains a true blocker scoped by its trigger terms.
- Output modifiers: frail elderly, diabetes general risk.

`suture_removal_or_wound_check_no_infection`

- True runtime blockers preserved: immunocompromise, diabetic foot, infection concern, dehiscence, high-risk wound location, retained foreign body, dirty wound, bite wound, poor follow-up, pediatric pathway, specialist-directed wound plan.
- Output modifiers: diabetes general risk, peripheral vascular disease, anticoagulation.
- Runtime requires both documented expected healing or explicit wound clearance and a clinician-entered wound follow-up plan.
- Wound readiness alone remains insufficient.

## Held Draft

`sprain_strain_non_ankle_xray_negative` remains draft-only.

Reason: elbow and foot clean cases still match the correct phenotype at low confidence. The current behavior is safe because the phenotype is not clinician reviewed, so these cases fall back instead of using reviewed ontology output.

Recommended next action after review: either split elbow/foot into site-specific variants or add site-specific high-confidence terms and stress cases before promotion.

## Needs Clinician Review

No new promoted-output language concerns were found in this audit.

Open concern for review:

- Should `sprain_strain_non_ankle_xray_negative` be split by site before future promotion, or should elbow and foot remain excluded from v1?

## Verification Commands

Passed:

- `python3 knowledge/ontology/evals/check_phase222_250_promotion_release.py`
- `python3 knowledge/ontology/evals/check_phase216_220_promotion_readiness.py`
- `python3 knowledge/ontology/evals/check_phase202_215_cycle.py`
- `python3 knowledge/ontology/evals/run_runtime_cases.py`
- `node knowledge/ontology/evals/run_netlify_runtime_smoke.mjs`
- `python3 knowledge/ontology/evals/check_phase21_expansion_gate.py`
- `node knowledge/ontology/evals/check_product_tailoring_contract.mjs`
- `npm run build`
- `git diff --check`

## Current Counts

- Runtime manifest phenotypes: 28.
- Graph nodes: 2133.
- Graph edges: 3212.
- Active draft phenotype count: 1.
- Active draft: `sprain_strain_non_ankle_xray_negative`.
- Phenotype expansion allowed: false.
