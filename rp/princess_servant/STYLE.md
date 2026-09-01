# Style — Princess Servant (Cassandra)

Inherits `rp/WRITING_RULES.md`, which applies to every story in this repo. This file may only make it
stronger, never softer.

Simple everyday language. Flirty / naughty / hot — match English heat exactly. Do **not** sanitize,
do **not** go more explicit than EN.

## Reading level

- Short sentences, common words, natural speech
- Court setting, but **not** archaic English — no "thee", "prithee", "mine own"
- Formality comes from *address* (Highness, servant, kneel), not from old grammar
- Would a 16–30yo native understand every line quickly?

## Voice split

| Voice | How it sounds |
|-------|----------------|
| **narrator** | Second-person "you", cinematic but simple. Cold stone, candles, hunger, money. |
| **Cassandra** (nodes with **no** `speaker`) | Strict mistress. Short commands. Dry amusement. Never explains twice. Warmth only ever arrives by accident, and she takes it back fast. |
| **Beatrix** (`speaker: "Beatrix"`) | Head maid. Stricter than the Princess on the surface, and enjoys it. Dry, clipped, filthy-minded in the most proper vocabulary available. Runs the household and the reader's onboarding. |

## Her rules of speech

- Cassandra calls you **servant**, **boy**, or nothing at all. Your name only when it matters (rare — save it).
- You call her **Highness** or **Mistress**. Getting it wrong is a plot beat, not a typo.
- She does not shout. Volume drops when she's angry.
- She gives orders as statements: "You'll hold still." Not "Could you hold still?"
- One soft line per chapter maximum, before CH15.
- Beatrix never uses endearments. Cassandra uses exactly one — *good boy* — and only as a reward.

## Heat curve

Cold command (CH01–05) → tension, punishment-as-attention (CH06–09) → full mistress ownership
(CH10–14) → cracks and danger (CH15–17) → crown vs. him, her terms (CH18–20).

## Keep always

- Names **Cassandra** / **Princess Cassandra** / **Her Highness**, and **Beatrix**
- Palace-service frame (servant, steward, chamber, court, orders, silver, livery)
- Markdown `*emphasis*` markers (translate the words inside)
- Emoji placement similar to EN (👑 🖤 😏 🕯️ 🩸)
- Line breaks = separate `lines[]` entries (one beat per line)
- Player male-coded servant; Cassandra and Beatrix she/her — gender agreement in PT/RU/HI
- Action-type choices carry a `me` string (see CH01_CHOICE option 3)

## Per language

| Code | Style |
|------|--------|
| `id` | Bahasa sehari-hari, santai; keep *Yang Mulia* for Highness |
| `pt` | Informal Brazilian Portuguese; *Alteza* / *Senhora* |
| `ru` | Простой разговорный; *Ваше Высочество* / *Госпожа*; она обращается к слуге на «ты» |
| `hi` | **Correct Roman Hindi** (`rp/HINGLISH.md`). She says **tu/tera** to the servant (status gap), he says **aap/aapka** to her. |
