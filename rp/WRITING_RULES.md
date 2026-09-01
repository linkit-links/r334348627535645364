# Writing rules — ALL roleplays (global)

Applies to every story folder under `rp/`: existing (`doctors_office`, `nurse_mei`,
`captured_princess_elara`, `yui`, `sasha_secret_agent`, `gym_trainer`, `same_room_weekend`,
`princess_servant`) and every new one. Each story's own `STYLE.md` inherits these rules and may only
make them *stronger*, never softer.

## Rule 1 — Tone is always flirty, sexy, naughty and bold

Every chapter, every locale, start to finish. The female lead teases, provokes, owns the room, and
says the thing a normal person wouldn't. Even the cold chapters, the sad chapters and the action
chapters keep the charge underneath.

- She flirts on purpose and enjoys the effect
- Suggestive lines, double meanings, teasing, dares, commands
- Bold: she says it out loud instead of hinting
- Physical closeness described plainly — hands, weight, breath, warmth, skin
- Never sanitize a beat into something polite. If a line can be hotter, make it hotter
- Clothed and non-explicit: fade at the line, don't cross it. Nothing that blocks a store listing
- All characters are adults

## Rule 2 — Very simple, day-to-day language

Write the way people actually talk. No complex grammar, no literary showing off.

**Do:**
- Short sentences. One idea each
- Common everyday words
- Contractions — *don't, you're, I'll, isn't*
- Natural speech rhythm: chat, soap opera, dating-app energy
- Fragments are fine. *Not tonight. Down. Again.*
- One beat per line in `lines[]`

**Don't:**
- Long sentences with three clauses stitched together
- Rare or bookish words when a plain one exists
- Archaic English in period settings — no *thee, thou, prithee, mine own, whilst, hence*
- Textbook grammar that nobody speaks
- Purple description that delays the beat

Test: would a 16–30 year old native speaker understand every line instantly, first read, without
stopping? If not, cut it down.

Period and fantasy settings get their formality from **how people address each other** (Highness,
servant, Mistress, kneel) — never from old grammar.

## Rule 3 — Player-facing choices

- Choices sound like something a real person would actually say
- Keep them short — one line, readable at a glance
- Give the player range: bold / teasing / obedient / silent-action
- Action choices go in parentheses and carry a `me` string

## Rule 4 — Structure

- Story is **linear**. Choices change her immediate reply, then reconverge on the same spine. No
  `vars`, no `set` blocks, no locked content
- Branches: `_A` / `_B` / `_C` → `_MERGE`
- `speaker: "narrator"` for narration; **omit `speaker`** for the female lead; named speaker for
  anyone else
- Chapters end on a hook: `(To be continued — Chapter N: Title)`

## Rule 5 — Translations

Match the English heat **exactly**. Do not soften it for any locale, and do not push it further than
EN either. Same simple everyday register in every language — informal, spoken, natural. See each
story's `GLOSSARY.md` for locked terms and address register.
