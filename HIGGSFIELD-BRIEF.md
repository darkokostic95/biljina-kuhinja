# Biljina Kuhinja — Higgsfield brief (for Claude chat)

You are Claude in Claude chat (or Cowork) with the **Higgsfield connector**. Your job is only to **generate the images and video clips** below with Higgsfield. The website itself is built separately in Claude Code, which picks up your results from the same Higgsfield account. Do not build any website here.

Why here: Darko's Higgsfield Ultra plan gives **unlimited generations only in Claude chat, Claude Cowork and ChatGPT**, not in Claude Code. So all generation happens here, with `use_unlim: true`.

---

## 1. What the project is

**Biljina Kuhinja** ("Bilja's Kitchen") is a family recipe website: 288 home recipes from Darko's mom Bilja's handwritten notebooks, in Serbian (default) and English. It's mostly used on phones.

The landing page is one full-screen, photoreal video that plays forward and backward as you scroll (scroll = time), in the style of a product film: **one food item, centered, on a seamless warm cream background, changing through the stages of being made.** Big headlines change with each stage (they are added later as real text on the website, so **no text in the images or videos**).

The video has three chapters, each ending on a finished dish:
1. **Torta** (cakes): ingredients → batter → sponge layers → finished cake → a slice pulled out
2. **Pecivo** (bread & pastry): dough ball → rolled dough → shaped crescent rolls → baked crescent rolls
3. **Glavno jelo** (a real meat meal): raw meat and vegetables → stew in a pot → served plate

Inspiration: an Instagram reel of a croissant website ("Maison Laminée") where one croissant goes from dough ball to baked to broken open as you scroll. Clean, premium, a lot of empty space, photoreal food.

---

## 2. Rules for every generation

- **Where:** create a Higgsfield project named **`Biljina Kuhinja landing`** and put every generation in it (use its folder for all images and clips). Claude Code finds the results there.
- **Unlimited:** always `use_unlim: true`. If a model or setting isn't covered by unlimited, **stop and tell Darko**, do not spend credits (the account has only ~10 credits).
- **Format:** vertical **9:16** for everything.
- **Look:** the same background, light and camera in every image and clip, so the chapter plays as one continuous film.
- **Video:** no audio (`generate_audio: false`), locked camera (no zoom, no pan), one continuous transformation, no cuts.
- **Nothing extra:** no people, no hands, no text, no logos, no watermark, no props that are not part of the dish.

### Style block — append to the end of EVERY image prompt
> Seamless warm cream studio background (#F6EFE4), soft even daylight from the upper left, gentle contact shadow under the subject, subject centered and filling about 60% of the frame width, vertical 9:16, photorealistic food photography, 85mm lens look, sharp detail, natural colors, no people, no hands, no text, no logos, no watermark, no extra props.

### Motion line — append to the end of EVERY clip prompt
> Slow, smooth, continuous transformation with no cuts. The camera is locked off, no zoom, no pan. The cream background and the lighting do not change.

### Models
- **Images:** `gpt_image_2_6` (GPT Image 2.6), quality high if unlimited covers it, otherwise the default. Use a 9:16 aspect ratio.
- **Clips:** `seedance_2_5` in `omni_reference` mode with **start_image** = the first key image and **end_image** = the second, 5–8 seconds, 720p (1080p if unlimited covers it). If Seedance 2.5 isn't covered by unlimited, try `seedance_2_0` with start and end images. If neither is covered, stop and tell Darko.

---

## 3. Step 1 — the 12 key images

Generate all 12 (a batch is fine). Name / caption each one with its code (T1, T2, …) so it can be matched later. After generating, **show all 12 to Darko and let him approve or ask for redos before any video.**

**Torta (cakes)**
- **T1:** A small heap of white flour with a shallow well in the top, three brown eggs, a block of butter, a few walnut halves and a small pile of sugar, arranged closely together as one group.
- **T2:** A wide ceramic mixing bowl seen from a 3/4 high angle, full of smooth pale cake batter with a soft swirl on the surface.
- **T3:** Three thin round sponge cake layers, golden brown, stacked slightly offset with visible space between them.
- **T4:** A tall round layered cake seen from the side at a slight high angle: thin walnut sponge layers with cream between them, covered in glossy dark chocolate glaze, a ring of walnut halves on top.
- **T5:** The same tall layered chocolate walnut cake with one slice pulled out a few centimetres toward the camera, showing the clean layers of sponge and cream inside, a few crumbs beside it.

**Pecivo (bread & pastry)**
- **P1:** A soft mound of white flour with a smooth round ball of raw yeast dough resting on it, lightly dusted with flour.
- **P2:** A thin round sheet of raw dough rolled flat, edges slightly uneven, lightly floured, seen from a 3/4 high angle.
- **P3:** Six raw crescent rolls (kiflice) rolled up from dough triangles, pale and soft, arranged in two neat rows.
- **P4:** Six golden-brown baked crescent rolls (kiflice) sprinkled with sesame, arranged in two rows; the front one is broken open showing the soft white inside, with a thin wisp of steam.

**Glavno jelo (main dish)**
- **M1:** Raw cubes of beef, two red bell peppers, one yellow onion cut in half, three garlic cloves and a small heap of ground red paprika, arranged closely together as one group.
- **M2:** A heavy enamel pot seen from a 3/4 high angle, filled with a rich red-brown meat and pepper stew gently simmering, small bubbles on the surface, light steam rising.
- **M3:** A deep ceramic plate with a generous portion of rich red-brown meat and pepper stew, a piece of bread on the rim, light steam rising.

Tip for consistency: after T1 is approved, you may pass it as an extra image reference for style (background, light) when generating the others, as long as the subject stays as written.

---

## 4. Step 2 — the 9 clips (only after Darko approves the images)

Each clip goes from one approved key image (start_image) to the next (end_image). Use the approved image's job/media id, not a URL.

| Clip | Start → End | Prompt (then add the motion line) |
|---|---|---|
| **T1-T2** | T1 → T2 | The ingredients gently come together and fold into a mixing bowl that rises around them; they blend into smooth pale batter with a soft swirl. |
| **T2-T3** | T2 → T3 | The batter sets and bakes; the bowl fades away and the batter becomes three thin golden sponge layers that lift and separate. |
| **T3-T4** | T3 → T4 | Cream spreads between the layers as they stack into a tall cake; dark chocolate glaze flows down over it and walnut halves settle on top. |
| **T4-T5** | T4 → T5 | One slice slides slowly out of the cake toward the camera, revealing the layers inside; a few crumbs fall. |
| **P1-P2** | P1 → P2 | The dough ball flattens and spreads outward into a thin round sheet as if rolled by an invisible rolling pin; flour dust drifts. |
| **P2-P3** | P2 → P3 | The dough sheet divides into triangles that roll themselves up into six crescent rolls and line up in two rows. |
| **P3-P4** | P3 → P4 | The raw rolls puff up and turn golden brown as they bake; sesame appears on top; the front one breaks open and steam rises. |
| **M1-M2** | M1 → M2 | The meat browns and the peppers and onion soften as a heavy pot forms around them; everything becomes a rich red-brown stew that starts to simmer. |
| **M2-M3** | M2 → M3 | The pot fades and the stew settles onto a deep ceramic plate; a piece of bread lands on the rim; steam rises. |

No clips are needed between chapters (T5 → P1, P4 → M1); the website cross-fades there.

Show each clip to Darko. If one looks wrong (food morphs into something strange, the camera moves, the background changes), regenerate it.

---

## 5. Step 3 — hand-off back to Claude Code

When everything is approved, write one final message listing, for each code (T1…M3 and the 9 clips), the **Higgsfield job id** and the **result URL**. Darko will paste that list into Claude Code, which downloads the files, turns the clips into scroll frames and builds the page. Everything should also be in the `Biljina Kuhinja landing` project.

---

## 6. Not your job here

- Don't build or publish a website, and don't use Higgsfield's website builder.
- Don't change the plan (subjects, colors, 9:16, no text) without asking Darko.
- Don't spend credits; unlimited only.
