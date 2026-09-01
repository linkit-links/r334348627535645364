# Media — One Room Weekend (Elena Rossi)

**Images only. No video in this story.** Every asset is a **`.webp`**, **9:16 vertical**. No `.mkv`,
no `.mp4`, no `bgVideoURL`.

One still per chapter. 16 chapters, 16 stills, plus the cover.

Inherits `rp/MEDIA_RULES.md` and `.kiro/steering/rp-visual-rules.md`. This file may only make those
rules **stronger**, never softer.

Full ready-to-paste prompts live in `IMAGE_PROMPTS.txt` in this folder, in order, one by one.

---

## Non-negotiable look rule

**Elena is sexy, revealing and bold in every single shot, in every chapter, no exceptions.** Lobby,
restaurant, balcony, fight, goodbye — she is dressed to be looked at. If a beat would realistically
put her in something modest, the answer is *no*: the neckline goes lower, the robe hangs open, the
slit goes higher, the sheet has already slipped.

Never a covered chest. Never a closed neckline. Never a shapeless silhouette. Never a shy pose.

**Paste this into every Elena prompt** (adapt the garment, keep every clause):

> plunging neckline, deep cleavage, bare shoulders and collarbones, cinched waist, thin clinging
> fabric, long bare legs, confident dominant posture, chin level, direct eye contact, glossy sleek
> dark hair, gold jewellery

Per-chapter minimum, even in the "covered" beats:

| Scene type | Minimum reveal |
|------------|----------------|
| Lobby / public / hotel corridor | Blazer worn open over a low silk camisole, no shirt under it, deep plunge, tight skirt slit high, sheer stockings, heels |
| Restaurant / evening / formal | Satin gown, halter plunge to the navel, open back to the waist, thigh-high slit, one bare leg out of the booth |
| Suite / night / bed | Black lace-trim silk slip off both shoulders, straps down, sheets low, bare legs and bare back |
| Bath / water / steam | Wet skin, wet clinging silk, hotel robe untied, bare shoulders and collarbones, steam |
| Soft / hurt / apology | Sheet held loosely and failing, or his open shirt over bare skin |
| Working / laptop / phone | Hotel robe open over the slip, belt loose, one bare leg folded up, reading glasses optional |
| Goodbye / departure | Back to the arrival look — blazer open, low camisole, tight skirt, bare leg, heels |

If a model refuses a prompt, soften the *wording* ("revealing silk slip, plunging neckline") — never
cover her up.

---

## Format

- **Everything 9:16 vertical `.webp`.** Put `9:16 vertical` in the prompt and `landscape
  orientation` in the negative.
- Modern luxury hotel. Warm practical light — lamps, city glow, bathroom mirror light, candles on
  restaurant tables. Single-source from one side, deep shadow on the other. Skin has shine. Never
  flat front lighting.
- **Male player character: face never visible.** Over the shoulder, back of the head, hands, or
  silhouette only.
- Feed `elena_ref.webp` as an image reference on every chapter still so her face never drifts.
- Bold and revealing but **clothed and non-explicit**. All characters are adults.

## Files this folder needs

| File | Purpose | Format |
|------|---------|--------|
| `rp_cover.webp` | Story card cover (`"cover": "rp_cover"`) | WebP, 9:16 |
| `elena_ref.webp` | Character reference — not shipped, keeps her face consistent | WebP, 9:16 |
| `elena_<slug>.webp` | Chapter still, one per chapter | WebP, 9:16 |

Attached in `en.json` on the chapter's strongest node:

```json
"imageUrl": "https://linkit-links.github.io/r334348627535645364/rp/same_bed_weekend/elena_onebed.webp"
```

---

## Character lock (paste into every prompt)

**Elena Rossi** — cute 21-year-old adult East Asian woman, Korean-Japanese features, youthful round
pretty face, tall, slim cinched waist, full figure, very upright confident posture. Long sleek glossy
black hair, centre part, worn loose over one shoulder or in a low twist. Big dark almond eyes,
luminous fair skin, soft brows, glossy pink-red lips, a sweet knowing half-smile. Small gold hoop
earrings, a thin gold chain at her throat, one gold ring, deep red nails. Cute and expensive — she
looks like she is used to being looked at and completely fine about it.

**Player character** — male, late twenties, lean, dark shirt with the sleeves pushed up. **Face never
visible** — over the shoulder, back of the head, hands only, or silhouette.

**World** — modern high-floor luxury hotel suite. Floor-to-ceiling windows, city skyline at night,
private balcony, velvet couch, one enormous bed, white-tiled bathroom with mirror lights, marble
lobby with white flowers.

**Style** — cinematic photography, shallow depth of field, single warm light source from one side,
deep shadow on the other, city bokeh through glass. Palette of warm gold, black, deep green, white
marble and skin tone. Sensual, glossy, high detail, editorial.

**Global negative prompt** — landscape orientation, flat front lighting, overexposed, visible male
face, nudity, text, watermark, logo, extra fingers, deformed hands, cartoon, anime, plastic skin,
crowd, children, covered chest, closed neckline, baggy clothing.

---

## Wardrobe / heat ladder

Same woman, same face, less fabric as the weekend escalates.

| Chapters | Wardrobe |
|----------|----------|
| CH01–02 | Fitted black blazer worn open over a low black silk camisole, deep plunge, tight skirt with a high slit, sheer stockings, stilettos. Cool and untouchable. |
| CH03–04 | Deep green satin gown — halter plunge to the navel, open back to the waist, thigh-high slit, bare leg. |
| CH05–07 | Undressed states — white hotel silk robe untied and hanging open, wet skin, black lace-trim slip, bare back. |
| CH08–13 | Boldest of the story. Black lace-trim silk slip off both shoulders, straps down, bare legs, sheets, city light on bare skin. |
| CH14–15 | Softer but still bare — sheet slipping, his open shirt over bare skin, hair down, no jewellery. |
| CH16 | Back to the arrival look, blazer open over the low camisole — bookend, sadder, just as bold. |

---

## Shot list

| CH | Node in `en.json` | Base name | Shot |
|----|-------------------|-----------|------|
| — | card cover | `rp_cover` | Suite window at night, slip off both shoulders, keycard in her fingers, city behind her |
| — | reference | `elena_ref` | Three-view character reference, not shipped |
| 01 | `CH01_N2` | `elena_frontdesk` | Marble front desk, blazer open over the low camisole, one hand on the counter, thunderstorm-calm |
| 02 | `CH02_N1` | `elena_onebed` | The one-bed reveal, arms crossed at the foot of the bed, slit skirt, skyline behind |
| 03 | `CH03_MERGE` | `elena_zipper` | Green gown open down her bare back, your hands at the zip, her eyes on you in the mirror |
| 04 | `CH04_MERGE` | `elena_dinner` | Dark restaurant booth, gown plunge to the navel, one bare leg out into the aisle |
| 05 | `CH05_MERGE` | `elena_bathdoor` | Bathroom door open a hand's width, wet bare arm and shoulder reaching out, steam |
| 06 | `CH06_MERGE` | `elena_hook` | Hotel robe hanging off both shoulders, bare back, your hands at the hook, her eyes in the mirror |
| 07 | `CH07_MERGE` | `elena_rules` | Lamplit bed, slip off both shoulders, one knee up, moving the pillow border herself |
| 08 | `CH08_MERGE` | `elena_balcony` | Balcony railing, twelve floors of city light, slip and bare legs, her hand in your shirt |
| 09 | `CH09_N2` | `elena_morning_text` | Gold morning light, sheets at her hips, phone face-down, slip straps down |
| 10 | `CH10_N1` | `elena_robe_laptop` | Cross-legged on the bed, robe open over the slip, laptop, coffee tray |
| 11 | `CH11_MERGE1` | `elena_cards` | Princess-carried, slip riding up, one arm around your neck, laughing |
| 12 | `CH12_MERGE2` | `elena_massage` | Leaning back against your chest, slip pushed off her shoulders, bare back, eyes half shut |
| 13 | `CH13_N2` | `elena_confession` | Low lamp, her hand on your jaw, slip barely on, no armour left |
| 14 | `CH14_N2` | `elena_argument` | Hard morning light, sheet pulled up like armour and slipping anyway, hurt and sharp |
| 15 | `CH15_MERGE` | `elena_onemore` | Late gold afternoon, his open shirt over bare skin, head on your shoulder |
| 16 | `CH16_MERGE` | `elena_goodbye` | Bags packed, blazer open over the camisole, her fingers laced through yours, window light |

## Generation notes

- Export **WebP only**, 9:16. Nothing in this folder is a video.
- If a model defaults to landscape, put `9:16 vertical` in the prompt **and** `landscape
  orientation` in the negative.
- Player's face out of frame in every shot.
- Warm light motivated from one side; never flat front lighting.
- Elena may smile with teeth in this story — she is warm, teasing and modern. That is the one place
  this folder differs from the period stories.
