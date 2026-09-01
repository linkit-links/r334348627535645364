# Media — Princess Servant (Cassandra)

**Everything is 9:16 portrait.** Cover, background loop, reference sheets, chapter stills, chapter
videos — all vertical, no exceptions.

One still image per chapter → one `.mkv` video generated **from that image**. Same base name for
both, so `cassandra_stair.jpg` produces `cassandra_stair.mkv`.

Look: bold, sexy, revealing. Royal but hot. Expensive fabric that clings, bare skin where a princess
shouldn't show it, candlelight doing half the work. Suggestive and confident — keep it clothed and
non-explicit so the assets stay usable on the store listing, but do **not** make it shy.

## Non-negotiable look rule

Inherits `rp/MEDIA_RULES.md`, which applies to every story in this repo. This file may only make it
stronger, never softer.

**Cassandra is revealing and sexy in every single shot, in every chapter, no exceptions.** Whatever
the scene is about — court, carriage, cane, ledger, blood, grief — she is dressed to be looked at.
If a beat would realistically put her in something modest, the answer is *no*: the gown is cut lower,
the robe is open further, the slit is higher, the sheet has slipped. Never a covered chest, never a
closed neckline, never a hem below mid-thigh unless it's a gown with a slit.

**Paste this into every Cassandra prompt** (adapt the garment, keep every clause):

> plunging neckline, deep cleavage, tight corseted waist, bare shoulders and collarbones, long
> thigh-high slit with one bare leg exposed, silk thin enough to cling to every curve, silver rings,
> long dark chestnut hair loose, thin silver circlet

Per-chapter minimum, even in the "covered" chapters:

| Scene type | Minimum reveal |
|------------|----------------|
| Court / public / formal | Backless gown or open-laced back, deep plunge to the waist, bare shoulders, slit to the hip |
| Outdoor / carriage / riding | Riding coat worn open over a low silk shift, bare legs on the seat, boots and thigh |
| Night / bed | Thin-strap silk slip falling off both shoulders, sheets low, bare legs and back |
| Grief / soft / wounded | His shirt worn open over bare skin, or a robe held closed by one hand and failing |
| Punishment / discipline | Corset and stockings, sleeves pushed up, silk disordered from the effort |

If a model refuses a prompt, soften the *wording* (say "revealing silk gown, plunging neckline")
rather than covering her up.


## Files this folder needs

| File | Purpose | Format |
|------|---------|--------|
| `rp_cover.webp` | Story card in `rp_lists.json` (`"cover": "rp_cover"`) | WebP, **9:16** |
| `bg_cover_video.mkv` | Card background loop (`bgVideoURL`) | MKV, **9:16**, 5s loop |
| `cassandra_ref.jpg` | Character reference — not shipped, keeps her face consistent | JPG, **9:16** |
| `beatrix_ref.jpg` | Character reference for the head maid | JPG, **9:16** |
| `cassandra_<slug>.jpg` | Chapter still, one per chapter | JPG, **9:16** |
| `cassandra_<slug>.mkv` | Chapter video, generated from that still | MKV, **9:16**, 3–5s |

Attach in the story JSON on the chapter's strongest node:

```json
"videoUrl": "https://linkit-links.github.io/r334348627535645364/rp/princess_servant/cassandra_stair.mkv"
```

---

## Character locks (paste into every prompt)

**Cassandra** — stunning young adult woman, mid-twenties appearance, tall, slim waist, full figure,
very upright posture. Long dark chestnut hair, half-pinned with a thin silver circlet, the rest
falling loose down her bare back. Grey-green eyes, pale flawless skin, dark straight brows, cool
unimpressed expression, lips slightly parted. Deep emerald-green silk gown: plunging neckline, tight
corseted bodice, off-shoulder sleeves, long thigh-high slit, silver embroidery. Silk thin enough to
catch every curve. Several silver rings on her right hand, a fine silver chain at her throat. Never
smiling with teeth.

**Beatrix** — striking woman in her late twenties, head maid. Severe black dress, high collar, but
cinched hard at the waist and tighter than it should be; white apron; sheer black stockings; dark
hair pinned up tight. Sharp cheekbones, dark eyes, one eyebrow permanently slightly raised. Brass
chatelaine of keys at her hip. Buttoned-up and obviously dangerous with it.

**Player character** — male servant, late twenties, lean, worn boots, black wool livery with silver
buttons (before hiring: patched linen shirt, open collar). **Face always out of frame** — over the
shoulder, back of head, or hands only.

**World** — late-medieval European palace, candle and firelight only, no electric light. Cold stone,
beeswax candles, dark oak, heavy tapestries, furs, tall narrow windows.

**Style** — cinematic, shallow depth of field, single-source warm candlelight from one side, deep
shadow on the other, rich oil-painting palette of emerald green, gold, black and skin tone. Sensual,
glossy, high detail.

**Global negative prompt** — modern clothing, modern objects, electric lighting, plastic, text,
watermark, logo, extra fingers, deformed hands, cartoon, anime, plastic skin, flat front lighting,
overexposed, teeth showing, crowd, children, landscape orientation.

---

## Wardrobe / heat ladder

Escalate what she's wearing as the arc escalates. Same woman, same face, less fabric.

| Chapters | Wardrobe |
|----------|----------|
| CH01–05 | Full emerald gown. Plunging neckline, corseted waist, thigh slit, bare shoulders. Cold and untouchable. |
| CH06–09 | Undressed states — loose robe half-open, unlaced bodice, bare back, sheer shift, wet skin from the bath chamber. |
| CH10–14 | Boldest of the story. Black silk slip, corset and stockings, sheets, bare legs, her rings and the token and nothing much else. |
| CH15–17 | Softer but still bare — his shirt, loose hair, firelight, blanket, no jewellery. |
| CH18–20 | Back into full royal armour for the court chapters, then the ending in the slip again, hair down, crown set aside. |

---

## Cover art — `rp_cover.webp` (9:16)

**Image prompt**

> Vertical cinematic portrait of a stunning young royal woman lounging sideways across a tall carved
> oak throne in a candlelit stone chamber. Deep emerald-green silk gown with a plunging neckline and a
> long thigh-high slit — one bare leg extended, the other bent, silk pooling off the edge of the seat.
> Tight corseted bodice, off-shoulder sleeves, bare shoulders and collarbones. Long dark chestnut hair
> half-pinned with a thin silver circlet, loose over one shoulder. Silver rings on the hand draped
> over the armrest. Grey-green eyes locked on the viewer, chin lowered, lips slightly parted — cool,
> bored, deciding what to do with you. In the blurred dark foreground, the back of a kneeling male
> servant in black livery. Warm candlelight from the left, deep shadow right, shallow depth of field,
> emerald and gold and black oil-painting palette. Sensual, glossy, high detail. 9:16 vertical.
>
> Negative: landscape orientation, flat lighting, modern clothing, text, watermark, extra fingers,
> teeth showing.

**`bg_cover_video.mkv` — video prompt (from the cover image)**

> Very slow push-in toward her. Candle flames flicker and gutter. The silk on her raised knee shifts
> as she breathes. Rings glint as her fingers tap the armrest twice, unhurried. Her eyes never leave
> camera. Nothing else moves. Loopable, 5 seconds, 9:16 vertical, no camera shake.

---

## Reference sheets (not shipped)

**`cassandra_ref.jpg`**

> Vertical character reference, three views (front, three-quarter, back) of the same stunning young
> royal woman. Emerald-green silk gown, plunging neckline, corseted waist, thigh-high slit, bare
> shoulders, thin silver circlet, long dark chestnut hair. Back view shows the open-backed gown and
> bare spine. Neutral dark grey background, soft even light, full body, identical face in all three
> views. 9:16 vertical. No text labels.

**`beatrix_ref.jpg`**

> Vertical character reference, three views (front, three-quarter, profile) of the same late-twenties
> head maid. Black high-collared dress cinched tight at the waist, white apron, sheer black stockings,
> dark hair pinned up, brass keys at her hip, one eyebrow slightly raised. Neutral dark grey
> background, soft even light, full body, identical face in all three views. 9:16 vertical. No text
> labels.

---

## CH01 — The Banner

Shot: the stair at the end of the chapter. **Her face must not be visible** — the reveal is CH02.
Everything else about her, however, is very much on display.

Base name: `cassandra_stair`

**Image prompt**

> Vertical low-angle shot from the bottom of a narrow stone servants' staircase in a candlelit palace,
> looking steeply up. On the landing above stands a young royal woman in a deep emerald-green silk
> gown, half-turned away — the turn of the stairwell hides her face and shoulders completely. Visible:
> the sweep of the skirt fallen open at the thigh-high slit, a long bare leg and hip exposed, the silk
> clinging to every curve of her waist and thigh, and one pale hand with several silver rings resting
> on the dark oak bannister. The silk catches the candlelight and shows everything it touches. Warm light from a sconce on the landing spills down worn stone steps; deep
> shadow in the foreground. Cold grey stone, dark oak, dust drifting in the light. Cinematic, shallow
> depth of field, emerald and gold and black palette, sensual and high detail. 9:16 vertical.
>
> Negative: visible face, landscape orientation, modern clothing, electric light, text, watermark,
> extra fingers, deformed hands.

**Video prompt (image-to-video, from `cassandra_stair.jpg`)**

> Static camera at the foot of the stair, or the faintest slow drift upward. Her fingers on the
> bannister tighten and then tap once, rings catching the candlelight. The silk over her bare leg
> settles as if she has just stopped walking, then shifts again as her weight moves to the other foot.
> Candle flame flickers, shadow crawls up the stone. She does not turn around and her face never
> enters frame. Dust motes drift. 4 seconds, 9:16, no zoom past the bannister, no camera shake, no
> other people in frame.

**Alternate CH01 shot** if you'd rather the chapter image show a face — base name
`beatrix_interview`:

> Vertical shot of a candlelit low-ceilinged servants' office, warm and cramped. A striking
> late-twenties head maid in a tight high-collared black dress and white apron leans forward over a
> writing table with an open leather ledger, quill in hand — the lean deliberate, the look up at
> camera appraising and faintly amused, one eyebrow raised. Brass keys at her hip. Beeswax candles,
> stacked linens behind her, one small barred window. The viewer's own hands rest on the table edge in
> the blurred foreground. Cinematic, shallow depth of field, warm amber light, dark palette. 9:16
> vertical.
>
> Video: she dips the quill, writes one slow line without looking down, then lifts her eyes back to
> camera and holds it. Candle flicker. 4 seconds, static camera, 9:16.

---

## CH02 — The Table

Her reveal chapter, and the story's thesis shot: she eats breakfast off his back. Her face **is**
visible here — that's the point. He is furniture and she is completely at ease about it.

Base name: `cassandra_table`

**Image prompt**

> Vertical cinematic shot inside a warm candlelit royal bedchamber, fur rugs on a stone floor, fire
> banked high, tall narrow window with morning light. A stunning young royal woman sits on the edge of
> a low emerald couch, leaning back, utterly relaxed and bored. She wears an emerald-green silk robe
> arranged rather than worn — falling off both shoulders, plunging open to the waist with deep
> cleavage, tight sash at the waist, split open past the hip, one long bare leg extended and the other
> bent, silk thin and clinging. Long dark chestnut hair loose over bare shoulders, thin silver circlet
> crooked in it.
> Grey-green eyes looking down and slightly toward camera with cool ownership, chin lifted, faint
> superior half-smile, no teeth.
>
> In front of her, a man in black servant's livery kneels on all fours, back flat and level, head down
> and turned away so his face is not visible. Her bare leg rests across his back, calf on his spine,
> ankle hooked, as a footrest. Laid out along his flat back on a folded white linen napkin: a porcelain
> plate with cut fruit, a small dish of honey, two crossed silver spoons, and a fine porcelain cup of
> steaming hot chocolate balanced high on his shoulder blade. Sweat shining on the back of his neck.
>
> Warm candle and firelight from the left, deep shadow right, shallow depth of field, emerald and gold
> and black oil-painting palette. Sensual, glossy, high detail, dominant mood. 9:16 vertical.
>
> Negative: his face visible, landscape orientation, flat lighting, modern clothing, electric light,
> text, watermark, extra fingers, deformed hands, teeth showing, spilled food.

**Video prompt (image-to-video, from `cassandra_table.jpg`)**

> Static camera, no push. She lifts a slice of fruit to her mouth slowly and eats without looking down
> at him. Her ankle shifts once on his back, deliberate and idle. Steam curls off the cup and the
> surface of the chocolate trembles very slightly with his breathing. His back tenses; sweat runs down
> the back of his neck. Candle flames flicker, firelight moves on the silk. Her eyes come up to camera
> at the end and hold. Nothing falls. 5 seconds, 9:16, no camera shake, no other people in frame.

**Alternate CH02 shot** — the loading, with Beatrix in frame. Base name `cassandra_table_loading`:

> Vertical shot, same chamber. A severe head maid in a tight high-collared black dress and white apron
> bends over the kneeling servant, both hands placing a porcelain cup of hot chocolate on his flat
> back, expression flat and professional. Behind her the royal woman lounges on the couch in the
> emerald silk robe, one bare leg out, watching with a faint bored smile, a folded page of paper in her
> ringed hand. Servant's face turned away, not visible. Candlelight, furs, fire, deep shadow. 9:16
> vertical.
>
> Video: the maid sets the cup down, adjusts it a half-inch, straightens up and steps back out of
> frame; the Princess's eyes never leave the servant. Steam rises. 4 seconds, static camera.

---

## CH03 — Learn the Bell

The 3am ring. She's in bed, he's on the cold floor in position, and she pulled the cord for no reason
at all. Her face visible — awake, bored, pleased with herself.

Base name: `cassandra_bell`

**Image prompt**

> Vertical cinematic night shot inside a warm royal bedchamber, one candle burned down to a stub, fire
> low and red, cold blue moonlight through a tall narrow window. A stunning young royal woman sits up
> in a great dark bed of furs and rumpled emerald-green silk — thin-strap silk slip falling off both
> shoulders, plunging neckline and deep cleavage, silk clinging, sheets pushed low, both bare legs out
> from under the furs, long dark chestnut hair loose and wild over bare shoulders, thin silver circlet
> abandoned on the bedside table. In her raised hand she holds a slender bell-pull cord, fingers curled
> around it, silver rings catching the candlelight. Expression: wide awake, faintly amused, bored
> superiority, looking down and toward camera, no teeth.
>
> Low in the foreground on cold floorboards, a man in a half-laced white servant's shirt kneels in
> perfect position — knees together, back straight, palms flat on his thighs, head lowered, face turned
> away and not visible. Bare feet, breath faintly visible in the cold air.
>
> Warm candlelight from her side, cold blue window light falling on him, heavy shadow between them.
> Shallow depth of field, emerald and gold and black palette, sensual and dominant mood, high detail.
> 9:16 vertical.
>
> Negative: his face visible, landscape orientation, flat lighting, modern clothing, electric light,
> text, watermark, extra fingers, deformed hands, teeth showing.

**Video prompt (image-to-video, from `cassandra_bell.jpg`)**

> Static camera. She pulls the cord once, unhurried — a small deliberate tug — and his shoulders flinch
> hard, then settle back into position without his head lifting. Her silk strap slides another
> half-inch off her shoulder as her arm comes down. Candle flame guts and recovers, firelight moves
> across the furs. Her eyes stay on him, then rise to camera and hold. 5 seconds, 9:16, no camera
> shake, no other people in frame.

**Alternate CH03 shot** — the drill in the corridor. Base name `cassandra_bell_run`:

> Vertical shot down a long cold stone servants' corridor at night, lit by one guttering wall sconce.
> In sharp focus in the foreground, a small brass bell on an iron bracket, still swinging, its wire
> running up into the ceiling. Behind it, blurred with motion, a man in a half-laced shirt runs toward
> camera with his boots in one hand, head down, face not visible. Cold blue light, damp stone, deep
> shadow, cinematic, shallow depth of field. 9:16 vertical.
>
> Video: the brass bell swings and rings twice in sharp focus while the running figure blurs past
> behind it and out of frame. Sconce flame shudders in the draught. 4 seconds, static camera, 9:16.

---

## CH04 — Wake Her Wrong

Six in the morning. Curtains thrown wide, cold light on the bed, and a princess who was already awake
and intends to be foul about it anyway. Her face visible — glaring straight down the lens.

Base name: `cassandra_morning`

**Image prompt**

> Vertical cinematic shot inside a dark royal bedchamber at dawn. Heavy curtains have just been thrown
> wide on a tall narrow window and hard cold blue morning light floods across a great disordered bed;
> the fire behind is down to red embers. A stunning young royal woman is caught half sitting up in the
> light, furs fallen to the floor, white sheet pushed low at her hips, long bare legs out and crossed
> at the ankle. She wears a thin emerald-green silk slip with both straps fallen off her shoulders,
> plunging neckline, deep cleavage, silk clinging to her waist and hip. Long dark chestnut hair wild
> from sleep, no circlet, silver rings on the hand pushing the hair back off her face. Expression:
> wide awake, murderous, entirely unbothered about what has slipped — chin lifted, glaring directly
> at camera, no teeth.
>
> At the edge of the frame in silhouette, a man in black servant's livery stands with one hand still
> on the curtain, head turned away, face not visible.
>
> Cold blue window light on her, warm red firelight behind, deep shadow between. Shallow depth of
> field, emerald and gold and black palette, sensual and dominant mood, high detail. 9:16 vertical.
>
> Negative: his face visible, landscape orientation, flat lighting, modern clothing, electric light,
> text, watermark, extra fingers, deformed hands, teeth showing, covered chest, closed neckline.

**Video prompt (image-to-video, from `cassandra_morning.jpg`)**

> Static camera. She lowers the hand from her hair, very slowly, and the glare lands and holds. One
> silk strap slides further down her arm; the sheet slips an inch at her hip. Her chest rises once with
> a long irritated breath. Dust drifts in the hard window light, embers pulse behind her. The servant's
> silhouette does not move at all. 5 seconds, 9:16, no camera shake, no other people in frame.

**Alternate CH04 shot** — after the chocolate, feet in his lap. Base name `cassandra_hearth`:

> Vertical shot, same chamber, warmer. The royal woman sits on the edge of the bed by a built-up fire
> in the thin emerald silk slip, both straps off her shoulders, sheet trailing, hair loose, holding a
> porcelain cup in both hands with her eyes half shut in pleasure. Both bare feet rest in the lap of a
> man kneeling on the floor at the hearth in black livery, back straight, head lowered, face not
> visible. Firelight from below and one narrow curtain-slice of cold light. Furs on the floor. 9:16
> vertical.
>
> Video: she drinks, tips her head back, and her toes flex once in his lap; firelight moves over the
> silk. He does not move. 4 seconds, static camera, 9:16.

---


## CH05 — A Hundred Strokes

Two shots this chapter: the mirror (hair, with Beatrix supervising off-frame) and the laces (Beatrix
gone). Use `cassandra_mirror` as the chapter video, `cassandra_laces` as the second still.

Base name: `cassandra_mirror`

**Image prompt**

> Vertical cinematic shot in a small warm candlelit dressing room, two candles either side of a large
> carved mirror. A stunning young royal woman sits on a low stool facing the glass, seen from behind and
> slightly to the side so both she and her reflection are in frame. She wears a thin emerald-green silk
> slip with both straps fallen off her shoulders — plunging neckline and deep cleavage in the reflection,
> silk clinging, her entire bare back and shoulders visible from behind, long dark chestnut hair lifted
> off her neck. Silver rings on her hands. In the mirror her grey-green eyes look past her own reflection
> straight up at the man behind her — amused, superior, openly enjoying herself, chin lifted, no teeth.
>
> Behind her stands a man in black servant's livery holding a silver-backed hairbrush, one hand lifting
> the weight of her hair, head lowered, face turned away and not visible — and only a blurred silhouette
> of him in the mirror.
>
> Warm candlelight from both sides of the glass, deep shadow behind, shallow depth of field, emerald and
> gold and black palette, sensual and dominant mood, high detail. 9:16 vertical.
>
> Negative: his face visible or in focus in the mirror, landscape orientation, flat lighting, modern
> clothing, electric light, text, watermark, extra fingers, deformed hands, teeth showing, covered chest,
> closed neckline.

**Video prompt (image-to-video, from `cassandra_mirror.jpg`)**

> Static camera. He draws the brush slowly down through her hair, once, all the way through. Her
> shoulders drop and her eyes half close in pleasure — then snap open in the mirror and fix on him. One
> silk strap slides further down her arm. Candle flames flicker either side of the glass. Nothing else
> moves. 5 seconds, 9:16, no camera shake.

**Second still — `cassandra_laces`**

> Vertical close cinematic shot from behind. A stunning young royal woman stands facing a candlelit
> mirror in an emerald-green silk gown pulled on but wide open at the back — her entire bare back, spine
> and shoulders exposed from nape to waist, two loose edges of silk hanging either side, thirty silver
> eyelets in two rows, waist cinched hard by a silver lace. She holds the front of the bodice against her
> chest with one forearm. Hair pinned up off her neck with loose strands down. In the mirror her face is
> visible over her shoulder — eyes up on the man behind her, lips just parted, superior and amused.
>
> Behind her, a man's hands in black livery cuffs pull the silver cord tight, knuckles against her bare
> skin, his face not visible. Warm candlelight raking across her back, deep shadow. Shallow depth of
> field, emerald and gold and black palette, sensual, high detail. 9:16 vertical.
>
> Video: his fists pull the cord tight in one motion — her back straightens, her shoulders lift, her
> chest rises with a short shallow breath, and her eyes come up in the mirror and hold. Candle flicker.
> 4 seconds, static camera, 9:16.

---

## Planned chapter shots (full prompts written as each chapter is written)

| CH | Base name | Shot concept |
|----|-----------|--------------|
| 01 | `cassandra_stair` | ✅ Hand and rings on bannister, bare leg through the slit, face hidden |
| 02 | `cassandra_table` | ✅ Breakfast served on the kneeling servant's back, her leg across him as a footrest, her face revealed |
| 03 | `cassandra_bell` | ✅ 3am — she sits up in bed pulling the bell cord, he kneels on the cold floor in position |
| 04 | `cassandra_morning` | ✅ Six a.m., curtains thrown wide, silk slip off both shoulders, sheet at her hips, glaring at camera |
| 05 | `cassandra_mirror` | ✅ At the glass, slip off both shoulders, bare back, your hands in her hair, her eyes on you in the reflection |
| 05b | `cassandra_laces` | ✅ Second shot for CH05 — bare back, bodice held to her chest by one forearm, your fists pulling the cord tight |
| 06 | `cassandra_bath` | Wet skin, steam, silk screen silhouette, water running over bare shoulders and collarbones |
| 07 | `cassandra_cane` | Corset and stockings, sleeves pushed up, cane in her ringed hand, candlelight along bare arms and thigh |
| 08 | `cassandra_ledger` | Robe open, her little book resting on a bare thigh, quill, your name written in it |
| 09 | `cassandra_court` | Backless gown plunging to the waist, bare shoulders and nape from behind her chair, nobles blurred |
| 10 | `cassandra_duke` | Courtyard, riding coat open over a low silk shift, her hand taken by another man, her eyes on yours |
| 11 | `cassandra_wine` | Midnight, wine glass, robe off both shoulders and barely closed, bare legs folded under her |
| 12 | `cassandra_token` | Her green ribbon being tied somewhere it won't be seen, bare thigh and bare shoulder in frame |
| 13 | `cassandra_ball` | Ballroom, backless gown slit to the hip, dancing with the Duke, you holding her cloak |
| 14 | `cassandra_orders` | Black silk slip off both shoulders, stockings, sheets, no ledger — boldest shot of the story |
| 15 | `cassandra_carriage` | Carriage interior, riding coat open, bare leg stretched across the seat, countryside light |
| 16 | `cassandra_wound` | Blood on emerald silk, bodice torn open at the shoulder, her bare hands shaking on your chest |
| 17 | `cassandra_soft` | Firelight, hair down, wearing your open shirt over bare skin, washing your hands |
| 18 | `cassandra_contract` | Full court gown, plunge to the waist, King's seal on the table, her fist closed in the silk |
| 19 | `cassandra_gate` | Rain, thin wet silk clinging, her at the lit window above, you walking out |
| 20 | `cassandra_terms` | Ledger burning in the grate, her in the slip off both shoulders, circlet set aside |

## Generation notes

- Everything vertical 9:16. If a model defaults to landscape, put `9:16 vertical` in the prompt
  **and** put `landscape orientation` in the negative.
- Feed `cassandra_ref.jpg` as an image reference on every chapter still so her face never drifts.
- Player's face out of frame in all shots — over-the-shoulder, hands, or back of head only.
- Candlelight motivated from one side; never flat front lighting. Skin should have shine.
- Video motion should be **small**: breath, silk settling, flame, one deliberate hand movement. Long
  camera moves break the loop and look generated.
- Export MKV to match the other folders. Chapter clips 3–5s, cover loop 5s.
- Bold and revealing is the target; keep it clothed and non-explicit so the store listing and the
  cover art stay safe to publish.
