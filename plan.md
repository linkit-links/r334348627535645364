# Plan: Localize `nurse_mei` RP (ID / PT-BR / RU / HI)

## Goal

Ship **Nurse Mei** as 5 language JSON files (English + 4 translations) under `rp/nurse_mei/`, using **simple everyday language** that stays **flirty / sexy / hot** like the English source. Android loads the correct locale file; media stays shared.

**Languages:** Indonesian (`id`), Brazilian Portuguese (`pt`), Russian (`ru`), Hindi (`hi`) — ordered by your Play analytics (Indonesia / Brazil / Russia, then Hindi for India volume).

---

## Source snapshot (what we are translating)

| Metric | Value |
|--------|------:|
| File | `rp/nurse_mei.json` (~100 KB, 2144 lines) |
| Nodes | 164 |
| Chapters | 15 (`CH01` … `CH15`) |
| Dialogue lines | 642 (~62K chars) |
| Choice labels | 45 |
| Silent action lines (`me`) | 10 |
| Est. total translatable chars | ~66K English source |

**Schema (keep identical across locales):**

```text
{
  id, title, emoji, subtitle, video, start,
  nodes: [{
    id, chapterStart?, chapterTitle?, speaker?,
    lines: string[],
    next?, videoUrl?, imageUrl?,
    choices?: [{ label, set, next, me? }]
  }]
}
```

---

## Target folder structure

Move story JSON **into** the existing media folder. One language = one full JSON (same graph, different strings).

```text
rp/
  rp_lists.json                 # update path + optional listing copy
  nurse_mei/
    en.json                     # moved from rp/nurse_mei.json (source of truth)
    id.json                     # Indonesian
    pt.json                     # Brazilian Portuguese (your Brazil users)
    ru.json                     # Russian
    hi.json                     # Hinglish (Roman script, not Devanagari)
    rp_cover_nurse.webp         # media unchanged
    mei_arrival.mkv
    ...
```

**Naming rules**

| Code | Language | Style |
|------|----------|--------|
| `en` | English | Source; polish only if needed |
| `id` | Indonesian | Bahasa sehari-hari, santai, menggoda |
| `pt` | Portuguese (Brazil) | Informal BR, flerte quente, not European PT |
| `ru` | Russian | Простой разговорный, игривый/горячий |
| `hi` | Hindi | Hinglish in **Roman script** (not Devanagari). Everyday chat: tum/tera, not aap. |

**Do not** invent parallel media folders. `videoUrl` / `imageUrl` stay English-path URLs as today.

---

## What to translate vs lock

### Translate (every locale file)

| Field | Notes |
|-------|--------|
| Top-level `title`, `subtitle` | Keep character name **Mei** |
| `nodes[].chapterTitle` | 15 titles |
| `nodes[].lines[]` | Main workload |
| `choices[].label` | Player choice UI |
| `choices[].me` | Silent “you do X” beat (10 places) |

Also update **catalog copy** in `rp_lists.json` (or locale overlays — see below): `title`, `subtitle`, `description`, `tags`.

### Never translate (copy byte-for-byte from `en.json`)

- `id`, `start`, `emoji`, `video`
- Every `nodes[].id`, `next`, `speaker`, `chapterStart`
- `videoUrl`, `imageUrl` (absolute GitHub Pages links)
- `choices[].next`
- Markdown emphasis markers `*like this*` — keep markers; translate the words inside
- Emojis in dialogue (🙂 😏 🩺 etc.) — keep placement similar

**Invariant:** same node count, same choice counts per node, same id graph. Only string values change.

---

## Tone & style guide (all languages)

Apply on every chapter before marking done.

1. **Reading level:** short sentences, common words, natural speech (chat / soap / dating-app energy). Avoid textbook grammar and rare literary words.
2. **Heat level:** match English. Soft tease early chapters → hotter later (`The Kiss`, bed, rain, rules broken). Do **not** sanitize, and do **not** jump more explicit than EN.
3. **Voice split:**
   - **narrator** = second-person “you”, cinematic but simple
   - **Mei** (nodes with no `speaker` / her dialogue) = warm, teasing, slightly bossy nurse energy
4. **Keep:** name **Mei**, medical-care frame (nurse, checkup, patient), slow-burn stats flavor in wording where it appears naturally
5. **Preserve:** line breaks as separate `lines[]` entries (one emotional beat per line where EN does)
6. **Gender:** player is addressed as in EN (male-coded recovery patient); Mei is she/her — mirror that in languages with gender agreement (PT, RU, HI)

### Mini glossary (consistent across chapters)

| English | id | pt-BR | ru | hi |
|---------|----|-------|----|----|
| nurse | perawat | enfermeira | медсестра | nurse |
| patient | pasien | paciente | пациент | patient |
| checkup | pemeriksaan | check-up / exame | осмотр | checkup |
| agency | agensi | agência | агентство | agency |
| doctor's orders | perintah dokter | ordens do médico | указания врача | doctor ke orders |
| night shift | shift malam | plantão da noite | ночная смена | night shift |
| Mei | Mei | Mei | Мэй / Mei | Mei |

(Lock final glossary in a small `rp/nurse_mei/GLOSSARY.md` during execution so all 15 chapters stay consistent.)

---

## Android / client loading contract

This repo hosts content (GitHub Pages). The **Android app** must resolve locale → file:

```text
base = .../rp/nurse_mei/
preferred = { device language mapped to en|id|pt|ru|hi }
load base + preferred + ".json"
if 404 or parse fail → load base + "en.json"
```

**Suggested device → file map**

| Device locale | File |
|---------------|------|
| `in` / `id` | `id.json` |
| `pt` / `pt-BR` | `pt.json` |
| `ru` | `ru.json` |
| `hi` | `hi.json` |
| everything else | `en.json` |

**`rp_lists.json` change**

```json
{
  "id": "nurse_mei",
  "folder": "nurse_mei",
  "file": "en.json",
  "locales": ["en", "id", "pt", "ru", "hi"],
  ...
}
```

(Or keep `"file": "nurse_mei/en.json"` if the app currently prefixes folder differently — **must match whatever the Android client already does**.)

**Backward compatibility:** after move, old URL `.../rp/nurse_mei.json` breaks. Options (pick one during implementation):

1. **Preferred:** update app + `rp_lists` only (clean).
2. **Safety:** leave a tiny stub `rp/nurse_mei.json` that is either a copy of `en.json` or redirects docs — only if old app builds still hardcode the path.

---

## How we execute a big RP (process)

### Phase 0 — Repo restructure (small, first PR)

1. Copy/move `rp/nurse_mei.json` → `rp/nurse_mei/en.json`
2. Update `rp_lists.json` `file` path + add `locales` if useful
3. Grep/fix any other references to `nurse_mei.json`
4. Add empty placeholders or omit until translated: `id.json`, `pt.json`, `ru.json`, `hi.json` only after each language completes (do not ship half-broken files)
5. Add `rp/nurse_mei/GLOSSARY.md` + `rp/nurse_mei/STYLE.md` (short)
6. Add a **validator script** (see Phase 2) run in CI or locally

### Phase 1 — Translate chapter-by-chapter (main work)

Work **one language at a time** (finish `id` fully before `pt`, etc.) so voice stays consistent.

**Order inside a language:** CH01 → CH15 (story order). Heavier mid/late chapters (Caught in the Rain ~6.4K chars, Stronger, Nurse's Orders) get extra tone review.

**Per chapter checklist**

1. Copy structure from `en.json` nodes for that chapter id prefix (`CH0N_…`)
2. Translate `chapterTitle`, all `lines`, choice `label` / `me`
3. Keep `*emphasis*` and emojis
4. Read aloud test: would a 16–30yo native understand every line quickly?
5. Heat check vs EN adjacent lines
6. Run validator on partial file if translating into full-file copies

**Practical batching:** each language ≈ 15 chapters. Suggest shipping:

| Batch | Chapters | Notes |
|-------|----------|--------|
| A | CH01–CH05 | Setup + early flirty care |
| B | CH06–CH10 | Heat rises |
| C | CH11–CH15 | Kiss / choice / ending |

After each batch: schema validate + spot-read 5 random hot lines.

### Phase 2 — Automated QA (required)

Script e.g. `tools/validate_rp_locale.py`:

- Parse `en.json` + target
- Assert equal: node ids set, each node’s `next`, choice count, each choice `next`, presence of `me`
- Assert no `vars` / `choices[].set` anywhere (stat flags are removed)
- Assert all `videoUrl`/`imageUrl` identical to EN
- Report: missing/extra nodes, empty strings, untranslated leftover English (heuristic: high ASCII ratio in `id`/`ru`/`hi` — careful with names/Mei)
- Optional: max line length for UI

Exit non-zero on structural mismatch.

### Phase 3 — Human tone pass (lightweight)

For each language, re-read only:

- Opening door scene (CH01)
- First real tension checkup
- Rain / kiss chapters
- Final “I love you” choice

Fix anything that sounds like machine translation or lost heat.

### Phase 4 — Catalog + app

1. Localized listing strings for Nurse Mei in store list UI (either multi-key in `rp_lists.json` or `rp_lists_{locale}.json` — prefer **one `rp_lists.json` with nested `i18n`** *or* keep EN list and localize only in-story if list UI is EN-only today)
2. Android: locale file picker + fallback
3. Smoke test on device: switch language, open CH01, hit a choice with `me`, confirm media still plays

### Phase 5 — Rollout order (matches your analytics)

1. **id** — Indonesia is #4 country, non-English-first  
2. **pt** — Brazil high engagement  
3. **ru** — Russia high engagement  
4. **hi** — India #1 volume (many still use EN; Hindi is expansion, not replacement of EN quality)

English file remains default for US / India users who prefer EN.

---

## Translation method recommendation

| Approach | Use? |
|----------|------|
| Raw Google/MT dump into JSON | **No** — kills flirty voice |
| AI draft **per chapter** with STYLE + GLOSSARY, then human edit | **Yes** — default for this repo |
| Full pro literary localization | Overkill for “simple daily” goal |

Prompt constraints to reuse every batch:

- Simple daily vocabulary  
- Keep sexy/teasing equal to English  
- Preserve JSON structure and ids  
- Output valid JSON fragment / full file only  
- Brazilian PT not European; Hinglish Roman script (not Devanagari); Indonesian informal natural  

---

## Out of scope (this plan)

- Translating other RPs (`yui`, `agent_sasha`, `captured_princess_elara`, …) — same pattern later  
- Re-encoding media  
- Changing branching / stats design  
- Full app rewrite (only locale resolution + path)

---

## Success criteria

- [ ] `rp/nurse_mei/en.json` exists; old top-level path handled  
- [ ] `id.json`, `pt.json`, `ru.json`, `hi.json` each pass structural validator vs `en.json`  
- [ ] Tone: simple + flirty on sampled chapters  
- [ ] Android can open story in all 5 languages with media OK  
- [ ] `rp_lists.json` points at new layout  

---

## Implementation todos (execution order)

1. **Restructure** — move EN JSON into `rp/nurse_mei/en.json`; update `rp_lists.json`; document path for Android  
2. **Style pack** — `STYLE.md` + `GLOSSARY.md` under `rp/nurse_mei/`  
3. **Validator** — structural parity script EN vs locale  
4. **Translate id** — batches A→B→C (CH01–15)  
5. **Translate pt** — same batches (pt-BR voice)  
6. **Translate ru** — same batches  
7. **Translate hi** — same batches (simple Hindi)  
8. **Catalog + app wiring** — list copy + locale fallback  
9. **Final QA** — validator all locales + heat spot-check  

---

## Risk notes

| Risk | Mitigation |
|------|------------|
| Broken old app path to `rp/nurse_mei.json` | Coordinate app release or keep stub copy |
| MT flattens heat | Chapter tone pass; glossary |
| Hindi formal / hard to read | Force conversational samples in STYLE.md |
| Huge file edit errors | Chapter batches + validator |
| `me` field forgotten | Validator requires `me` iff EN has `me` |
