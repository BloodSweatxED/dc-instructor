// Scheduled ping to keep the Supabase free-tier project from auto-pausing.
// Runs weekly; a single lightweight read is enough to count as activity.
export const config = { schedule: '@weekly' };

export default async () => {
  const url = process.env.VITE_SUPABASE_URL || process.env.SUPABASE_URL;
  const svc = process.env.SUPABASE_SERVICE_ROLE_KEY;
  if (!url || !svc) {
    console.error('keepalive: Supabase env vars missing');
    return new Response('missing env', { status: 500 });
  }
  try {
    const r = await fetch(`${url}/rest/v1/generation_count?select=count`, {
      headers: { apikey: svc, Authorization: `Bearer ${svc}` },
    });
    if (!r.ok) {
      console.error(`keepalive: Supabase responded ${r.status}`);
      return new Response(`supabase ${r.status}`, { status: 502 });
    }
    console.log('keepalive: ok');
    return new Response('ok');
  } catch (e) {
    console.error('keepalive: fetch failed', e);
    return new Response('fetch failed', { status: 502 });
  }
};
