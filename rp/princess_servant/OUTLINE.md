# Outline — Princess Servant (Cassandra)

**Premise.** You're broke, hungry, and out of options. A banner nailed to a post on the north road:
*SERVANT WANTED — HOUSEHOLD OF HER HIGHNESS THE PRINCESS CASSANDRA. TWENTY SILVER A WEEK.* Twenty
silver is four times the going rate. You take the job before you think about why.

**Her.** Princess Cassandra, nineteen, brilliant, bored, and watched by four hundred people who all
want something from her. Strict from the first breath — not cruel for fun, but *precise*, which is
worse, because cruelty gets tired and precision never does. Under it: starving for one person who
isn't performing for her.

**Beatrix.** Head of the household. Runs the interview, the rules, and the reader's onboarding.
Stricter than Cassandra on the surface and enjoys it. Keeps a ledger. Her own entry is nineteen
pages long and she has never once been late.

**Player.** Male-coded, poor, proud in a way that keeps getting him in trouble. Not a fool — he
learns her rules fast and finds the gaps in them.

## Heat curve

| Chapters | Register |
|----------|----------|
| CH01–05 | Cold command. Rules, corrections, humiliation played dry and flirty. Zero softness. |
| CH06–09 | Tension. She notices him noticing. Punishment starts to feel like attention. |
| CH10–14 | Mistress mode. Ownership, the token, the kneeling, the heat peak. |
| CH15–17 | Cracks. Danger outside the palace, and a night where she drops the voice. |
| CH18–20 | Crown vs. him. She chooses, and rewrites her own terms. |

## Chapters

1. **The Banner** ✅ *written* — The road, the sign, the west gate. Nine men interviewed and rejected before you. Beatrix's inspection and three questions. You're hired, dressed in livery, and Cassandra speaks to you from the top of the stair without letting you see her face.
2. **The Table** ✅ *written* — Third bell. She has you kneel on all fours as furniture, rests her bare leg across your back while she reads Beatrix's written assessment of you aloud, then calls for breakfast with the tray left in the passage — because she has a table. Plate, honey, fruit, spoons and a full cup of hot chocolate balanced on your spine. If anything falls you're dismissed out the west gate. Her face is revealed. Twenty-two minutes. Nothing falls.
3. **Learn the Bell** ✅ *written* — A brass bell is screwed into the wall above your cot, wired to her hand. It rings, you appear, already in position — she counts, ten is acceptable, twelve is a failure. Ten rings across a day and a night: mid-errand, mid-meal, twice after midnight, several for no reason at all. She teaches you the kneeling shape herself at ring one. You fail ring nine at nineteen seconds and it goes in her book unpunished, which is worse. By ring ten you're already in the room and you flinch anyway — which is what she was buying.
4. **Wake Her Wrong** ✅ *written* — Twenty to six. Beatrix's briefing: there is no right way to wake her, all four previous tables found a different wrong one, so pick your wrong and commit. Her chamber is dark, the furs are on the floor, and you look. Whatever you choose she's foul about it — and admits you did nothing wrong, because before six-thirty she isn't a princess, she's "something with a temper in a bed." Chocolate arrives, she puts her bare feet in your lap, and gives you three new rules, then cancels two of them and holds you to all three: the only way to know which one you're in is to watch her constantly, which is what she's actually buying. Rule four: when you look, you don't get to pretend you didn't.
5. **A Hundred Strokes** ✅ *written* — The mirror trap: she faces the glass so she watches your face for twenty minutes while Beatrix calls out everything you're doing wrong. A hundred strokes, and somewhere in the sixties she stops being a princess on purpose — nobody's brushed her hair since her mother died and she's furious at herself for admitting it. You go round the nape without touching it, which is when she sends Beatrix out. Then thirty laces on her bare back, tighter, tighter than that, nine flinches counted, and the promise that you'll do her hair and her laces every day twice a day for as long as you last — and she won't tell you what that's for.
6. **Keep Your Eyes on the Water** — You attend the bath before court. Beatrix is very clear about where to stand, which is not the same as where to look.
7. **Caught Looking** — She saw. The cane comes out of the cabinet. You thank her for it.
8. **The Ledger** — Her little book of your failures. The list is getting long on purpose.
9. **Court Day** — Stand behind her chair, say nothing, while nobles discuss your kind.
10. **The Suitor's Gift** — Duke Roderic arrives with horses and intentions.
11. **Wine at Midnight** — She drinks. Her voice slips. The rules bend and snap back.
12. **The Token** — A ribbon, a ring, a mark. Something of hers that you wear where no one sees.
13. **The Ball** — She dances with the Duke. You hold her cloak and your tongue.
14. **On Your Knees** — Heat peak. Her chamber, her orders, no ledger.
15. **The Ride Out** — A carriage, no guards, and a princess pretending it's an errand.
16. **The Wound** — Bandits on the north road. You bleed for her. She doesn't handle that well.
17. **No Rules Tonight** — Soft mistress. She washes your hands and forgets to be Highness.
18. **The King's Command** — The marriage contract is signed. Not by her.
19. **Refuse the Crown** — Scandal, an ultimatum, and a servant told to leave for his own good.
20. **Her Terms** — Ending. She keeps you — on terms she writes herself, out loud, for once.

## Threads to pay off

- **The small writing on the banner** — CH01 flags it and doesn't explain it. Cash it in around CH08–09.
- **Cassandra's ledger** — Beatrix mentions it CH01; it becomes a whole chapter at CH08 and the thing she burns at CH20.
- **"Nobody will come looking for you"** — she wrote that down in CH01. It should matter in CH19.
- **The ninth applicant who ran** — bring him back as a rumour or a face at court.
- **"Good boy"** — her only endearment, first used CH01. Keep it rare so it lands in CH14 and CH17.

## Node conventions (match `nurse_mei` / `doctors_office`)

- Chapter opener: `chapterStart: true` + `chapterTitle`
- `speaker: "narrator"` for narration; `speaker: "Beatrix"` for the head maid; **omit `speaker`** for Cassandra
- One beat per entry in `lines[]`; 4–6 lines per node
- ~13 nodes per chapter, one 3-option choice, branches `_A` / `_B` / `_C` → `_MERGE`
- Action-type choices get a `me` string describing what the player does
- IDs: `CH07_N1`, `CH07_HER1`, `CH07_CHOICE`, `CH07_A`, `CH07_MERGE`, `CH07_END`
- Chapter closes with `(To be continued — Chapter N: Title 🕯️)`; CH20 closes with `— The End —`
- Media: add `videoUrl` / `imageUrl` only once the asset exists in this folder
- No `vars` / no `set` blocks — branching by `next` only
