# Style guide — Captured Princess Elara

## Goal

Ship **simple everyday language** in each locale that matches English: dark, tragic, intimate, and intense — never sanitized, never more explicit/brutal than EN.

## Reading level

- Short sentences, common words, natural speech
- Chat / oral storytelling energy (not textbook, not literary epic)
- A 16–30yo native should understand every line quickly

## Heat / darkness level

- Match EN chapter by chapter
- Early: duty, shame, quiet care (feeding by hand, name given)
- Mid: interrogation, lash, brand, rack, trough — keep the cruelty clear and the guard’s tenderness clear
- Late: love under threat, last stand, fight
- Do **not** soften torture or emotional stakes
- Do **not** add gore or sex beyond what EN already has

## Voice split

| Voice | How it sounds |
|-------|----------------|
| **narrator** | Second person “you” (the guard). Cinematic but simple. Feels what you feel. |
| **Elara** (nodes without `speaker`) | Pride, dry edge, fear under control, rare soft cracks. She is a princess-soldier, not a damsel monologue. |

## Always keep

- Names: **Elara**, **Liora**, **Vance**, place **Valdere** (transliterate only where the script requires it — see GLOSSARY)
- Markdown emphasis: keep `*markers*`; translate words inside
- Emojis if any: same placement
- Line breaks: same number of `lines[]` entries per node (one beat per line as EN)
- Gender: player = male-coded guard/soldier; Elara = she/her — mirror agreement in PT / RU / HI

## Per-language voice

| Code | Language | Style |
|------|----------|--------|
| `en` | English | Source of truth |
| `id` | Indonesian | Bahasa sehari-hari, santai tapi serius; gelap & emosional |
| `pt` | Portuguese (Brazil) | Informal BR, drama quente, **not** European PT |
| `ru` | Russian | Простой разговорный, тёмный / нежный, не книжный |
| `hi` | Hindi | **Correct Roman Hindi** (`rp/HINGLISH.md`). tum/tumhara, not tu. |

## Do not translate (copy from `en.json`)

- `id`, `start`, `emoji`
- Every `nodes[].id`, `next`, `speaker`, `chapterStart`
- `videoUrl`, `imageUrl`
- Structure: same node count, same lines array lengths

## Translate

- Top-level `title`, `subtitle`
- `nodes[].chapterTitle`
- `nodes[].lines[]`
