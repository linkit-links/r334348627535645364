# Plan: Android app — multi-locale RP loading

## Goal

Ship an Android change so the app loads the **correct language story JSON** for localized RPs (Nurse Mei first, then the same pattern for other packs), with **safe fallback to English**, **shared media**, and **localized catalog copy** where available.

Content is already on GitHub Pages. This plan is **app-only** (resolve locale → URL, parse list metadata, smoke-test).

---

## Context (content already shipped)

Base content host (example):

```text
https://linkit-links.github.io/r334348627535645364/rp/
```

### Catalog: `rp/rp_lists.json`

Each story may now include:

| Field | Meaning |
|-------|---------|
| `folder` | Media folder name under `rp/` (covers, videos, images) |
| `file` | Default / English story path relative to `rp/` (varies by story — see below) |
| `locales` | Optional list of supported language codes, e.g. `["en","id","pt","ru","hi"]` |
| `i18n` | Optional map of locale → `{ title, subtitle, description, tags }` for the **store list UI** |
| `cover`, `bgVideoURL` | Unchanged; still media, not dialogue |

**`file` path shapes currently in catalog (normalize in app):**

| Story `id` | `file` value | Locale files live at |
|------------|--------------|----------------------|
| `nurse_mei` | `nurse_mei/en.json` | `rp/nurse_mei/{locale}.json` |
| `doctors_office` | `doctors_office/en.json` | `rp/doctors_office/{locale}.json` |
| `yui` | `en.json` (+ `folder`: `yui`) | `rp/yui/{locale}.json` |
| `captured_princess_elara` | `en.json` (+ `folder`: `…`) | `rp/captured_princess_elara/{locale}.json` |
| `agent_sasha` | `sasha_secret_agent/en.json` | `rp/sasha_secret_agent/{locale}.json` |

**Invariant for localized packs:** one full graph per language file; same node ids / choices / media URLs; only strings differ.

**Backward-compat stubs** still exist for some packs (`rp/nurse_mei.json`, `rp/yui.json`, …) equal to English. Old app builds that hardcode those URLs keep working but **always get EN**.

### Supported RP locales (when `locales` is present)

| Code | Language | Notes |
|------|----------|--------|
| `en` | English | Default / fallback |
| `id` | Indonesian | Device often reports `in` (legacy) or `id` |
| `pt` | Portuguese (Brazil) | Use for `pt` and `pt-BR` |
| `ru` | Russian | Cyrillic UI/fonts |
| `hi` | Hindi | Hinglish in **Roman script** (not Devanagari) |

---

## Non-goals

- Translating app chrome (menus, settings, paywall) beyond story content — optional later
- Changing branching, stats (`set`), or media encoding
- Per-language media folders
- Offline pack redesign (unless cache keys must include locale — see below)

---

## Design

### 1. Resolve “preferred story locale”

Single pure function used everywhere:

```text
fun resolveStoryLocale(
  deviceLocales: List<Locale>,   // Configuration.getLocales() order
  supported: List<String>?       // from story.locales; null/empty → ["en"] only
): String
```

**Rules (in order):**

1. If `supported` is null or empty → return `"en"` (legacy single-file stories).
2. Walk **device locale list** (user preference order):
   - Map language tag → story code:
     - `in` or `id` → `id`
     - `pt` (any region, including `pt-BR`, `pt-PT`) → `pt`  
       *(content is Brazilian voice; still better than EN for European PT users)*
     - `ru` → `ru`
     - `hi` → `hi`
     - `en` → `en`
     - other → skip
   - First mapped code that is in `supported` wins.
3. If none match → `"en"` if supported, else first entry of `supported`.

**Do not** use app UI language only if you already force EN UI; prefer **device / system locales** so Indonesia/Brazil/Russia/Hindi users get story language even if the shell is English.

**Optional later:** Settings toggle “Story language” override stored in DataStore; if set and in `supported`, wins over device.

### 2. Resolve story JSON URL

Content base (existing constant), e.g. `RP_BASE = …/rp/`.

```text
fun resolveStoryJsonUrl(story: RpListItem, locale: String): String
```

**Recommended algorithm (handles both `file` shapes):**

```text
supported = story.locales ?: emptyList()
hasLocales = supported.isNotEmpty()

if (!hasLocales) {
  // Legacy: single file as today
  return RP_BASE + story.file.trimStart('/')
}

// Localized pack: always {folder}/{locale}.json
folder = story.folder
  ?: parentDir(story.file)   // "nurse_mei/en.json" → "nurse_mei"
  ?: story.id

code = locale if locale in supported else "en"
return RP_BASE + folder + "/" + code + ".json"
```

**Do not** naively string-replace `en.json` inside `file` unless you also handle `file: "en.json"` + `folder` and `file: "nurse_mei.json"`.

**Fallback load chain (required):**

```text
url = resolveStoryJsonUrl(story, preferred)
try fetch + parse
on HTTP 404 / network failure after retry / JSON parse error / schema missing nodes:
  if preferred != "en":
    fetch resolveStoryJsonUrl(story, "en")
  else:
    show error UI
```

Log which URL/locale actually loaded (analytics + debug).

### 3. Catalog list UI (`i18n`)

When binding the RP list / detail card:

```text
locale = resolveStoryLocale(deviceLocales, story.locales)
copy = story.i18n?.get(locale)
title = copy?.title ?: story.title
subtitle = copy?.subtitle ?: story.subtitle
description = copy?.description ?: story.description
tags = copy?.tags ?: story.tags
```

If `i18n` missing for that locale (e.g. Elara has `locales` but may lack full `i18n`), keep English list strings; **in-story** text still comes from `{locale}.json`.

### 4. Models / parsing

Extend the `rp_lists` DTO:

```kotlin
data class RpStoryMeta(
  val id: String,
  val title: String,
  val emoji: String? = null,
  val subtitle: String? = null,
  val description: String? = null,
  val tags: List<String>? = null,
  val folder: String? = null,
  val cover: String? = null,
  val bgVideoURL: String? = null,
  val file: String,                    // default EN path or legacy path
  val locales: List<String>? = null, // null = not localized
  val i18n: Map<String, RpListI18n>? = null,
)

data class RpListI18n(
  val title: String? = null,
  val subtitle: String? = null,
  val description: String? = null,
  val tags: List<String>? = null,
)
```

Use defaults so **old catalog entries without `locales`/`i18n` keep working**.

Story graph model: **no schema change**. Localized files are the same shape as EN (`nodes`, `lines`, `choices`, `me`, media URLs).

### 5. Media paths

`videoUrl` / `imageUrl` inside story JSON stay **absolute** and **language-independent**.  
Cover / folder media still use `folder` + `cover` as today.

**No Android change required for media** beyond ensuring you do not rewrite URLs by locale.

### 6. Cache & offline

If story JSON is cached by URL or by `story.id` only:

| Bad | Good |
|-----|------|
| Cache key = `story.id` only → user switches language, still sees EN | Cache key = `story.id + ":" + locale` (or full URL) |
| Disk file `nurse_mei.json` | Disk file `nurse_mei_id.json` / URL hash |

On locale change (device language or future override): invalidate or bypass cache for that story and re-fetch.

Progress / saves (node id, stats) stay **locale-independent** (same graph ids). Do **not** key saves by language.

### 7. Fonts & text rendering

| Script | Risk |
|--------|------|
| Latin (en, id, pt) | Default Roboto OK |
| Cyrillic (ru) | Usually OK on modern Android |
| Hinglish (hi) | Roman script; default Latin fonts OK. Confirm emoji + long mixed lines don't clip |

Checklist:

- Dialogue `TextView` / Compose `Text`: no forced single-line ellipsis on long choice labels
- Choice buttons: multi-line enabled (PT/RU can be longer than EN)
- `me` narrator beats: same as other lines
- RTL: none of the five locales are RTL; no layout flip required for this feature

### 8. Where to plug in (typical app layers)

Exact class names vary; touch these concerns:

1. **Rp catalog repository** — parse new fields; expose `locales` / `i18n`
2. **Story loader / use case** — `resolveStoryLocale` + `resolveStoryJsonUrl` + EN fallback
3. **List / detail UI** — apply `i18n` strings
4. **HTTP / cache** — locale-aware keys
5. **Analytics** — `story_id`, `requested_locale`, `loaded_locale`, `fallback_used`

No change to choice/`set`/save game logic.

---

## Implementation steps

### Phase A — Core resolution (must ship)

1. Add `RpListI18n` + optional `locales` / `i18n` on list model (Gson/Moshi/kotlinx.serialization: ignore unknown is already fine).
2. Implement `resolveStoryLocale` unit tests (table-driven):

   | Device locales | supported | expected |
   |----------------|-----------|----------|
   | `en-US` | en,id,pt,ru,hi | en |
   | `id-ID` | en,id,… | id |
   | `in-ID` (legacy) | en,id,… | id |
   | `pt-BR` | en,id,pt,… | pt |
   | `pt-PT` | en,pt,… | pt |
   | `ru-RU` | en,ru,… | ru |
   | `hi-IN` | en,hi,… | hi |
   | `ja-JP` | en,id,… | en |
   | `id-ID,en` | en only | en |
   | `fr-FR` | null | en (legacy path) |

3. Implement `resolveStoryJsonUrl` unit tests for:

   - `file=nurse_mei/en.json`, folder=nurse_mei, locale=id → `…/rp/nurse_mei/id.json`
   - `file=en.json`, folder=yui, locale=ru → `…/rp/yui/ru.json`
   - no locales, file=agent_sasha.json → `…/rp/agent_sasha.json`

4. Wire story open path: preferred → fetch → on fail EN → error.
5. Wire cache keys to include locale.

### Phase B — Catalog copy

6. List adapter / Compose list: prefer `i18n[locale]` for title/subtitle/description/tags.
7. Detail/header screen same.
8. If `i18n` absent, show EN metadata (Elara-style until catalog filled).

### Phase C — Hardening

9. Analytics events for locale + fallback.
10. Optional: in-app “Story language” setting (default: System).
11. ProGuard: keep new DTO fields if reflection-based JSON.
12. Screenshot / font check on hi + ru devices or emulators.

### Phase D — QA matrix (device)

| # | Case | Pass criteria |
|---|------|----------------|
| 1 | Device language EN, open Nurse Mei | Loads `en.json`; EN list copy |
| 2 | Device language ID, open Nurse Mei | Loads `id.json`; ID list copy from `i18n` |
| 3 | Device language PT-BR | Loads `pt.json` |
| 4 | Device language RU | Loads `ru.json`; Cyrillic readable |
| 5 | Device language HI | Loads `hi.json`; Roman Hinglish readable |
| 6 | Device language JA | Falls back to `en.json` |
| 7 | Airplane mode after EN cache, switch device to ID | Re-fetch or correct cache miss → ID (or clear message) |
| 8 | Force 404 on `id.json` (debug) | Falls back to `en.json`, story playable |
| 9 | Choice with `me` field | Silent beat shows; graph continues |
| 10 | Play video node (e.g. arrival) | Media still plays (shared URL) |
| 11 | Save mid-story, rotate language, resume | Same node id; new language text for that node OK |
| 12 | Open Sasha (no locales) | Still loads single `agent_sasha.json` |
| 13 | Open Yui with locales | `folder`+`en.json` style resolves correctly |
| 14 | Cold start list | `rp_lists.json` parse; no crash if `i18n` null |

---

## Rollout

1. **App release** with Phase A+B before or with content already live (content is live-safe: stubs + `en.json`).
2. No content migration required on users’ devices; only re-fetch list + story JSON.
3. Old app versions: keep using stub/top-level or old `file` if still cached in an old `rp_lists` — acceptable EN-only until update.
4. Monitor crash/analytics: `fallback_used=true` rate; high rate may mean wrong URL join (`folder`/`file` bug).

### Suggested version flag

```text
// Optional remote config later
rp_locale_loading_enabled = true
```

If false, always load `story.file` as today (EN path). Useful for kill-switch first week.

---

## Pseudocode (reference)

```kotlin
fun mapDeviceToStoryCode(locale: Locale): String? {
  return when (locale.language.lowercase(Locale.ROOT)) {
    "id", "in" -> "id"
    "pt" -> "pt"
    "ru" -> "ru"
    "hi" -> "hi"
    "en" -> "en"
    else -> null
  }
}

fun resolveStoryLocale(device: LocaleListCompat, supported: List<String>?): String {
  val sup = supported?.map { it.lowercase() }?.ifEmpty { null }
  if (sup == null) return "en"
  for (i in 0 until device.size()) {
    val code = mapDeviceToStoryCode(device[i] ?: continue) ?: continue
    if (code in sup) return code
  }
  return if ("en" in sup) "en" else sup.first()
}

fun storyJsonUrl(base: String, story: RpStoryMeta, locale: String): String {
  val sup = story.locales.orEmpty()
  if (sup.isEmpty()) {
    return base.trimEnd('/') + "/" + story.file.trimStart('/')
  }
  val folder = story.folder
    ?: story.file.substringBeforeLast('/', missingDelimiterValue = "")
      .takeIf { it.isNotEmpty() }
    ?: story.id
  val code = locale.takeIf { it in sup } ?: "en"
  return base.trimEnd('/') + "/" + folder.trim('/') + "/" + code + ".json"
}
```

---

## Success criteria

- [ ] Device language ID/PT/RU/HI opens Nurse Mei dialogue in that language
- [ ] Unsupported device language gets EN story, no crash
- [ ] 404/parse fail on locale file falls back to EN
- [ ] Media nodes still play
- [ ] Choices + `me` + saves work across languages (same node ids)
- [ ] List card shows `i18n` when present
- [ ] Stories without `locales` unchanged (Sasha, any future single-file)
- [ ] Unit tests cover locale map + URL builder
- [ ] QA matrix rows 1–14 signed off on at least one real device + emulators for hi/ru

---

## Effort estimate (rough)

| Work | Size |
|------|------|
| DTO + resolvers + unit tests | 0.5–1 day |
| Loader + cache key + fallback | 0.5 day |
| List/detail i18n binding | 0.25 day |
| QA matrix + font pass | 0.5 day |
| **Total** | **~2 days** including QA |

---

## Related docs (this repo)

| Doc | Role |
|-----|------|
| `plan.md` | Original Nurse Mei localization plan (content) |
| `rp/nurse_mei/README.md` | Content load contract for Mei |
| `rp/nurse_mei/STYLE.md` / `GLOSSARY.md` | Translation voice (content authors) |
| `tools/validate_rp_locale.py` | Structural parity EN vs locale JSON |
| `rp/rp_lists.json` | Live catalog fields app must parse |

---

## Implementation todos (app repo)

1. **Models** — parse `locales` + `i18n`; keep backward compatible
2. **Locale resolver** — device list → `en|id|pt|ru|hi` with `in`→`id`
3. **URL resolver** — `{folder}/{locale}.json` when localized; else `file` as today
4. **Fetch + EN fallback** — 404/parse → `en.json`
5. **Cache keys** — include locale
6. **List UI** — apply `i18n` copy
7. **Unit tests** — tables above
8. **Device QA** — matrix; hi/ru fonts; media + `me` choice
9. **Ship** — optional remote kill-switch; watch fallback analytics
