-- DC Instructor — initial schema
create extension if not exists "pgcrypto";

create table if not exists generations (
  id uuid primary key default gen_random_uuid(),
  created_at timestamptz not null default now(),
  reading_level text not null,
  language text not null,
  condition_input text,
  has_image_request boolean not null default false,
  rating integer
);

create table if not exists ratings (
  id uuid primary key default gen_random_uuid(),
  generation_id uuid references generations(id) on delete set null,
  stars integer not null check (stars between 1 and 5),
  comment text,
  created_at timestamptz not null default now()
);

create or replace view generation_count as
  select count(*)::int as count from generations;

alter table generations enable row level security;
alter table ratings enable row level security;

-- Anon clients can submit ratings
create policy "anon insert ratings" on ratings
  for insert to anon with check (true);

-- The public counter view is readable by anon
grant select on generation_count to anon;

-- Generations are written only by the service role (Netlify Functions)
-- No anon insert policy → blocked by RLS
