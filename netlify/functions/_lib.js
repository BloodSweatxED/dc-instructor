export function jsonResponse(status, body, extraHeaders = {}) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { 'Content-Type': 'application/json', ...extraHeaders },
  });
}

// Browser-enforced guard: blocks other websites from calling these functions
// cross-origin. Requests without an Origin header (curl, server-to-server) pass.
export function originAllowed(req) {
  const origin = req.headers.get('origin');
  if (!origin) return true;
  const allowed = [
    process.env.URL,
    process.env.DEPLOY_PRIME_URL,
    process.env.DEPLOY_URL,
    'http://localhost:5173',
    'http://localhost:8888',
  ].filter(Boolean);
  return allowed.includes(origin);
}

export async function checkLimits() {
  const url = process.env.VITE_SUPABASE_URL || process.env.SUPABASE_URL;
  const svc = process.env.SUPABASE_SERVICE_ROLE_KEY;
  if (url && svc) {
    try {
      const r = await fetch(`${url}/rest/v1/generation_count?select=count`, {
        headers: { apikey: svc, Authorization: `Bearer ${svc}` },
      });
      const rows = await r.json();
      const count = Array.isArray(rows) ? (rows[0]?.count ?? 0) : 0;
      if (count >= 500) return { blocked: true, reason: 'limit', count };
      return { blocked: false, count, warning: count >= 400 };
    } catch (e) {
      // Fail open so an unreachable Supabase never blocks generation,
      // but make the degraded state visible in function logs.
      console.error('checkLimits: Supabase unreachable, limit not enforced', e?.message);
      return { blocked: false, count: 0, degraded: true };
    }
  }
  return { blocked: false, count: 0 };
}

export async function logGeneration({ reading_level, language, condition_input, has_image_request }) {
  const url = process.env.VITE_SUPABASE_URL || process.env.SUPABASE_URL;
  const svc = process.env.SUPABASE_SERVICE_ROLE_KEY;
  if (!url || !svc) return null;
  try {
    const r = await fetch(`${url}/rest/v1/generations`, {
      method: 'POST',
      headers: {
        apikey: svc,
        Authorization: `Bearer ${svc}`,
        'Content-Type': 'application/json',
        Prefer: 'return=representation',
      },
      body: JSON.stringify({
        reading_level,
        language,
        condition_input: (condition_input || '').slice(0, 200),
        has_image_request: !!has_image_request,
      }),
    });
    const rows = await r.json();
    return Array.isArray(rows) ? rows[0]?.id : null;
  } catch (e) {
    console.error('logGeneration: insert failed', e?.message);
    return null;
  }
}
