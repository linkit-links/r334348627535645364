# Nurse Mei — Localization Style

## Goal

Simple everyday language that stays **flirty / sexy / hot** like English. Chat / soap / dating-app energy — not textbook or literary.

## Reading level

- Short sentences, common words, natural speech
- A 16–30 year old native should understand every line quickly
- Avoid rare literary words, stiff formal grammar, and machine-translation flatness

## Heat curve

| Chapters | Heat |
|----------|------|
| CH01–CH05 | Soft tease, warm care, light tension |
| CH06–CH10 | Heat rises (rain, pinned, rules, body closeness) |
| CH11–CH15 | Kiss, choice, “I love you”, afterglow — match EN explicitness |

Do **not** sanitize. Do **not** go more explicit than English.

## Voice split

1. **narrator** — second person “you”, cinematic but simple
2. **Mei** (nodes without speaker, or her dialogue) — warm, teasing, slightly bossy nurse energy

## Must preserve

- Name **Mei** (see GLOSSARY for script variants)
- Medical-care frame: nurse, checkup, patient, doctor’s orders
- Line breaks: one emotional beat per `lines[]` entry as in EN
- Markdown emphasis `*like this*` — keep asterisks; translate words inside
- Emojis 🙂 😏 🩺 🙊 😌 etc. — similar placement
- JSON structure: same nodes, same choices, same ids, same `next` / `set` / media URLs

## Never change

`id`, `start`, `emoji`, `video`, `nodes[].id`, `next`, `speaker`, `chapterStart`, `videoUrl`, `imageUrl`, `choices[].set`, `choices[].next`

## Locale voice notes

| Code | Voice |
|------|--------|
| **id** | Bahasa sehari-hari, santai, menggoda. Not stiff formal Indonesian. |
| **pt** | Informal **Brazilian** Portuguese (você, tá, pra, né). Not European PT. |
| **ru** | Простой разговорный русский, игривый/горячий. Ты to player. |
| **hi** | **Correct Roman Hindi** (`rp/HINGLISH.md`). tum/tumhara, not tu. Full Hindi verbs. |

## Spot-check scenes (tone pass)

1. Opening door (CH01)
2. First real tension checkup (CH02)
3. Rain / kiss (CH08, CH12)
4. Final “I love you” choice (CH14–CH15)
