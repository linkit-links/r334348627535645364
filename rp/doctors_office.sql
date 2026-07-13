-- Insert new roleplay: The Doctor's Office (hidden for now)
insert into public.roleplays (
  id,
  title,
  emoji,
  subtitle,
  description,
  tags,
  cover,
  folder,
  content_file,
  is_hidden,
  sort_order
) values (
  'doctors_office',
  'The Doctor''s Office',
  '🩺',
  'She''ll examine you very, very thoroughly',
  'A routine check-up with a beautiful doctor who takes her time. She leans in close, warm hands and a soft voice, promising to be gentle as the examination gets more personal than you ever expected.',
  array['Flirty', 'Caring', 'Slow Burn']::text[],
  'rp_cover',
  'doctors_office',
  'doctors_office.json',
  true,
  0
)
on conflict (id) do update set
  title = excluded.title,
  emoji = excluded.emoji,
  subtitle = excluded.subtitle,
  description = excluded.description,
  tags = excluded.tags,
  cover = excluded.cover,
  folder = excluded.folder,
  content_file = excluded.content_file,
  is_hidden = excluded.is_hidden,
  sort_order = excluded.sort_order;
