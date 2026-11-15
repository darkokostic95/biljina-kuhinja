# Biljina Kuhinja — Higgsfield brief v2 ("the film is the page")

You are Claude in Claude chat (or Cowork) with the **Higgsfield connector**. Your job is only to **generate images and video clips** with Higgsfield. The website is built separately in Claude Code from your results. Do not build a website here.

This replaces `HIGGSFIELD-BRIEF.md` (v1). The v1 media (small objects centered on a cream studio background, locked camera) is live but looks too simple. v2 follows a better reference.

---

## 1. Reference and what makes it work

Reference: Instagram reel of a cheesecake website "Casa Brûlée" (polanaeem.tech). Watching it frame by frame:

1. **The film fills the whole page**, edge to edge. The food is big and bleeds off the screen edges; it is not a small object in a box.
2. **Text sits on the film**: headline, two lines of text and a small button in the **left third**; the food lives in the **right two thirds**. The top bar (logo, menu) floats over the film.
3. **The scene changes with the story**: light cream counter (batter pours into a tin) → **dark oven** (it bakes, steam, white text) → light table (cake lands on a plate, a knife cuts it, the creamy middle shows). The page goes light → dark → light.
4. **Real cooking actions, real motion**: pouring, baking, steam, a knife and a hand cutting. Shallow depth of field, a low 3/4 camera angle, close to the food. Not a top-down catalog shot and not objects magically morphing.
5. **It feels like the product travels down the page**: at the end of a section the food moves on into the next scene instead of cutting.

Everything below is designed to get those five things.

---

## 2. The project

**Biljina Kuhinja** ("Bilja's Kitchen"): 288 home recipes from Darko's mom Bilja's notebooks, Serbian + English, used mostly on phones but must look great on desktop too. The landing page is one film scrubbed by scroll, in three chapters, each ending on a finished dish. Headlines are added later as real text, so **never put text in images or videos**.

1. **Torta** — layered chocolate walnut cake
2. **Pecivo** — kiflice (small crescent rolls with sesame)
3. **Glavno jelo** — beef and red pepper stew

---

## 3. Rules for every generation

- **Project:** create a Higgsfield project **`Biljina Kuhinja landing v2`** and put everything in it.
- **Unlimited only:** always `use_unlim: true`. If something isn't covered by unlimited, **stop and tell Darko**. Never spend credits.
- **Two formats of everything:**
  - **Desktop 16:9** — food in the **right 60%** of the frame, the **left 40% calm and empty** (plain surface/background, no objects) so text can sit there.
  - **Phone 9:16** — food in the **lower 60%**, the **top 35% calm and empty** for text.
  - Make the 16:9 set first. For 9:16, generate each key image again with the 16:9 image as a reference ("same scene, same food, same light, recomposed vertically, food in the lower part"), then generate the 9:16 clips from those. (If Higgsfield's reframe tool is covered by unlimited and keeps the quality, you may reframe the 16:9 clips instead; show Darko one before doing all.)
- **Camera:** low 3/4 angle, close to the food, shallow depth of field (soft background), like a food commercial. Slow, smooth camera moves are welcome (gentle push-in, slight slide). No cuts inside a clip.
- **Hands:** a hand may come into frame for an action (pouring, cutting, sprinkling). Never a face or a full person.
- **No** text, logos, watermarks, brand names on tools.
- **Video:** no audio (`generate_audio: false`), 8 seconds, 1080p if unlimited covers it, otherwise 720p.
- **Continuity:** each clip starts on one approved key image (start_image) and ends on the next (end_image), so the chapter plays as one continuous film.

### Look block — append to every image prompt
> Photorealistic food commercial still, low three-quarter camera angle close to the food, shallow depth of field, soft natural window light from the left, rich natural colors, fine texture detail, no text, no logos, no watermark, no faces.

### Motion block — append to every clip prompt
> One continuous shot, no cuts. Slow, smooth, natural motion, like a food commercial. Realistic physics. Keep the empty text area of the frame calm.

### Models
- **Images:** `gpt_image_2_6`, quality high if unlimited covers it.
- **Clips:** `seedance_2_5` in `omni_reference` mode with start_image and end_image. If it isn't covered by unlimited, try `seedance_2_0` with start and end images. If neither, stop and tell Darko.

---

## 4. Key images (make 16:9 first, then matching 9:16)

Scenes: **LIGHT** = warm cream kitchen counter (#F6EFE4 tones), linen, soft daylight. **DARK** = inside or in front of a dark oven / on a dark stove, warm glow, deep brown-black background.

### Torta (chocolate walnut layer cake)
- **T1 (LIGHT):** A stream of smooth pale cake batter pouring from the top of the frame into a round metal cake tin lined with baking paper.
- **T2 (DARK):** The same tin inside a dark oven, the sponge risen and golden, warm oven glow, a little steam.
- **T3 (LIGHT):** Three thin golden sponge layers stacked with white cream between them on a ceramic cake stand, glossy dark chocolate glaze pouring over the top and running down the sides.
- **T4 (LIGHT):** The finished cake, glazed in dark chocolate with a ring of walnut halves on top, on the cake stand; a knife has cut one slice which is pulled slightly out, showing the clean layers of sponge and cream.

### Pecivo (kiflice)
- **P1 (LIGHT):** A smooth ball of yeast dough on a floured wooden board, a rolling pin beside it, flour dust in the air.
- **P2 (LIGHT):** The dough rolled out and cut into triangles; several are already rolled up into small crescent rolls on the board.
- **P3 (DARK):** A baking tray of crescent rolls inside a dark oven, turning golden brown, sprinkled with sesame, warm glow.
- **P4 (LIGHT):** A linen-lined basket of golden kiflice with sesame; one is torn open in front, soft white inside, steam rising.

### Glavno jelo (beef and pepper stew)
- **M1 (LIGHT):** Raw cubes of beef, red bell peppers, a halved onion, garlic and a small bowl of ground red paprika on a wooden cutting board, a knife beside them.
- **M2 (DARK):** A heavy enamel pot on a dark stove, the beef browning with onion and peppers, steam and a little sizzle, warm light.
- **M3 (DARK):** The same pot full of rich red-brown stew gently simmering, a wooden spoon resting in it, steam rising.
- **M4 (LIGHT):** A deep ceramic bowl of the stew on a linen cloth, a piece of crusty bread on the rim, steam rising.

**Show Darko all 12 in 16:9 and get his OK before the 9:16 versions and before any video.**

---

## 5. Clips (after the images are approved; do each in 16:9 and 9:16)

| Clip | Start → End | Prompt (then add the motion block) |
|---|---|---|
| **T1-T2** | T1 → T2 | The batter finishes pouring and settles; the tin slides away from the light counter into a dark oven, where the sponge slowly rises and turns golden. |
| **T2-T3** | T2 → T3 | The baked sponge comes out of the dark oven into daylight; layers stack on a cake stand with cream between them and dark chocolate glaze starts pouring over the top. |
| **T3-T4** | T3 → T4 | The glaze finishes running down the sides and sets glossy; walnut halves are placed on top; a knife cuts one slice and pulls it slightly out, showing the layers. |
| **P1-P2** | P1 → P2 | A rolling pin rolls the dough ball out flat; it is cut into triangles and hands roll the first triangles up into small crescent rolls. |
| **P2-P3** | P2 → P3 | The shaped rolls are placed on a tray that slides into a dark oven; they puff up and turn golden brown, sesame on top. |
| **P3-P4** | P3 → P4 | The tray comes out of the oven into daylight; the rolls land in a linen-lined basket; one is torn open and steam rises from its soft inside. |
| **M1-M2** | M1 → M2 | The beef, onion and peppers are swept from the board into a hot pot on a dark stove, where they start to sizzle and brown. |
| **M2-M3** | M2 → M3 | Paprika is sprinkled in and liquid is poured over; the pot fills into a rich red-brown stew that begins to simmer, a wooden spoon stirring once. |
| **M3-M4** | M3 → M4 | A ladle lifts the stew out of the pot into a deep ceramic bowl on a linen cloth in daylight; a piece of bread is set on the rim; steam rises. |

Show Darko each clip. Redo any where the food turns into something else, the empty text area gets busy, or the motion looks unnatural.

---

## 6. Hand-off back to Claude Code

When everything is approved, write one final list: for every code and format (for example `T1 16:9`, `T1 9:16`, `T1-T2 16:9`, `T1-T2 9:16`) the **job id** and the **file name / result URL**, plus the common URL base. Darko pastes it into Claude Code, which downloads the files and builds the page: the film full-screen behind the page, text in the calm area, light and dark sections following the film.

## 7. Not your job

- No website building or publishing here.
- No changes to the plan without asking Darko.
- No credits; unlimited only.
