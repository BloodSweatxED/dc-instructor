import { createClient } from '@supabase/supabase-js';

const url = import.meta.env.VITE_SUPABASE_URL;
const anon = import.meta.env.VITE_SUPABASE_ANON_KEY;

export const supabase = url && anon ? createClient(url, anon) : null;

export async function getGenerationCount() {
  if (!supabase) return 0;
  const { data, error } = await supabase.from('generation_count').select('count').single();
  if (error) return 0;
  return data?.count ?? 0;
}

export async function submitRating({ generation_id, stars, comment }) {
  if (!supabase) return;
  await supabase.from('ratings').insert({ generation_id, stars, comment: comment || null });
}
