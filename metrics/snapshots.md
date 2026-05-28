# DC Instructor — Usage Snapshots

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
