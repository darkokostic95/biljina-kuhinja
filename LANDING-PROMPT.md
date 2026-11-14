# Biljina Kuhinja — landing page prompt (v2, "made in stages")

Reference: Instagram reel by polanaeem.tech (croissant site "Maison Laminée", marked "AI content").
What that site does: one hero food object on a clean cream background. As you scroll, the same object changes through the stages of being made (dough ball → butter on dough → folded → rolled → raw croissant → baked → broken open), and a big headline changes with every stage ("Crafted in layers", "Layer by layer", "Baked to rise", "Made to flake", "Layers worth breaking"). Minimal menu, lots of empty space, photoreal food, no decoration.

The previous version (flat-lay table with the logo objects) is kept as backup: git tag `v1-simple`, branch `backup/v1-simple`.

---

## 1. The page prompt (what to build)

> Build the landing page of **Biljina Kuhinja**, a family recipe site (288 Serbian home recipes, Serbian Latin + English), **mobile first**.
>
> The whole first part of the page is **one pinned, full-screen, photoreal video that plays forward and backward with the scroll** (scroll = time). The video shows food being made in stages, always **one hero subject, centered, on a seamless warm-cream background** (#F6EFE4) with a soft shadow under it, like a product film. Nothing else is in frame: no hands, no people, no text, no props that are not part of the dish.
>
> The video has **three chapters**, and each chapter ends on a finished dish:
> 1. **Torta** (cakes and sweets): ingredients → batter → baked layers → layers stacked with cream → finished walnut-chocolate cake → one slice pulled out.
> 2. **Pecivo** (bread and pastry): flour mound → dough ball → dough rolled flat → shaped kiflice → baked golden kiflice, one broken open with steam.
> 3. **Glavno jelo** (a real meat meal): raw meat, peppers and onion → browned in a pot → stew simmering → served on a plate, steaming.
>
> **Over the video, real HTML text changes with the stages**: a small label (chapter name), a very large headline (2–4 words) and one short line. Text sits in the top third; the subject stays in the middle; the bottom third stays free for buttons.
>
> **When a chapter reaches its finished dish, details come up from the bottom**: a card with the recipe groups that belong to that chapter (each a big tap target with the number of recipes) and a main button "Pogledaj recepte". The video holds on the finished dish while the card is up, then the next chapter starts as you keep scrolling.
> - After Torta: Torte · Kolači · Bez pečenja · Sitni kolači · Kremovi i sladoledi
> - After Pecivo: Peciva · Pite
> - After Glavno jelo: Glavna jela · Salate i predjela · Zimnica · Napici
>
> **Always visible:** a slim top bar (logo, SR/EN, search icon) and, on phones, the bottom tab bar (Početna · Pretraga · Grupe · Knjiga · Omiljeni). A thin progress line and three dots show which chapter you are in; tapping a dot jumps to that chapter. A "Preskoči" link jumps to the groups.
>
> **After the video:** search bar "Šta danas kuvamo?", all 11 groups as a grid, "Čitaj kao knjigu", "Iznenadi me", the tiramisu video recipe, footer.
>
> **Look:** warm cream background, espresso text (#3B2A20), terracotta buttons (#C0643B), honey accents (#E0A53C). Font: Bricolage Grotesque, headlines very large and tight (weight 800). Calm, premium, a lot of empty space. No handwriting fonts, no emoji, no checkboxes.
>
> **Phone rules:** portrait 9:16 video, subject never wider than 80 % of the screen, headline max 3 lines at 390 px, tap targets ≥ 48 px, nothing under the notch or the tab bar. Total scroll length about 9–10 screens. With "reduce motion" or a slow connection: three still photos (the finished dishes) with the same text and cards, no scrubbing.
>
> **Tech:** video is delivered as image frames (WebP, ~540×960 on phones) drawn on a canvas and scrubbed by scroll; first frame is a normal image so the page appears instantly; frames load in a coarse pass first, then fill in. Static site (Astro), GitHub Pages.

---

## 2. On-screen text (HTML, changes with scroll)

| Chapter | Stage | Label | Headline (SR) | Headline (EN) |
|---|---|---|---|---|
| Torta | ingredients | Torte i kolači | Sve počinje od brašna. | It all starts with flour. |
| Torta | batter | | Umućeno s ljubavlju. | Whisked with love. |
| Torta | layers | | Kora po kora. | Layer by layer. |
| Torta | finished | | Torta za svaku slavu. | A cake for every celebration. |
| Torta | slice | | Parče za vas. | A slice for you. |
| Pecivo | flour/dough | Peciva i pite | Testo koje raste. | Dough that rises. |
| Pecivo | rolled | | Razvučeno rukom. | Rolled by hand. |
| Pecivo | shaped | | Uvijeno, pa u rernu. | Rolled up, then baked. |
| Pecivo | baked | | Toplo iz rerne. | Warm from the oven. |
| Jelo | raw | Glavna jela | Od svežeg… | From fresh… |
| Jelo | pot | | …do krčkanja. | …to a slow simmer. |
| Jelo | plate | | Ručak je gotov. | Lunch is ready. |

---

## 3. Generation prompts

### Style block (put at the end of every image and video prompt)
`Seamless warm cream studio background (#F6EFE4), soft even daylight from the upper left, gentle contact shadow under the subject, subject centered and filling about 60% of the frame width, vertical 9:16, photorealistic food photography, 85mm lens look, sharp detail, natural colors, no people, no hands, no text, no logos, no watermark, no extra props.`

### Key frames (images, 9:16) — generated first so the look stays consistent
**Torta**
- T1: `A small heap of white flour with a shallow well in the top, three brown eggs, a block of butter, a few walnut halves and a small pile of sugar, arranged closely together as one group.`
- T2: `A wide ceramic mixing bowl seen from a 3/4 high angle, full of smooth pale cake batter with a soft swirl on the surface.`
- T3: `Three thin round sponge cake layers, golden brown, stacked slightly offset with visible space between them.`
- T4: `A tall round layered cake seen from the side at a slight high angle: thin walnut sponge layers with cream between them, covered in glossy dark chocolate glaze, a ring of walnut halves on top.`
- T5: `The same tall layered chocolate walnut cake with one slice pulled out a few centimetres toward the camera, showing the clean layers of sponge and cream inside, a few crumbs beside it.`

**Pecivo**
- P1: `A soft mound of white flour with a smooth round ball of raw yeast dough resting on it, lightly dusted with flour.`
- P2: `A thin round sheet of raw dough rolled flat, edges slightly uneven, lightly floured, seen from a 3/4 high angle.`
- P3: `Six raw crescent rolls (kiflice) rolled up from dough triangles, pale and soft, arranged in two neat rows.`
- P4: `Six golden-brown baked crescent rolls (kiflice) sprinkled with sesame, arranged in two rows; the front one is broken open showing the soft white inside, with a thin wisp of steam.`

**Glavno jelo**
- M1: `Raw cubes of beef, two red bell peppers, one yellow onion cut in half, three garlic cloves and a small heap of ground red paprika, arranged closely together as one group.`
- M2: `A heavy enamel pot seen from a 3/4 high angle, filled with a rich red-brown meat and pepper stew gently simmering, small bubbles on the surface, light steam rising.`
- M3: `A deep ceramic plate with a generous portion of rich red-brown meat and pepper stew, a piece of bread on the rim, light steam rising.`

### Clips (video, 9:16, 5–8 s each, start image → end image, no audio)
Common motion line: `Slow, smooth, continuous transformation with no cuts. The camera is locked off, no zoom, no pan. The background and lighting do not change.`

- T1→T2: `The ingredients gently come together and fold into a mixing bowl that rises around them; they blend into smooth pale batter with a soft swirl.`
- T2→T3: `The batter sets and bakes; the bowl fades away and the batter becomes three thin golden sponge layers that lift and separate.`
- T3→T4: `Cream spreads between the layers as they stack into a tall cake; dark chocolate glaze flows down over it and walnut halves settle on top.`
- T4→T5: `One slice slides slowly out of the cake toward the camera, revealing the layers inside; a few crumbs fall.`
- P1→P2: `The dough ball flattens and spreads outward into a thin round sheet as if rolled by an invisible rolling pin; flour dust drifts.`
- P2→P3: `The dough sheet divides into triangles that roll themselves up into six crescent rolls and line up in two rows.`
- P3→P4: `The raw rolls puff up and turn golden brown as they bake; sesame appears on top; the front one breaks open and steam rises.`
- M1→M2: `The meat browns and the peppers and onion soften as a heavy pot forms around them; everything becomes a rich red-brown stew that starts to simmer.`
- M2→M3: `The pot fades and the stew settles onto a deep ceramic plate; a piece of bread lands on the rim; steam rises.`

Chapter joins (T5→P1, P4→M1) are done in the page as a soft cross-fade, not as a generated clip.

---

## 4. Build notes

- Each clip → extract ~40 frames at 540×960 → WebP → `public/hero/<chapter>/NNNN.webp` + manifest. `src/components/Story.astro` becomes chapter-aware (list of clips, text cues and card cues by scroll position).
- Frame extraction needs `ffmpeg` (`brew install ffmpeg`).
- The video is decoration: all text, links and groups are real HTML, so search engines and screen readers get everything.
- Generated media is marked as illustration in the footer ("Fotografije i video su ilustracije").

---

## 5. Where this stands (2026-11-14) — pick up here in a new session

- **Blocked on generation only.** The Higgsfield connector exposed just read tools (balance, models, history) in the old session. Darko is reconnecting it; he has a 3-day unlimited trial and wants generation done **through the connector, not through Chrome**.
- **First thing to do:** list the Higgsfield tools. If a generate tool exists: generate the key images (§3) at 9:16, then the clips with start image → end image, no audio, 5–8 s. Prefer a model marked unlimited (Seedance 2.0 / 2.5 in the catalog). Do one test clip (P1→P2) and show it to Darko before the rest.
- **Then build:** download clips to `blender/out/clips/` (not in git), extract frames with ffmpeg (`brew install ffmpeg` was started; check `ffmpeg -version`), convert with `scripts/frames.py`, make `src/components/Story.astro` chapter-aware (clips, headline cues, category cards per §1–2), keep the reduce-motion fallback.
- **Live now:** https://darkokostic95.github.io/biljina-kuhinja/ with the old flat-lay hero (backup tag `v1-simple`). Checking pages at phone width: `design/shots/shot.sh <path> <name> [height]` with `npx astro dev --port 4321` running.
- **Darko's preferences so far:** phone first; palette B; Bricolage Grotesque, no handwriting fonts; no checkboxes on ingredients; no photo file names anywhere; real-looking food, not cartoon; style of the croissant reel.
