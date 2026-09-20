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

> plunging neckline, deep cleavage, very busty, tight corseted waist, bare shoulders and collarbones, long
> thigh-high slit with one bare leg exposed, silk thin enough to cling to every curve, silver rings,
> long dark chestnut hair loose, silver crown with emerald stones sitting on her head, rose-pink and red
> princess gown, witch-queen face: sharp cheekbones, intense grey-green eyes, strong dark brows, pale
> porcelain skin, pointed chin, small knowing smirk, lips slightly parted, no teeth

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

**Cassandra** — stunning young adult woman, mid-twenties appearance, tall, slim waist, very busty,
full chest, very upright posture. Witch-queen face: sharp high cheekbones, slightly long
aristocratic face, pointed chin, intense grey-green eyes, strong dark brows, pale porcelain skin.
Expression: small knowing smirk, lips slightly parted, confident, not stern — never smiling with
teeth. Long dark chestnut hair falling loose down her bare back. A real silver crown with emerald
stones sitting on her head — never a thin circlet. Rose-pink silk princess gown with a red corset:
plunging neckline, deep cleavage, tight corseted waist, off-shoulder sleeves, long thigh-high slit.
Silk thin enough to catch every curve. Several silver rings on her right hand. Never smiling with
teeth.

**Beatrix** — striking woman in her late twenties, head maid. Severe black dress, high collar, but
cinched hard at the waist and tighter than it should be; white apron; sheer black stockings; dark
hair pinned up tight. Sharp cheekbones, dark eyes, one eyebrow permanently slightly raised. Brass
chatelaine of keys at her hip. Buttoned-up and obviously dangerous with it.

**Player character** — male servant, late twenties, lean, worn boots, black wool livery with silver
buttons (before hiring: patched linen shirt, open collar). **Face always out of frame** — over the
shoulder, back of head, or hands only.

**World** — late-medieval European palace, candle and firelight only, no electric light. Cold stone,
beeswax candles, dark oak, heavy tapestries, furs, tall narrow windows.

**Style** — bright and clearly lit, not dark, not moody, not cinematic low-key. Soft even palace
daylight or bright lamps so faces, dress, and room are all easy to see. Clean photograph, glossy,
high detail. No heavy shadows swallowing the frame.

**Global negative prompt** — modern clothing, modern objects, electric lighting, plastic, text,
watermark, logo, extra fingers, deformed hands, cartoon, anime, plastic skin, flat front lighting,
overexposed, teeth showing, crowd, children, landscape orientation.

---

## Wardrobe / heat ladder

Escalate what she's wearing as the story escalates. Same woman, same face, less fabric. No fixed
chapter numbers — pick the row that matches the beat being written.

| Register | Wardrobe |
|----------|----------|
| Cold command / early | Rose-pink and red princess gown. Plunging neckline, busty, corseted waist, thigh slit, bare shoulders. Untouchable. |
| Court / public / formal | Backless or open-laced back, plunge to the waist, bare shoulders, slit to the hip |
| Undressed states | Loose robe half-open, unlaced bodice, bare back, sheer shift, wet skin |
| Night / bed | Thin-strap silk slip off both shoulders, sheets low, bare legs and back |
| Peak heat | Black silk slip, corset and stockings, sheets, bare legs, rings and nothing much else |
| Soft / cracked | His shirt worn open over bare skin, loose hair, firelight, no jewellery |
| Outdoor / travel | Riding coat worn open over a low silk shift, bare legs on the seat, boots and thigh |

---

## Cover art — `rp_cover.webp` (9:16)

**Image prompt**

> Vertical cinematic portrait of a stunning young royal woman lounging sideways across a tall carved
> oak throne in a candlelit stone chamber. Rose-pink silk princess gown with a red corset, plunging
> neckline, very busty, deep cleavage, and a long thigh-high slit — one bare leg extended, the other
> bent, silk pooling off the edge of the seat. Tight corseted bodice, off-shoulder sleeves, bare
> shoulders and collarbones. Long dark chestnut hair, a silver crown with emerald stones sitting on
> her head. Silver rings on the hand draped over the armrest. Grey-green eyes locked on the viewer,
> small knowing smirk, lips slightly parted — deciding what to do with you. In the blurred dark
> foreground, the back of a kneeling male servant in black livery. Warm candlelight from the left,
> deep shadow right, shallow depth of field, rose, crimson, gold and black oil-painting palette.
> Sensual, glossy, high detail. 9:16 vertical.
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

> Vertical character reference of the same stunning young royal woman with a witch-queen face (sharp
> cheekbones, intense grey-green eyes, strong dark brows, pale porcelain, pointed chin, small knowing
> smirk). Very busty. Rose-pink silk princess gown with a red corset, plunging neckline, deep
> cleavage, corseted waist, thigh-high slit, bare shoulders, a silver crown with emerald stones
> sitting on her head, long dark chestnut hair. Neutral dark grey background, soft even light, full
> body. 9:16 vertical. No text labels. Feed `cassandra_ref_face.jpg` for likeness.

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

## CH06 — Head Back

Her head tipped back over the copper rim, throat bare, eyes shut, his hands in her hair. She's in a
thin wet linen shift in the water — wet linen, not bare. Her face visible and completely undefended,
which happens exactly once in the story.

Base name: `cassandra_bath`

**Image prompt**

> Vertical cinematic shot in a small stone bath chamber thick with steam, lit by one candle and a
> brazier. A large copper tub. A stunning young royal woman lies back in the water and has tipped her
> head all the way back over the rim toward camera — throat and collarbones bare and stretched, chin up,
> eyes closed, lips just parted. She wears a thin white linen shift, soaked through and clinging, straps
> off both shoulders, plunging wet neckline, deep cleavage at the waterline. Long dark chestnut hair
> spread wet and heavy over the copper rim and over a man's hands.
>
> Behind her at the head end, a man in a soaked black livery shirt kneels on wet stone, sleeves rolled
> high, both hands buried in her hair, head lowered, face turned away and not visible.
>
> Steam curling, water beaded on her skin, warm candlelight raking low across her throat and chest, deep
> shadow behind. Shallow depth of field, copper and emerald and gold palette, sensual, high detail. 9:16
> vertical.
>
> Negative: his face visible, nudity, landscape orientation, flat lighting, modern clothing, electric
> light, text, watermark, extra fingers, deformed hands, teeth showing.

**Video prompt (image-to-video, from `cassandra_bath.jpg`)**

> Static camera. His fingers work slowly through her hair at the scalp; her head presses back into his
> hands and her throat stretches further; her lips part and her chest rises once, long and slow. Water
> runs off a strand of hair down the copper. Steam drifts across the frame, candle flame shudders. Her
> eyes stay shut the entire time. 5 seconds, 9:16, no camera shake.

**Alternate CH06 shot** — the dropped ring. Base name `cassandra_bath_reach`:

> Vertical shot, same steamy chamber, from the side. The royal woman lies back in the copper tub in the
> soaked clinging linen shift, one arm along the rim, watching with lazy amusement and a faint superior
> smile as a man's bare arm goes into the water past the elbow beside her knee, searching. His head is
> turned away, face not visible. Ruby ring glinting on the bottom of the tub. Candlelight, steam, wet
> copper. 9:16 vertical.
>
> Video: his arm goes deeper into the water and the surface breaks; she doesn't help; her smile widens
> very slightly and her eyes come up to camera. 4 seconds, static camera, 9:16.

---

## CH07 — Under the Table

Two hours on his knees under her council table with her bare feet on him, four of the King's men a
foot from his head. The trick is showing both sides of the green cloth at once.

Base name: `cassandra_table_court`

**Image prompt**

> Vertical cinematic shot inside a grand stone council chamber, hard morning light through tall narrow
> windows, dust in the air. Camera low, at floor level, looking along and slightly under a heavy oak
> writing table draped in a green cloth that reaches the floor — the cloth lifted and held open on one
> side so we see both worlds at once.
>
> Above the table: a stunning young royal woman sits in a carved chair in a fitted grey silk court gown
> with a deep plunging neckline, deep cleavage, bare shoulders, waist laced hard, emerald at her throat,
> hair up with a thin silver circlet, silver rings. She is turned slightly away speaking to men we see
> only as blurred dark shapes and boots at the edges of frame — chin lifted, cold, bored, entirely in
> command, no teeth.
>
> Below the table in the green half-light: a man in black servant's livery kneels on all fours, back flat
> and level, head down and turned away so his face is not visible. One of her bare feet rests on the small
> of his back; her grey silk shoes lie discarded on the rug beside his knee. Balanced between his shoulder
> blades, a fine porcelain teacup and saucer, full, steaming. Dust on his shoulders, sweat at the back of
> his neck.
>
> Hard daylight above, deep green gloom below, shallow depth of field, grey and emerald and gold palette,
> tense and sensual and dominant. 9:16 vertical.
>
> Negative: his face visible, other faces in focus, landscape orientation, flat lighting, modern
> clothing, electric light, text, watermark, extra fingers, deformed hands, teeth showing, covered chest.

**Video prompt (image-to-video, from `cassandra_table_court.jpg`)**

> Almost static, the faintest push in. Above the table she keeps talking, unbothered, and turns a page
> without looking down. Below it, her bare heel drags slowly up his spine and the full teacup tilts on his
> back — steam shivering, a thread of tea running over the rim and down his ribs. His back locks; his head
> stays down; the porcelain makes no sound. Dust drifts through the window light. Her expression never
> changes. 5 seconds, 9:16, no camera shake.

**Alternate CH07 shot** — after, the shoes. Base name `cassandra_shoes`:

> Vertical shot in the empty council chamber, papers still on the table, hard sideways daylight. The
> royal woman sits back in the carved chair with her legs crossed at the ankle, grey court gown plunging
> and slit open along one thigh, chin on her hand, looking down with open ownership and a faint smile. A
> man in dusty black livery kneels in front of her chair fitting a grey silk shoe onto her bare foot, her
> ankle held in his hand, his head lowered and face not visible. Dust in the light, empty chairs behind.
> 9:16 vertical.
>
> Video: he slides the shoe on and his hand stays on her ankle a beat too long; her foot flexes once in
> his grip; her smile moves and her eyes come up to camera. 4 seconds, static camera, 9:16.

---

## CH08 — Payday

Twenty silver counted one coin at a time into his cupped hands while he kneels. She's in the green
robe on the window sill, bored and generous and about to take a day of his life apart.

Base name: `cassandra_payday`

**Image prompt**

> Vertical cinematic shot in a warm candlelit royal bedchamber, bright winter light through a tall narrow
> window. A stunning young royal woman sits sideways on the deep stone window sill in an emerald-green
> silk robe worn open — plunging to the waist, deep cleavage, sash loose, bare shoulders, one bare leg
> drawn up and the other stretched down, silk clinging. Long dark chestnut hair loose, thin silver
> circlet, silver rings. She holds a single silver coin up between two fingers at eye level, looking down
> past it with lazy amusement and total ownership, chin lifted, no teeth. A small leather purse and a
> neat stack of coins on the table beside her.
>
> Kneeling below her on the floor, a man in black servant's livery holds both hands cupped together like
> a bowl, already half full of silver coins, head lowered, face turned away and not visible.
>
> Cold window light on her, warm firelight from behind camera, deep shadow, shallow depth of field,
> emerald and gold and silver palette, sensual and dominant. 9:16 vertical.
>
> Negative: his face visible, landscape orientation, flat lighting, modern clothing, electric light, text,
> watermark, extra fingers, deformed hands, teeth showing, covered chest.

**Video prompt (image-to-video, from `cassandra_payday.jpg`)**

> Static camera. She lets the coin drop from her fingers into his cupped hands — it lands, the small stack
> shifts, his hands sink a fraction under the weight. Her robe slides another inch off her shoulder as her
> arm lowers. She watches the coins, then raises her eyes to camera and holds. Window light, dust, no
> other movement. 5 seconds, 9:16, no camera shake.

---

## CH09 — The Wall

Nose to six-hundred-year-old stone, arms out, an hour — while she and Lady Mirren drink wine four feet
behind him and discuss him as furniture. Two women, one wall, one man being ignored on purpose.

Base name: `cassandra_wall`

**Image prompt**

> Vertical cinematic shot in a warm royal chamber, firelight and cold morning window light. In the
> foreground on the left, close to camera, a man in black servant's livery stands pressed nose-first
> against a blank wall of old grey stone, feet together, both arms straight out at his sides with palms
> flat to the wall, head turned away so his face is not visible, shoulders shaking with strain.
>
> Behind him, in focus, two seated women with wine. Nearest: a stunning young royal woman lounging back in
> a carved chair in an emerald-green silk gown — plunging neckline, deep cleavage, bare shoulders, skirt
> split open along one bare thigh, silver rings, hair up with a thin silver circlet, glass held loosely,
> looking straight at camera past the servant with cool amusement. Beside her, a second noblewoman in a
> wine-red gown, also low-cut, leaning forward with open curiosity toward the man at the wall.
>
> Warm firelight, deep shadow on the stone, shallow depth of field, emerald and red and gold palette,
> tense and sensual. 9:16 vertical.
>
> Negative: his face visible, landscape orientation, flat lighting, modern clothing, electric light, text,
> watermark, extra fingers, deformed hands, teeth showing, covered chest.

**Video prompt (image-to-video, from `cassandra_wall.jpg`)**

> Static camera. His outstretched arms tremble and sag a few inches; without looking away from camera she
> lifts one finger from her glass and they come straight back up. The other woman leans in further and
> laughs silently. Firelight moves; wine tilts in the glass. Nobody looks at him. 5 seconds, 9:16, no
> camera shake.

---

## CH10 — The Maid Who Saw

A fourteen-year-old laundry maid made complicit — cold water poured over a kneeling man on the
Princess's orders, and the Princess watching *his* face rather than the girl's.

Base name: `cassandra_maid`

**Image prompt**

> Vertical cinematic shot in a warm royal chamber, daylight through a tall window, fire in the grate. In
> the centre, a bare-chested man in dark servant's trousers kneels upright on wet floorboards in a
> spreading puddle — knees together, palms flat on his thighs, head lowered, face turned away and not
> visible, soaked hair, water running off him, a brown circular burn mark visible on his upper back.
>
> Standing in front of him, a small young maid in a plain grey dress and white cap holds an empty white
> jug in both shaking hands, eyes shut, face crumpled — she is fully dressed, plain and modest.
>
> Behind them both, seated in a carved chair, a stunning young royal woman in a grey silk court gown with
> a deep plunging neckline, deep cleavage, bare shoulders, waist laced hard, skirt open along one bare
> thigh, hair up with a silver circlet, chin on her hand — watching the kneeling man, not the maid, with
> cold fascination. No teeth.
>
> Cold window light, warm fire, water shine on the boards, shallow depth of field, grey and emerald and
> gold palette, high detail. 9:16 vertical.
>
> Negative: his face visible, nudity, revealing clothing on the maid, landscape orientation, flat lighting,
> modern clothing, electric light, text, watermark, extra fingers, deformed hands.

**Video prompt (image-to-video, from `cassandra_maid.jpg`)**

> Static camera. The last of the water runs off his hair and shoulders and drips into the puddle; his back
> tenses once and holds. The maid's hands shake on the empty jug. Behind them the Princess's eyes never
> leave him; she tilts her head very slightly. Firelight moves on the wet floor. 5 seconds, 9:16, no
> camera shake.

---

## CH11 — The Blindfold

Her stocking tied over his eyes, an hour of service blind, and her circling him in the dark in the
black silk slip while he can't tell where she is.

Base name: `cassandra_blindfold`

**Image prompt**

> Vertical cinematic shot in a dark royal bedchamber lit by one candle and a low red fire, curtains shut.
> A man in a white servant's shirt kneels in the middle of the room, upright, palms flat on his thighs,
> a length of fine black silk stocking tied twice over his eyes and knotted at the back of his head; head
> lifted slightly, listening, face angled away from camera so it is not identifiable.
>
> Standing behind and to the side of him, a stunning young royal woman in a black silk slip — thin straps
> off both shoulders, plunging neckline, deep cleavage, silk clinging, bare legs, barefoot, silver rings,
> long dark chestnut hair loose. She is reaching out with two fingertips toward the side of his throat,
> not quite touching, watching his face with intense delighted focus, lips parted, chin lifted. She knows
> he can't see her.
>
> Single candle rim-lighting her shoulder and his jaw, everything else deep shadow, shallow depth of
> field, black and gold and skin palette, sensual and dominant, high detail. 9:16 vertical.
>
> Negative: his face identifiable, landscape orientation, flat lighting, modern clothing, electric light,
> text, watermark, extra fingers, deformed hands, teeth showing, covered chest.

**Video prompt (image-to-video, from `cassandra_blindfold.jpg`)**

> Static camera. Her two fingertips come down and trail slowly along the side of his throat; his head
> turns a fraction toward the touch, blindfolded, and his jaw tightens. One silk strap slides off her
> shoulder. The candle flame leans and recovers. She smiles without showing teeth and looks up at camera.
> 5 seconds, 9:16, no camera shake.

**Second still — `cassandra_kettle`** (the spill that becomes the excuse)

> Vertical close shot at the hearth, firelight only. A blindfolded man's hands pour from a heavy iron
> kettle into a fine porcelain cup on a tray — the pour slightly off, three drops of boiling water going
> over the rim onto the polished boards, steam rising. His face is out of frame or turned away. In the
> blurred background, bare legs and black silk: the royal woman standing watching, one hand on the bedpost.
> 9:16 vertical.
>
> Video: the drops fall and hit the wood; steam curls; his wrist freezes mid-pour. Behind him, her bare
> feet turn toward him on the boards. 4 seconds, static camera, 9:16.

---

## CH12 — Hands Behind Your Back

The best shot in the story so far: a foot of fresh snow, a man on his knees with his wrists tied
behind his back and his face in the white, and her forty feet up at a lit window with a glass of red.

Base name: `cassandra_snow`

**Image prompt**

> Vertical cinematic shot, low winter light, a walled stone courtyard under a foot of untouched fresh snow.
> In the foreground, a man in black servant's livery kneels deep in the snow with his wrists tied behind
> his back with black silk cord, coatless, soaked to the knees, head down and face turned into the snow so
> it is not visible, breath steaming.
>
> Above and behind him, forty feet up, an open lit balcony window in the palace wall — warm gold light
> spilling out. A stunning young royal woman leans on the rail in it, framed by the warm light: grey wool
> gown open over emerald silk, plunging neckline, deep cleavage, bare shoulders, one bare leg visible
> through the split skirt against the stone, silver rings, hair up with a thin silver circlet, a glass of
> red wine held loose in one hand. She is looking down at him with warm, delighted, unrepentant ownership.
> No teeth.
>
> Cold blue-white snow below, single warm gold window above, deep shadow between, falling snow, shallow
> depth of field, blue and gold and emerald palette, cruel and beautiful. 9:16 vertical.
>
> Negative: his face visible, landscape orientation, flat lighting, modern clothing, electric light, text,
> watermark, extra fingers, deformed hands, teeth showing, covered chest.

**Video prompt (image-to-video, from `cassandra_snow.jpg`)**

> Almost static, the faintest drift downward. He pushes forward through the snow with his shoulder and
> face, hands tied, breath steaming; snow falls steadily. Forty feet up she tilts her glass, takes a slow
> mouthful, and calls something down without changing her expression. Warm light flickers behind her. 5
> seconds, 9:16, no camera shake.

**Second still — `cassandra_hands`** (after, at the fire)

> Vertical close shot, firelight only, a dark chamber. A stunning young royal woman sits on the floor in
> front of the fire in a grey wool gown open over emerald silk — plunging neckline, deep cleavage, bare
> shoulders, skirt fallen open along both bare legs folded under her, hair coming down, circlet crooked.
> She holds a man's raw red hands between both of her own, working the fingers, looking at the fire rather
> than at him. He sits on the floor opposite, head down, face not visible, shirt soaked dark, black silk
> cord discarded on the boards beside them.
>
> Warm low firelight from one side, deep shadow, shallow depth of field, gold and emerald and black
> palette, intimate and dangerous. 9:16 vertical.
>
> Video: she works one finger at a time and his hands twitch; she doesn't stop and doesn't look up; the
> fire shifts and a log settles. Her thumb moves once across his knuckles. 4 seconds, static camera, 9:16.

---

## CH13 — The Ankle

3:10am. She's on the edge of the bed in an emerald silk crop top and mini skirt. He's on the floor
between her knees, mouth on her right ankle, hands flat on the boards. Face not visible.

Base name: `cassandra_ankle`

**Image prompt**

> Vertical cinematic shot, dark royal bedchamber, one candle and a dying fire. A stunning young royal
> woman sits on the edge of a carved four-poster bed: emerald silk crop top, tight, plunging neckline,
> deep cleavage, bare midriff, matching emerald silk mini skirt ridden up both thighs, one knee on the
> mattress, the other bare leg hanging off the bed, silver rings, long dark chestnut hair loose, thin
> silver circlet slightly crooked, lips parted, chin lifted, looking down with delighted unrepentant
> ownership. No teeth.
>
> On the floor between her knees, a man in black servant's livery kneels, hands flat on the boards,
> head down, mouth on her right ankle, face turned away so it is not identifiable. Mini skirt silk
> brushing his hair.
>
> Single candle from the left, warm gold on her stomach and his bowed head, deep shadow behind, shallow
> depth of field, emerald and gold and skin palette, sensual and dominant, high detail. 9:16 vertical.
>
> Negative: his face visible, nudity, landscape orientation, flat lighting, modern clothing on him,
> electric light, text, watermark, extra fingers, deformed hands, teeth showing, covered chest.

**Video prompt (image-to-video, from `cassandra_ankle.jpg`)**

> Static camera. Her ankle turns a fraction into his mouth; his hands stay flat on the boards. She
> looks down, breathes once, and does not pull the mini skirt down. Candle flame leans and recovers.
> 5 seconds, 9:16, no camera shake.

**Second still — `cassandra_heel`** (after, heel on his shoulder)

> Vertical close shot, firelight and one candle. She sits on the edge of the bed in the same emerald
> silk crop top and mini skirt, one bare heel resting on a kneeling man's shoulder, pushing him back
> onto his heels so he has to look at her. His face is out of frame or turned away. Circlet crooked,
> colour in her face, crop slipped on one side, she has not fixed it. She looks down at him like she
> lost an argument with herself. 9:16 vertical.
>
> Video: her heel presses once; the crop strap slips a little further; she does not fix it; candle
> moves. 4 seconds, static camera, 9:16.

---

## CH14 — The Door

The sealed room breaks. She's in his lap on the floor in the crop and mini, his hands on her waist —
and Beatrix in the open doorway, grey dawn, keys, no knock.

Base name: `cassandra_door`

**Image prompt**

> Vertical cinematic shot, royal bedchamber at grey dawn, door standing open. In the foreground on the
> floor at the foot of a carved bed: a stunning young royal woman sitting in a man's lap, emerald silk
> crop top, plunging neckline, deep cleavage, bare midriff, matching mini skirt ridden up her thighs,
> bare legs either side of him, silver rings, long dark chestnut hair loose, thin silver circlet crooked,
> his hands on her waist. She is looking over her shoulder at the door, face gone still, lips parted, no
> teeth. The man is in black servant's livery, face turned away or hidden against her, not identifiable.
>
> In the doorway, grey morning light behind her: a striking woman in a severe black dress cinched hard
> at the waist, white apron, sheer black stockings, dark hair pinned tight, brass chatelaine of keys at
> her hip. She is looking at the Princess, not at the man. One eyebrow slightly raised. She has not
> knocked.
>
> Cold grey light from the door, dying candle on the table, deep shadow in the room, shallow depth of
> field, emerald and black and winter palette, intimate and interrupted, high detail. 9:16 vertical.
>
> Negative: his face visible, nudity, landscape orientation, flat lighting, modern clothing on him,
> electric light, text, watermark, extra fingers, deformed hands, teeth showing, covered chest.

**Video prompt (image-to-video, from `cassandra_door.jpg`)**

> Static camera. Beatrix's keys shift once on the chatelaine. Cassandra's hands tighten in her own
> silk; she does not look at the man in her lap. Grey light holds. 5 seconds, 9:16, no camera shake.

**Second still — `cassandra_gate`** (the yard)

> Vertical shot, blue winter morning, a palace courtyard and south gate. Fourteen dark-painted carts
> on the cleared road, horses steaming. In the foreground, a man in black livery with an armful of
> firewood, back to camera, face not visible. In the distance a man in a black coat already off his
> horse, looking up at a high shuttered window. The shutters stay shut. 9:16 vertical.
>
> Video: horses shift, breath steams, the man in the coat does not look away from the window. 4
> seconds, static camera, 9:16.

---

## CH15 — Her Terms

Finale. Noon in the hall: grey backless gown, wine jug, the Duke asking who he is. Then her rooms —
the market ribbon on his wrist, her in his lap, door unlocked.

Base name: `cassandra_terms`

**Image prompt**

> Vertical cinematic shot, a royal receiving hall at noon, tall windows, winter light. A stunning young
> royal woman stands by a carved chair in a grey silk gown: plunging neckline, deep cleavage, backless
> to the waist, tight corseted bodice, long thigh-high slit with one bare leg exposed, silver rings,
> long dark chestnut hair half-pinned, thin silver circlet, chin lifted, speaking quietly with unrepentant
> ownership, lips parted, no teeth.
>
> Behind her chair, a man in black servant's livery holds a wine jug, head down, face not identifiable.
> At the table, slightly out of focus: a man in a black coat seated, watching her not the servant; an
> older uncle gone pale.
>
> Single-source cold noon light from the windows, deep shadow on the far wall, shallow depth of field,
> grey and silver and skin palette, regal and dangerous, high detail. 9:16 vertical.
>
> Negative: his face visible, nudity, landscape orientation, flat lighting, modern clothing, electric
> light, text, watermark, extra fingers, deformed hands, teeth showing, covered chest.

**Video prompt (image-to-video, from `cassandra_terms.jpg`)**

> Static camera. She does not raise her voice; her hand settles on the arm of the chair, silver rings
> catching the light. The servant does not look up. The Duke sits back a fraction. 5 seconds, 9:16, no
> camera shake.

**Second still — `cassandra_ribbon`** (her rooms, after)

> Vertical close shot, her bedchamber, noon light through shutters. A stunning young royal woman sits
> in a man's lap on the floor at the foot of the bed, still in the grey silk gown — plunging neckline,
> deep cleavage, backless, slit fallen open along both bare legs, circlet on, hair coming down. She has
> tied a length of cheap green market ribbon around his wrist; her fingers are still on the knot. He is
> in black livery, face turned away, not identifiable. The chamber door stands unlocked behind them.
> She looks at the ribbon, not at the camera, like a woman who has won an argument she will hate in the
> morning. No teeth.
>
> Warm leftover fire, cold noon at the shutters, shallow depth of field, grey and green and gold
> palette, intimate and claimed, high detail. 9:16 vertical.
>
> Video: her thumb settles on the knot; she does not untie it; she sits a little heavier in his lap;
> the unlocked door does not move. 4 seconds, static camera, 9:16.

---

## Chapter shots

One still + one video per chapter, added here as each chapter is written. No forward plan — the story
is decided chapter by chapter.

| CH | Base name | Shot |
|----|-----------|------|
| 01 | `cassandra_stair` | ✅ Hand and rings on bannister, bare leg through the slit, face hidden |
| 02 | `cassandra_table` | ✅ Breakfast served on the kneeling servant's back, her leg across him as a footrest, her face revealed |
| 03 | `cassandra_bell` | ✅ 3am — she sits up in bed pulling the bell cord, he kneels on the cold floor in position |
| 04 | `cassandra_morning` | ✅ Six a.m., curtains thrown wide, silk slip off both shoulders, sheet at her hips, glaring at camera |
| 05 | `cassandra_mirror` | ✅ At the glass, slip off both shoulders, bare back, your hands in her hair, her eyes on you in the reflection |
| 05b | `cassandra_laces` | ✅ Second shot for CH05 — bare back, bodice held to her chest by one forearm, your fists pulling the cord tight |
| 06 | `cassandra_bath` | ✅ Head back over the copper rim, throat bare, wet clinging shift, your hands in her hair |
| 07 | `cassandra_table_court` | ✅ Under the council table — on all fours, her scalding teacup on your back and her heel on your spine, King's men above, cloth lifted to show both halves |
| 08 | `cassandra_payday` | ✅ Coin dropped into cupped hands, her on the window sill in the open green robe |
| 09 | `cassandra_wall` | ✅ Nose to the stone, arms out, two women with wine behind him |
| 10 | `cassandra_maid` | ✅ The maid pouring cold water over a kneeling man while the Princess watches his face |
| 11 | `cassandra_blindfold` | ✅ Her stocking over his eyes, her fingertips an inch off his throat in the dark |
| 11b | `cassandra_kettle` | ✅ Second shot for CH11 — the blind pour, three drops going over the rim |
| 12 | `cassandra_snow` | ✅ Kneeling in a foot of snow with wrists tied, her forty feet up at a lit window with red wine |
| 12b | `cassandra_hands` | ✅ Second shot for CH12 — she brings his frozen hands back at the fire, cord on the boards |
| 13 | `cassandra_ankle` | ✅ On the bed in silk crop and mini, him on the floor, mouth on her ankle |
| 13b | `cassandra_heel` | ✅ Second shot for CH13 — her heel on his shoulder, crop slipped, circlet crooked |
| 14 | `cassandra_door` | ✅ Beatrix in the doorway, Cassandra in his lap on the floor, crop and mini |
| 14b | `cassandra_gate` | ✅ Second shot for CH14 — fourteen carts, him with wood, the Duke looking at her shutter |
| 15 | `cassandra_terms` | ✅ Hall at noon — grey backless gown, wine jug, she tells the Duke no |
| 15b | `cassandra_ribbon` | ✅ Second shot for CH15 — green market ribbon on his wrist, her in his lap, door unlocked |

## Generation notes

- Everything vertical 9:16. If a model defaults to landscape, put `9:16 vertical` in the prompt
  **and** put `landscape orientation` in the negative.
- Feed `cassandra_ref.jpg` as an image reference on every chapter still so her face never drifts.
- Player's face out of frame in all shots — over-the-shoulder, hands, or back of head only.
- Bright even palace light. Not dark, not cinematic, not moody. Skin should have shine.
- Video motion should be **small**: breath, silk settling, flame, one deliberate hand movement. Long
  camera moves break the loop and look generated.
- Export MKV to match the other folders. Chapter clips 3–5s, cover loop 5s.
- Bold and revealing is the target; keep it clothed and non-explicit so the store listing and the
  cover art stay safe to publish.
