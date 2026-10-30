# RP naming convention — the rules

Scope: `rp/**` in this repo, and the matching code in `DearDarling`
(`app/src/main/java/com/thebravecoders/deardarling/`) plus the `roleplays` table in
Supabase project `ptnyidnttrojrpsatjae`.

## 0. Migration status

Branch `rp-naming-migration`. Validate with `python3 rp/validate_rp.py`.

**Done in this repo**

- One story file per story: `rp/<id>/<id>.json`, all 10 folders
- 32 translation packs deleted (`hi/id/pt/ru.json`) — it was 32, not the 36 an earlier
  draft claimed; `lingerie_thief` and `the_neighbor` never had any
- `bg_cover_video.mkv` → `bg_cover.mkv` ×8
- `rp_cover_nurse.webp` / `rp_cover_yui.webp` → `rp_cover.webp`
- `trending_landscape_cover.{mkv,webp}` → `rp_trending.{mkv,webp}`
- `captured_princess_elara`: `sitting_in_cell_2.mkv` → `bg_cover.mkv` (renamed, not copied
  — no chapter referenced it)
- 8 `bg_cover.webp` posters extracted from frame 0, satisfying R6
- 4 duplicate background files deleted (`bg_cover_frame.jpg`, `bg_video.webp`,
  `bg_video.png`)
- 2 fake background videos deleted — `lingerie_thief` and `pay_with_body` shipped a 90 KB
  *static image encoded as a 6-second video*. Frame 0 vs frame 150 differs by PSNR 43 dB
  (≈1/255 per pixel) against 10 dB for a real loop like `gym_trainer`. The extracted
  `bg_cover.webp` is identical content, so the videos were pure ambiguity.
- `rp_lists.json` rewritten: 14,578 → 2,310 bytes, 9 stories, generated from disk
- `rp/validate_rp.py` added to enforce R1–R10

**Deliberately not done**

- `en.json` is **kept** alongside `<id>.json` as a compatibility copy. "English-only"
  settles deleting the *translations*; it does not prove nothing reads `<folder>/en.json`,
  and `roleplays.content_file` still literally holds that path. One `git rm` removes them
  once confirmed.
- R10 (relative URLs in story JSONs) deferred. 283 absolute URLs across 9 stories, and it
  needs a coupled change at 8 app use sites — better as its own reviewable commit.
- `the_neighbor` left untouched beyond adding `the_neighbor.json`. It is in no catalog
  (not in Supabase, not in the manifest) and its 53 PNGs were already uncommitted in your
  working tree, so committing or deleting them is your call, not mine.

**Bugs this surfaced**

- `lingerie_thief` references three chapter images that have never existed:
  `mistress_garage.webp`, `mistress_rules.webp`, `mistress_trunkride.webp`. Those chapters
  404 in production today. Needs art generated, or the references removed.
- `princess_servant` ships with zero chapter media — no `imageUrl` or `videoUrl` anywhere
  in its story file. Possibly intentional, worth a look.
- `lingerie_thief`'s Supabase row pointed `bg_image_url` at `bg_cover.webp`, which did not
  exist until this migration created it. Its background was silently falling back.

Media compression is **out of scope** — files keep their current codecs and sizes. The
measurements behind that decision are parked in the appendix. Because we are *not*
re-encoding, extensions stay mixed (`.mkv` and `.mp4`, `.webp` and `.png` and `.jpg`),
which makes rule **R8** below load-bearing rather than cosmetic.

> **Read §5 before executing anything.** Both the `roleplays` table and this repo are
> shared with the LoveStories app, and two of the changes below are destructive to it.

---

## 1. The rules

Normative. "MUST" means a CI check should fail if it is violated.

**R1 — One folder per story, named for the story id.**
`rp/<id>/`. `folder` MUST equal `id`. No exceptions, so `folder` stops being a separate
concept you can get wrong.

**R2 — One story file, named for the story.**
`rp/<id>/<id>.json` — e.g. `rp/nurse_mei/nurse_mei.json`. English only. No `en.json`, no
`hi.json`, `id.json`, `pt.json`, `ru.json`.

**R3 — List cover: `rp_cover.<ext>`.** Image or video. This is the card on the hub grid.

**R4 — Play background: `bg_cover.<ext>`.** Image or video. This is the first thing the
play screen shows and the sticky background behind the feed.

**R5 — Hub promo: `rp_trending.<ext>`.** Optional. Landscape.

**R6 — A video slot MUST also ship a still with the same base name.**
If `rp_cover.mp4` exists, `rp_cover.webp` MUST exist too. Same for `bg_cover` and
`rp_trending`. The still is the poster while the video decodes, and it is the slot's
content outright when there is no video. A grid cell has to paint on the first frame of a
scroll and a decoder cannot do that, so the still is not optional decoration.

**R7 — Chapter media keeps free-form names.** Referenced by the story JSON, so they
describe themselves. No convention needed, none imposed.

**R8 — The extension lives in the manifest, never in code.**
No Kotlin anywhere may append `.webp`, `.mp4` or `.mkv` to a name. This is what lets a
cover be `rp_cover.webp` in one story and `rp_cover.png` in another without a code change,
and it is why the mixed extensions we are keeping are harmless.

**R9 — Aspect: `rp_cover` and `bg_cover` are 9:16 portrait. `rp_trending` is 16:9.**

**R10 — No absolute URLs in content.** Story JSONs and the manifest carry paths relative to
the CDN root. The host lives in exactly one Kotlin constant.

---

## 2. What is broken today

### Every story spells the same two slots differently

| story | list cover | play background |
|---|---|---|
| `doctors_office` | `rp_cover.webp` | `bg_cover_video.mkv` |
| `gym_trainer` | `rp_cover.webp` | `bg_cover_video.mkv` |
| `princess_servant` | `rp_cover.webp` | `bg_cover_video.mkv` |
| `same_room_weekend` | `rp_cover.webp` | `bg_cover_video.mkv` |
| `nurse_mei` | `rp_cover_nurse.webp` | `bg_cover_video.mkv` |
| `yui` | `rp_cover_yui.webp` | `bg_cover_video.mkv` |
| `captured_princess_elara` | `rp_cover.webp` | `sitting_in_cell_2.mkv` — a chapter clip |
| `lingerie_thief` | `rp_cover.webp` | `bg_cover_video.mkv` + `bg_cover_frame.jpg` + `bg_video.webp` |
| `pay_with_body` | `rp_cover.webp` | `bg_cover_video.mkv` + `bg_cover_frame.jpg` + `bg_cover.webp` + `bg_video.png` |
| `the_neighbor` | `rp_cover.png` | none |

Five spellings of the cover, four of the background, and one story pointing its background
at a chapter clip.

### Three sources disagree about what exists

Queried live, not assumed:

| source | stories | notes |
|---|---|---|
| folders on disk | **10** | |
| Supabase `roleplays` | **9** | missing `the_neighbor` |
| `rp_lists.json` | **6** | only 5 real + `agent_sasha`, which exists nowhere |

So `the_neighbor` — 50 PNGs, 4 MP4s, 5 locale JSONs, ~55 MB — is in neither catalog. It has
never shipped. And `agent_sasha` is listed with a cover name but no folder and no row.

### The extension is hardcoded in Kotlin

`Roleplay.coverUrl` (`Roleplay.kt:36`) appends `.webp`. `trendingVideoUrl` and
`trendingThumbUrl` hardcode `trending_landscape_cover.mkv` / `.webp`. `SideloadManager`
has three more hardcoded builders (`coverUrl`, `listCoverUrl`, `sceneBgUrl` →
`bg_cover.webp`) that nothing calls.

Consequence: `the_neighbor/rp_cover.png` can never render. The app asks for
`rp_cover.webp`, which does not exist. That is rule R8 being violated, and it is a bug
today, not a hypothetical.

---

## 3. Story JSON: drop multi-language

### The app is already English-only

`RpLocale.storyJsonUrl` (`RpLocale.kt:21`) has a comment saying so outright, and always
resolves to `en.json` regardless of what `locales` says. So the non-English packs are dead
weight for DearDarling: **32 files that were never fetched.**

### What changes

- `rp/<id>/en.json` → `rp/<id>/<id>.json`
- delete `rp/<id>/{hi,id,pt,ru}.json`
- `rp_lists.json`: drop the `locales` and `file` fields
- `RpLocale.kt`: `storyJsonUrl` collapses to `"$BASE/$id/$id.json"`. The `locales`
  branching, the `folder` fallback chain and `RpListItem.locales` / `.file` all go.
- `Roleplay.kt`: `locales` and `listFile` fields go; `withOverlay` shrinks
- delete `app/src/test/.../RpLocaleTest.kt`

Note that `RpLocaleTest.kt` is already deleted in your working tree, along with
`LocaleHelper.kt`, `RpLanguagePickerDialog.kt`, `AppLanguageDialog.kt`, `locales_config.xml`
and all four `values-*/strings.xml`. You have a locale-removal refactor in flight already
— this finishes the CDN half of it. Worth landing them together.

### Why this is safe for the app but not obviously safe for the repo

See §5. DearDarling never reads the locale packs. Whether anything *else* does is the open
question.

---

## 4. Supabase

### Live state of `roleplays`, 9 rows

`content_file` is `<folder>/en.json` for every single row:

```
captured_princess_elara  folder=captured_princess_elara  cover=rp_cover        content_file=captured_princess_elara/en.json
doctors_office           folder=doctors_office           cover=rp_cover        content_file=doctors_office/en.json
gym_trainer              folder=gym_trainer              cover=rp_cover        content_file=gym_trainer/en.json
lingerie_thief           folder=lingerie_thief           cover=rp_cover        content_file=lingerie_thief/en.json
nurse_mei                folder=nurse_mei                cover=rp_cover_nurse  content_file=nurse_mei/en.json
pay_with_body            folder=pay_with_body            cover=rp_cover        content_file=pay_with_body/en.json
princess_servant         folder=princess_servant         cover=rp_cover        content_file=princess_servant/en.json
same_room_weekend        folder=same_room_weekend        cover=rp_cover        content_file=same_room_weekend/en.json
yui                      folder=yui                      cover=rp_cover_yui    content_file=yui/en.json
```

`folder` equals `id` on all 9 rows, which is what makes R1 and R2 safe to impose. Under
those rules the story path is always `<id>/<id>.json`, so **`content_file` carries no
information** — it is fully derivable. You were right that it should go.

`bg_video_url` and `bg_image_url` are absolute URLs with the CDN host baked in. Seven rows
point at a video, two (`lingerie_thief`, `pay_with_body`) at an image. That is exactly the
image-or-video distinction R4 describes, so the data already supports the rule — it just
encodes it as two nullable columns instead of one.

### What changes — and it turned out to be nothing schema-side

Because the manifest now carries every media filename (§6), the Supabase media columns
become redundant rather than needing replacement. **No `alter table` is required.** The app
simply stops selecting them:

| column | now | after |
|---|---|---|
| `content_file` | `nurse_mei/en.json` | **unused** — derivable as `<id>/<id>.json` |
| `folder` | `nurse_mei` | **unused** — R1 makes it equal `id` |
| `cover` | `rp_cover_nurse` | **unused** — manifest owns it, with the extension |
| `bg_video_url` | absolute URL | **unused** — manifest `bgVideo` |
| `bg_image_url` | absolute URL | **unused** — manifest `bg` |

`roleplays` keeps serving what it is actually good for: `id`, `title`, `emoji`, `subtitle`,
`description`, `tags`, `badge`, `is_hidden`, `play_count`. Metadata in the database, file
names in the repo next to the files, each checkable on its own.

Dropping the five columns outright is optional tidiness and still gated on §5 — grep
LoveStories first. Not dropping them costs nothing now that nothing reads them.

---

## 5. Shared-infrastructure warnings

Two of the changes above are destructive to something I cannot see from here, so they need
your confirmation before anyone runs them.

### The `roleplays` table is shared with LoveStories

`supabase/deardarling_schema.sql:5-8` says it plainly: the DearDarling tables were kept
separate *because* `roleplays` is "the shared `roleplays` catalog table … reused as-is
(read-only from the app)". `StoryContent.kt:13` likewise notes the story schema is "the
same schema the LoveStories app plays."

So **dropping `content_file`, `bg_video_url` or `bg_image_url` is not DearDarling's call to
make.** If LoveStories selects any of them, the drop breaks it in production, and
LoveStories is not on this volume so I could not check.

Safe sequencing:

1. **Now:** remove the columns from DearDarling's `ROLEPLAY_COLUMNS` and from the
   `Roleplay` data class. DearDarling stops depending on them. Zero risk.
2. **Then:** grep LoveStories for `content_file`, `bg_video_url`, `bg_image_url`.
3. **Only if clean:** `alter table roleplays drop column …`.
4. **Add** the new `bg` / `bg_video` columns as nullable, so LoveStories ignores them.

Step 1 gets you the whole simplification benefit. Step 3 is tidiness and can wait.

### This repo may serve LoveStories too

The locale packs are the risk. DearDarling is English-only and never reads them, but the
`locales` field exists in `rp_lists.json` for a reason, and a multi-language LoveStories
reading `rp/<id>/hi.json` from this same CDN would break the moment we delete those 36
files.

Before `git rm` on any locale JSON, confirm one of:

- LoveStories is also English-only, or
- LoveStories does not read from `linkit-links.github.io/r334348627535645364`, or
- LoveStories ships its own copies.

If none holds, the safe version is: add `<id>.json`, leave the locale packs in place,
delete them a release later once logs confirm nothing fetches them. Renaming is reversible;
deleting 36 files another app depends on is a production outage.

---

## 6. The manifest

`rp_lists.json` is the single authority for filenames. Actual shape as generated:

```json
{
  "version": 2,
  "stories": [
    {
      "id": "nurse_mei",
      "story": "nurse_mei.json",
      "cover": "rp_cover.webp",
      "coverVideo": null,
      "bg": "bg_cover.webp",
      "bgVideo": "bg_cover.mkv",
      "trending": "rp_trending.webp",
      "trendingVideo": "rp_trending.mkv"
    }
  ]
}
```

No `folder` (R1: it equals `id`). No `locales` (§3). No `title`/`subtitle`/`description`/
`i18n` — Supabase owns metadata, and that duplication was most of the old 14.5 KB. Still
fields are never null; video fields are null when absent, and that null is what the app
branches on instead of probing for a 404.

URL construction becomes `"$BASE/$id/$name"` everywhere, and nothing else.

Note the `.mkv` in that example sitting next to `.webp`. Since we are not re-encoding, the
manifest is what makes mixed extensions a non-issue — which is the whole point of R8.

The file is **generated from disk**, not hand-edited. Regenerate rather than patch it, and
let `validate_rp.py` confirm the result.

---

## 7. Every change, both repos

### Repo A — `r334348627535645364` (resources) — DONE, see §0

A1–A11 and A13 are applied on branch `rp-naming-migration`. A2 is partial (translations
gone, `en.json` retained as a shim). A10 (`the_neighbor`) and A12 (R10 relative URLs) are
open — see §0 "Deliberately not done".

### Repo B — `DearDarling` (app)

**B1.** `data/rp/Roleplay.kt` — delete the `.webp` append in `coverUrl` and the hardcoded
`trending_landscape_cover.*` paths. Add `cover`, `coverVideo`, `bg`, `bgVideo`, `trending`,
`trendingVideo` from the manifest. Remove `folder`, `contentFile`, `locales`, `listFile`,
`bgVideoUrl`, `bgImageUrl`, and shrink `withOverlay`.
**B2.** `data/rp/RpLocale.kt` — `storyJsonUrl` collapses to `"$BASE/$id/$id.json"`. Remove
the `locales` branch and the `folder` fallback chain. `RpListItem` becomes the §6 shape.
**B3.** `data/rp/RpRepository.kt:234` — `ROLEPLAY_COLUMNS` drops `folder`, `cover`,
`content_file`, `bg_video_url`, `bg_image_url`. Nothing is added; the manifest covers it.
**B4.** `ui/roleplay/RoleplayPlayViewModel.kt:145` — the
`bgVideoUrl ?: bgImageUrl ?: coverUrl` chain becomes `bgVideo` with `bg` as its poster, or
`bg` alone.
**B5.** `ui/roleplay/RoleplayHubScreen.kt:447` — delete the trending banner's
probe-and-fall-back-on-404; `trendingVideo == null` is now known from the manifest.
**B6.** `services/SideloadManager.kt:80-84` — delete `coverUrl`, `listCoverUrl`,
`sceneBgUrl`. All three are uncalled and all three hardcode extensions.
**B7.** Delete `app/src/test/.../RpLocaleTest.kt` (already gone in your working tree).

### Repo C — Supabase `ptnyidnttrojrpsatjae`

**No schema change needed** (§4). Dropping the five now-unread columns is optional
tidiness, still gated on §5.

### Order

1. B1–B7. The manifest and files are already in the new shape, so the app is the only
   thing left before this is live.
2. Deploy both together — the renames break the current app, and the new app expects the
   new names.
3. Then, at leisure: `git rm` the 10 `en.json` shims once LoveStories is confirmed; A12
   (R10); A10 (`the_neighbor`); C3 (drop the dead columns).
4. Wire `validate_rp.py` into CI so this cannot drift again.

---

## Appendix — compression, deferred

Measured but not proceeding; media stays as-is. Kept so the work isn't repeated.

VMAF-matched, `gym_trainer/lexi_tour` (720×1280, 2.51 MB): x265 crf 24 → 956 KB @ 98.4;
SVT-AV1 crf 28 → 905 KB @ 98.3. AV1's edge at near-transparent quality is ~5%, rising to
~22% only at VMAF ~96. On grainy content (`captured_princess_elara`) AV1 is level with or
behind HEVC, and x265 crf 20 produces files *larger* than the source — that folder is
already near its compression limit.

If this is ever revisited: HEVC in MP4, no bundled decoder. AV1 decode is only guaranteed
from API 34 ([Android supported media formats](https://developer.android.com/media/platform/supported-formats)),
and a bundled software decoder costs CPU per frame for a 5% size gain. Stills to WebP q92
would take 96 MB → ~13 MB at PSNR ~44, which is the one piece that is nearly free if you
change your mind.
