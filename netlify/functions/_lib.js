export function jsonResponse(status, body, extraHeaders = {}) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { 'Content-Type': 'application/json', ...extraHeaders },
  });
}

export async function checkLimits() {
  const launch = process.env.LAUNCH_DATE;
  if (launch) {
    const launchMs = Date.parse(launch);
    if (!Number.isNaN(launchMs)) {
      const ageDays = (Date.now() - launchMs) / (1000 * 60 * 60 * 24);
      if (ageDays > 30) return { blocked: true, reason: 'expired' };
    }
  }
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
    } catch {
      return { blocked: false, count: 0 };
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
  } catch {
    return null;
  }
}
