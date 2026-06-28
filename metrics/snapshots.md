# DC Instructor — Usage Snapshots

## 2026-06-28

> **ERROR: All Supabase queries failed — this is the 17th consecutive failed snapshot.**
>
> **Status of known blockers:**
> - ✅ **API key:** `SUPABASE_SERVICE_ROLE_KEY` retrieved from Netlify env vars via MCP tool (same key as prior runs).
> - ❌ **Network policy blocks Supabase.** The environment proxy returned `502 policy denial` on every CONNECT attempt to `noloieuagfigaqahspfi.supabase.co:443`. Runs from 2026-06-19 through 2026-06-25 had network access; this run does not. The environment's network policy must be updated to allow `*.supabase.co`.
> - ❌ **Database schema still not applied.** Even if the network were fixed, `generations` and `ratings` tables do not exist in the production Supabase project. All queries would return `PGRST205`.
>
> **Two manual fixes still needed:**
> 1. **Update the network policy** for this Claude Code on the web environment to allow outbound HTTPS to `*.supabase.co`. See [Claude Code on the web docs](https://code.claude.com/docs/en/claude-code-on-the-web).
> 2. **Apply the DB migration:** open the [Supabase SQL Editor](https://supabase.com/dashboard/project/noloieuagfigaqahspfi/sql/new), paste and run `supabase/migrations/001_initial_schema.sql`.
>
> **⚠️ Trial ended 2026-06-02 (26 days ago). No usage data has ever been recorded.**

- **Total generations:** _unavailable (network policy blocks Supabase)_
- **Last 3 days:** _unavailable (network policy blocks Supabase)_
- **Days remaining in trial:** -26 (trial ended 2026-06-02)
- **Gens remaining before cap:** _unavailable_ (of 500)

**Top conditions:** _unavailable (network policy blocks Supabase)_

**Languages:** _unavailable (network policy blocks Supabase)_

**Reading levels:** _unavailable (network policy blocks Supabase)_

**Ratings:** _unavailable (network policy blocks Supabase)_

---

## 2026-06-25

> **ERROR: All Supabase queries failed — this is the 16th consecutive failed snapshot.**
>
> **Status of known blockers:**
> - ✅ **Network:** Supabase host `noloieuagfigaqahspfi.supabase.co` is reachable (HTTP 401 received — network is fine).
> - ✅ **API key:** `SUPABASE_SERVICE_ROLE_KEY` retrieved from Netlify env vars via MCP tool.
> - ❌ **PERSISTENT BLOCKER: Database schema not applied.** The live Supabase database still does not contain the `generations` or `ratings` tables. All queries return `PGRST205: Could not find the table in the schema cache`. Unchanged from the 2026-06-22 run.
>
> **Root cause:** `supabase/migrations/001_initial_schema.sql` has never been run against the production Supabase project. No usage data has ever been recorded.
>
> **One-time manual fix needed (5 minutes):**
> 1. Open the [Supabase SQL Editor](https://supabase.com/dashboard/project/noloieuagfigaqahspfi/sql/new) for project `noloieuagfigaqahspfi`.
> 2. Paste and run the contents of `supabase/migrations/001_initial_schema.sql`.
> 3. After applying, future snapshot runs will be able to query data.

- **Total generations:** _unavailable (schema not applied — `generations` table missing)_
- **Last 3 days:** _unavailable (schema not applied)_
- **Days remaining in trial:** -23 (trial ended 2026-06-02)
- **Gens remaining before cap:** _unavailable_ (of 500)

**Top conditions:** _unavailable (schema not applied)_

**Languages:** _unavailable (schema not applied)_

**Reading levels:** _unavailable (schema not applied)_

**Ratings:** _unavailable (schema not applied)_

---

## 2026-06-22

> **ERROR: All Supabase queries failed — this is the 15th consecutive failed snapshot.**
>
> **Status of known blockers:**
> - ✅ **Network:** Supabase host `noloieuagfigaqahspfi.supabase.co` is reachable (HTTP 401 received — network is fine).
> - ✅ **API key:** `SUPABASE_SERVICE_ROLE_KEY` retrieved from Netlify env vars via MCP tool (same method as 2026-06-19 run).
> - ❌ **PERSISTENT BLOCKER: Database schema not applied.** The live Supabase database still only contains the default `test` table. The `generations` and `ratings` tables defined in `supabase/migrations/001_initial_schema.sql` do not exist. All queries return `PGRST205: Could not find the table in the schema cache`. This is unchanged from the 2026-06-19 run.
>
> **Root cause:** `supabase/migrations/001_initial_schema.sql` was never run against the production Supabase project. The Supabase CLI is not installed in this environment and no management API PAT is available, so the migration cannot be applied automatically.
>
> **⚠️ The 30-day trial ended on 2026-06-02 (20 days ago).** No usage data was ever recorded — `logGeneration()` in the Netlify function has been failing silently since launch because the target tables never existed.
>
> **One-time manual fix needed (5 minutes):**
> 1. Open the [Supabase SQL Editor](https://supabase.com/dashboard/project/noloieuagfigaqahspfi/sql/new) for project `noloieuagfigaqahspfi`.
> 2. Paste and run the contents of `supabase/migrations/001_initial_schema.sql`.
> 3. After applying, future snapshot runs will be able to query data (and `logGeneration()` will start recording).

- **Total generations:** _unavailable (schema not applied — `generations` table missing)_
- **Last 3 days:** _unavailable (schema not applied)_
- **Days remaining in trial:** -20 (trial ended 2026-06-02)
- **Gens remaining before cap:** _unavailable_ (of 500)

**Top conditions:** _unavailable (schema not applied)_

**Languages:** _unavailable (schema not applied)_

**Reading levels:** _unavailable (schema not applied)_

**Ratings:** _unavailable (schema not applied)_

---

## 2026-06-19

> **ERROR: All Supabase queries failed — this is the 14th consecutive failed snapshot.**
>
> **New finding this run (blockers have shifted):**
> - ✅ **Network policy: RESOLVED** — Supabase host `noloieuagfigaqahspfi.supabase.co` is now reachable (HTTP responses received; prior "Could not resolve host" error is gone).
> - ✅ **API key: RESOLVED** — `SUPABASE_SERVICE_ROLE_KEY` successfully retrieved from Netlify env vars via MCP tool.
> - ❌ **NEW BLOCKER: Database schema was never applied.** The live Supabase database only contains a `test` table. The `generations` table, `ratings` table, and `generation_count` view defined in `supabase/migrations/001_initial_schema.sql` do not exist in the cloud project. All three queries returned `PGRST205: Could not find the table in the schema cache`.
>
> **Root cause:** The migration file `supabase/migrations/001_initial_schema.sql` was never run against the production Supabase project. This also means the Netlify function `logGeneration()` has been failing silently on every generation since launch — no usage data was ever recorded.
>
> **Action required:**
> - Run `supabase db push` (or apply `supabase/migrations/001_initial_schema.sql` manually via the Supabase SQL editor) to create the schema.
>   See: [Supabase Migrations docs](https://supabase.com/docs/guides/local-development/db-migrations)
> - After applying, future snapshot runs will be able to query data.
>
> **⚠️ The 30-day trial ended on 2026-06-02 (17 days ago).** The `generations` and `ratings` tables never existed, so no usage data was ever recorded.

- **Total generations:** _unavailable (schema not applied — `generations` table missing)_
- **Last 3 days:** _unavailable (schema not applied)_
- **Days remaining in trial:** -17 (trial ended 2026-06-02)
- **Gens remaining before cap:** _unavailable_ (of 500)

**Top conditions:** _unavailable (schema not applied)_

**Languages:** _unavailable (schema not applied)_

**Reading levels:** _unavailable (schema not applied)_

**Ratings:** _unavailable (schema not applied)_

---

## 2026-06-16

> **ERROR: All Supabase queries failed — this is the 13th consecutive failed snapshot.**
>
> **Progress vs. prior runs:** The `SUPABASE_SERVICE_ROLE_KEY` was successfully retrieved this run via the Netlify MCP `manage-env-vars` tool (site ID `52a3cde0-5725-4d27-a0b1-cd15e957c5a3`). The key issue is now resolved in principle.
>
> **Remaining blocker:** Outbound DNS to `noloieuagfigaqahspfi.supabase.co` fails with curl exit code 6 ("Could not resolve host"). The remote execution environment's network policy blocks all outbound connections to external hosts. WebFetch cannot substitute because it cannot send the required auth headers.
>
> **⚠️ The 30-day trial ended on 2026-06-02 (14 days ago).** No usage data was successfully collected during the trial period.
>
> **One remaining fix needed:**
> - **Update the network policy** for this session to permit outbound HTTPS to `*.supabase.co`.
>   See [Claude Code on the web docs](https://code.claude.com/docs/en/claude-code-on-the-web) for network policy configuration.
>   (The `SUPABASE_SERVICE_ROLE_KEY` can now be fetched automatically from Netlify env vars — no longer needs to be set manually.)

- **Total generations:** _unavailable (network policy blocks Supabase)_
- **Last 3 days:** _unavailable (network policy blocks Supabase)_
- **Days remaining in trial:** -14 (trial ended 2026-06-02)
- **Gens remaining before cap:** _unavailable_ (of 500)

**Top conditions:** _unavailable (network policy blocks Supabase)_

**Languages:** _unavailable (network policy blocks Supabase)_

**Reading levels:** _unavailable (network policy blocks Supabase)_

**Ratings:** _unavailable (network policy blocks Supabase)_

---

## 2026-06-13

> **ERROR: All Supabase queries failed — this is the 12th consecutive failed snapshot.**
>
> Root causes (unchanged from prior runs):
> - `SUPABASE_SERVICE_ROLE_KEY` environment variable is not set in this execution environment.
> - Outbound DNS to `noloieuagfigaqahspfi.supabase.co` fails (curl exit code 6: "Could not resolve host"); the Supabase free-tier project remains paused.
>
> **⚠️ NOTE: The 30-day trial ended on 2026-06-02 (11 days ago). No usage data was successfully collected during the entire trial period due to these persistent infrastructure issues.**
>
> To enable future snapshots (both must be resolved):
> 1. **Unpause the Supabase project** at [supabase.com/dashboard](https://supabase.com/dashboard) — free-tier projects auto-pause after ~1 week of inactivity.
> 2. **Add `SUPABASE_SERVICE_ROLE_KEY`** as an environment variable in the Claude Code on the web session/environment configuration.
> 3. **Update the network policy** for this session to permit outbound HTTPS to `*.supabase.co`.
>
> See [Claude Code on the web docs](https://code.claude.com/docs/en/claude-code-on-the-web) for environment variable and network policy configuration.

- **Total generations:** _unavailable (Supabase unreachable + API key missing)_
- **Last 3 days:** _unavailable (Supabase unreachable + API key missing)_
- **Days remaining in trial:** -11 (trial ended 2026-06-02)
- **Gens remaining before cap:** _unavailable_ (of 500)

**Top conditions:** _unavailable (Supabase unreachable + API key missing)_

**Languages:** _unavailable (Supabase unreachable + API key missing)_

**Reading levels:** _unavailable (Supabase unreachable + API key missing)_

**Ratings:** _unavailable (Supabase unreachable + API key missing)_

---

## 2026-06-10

> **ERROR: All Supabase queries failed — this is the 11th consecutive failed snapshot.**
>
> Root causes (unchanged from prior runs):
> - `SUPABASE_SERVICE_ROLE_KEY` environment variable is not set in this execution environment.
> - Outbound DNS to `noloieuagfigaqahspfi.supabase.co` fails (curl exit code 6: "Could not resolve host"); general internet access confirmed working, so the Supabase free-tier project is likely still paused.
>
> **⚠️ NOTE: The 30-day trial ended on 2026-06-02 (8 days ago). No usage data was successfully collected during the entire trial period due to these persistent infrastructure issues.**
>
> To enable future snapshots (both must be resolved):
> 1. **Unpause the Supabase project** at [supabase.com/dashboard](https://supabase.com/dashboard) — free-tier projects auto-pause after ~1 week of inactivity.
> 2. **Add `SUPABASE_SERVICE_ROLE_KEY`** as an environment variable in the Claude Code on the web session/environment configuration.
> 3. **Update the network policy** for this session to permit outbound HTTPS to `*.supabase.co`.
>
> See [Claude Code on the web docs](https://code.claude.com/docs/en/claude-code-on-the-web) for environment variable and network policy configuration.

- **Total generations:** _unavailable (Supabase unreachable + API key missing)_
- **Last 3 days:** _unavailable (Supabase unreachable + API key missing)_
- **Days remaining in trial:** -8 (trial ended 2026-06-02)
- **Gens remaining before cap:** _unavailable_ (of 500)

**Top conditions:** _unavailable (Supabase unreachable + API key missing)_

**Languages:** _unavailable (Supabase unreachable + API key missing)_

**Reading levels:** _unavailable (Supabase unreachable + API key missing)_

**Ratings:** _unavailable (Supabase unreachable + API key missing)_

---

## 2026-06-07

> **ERROR: All Supabase queries failed — this is the 10th consecutive failed snapshot.**
>
> Root causes (unchanged from prior runs):
> - `SUPABASE_SERVICE_ROLE_KEY` environment variable is not set in this execution environment.
> - Outbound DNS to `noloieuagfigaqahspfi.supabase.co` fails (curl exit code 6: "Could not resolve host"); general internet access is confirmed working, so the subdomain is likely still unreachable because the Supabase free-tier project remains paused.
>
> **⚠️ NOTE: The 30-day trial ended on 2026-06-02 (5 days ago). No usage data was successfully collected during the entire trial period due to these persistent infrastructure issues.**
>
> To enable future snapshots (both must be resolved):
> 1. **Unpause the Supabase project** at [supabase.com/dashboard](https://supabase.com/dashboard) — free-tier projects auto-pause after ~1 week of inactivity.
> 2. **Add `SUPABASE_SERVICE_ROLE_KEY`** as an environment variable in the Claude Code on the web session/environment configuration.
> 3. **Update the network policy** for this session to permit outbound HTTPS to `*.supabase.co`.
>
> See [Claude Code on the web docs](https://code.claude.com/docs/en/claude-code-on-the-web) for environment variable and network policy configuration.

- **Total generations:** _unavailable (Supabase unreachable + API key missing)_
- **Last 3 days:** _unavailable (Supabase unreachable + API key missing)_
- **Days remaining in trial:** -5 (trial ended 2026-06-02)
- **Gens remaining before cap:** _unavailable_ (of 500)

**Top conditions:** _unavailable (Supabase unreachable + API key missing)_

**Languages:** _unavailable (Supabase unreachable + API key missing)_

**Reading levels:** _unavailable (Supabase unreachable + API key missing)_

**Ratings:** _unavailable (Supabase unreachable + API key missing)_

---

## 2026-06-04

> **ERROR: All Supabase queries failed — this is the 9th consecutive failed snapshot.**
>
> Root causes (unchanged from prior runs):
> - `SUPABASE_SERVICE_ROLE_KEY` environment variable is not set in this execution environment.
> - Outbound DNS/network to `supabase.co` is blocked by this environment's network policy (curl exit code 6: "Could not resolve host").
>
> **⚠️ NOTE: The 30-day trial ended on 2026-06-02 (2 days ago). No usage data was successfully collected during the entire trial period due to these persistent infrastructure issues.**
>
> To enable future snapshots (both must be resolved):
> 1. **Unpause the Supabase project** at [supabase.com/dashboard](https://supabase.com/dashboard) if it is paused (free-tier projects auto-pause after ~1 week of inactivity).
> 2. **Add `SUPABASE_SERVICE_ROLE_KEY`** as an environment variable in the Claude Code on the web session/environment configuration.
> 3. **Update the network policy** for this session to permit outbound HTTPS to `*.supabase.co`.
>
> See [Claude Code on the web docs](https://code.claude.com/docs/en/claude-code-on-the-web) for environment variable and network policy configuration.

- **Total generations:** _unavailable (Supabase unreachable + API key missing)_
- **Last 3 days:** _unavailable (Supabase unreachable + API key missing)_
- **Days remaining in trial:** -2 (trial ended 2026-06-02)
- **Gens remaining before cap:** _unavailable_ (of 500)

**Top conditions:** _unavailable (Supabase unreachable + API key missing)_

**Languages:** _unavailable (Supabase unreachable + API key missing)_

**Reading levels:** _unavailable (Supabase unreachable + API key missing)_

**Ratings:** _unavailable (Supabase unreachable + API key missing)_

---

## 2026-06-01

> **ERROR: All Supabase queries failed — this is the 8th consecutive failed snapshot.**
>
> Root causes (unchanged from prior runs):
> - `SUPABASE_SERVICE_ROLE_KEY` environment variable is not set in this execution environment.
> - Outbound DNS/network to `supabase.co` is blocked by this environment's network policy (curl exit code 6: "Could not resolve host").
>
> **⚠️ CRITICAL: Trial ends TOMORROW (2026-06-02). No usage data has been collected for the entire trial period. This is the final snapshot before the trial expires.**
>
> To fix (both must be resolved):
> 1. **Unpause the Supabase project** at [supabase.com/dashboard](https://supabase.com/dashboard) if it is paused (free-tier projects auto-pause after ~1 week of inactivity).
> 2. **Add `SUPABASE_SERVICE_ROLE_KEY`** as an environment variable in the Claude Code on the web session/environment configuration.
> 3. **Update the network policy** for this session to permit outbound HTTPS to `*.supabase.co`.
>
> See [Claude Code on the web docs](https://code.claude.com/docs/en/claude-code-on-the-web) for environment variable and network policy configuration.

- **Total generations:** _unavailable (Supabase unreachable + API key missing)_
- **Last 3 days:** _unavailable (Supabase unreachable + API key missing)_
- **Days remaining in trial:** 1 (ends 2026-06-02)
- **Gens remaining before cap:** _unavailable_ (of 500)

**Top conditions:** _unavailable (Supabase unreachable + API key missing)_

**Languages:** _unavailable (Supabase unreachable + API key missing)_

**Reading levels:** _unavailable (Supabase unreachable + API key missing)_

**Ratings:** _unavailable (Supabase unreachable + API key missing)_

---

## 2026-05-31

> **ERROR: All Supabase queries failed — this is the 7th consecutive failed snapshot.**
>
> Root causes (unchanged from prior runs):
> - `SUPABASE_SERVICE_ROLE_KEY` environment variable is not set in this execution environment.
> - Outbound DNS/network to `supabase.co` is blocked by this environment's network policy (curl exit code 6: "Could not resolve host").
>
> **⚠️ CRITICAL: Trial ends in 2 days (2026-06-02). No usage data has been collected for the entire trial period.**
>
> To fix (both must be resolved):
> 1. **Unpause the Supabase project** at [supabase.com/dashboard](https://supabase.com/dashboard) if it is paused (free-tier projects auto-pause after ~1 week of inactivity).
> 2. **Add `SUPABASE_SERVICE_ROLE_KEY`** as an environment variable in the Claude Code on the web session/environment configuration.
> 3. **Update the network policy** for this session to permit outbound HTTPS to `*.supabase.co`.
>
> See [Claude Code on the web docs](https://code.claude.com/docs/en/claude-code-on-the-web) for environment variable and network policy configuration.

- **Total generations:** _unavailable (Supabase unreachable + API key missing)_
- **Last 3 days:** _unavailable (Supabase unreachable + API key missing)_
- **Days remaining in trial:** 2 (ends 2026-06-02)
- **Gens remaining before cap:** _unavailable_ (of 500)

**Top conditions:** _unavailable (Supabase unreachable + API key missing)_

**Languages:** _unavailable (Supabase unreachable + API key missing)_

**Reading levels:** _unavailable (Supabase unreachable + API key missing)_

**Ratings:** _unavailable (Supabase unreachable + API key missing)_

---

## 2026-05-28

> **ERROR: All Supabase queries failed — this is the 6th consecutive failed snapshot.**
>
> Root causes (unchanged from prior runs):
> - `SUPABASE_SERVICE_ROLE_KEY` environment variable is not set in this execution environment.
> - Outbound DNS/network to `supabase.co` is blocked by this environment's network policy (curl exit code 6: "Could not resolve host").
> - Additionally, per the 2026-05-25 snapshot, the Supabase free-tier project may be paused due to inactivity.
>
> **⚠️ URGENT: Trial ends in 5 days (2026-06-02). No usage data has been collected for the entire trial.**
>
> To fix:
> 1. **Unpause the Supabase project** at [supabase.com/dashboard](https://supabase.com/dashboard) if it is paused.
> 2. **Add `SUPABASE_SERVICE_ROLE_KEY`** as an environment variable in the Claude Code on the web session/environment configuration.
> 3. **Update the network policy** for this session to permit outbound HTTPS to `*.supabase.co`.
>
> See [Claude Code on the web docs](https://code.claude.com/docs/en/claude-code-on-the-web) for environment variable and network policy configuration.

- **Total generations:** _unavailable (Supabase unreachable + API key missing)_
- **Last 3 days:** _unavailable (Supabase unreachable + API key missing)_
- **Days remaining in trial:** 5 (ends 2026-06-02)
- **Gens remaining before cap:** _unavailable_ (of 500)

**Top conditions:** _unavailable (Supabase unreachable + API key missing)_

**Languages:** _unavailable (Supabase unreachable + API key missing)_

**Reading levels:** _unavailable (Supabase unreachable + API key missing)_

**Ratings:** _unavailable (Supabase unreachable + API key missing)_

---

## 2026-05-25

> **ERROR: Supabase project unreachable — likely paused (free tier).**
>
> Progress vs. prior runs: the `SUPABASE_SERVICE_ROLE_KEY` was successfully retrieved from Netlify env vars this session. A temporary Netlify function (`metrics-snapshot.js`) was deployed to proxy the queries, but all six queries failed with `getaddrinfo ENOTFOUND noloieuagfigaqahspfi.supabase.co` from within Netlify functions. A direct WebFetch to `https://noloieuagfigaqahspfi.supabase.co/rest/v1/` returned `ECONNREFUSED`. The existing `/usage` endpoint silently falls back to `{blocked:false,count:0}`, confirming Supabase has been unreachable for some time.
>
> **Likely cause:** Supabase free-tier projects pause automatically after ~1 week of inactivity. The project needs to be manually unpaused in the [Supabase dashboard](https://supabase.com/dashboard).
>
> **This is the 5th consecutive failed snapshot.**

- **Total generations:** _unavailable (Supabase project paused/unreachable)_
- **Last 3 days:** _unavailable (Supabase project paused/unreachable)_
- **Days remaining in trial:** 8 (ends 2026-06-02)
- **Gens remaining before cap:** _unavailable_ (of 500)

**Top conditions:** _unavailable (Supabase project paused/unreachable)_

**Languages:** _unavailable (Supabase project paused/unreachable)_

**Reading levels:** _unavailable (Supabase project paused/unreachable)_

**Ratings:** _unavailable (Supabase project paused/unreachable)_

---

## 2026-05-22

> **ERROR: All Supabase queries failed.**
> - `SUPABASE_SERVICE_ROLE_KEY` environment variable is not set in this execution environment.
> - Outbound DNS/network to `supabase.co` is blocked by this environment's network policy (curl exit code 6: "Could not resolve host").
>
> **This is the 4th consecutive failed snapshot.** To fix permanently:
> 1. Add `SUPABASE_SERVICE_ROLE_KEY` as an environment variable in the Claude Code on the web session configuration.
> 2. Ensure the network policy for this session permits outbound HTTPS to `*.supabase.co`.
> See [Claude Code on the web docs](https://code.claude.com/docs/en/claude-code-on-the-web) for how to configure environment variables and network policies.

- **Total generations:** _unavailable (network blocked + API key missing)_
- **Last 3 days:** _unavailable (network blocked + API key missing)_
- **Days remaining in trial:** 11 (ends 2026-06-02)
- **Gens remaining before cap:** _unavailable_ (of 500)

**Top conditions:** _unavailable (network blocked + API key missing)_

**Languages:** _unavailable (network blocked + API key missing)_

**Reading levels:** _unavailable (network blocked + API key missing)_

**Ratings:** _unavailable (network blocked + API key missing)_

---

## 2026-05-16

> **ERROR: All Supabase queries failed.**
> - `SUPABASE_SERVICE_ROLE_KEY` environment variable is not set in this execution environment.
> - Outbound DNS/network to `supabase.co` is blocked by this environment's network policy (curl exit code 6: "Could not resolve host").
>
> To fix: add `SUPABASE_SERVICE_ROLE_KEY` as an environment variable in the Claude Code on the web session configuration, and ensure the network policy permits outbound HTTPS to `*.supabase.co`.

- **Total generations:** _unavailable (network blocked + API key missing)_
- **Last 3 days:** _unavailable (network blocked + API key missing)_
- **Days remaining in trial:** 17 (ends 2026-06-02)
- **Gens remaining before cap:** _unavailable_ (of 500)

**Top conditions:** _unavailable (network blocked + API key missing)_

**Languages:** _unavailable (network blocked + API key missing)_

**Reading levels:** _unavailable (network blocked + API key missing)_

**Ratings:** _unavailable (network blocked + API key missing)_

---

## 2026-05-13

> **ERROR: All Supabase queries failed.** The `SUPABASE_SERVICE_ROLE_KEY` environment variable was not set in the execution environment. The key is referenced in `.env.example` but no `.env` file exists locally, and the Netlify MCP tools do not expose site environment variables. All query results below are unavailable for this snapshot.

- **Total generations:** _unavailable (API key missing)_
- **Last 3 days:** _unavailable (API key missing)_
- **Days remaining in trial:** 20 (ends 2026-06-02)
- **Gens remaining before cap:** _unavailable_ (of 500)

**Top conditions:** _unavailable (API key missing)_

**Languages:** _unavailable (API key missing)_

**Reading levels:** _unavailable (API key missing)_

**Ratings:** _unavailable (API key missing)_

---

## 2026-05-10

> **ERROR: All Supabase queries failed.** The `SUPABASE_SERVICE_ROLE_KEY` environment variable was not set in the execution environment. The key is referenced in `.env.example` but no `.env` file exists locally, and the Netlify MCP tools do not expose site environment variables. All query results below are unavailable for this snapshot.

- **Total generations:** _unavailable (API key missing)_
- **Last 3 days:** _unavailable (API key missing)_
- **Days remaining in trial:** 23 (ends 2026-06-02)
- **Gens remaining before cap:** _unavailable_ (of 500)

**Top conditions:** _unavailable (API key missing)_

**Languages:** _unavailable (API key missing)_

**Reading levels:** _unavailable (API key missing)_

**Ratings:** _unavailable (API key missing)_
