# Detective Sasha — Localization Style

Simple everyday language. Flirty / sexy / slow-burn spy heat — match English exactly. Do **not** sanitize. Do **not** go more explicit than EN.

## Reading level

- Short sentences, common words, natural speech (thriller / dating-app energy)
- A 16–30 year old native should understand every line quickly
- Avoid textbook grammar, rare literary words, and machine-translation flatness

## Voice split

| Voice | How it sounds |
|-------|----------------|
| **narrator** | Second-person “you”, cinematic but simple |
| **Sasha** (nodes with no `speaker`) | Dry, lethal, teasing. Calls the player *husband* / *darling*. Armor first, heat later. |

## Heat curve

| Chapters | Heat |
|----------|------|
| CH01–CH04 | Cover marriage, tease, one bed, performance |
| CH05–CH08 | Close call, almost-kiss, gala, compromised |
| CH09–CH11 | Wound, honeypot, the line |
| CH12–CH15 | Betrayal, all-in, extraction, “I love you”, off-grid |

## Must preserve

- Names: **Sasha**, **Volkov**, **Cole** (Mr. / Mrs. Cole)
- Spy frame: cover, handler, mission, tap, gala, extraction
- Markdown `*emphasis*` — keep asterisks; translate words inside
- Emojis 🙂 😏 💍 🕵️‍♀️ 🛩️ 🌅 etc. — similar placement
- Line breaks: one beat per `lines[]` entry as in EN
- Player male-coded; Sasha she/her — gender agreement in PT/RU/HI

## Never change

`id`, `start`, `emoji`, `video`, `vars`, `nodes[].id`, `next`, `speaker`, `chapterStart`, `videoUrl`, `imageUrl`, `choices[].set`, `choices[].next`

## Per language

| Code | Voice |
|------|--------|
| **id** | Bahasa sehari-hari, santai, menggoda. Not stiff formal Indonesian. |
| **pt** | Informal **Brazilian** Portuguese (você, tá, pra, né). Not European PT. |
| **ru** | Простой разговорный, игривый/горячий. **Ты** to the player. |
| **hi** | **Correct Roman Hindi** (`rp/HINGLISH.md`). tum/tumhara, not tu. Full Hindi verbs. Husband/cover stay as loans. |
