-- Insert new roleplay: One Room Weekend (hidden for now)
insert into public.roleplays (
  id,
  title,
  emoji,
  subtitle,
  description,
  tags,
  badge,
  cover,
  folder,
  content_file,
  is_hidden,
  sort_order
) values (
  'same_room_weekend',
  'Same Bed Weekend',
  '🏨',
  'One suite. One bed. One very interesting weekend.',
  'A hotel booking error puts you in the same suite as Elena Rossi — sleek, composed, and impossible to ignore. One bed, one weekend, and a slow burn that turns a stranger into the best mistake of your year.',
  array['Flirty', 'Slow Burn', 'Bold']::text[],
  'New',
  'rp_cover',
  'same_room_weekend',
  'same_room_weekend/en.json',
  true,
  6
)
on conflict (id) do update set
  title = excluded.title,
  emoji = excluded.emoji,
  subtitle = excluded.subtitle,
  description = excluded.description,
  tags = excluded.tags,
  badge = excluded.badge,
  cover = excluded.cover,
  folder = excluded.folder,
  content_file = excluded.content_file,
  is_hidden = excluded.is_hidden,
  sort_order = excluded.sort_order;
