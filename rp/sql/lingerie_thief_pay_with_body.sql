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
  array['Dark', 'Ownership', 'Explicit']::text[],
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
  array['Dark', 'Debt', 'Explicit']::text[],
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
