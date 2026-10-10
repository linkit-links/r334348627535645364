-- Catalog rows for Lingerie Thief and Pay With Her Body.
-- There is no table named "Lingerie Thef Salve"; stories live in public.roleplays.

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
  badge,
  is_hidden,
  sort_order
) values
(
  'lingerie_thief',
  'Lingerie Thief',
  '🖤',
  'You bought the thief soft. You pack her hard. The trunk is only the start.',
  'She walked into the boutique for three lace sets and left the counter with one. You caught the rest on her body. The bill stops being money, and the thief becomes yours.',
  array['BDSM', 'Ownership', 'Slave']::text[],
  'rp_cover',
  'lingerie_thief',
  'lingerie_thief/en.json',
  '18+',
  false,
  1
),
(
  'pay_with_body',
  'Pay With Her Body',
  '🔑',
  'The ledger is open. Cash is gone. Her body is next.',
  'Unit 4B is behind on rent. The landlord opens the ledger, crosses out the cash, and starts taking payment from Elena one receipt at a time.',
  array['BDSM', 'Ownership', 'Slave']::text[],
  'rp_cover',
  'pay_with_body',
  'pay_with_body/en.json',
  'New',
  false,
  9
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
  badge = excluded.badge,
  is_hidden = excluded.is_hidden,
  sort_order = excluded.sort_order,
  updated_at = now();

-- Lingerie Thief takes slot 1. Every other story keeps its previous order and shifts down.
update public.roleplays
set sort_order = case id
  when 'lingerie_thief' then 1
  when 'gym_trainer' then 2
  when 'doctors_office' then 3
  when 'nurse_mei' then 4
  when 'yui' then 5
  when 'captured_princess_elara' then 6
  when 'same_room_weekend' then 7
  when 'princess_servant' then 8
  when 'pay_with_body' then 9
end,
updated_at = now()
where id in (
  'lingerie_thief',
  'gym_trainer',
  'doctors_office',
  'nurse_mei',
  'yui',
  'captured_princess_elara',
  'same_room_weekend',
  'princess_servant',
  'pay_with_body'
);

delete from public.roleplays where id = 'agent_sasha';

update public.roleplays
set bg_video_url = case id
  when 'lingerie_thief' then 'https://linkit-links.github.io/r334348627535645364/rp/lingerie_thief/bg_cover_video.mkv'
  when 'pay_with_body' then 'https://linkit-links.github.io/r334348627535645364/rp/pay_with_body/bg_cover_video.mkv'
end,
updated_at = now()
where id in ('lingerie_thief', 'pay_with_body');

-- Still backgrounds until a real clip exists. The app uses bg_video_url first, so clear it.
update public.roleplays
set bg_video_url = null,
    bg_image_url = case id
      when 'lingerie_thief' then 'https://linkit-links.github.io/r334348627535645364/rp/lingerie_thief/bg_cover.webp'
      when 'pay_with_body' then 'https://linkit-links.github.io/r334348627535645364/rp/pay_with_body/bg_cover.webp'
    end,
    updated_at = now()
where id in ('lingerie_thief', 'pay_with_body');
