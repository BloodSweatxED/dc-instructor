# DC Instructor - Session Handoff

Last updated 2026-06-16. Branch `v1.2` (commits `d2ba9bf`, `df436b0`). CI green.

This file is a cold-start brief. Read it, then read `docs/AUDIT-2026-06-11.md` for the full audit.

## Where things stand

- `v1.2` branch holds the hardening work: input validation, same-origin guard on the three key-spending functions, logged-instead-of-silent Supabase failures, expanded PHI whitelist, CSP/HSTS headers, 16 vitest tests, GitHub Actions CI. All shipped and passing.
- `main` is unchanged. `v1.2` has not been merged or deployed yet.
- The repo is normally private. It was made public for review and may be private again now.

## The decision that drives everything else

The product is moving from "live LLM generation every time" toward a **hybrid: a clinician-reviewed library of discharge instructions, with live generation as the fallback.** The library is the asset and the better liability story. Live generation fills gaps and feeds the library.

Why a library is worth building: the only comparable product is Elsevier / Krames patient-education content, which is paywalled and institution-only. There is no good accessible library for individual clinicians. ED discharge diagnoses are concentrated (roughly 50 to 75 conditions cover most discharges), so the corpus is tractable: about 60 conditions x 5 reading levels x 5 languages is around 1,500 documents. The agent pipeline in `knowledge/` (`batch_review.py`, `clinician_review.py`) was built to draft exactly this.

The RAG pipeline in `knowledge/` is grounding and QA tooling for building the library, not a product feature on its own. The "on-prem for HIPAA" angle is a footnote: the retrieval corpus is MedlinePlus (public, no PHI), so on-prem only matters as an enterprise sales checkbox much later.

## The data model we agreed on

Capture everything, gate nothing on ratings. Curate downstream from signals that cost the user nothing.

Signal value, highest to lowest:
1. **Edit diffs.** The output renders in an editable textarea. If a clinician edits before copying, the diff between generated text and copied text is a physician correction. This is the most valuable signal and it is currently thrown away.
2. **Copy without edits.** A weak positive.
3. **Demand frequency.** How often a condition x level x language cell is requested. Prioritizes the review queue regardless of ratings.
4. **Star ratings.** Sparse (expect 10 to 30 percent), extreme-skewed. A tiebreaker, never a gate.

Flow: capture all -> cluster by condition x level x language -> rank within cluster (edits > copies > ratings > recency) -> human reviews only the cluster winners -> reviewed doc enters `library/`. Stored outputs are ore, not training data. Most will never be used directly and that is fine; they still contributed demand and edit signals.

Note: this is curation for a library, not model fine-tuning. A few hundred examples is not worth fine-tuning; it is worth curating.

## Next actionable steps, in order

### Step 1 (PREREQUISITE, dashboard only, ~30 min) - Restore Supabase
Nothing below captures any data until this is done. The project has been paused/unreachable for 11+ metric snapshots.
- Unpause the Supabase project and confirm the data still exists (paused free-tier projects can be auto-deleted after long inactivity).
- Move it off free tier or add a keep-alive ping so it cannot re-pause before any demo.
- Set `SUPABASE_SERVICE_ROLE_KEY` and a `*.supabase.co` network allowance in the snapshot/build environment.
- Run one metrics snapshot manually and confirm it is green.

### Step 2 (code, ~half day) - Build the capture layer on v1.2
No dependence on ratings. Three pieces:
- **Migration:** add `output_text` and `output_completed_at` to the `generations` table. New file under `supabase/migrations/`.
- **Server (`netlify/functions/generate.js`):** the function already proxies the Anthropic stream. Accumulate the full text as it streams, and on stream end write it back to the generation row by `generation_id`. About 15 lines, no client change for this part.
- **Client (`src/components/OutputPanel.jsx` + `src/lib/api.js`):** on copy, send a lightweight `copy` event with the final textarea contents and the `generation_id`. This captures edit diffs, the top signal. About 10 lines plus a small function or table for copy events.

### Step 3 (docs, ~15 min, do with Step 2) - Fix the privacy wording
The README currently promises "ED note content is never written to the DB." Storing outputs is a small step beyond that, because an output can echo note details (identifiers should already be stripped by redaction). Recommended: store the full output, continue to never store the raw note, and update the README and the in-app footer to say generated instructions are retained for quality improvement. The footer already discloses QI use.

### Step 4 (parser, when ready) - Recover the artifact history
- Request the claude.ai data export: Settings -> Privacy -> Export data.
- Instructions generated **as chat messages** are in the export and recoverable. Instructions typed into an **interactive artifact UI** are ephemeral and almost certainly not in the export. Expect a mix.
- When the export arrives, write a parser to extract discharge instructions, dedupe, and convert to `library/` seed files. This bootstraps the library from the 100+ instructions already generated.

### Step 5 (later, the headline feature) - Library-first lookup in /generate
- On request, fuzzy-match the condition against `library/` (alias map against `ALLOWED_TOPICS` in `knowledge/ingest_medlineplus.py`).
- Hit: serve reviewed content instantly, badge "clinician-reviewed", skip the Sonnet call.
- Miss: live generation as today, badge "unreviewed - AI generated", enqueue as a library candidate.
- This is the demoable flywheel and the investor narrative. Worth doing even with only a handful of seeded conditions.

## Open questions for Andre

1. Fail-open vs fail-closed when Supabase is unreachable. Generation currently proceeds uncapped (now logged). Acceptable, or fail closed after N unverified generations?
2. Library narrative for a demo: wire library-first lookup in (Step 5, real work) or present it as roadmap?
3. When does clinician auth land, and the BAA conversation, relative to any pilot or demo?
4. Should a failed PHI verify pass block sending the note, warn loudly, or stay as the current silent badge change?

## Watch out for

- `/tmp/dc-instructor` is a scratch clone and gets wiped. Re-clone as needed.
- Local git commits show an auto-configured author identity. Set name/email before committing if it matters.
- `knowledge/db/` is git-ignored and must be rebuilt locally with `ingest_medlineplus.py`. CLAUDE.md and AGENTS.md describe a `library/` workflow for a `library/` that is still empty.
