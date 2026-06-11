# DC Instructor

Plain-language ED discharge instruction generator for clinicians. Picks reading level (4th–10th grade or HL-1) and language, optionally generates a clean medical illustration, and auto-redacts PHI from any pasted ED note before it leaves the browser.

Built by [@BloodSweatxED](https://x.com/BloodSweatxED) — EM physician, clinician-developer.

## Stack
- React + Vite + Tailwind
- Netlify Functions (serverless API proxy — keys never reach the browser)
- Anthropic Claude (`claude-sonnet-4-5` for generation, `claude-haiku-4-5` for PHI verify)
- Stability AI for medical line-art
- Supabase for usage counter + ratings

## Setup

```bash
git clone <repo> dc-instructor
cd dc-instructor
npm install
cp .env.example .env
# fill in env values
npx netlify dev   # runs Vite + Functions together
```

### Supabase
1. Create a Supabase project.
2. In SQL editor, run `supabase/migrations/001_initial_schema.sql`.
3. Copy the project URL and anon key into `.env` (`VITE_SUPABASE_URL`, `VITE_SUPABASE_ANON_KEY`).
4. Copy the **service role key** (Settings → API) into `SUPABASE_SERVICE_ROLE_KEY` — server-side only, do **not** prefix with `VITE_`.

### Netlify deploy
1. Push to GitHub.
2. Connect the repo in Netlify (build cmd `npm run build`, publish `dist`).
3. Set env vars in Netlify dashboard:
   - `ANTHROPIC_API_KEY`
   - `STABILITY_API_KEY`
   - `SUPABASE_SERVICE_ROLE_KEY`
   - `VITE_SUPABASE_URL`, `VITE_SUPABASE_ANON_KEY`
4. Point `dcinstructor.com` at the Netlify site.

## PHI redaction

Two layers, runs only when the optional ED note field has content:

1. **Client-side regex** (`src/lib/phiRedact.js`) — HIPAA Safe Harbor 18 identifiers (names, MRNs, dates, phone, address, SSN, age >89, email, URL). Replaces matches with typed tokens (`[NAME]`, `[MRN]`, …). Original strings never leave the browser.
2. **LLM verify** (`netlify/functions/redact-verify.js`) — fast Haiku pass on the already-scrubbed text catches contextual identifiers regex misses (employer, public role, rare condition, geography).

The `PHIRedactionBadge` shows what was removed; the verified state is shown once the second pass returns.

## Usage limits

- Hard wall at 500 total generations (counted in Supabase). The time-based expiry gate was removed in June 2026.
- Banner at 400 generations.
- After the cap, the app shows a contact card; no further API calls fire.
- Note: the limit check fails open — if Supabase is unreachable (e.g. free-tier project paused), generation continues and the cap is not enforced. Degraded state is logged in the Netlify function logs.

## Tests

```bash
npm test   # vitest — covers PHI redaction and rating cadence
```
CI (GitHub Actions) runs tests and a production build on every push and PR.

## Privacy
- ED note content is never written to the DB. Only `condition_input` (chief complaint) is stored, and only the first 200 chars.
- All Anthropic / Stability calls go through Netlify Functions; the browser bundle contains no third-party API keys.
