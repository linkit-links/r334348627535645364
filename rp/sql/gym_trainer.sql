-- Insert new roleplay: Gym Trainer Lexi (hidden for now)
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
  'gym_trainer',
  'Private Session',
  '💪',
  'You booked her private. She brought other plans.',
  'Your home gym. After hours. You paid for a private trainer — and Lexi walks in like she already owns the room. Sports bra, wicked little smile, hands correcting your form a little too close. By the first stretch it''s obvious this session was never only about your gains.',
  array['Flirty', 'Teasing', 'Slow Burn']::text[],
  'rp_cover',
  'gym_trainer',
  'gym_trainer/en.json',
  true,
  5
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
