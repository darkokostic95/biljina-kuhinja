# Biljina Kuhinja — website plan (design + technical)

Status: **draft for Darko's approval** (2026-11-13). Replaces Phase 3–4 of `PLAN.md` where they differ.
Fixed decisions so far: palette B "Seoska kuhinja", font Bricolage Grotesque (no handwriting fonts), logo S3a (rolling pin + bread = B, fork + knife = K), Serbian Latin default + English, GitHub Pages, no database, 288 recipes in `src/content/recipes/`.

---

## 1. The idea in one sentence

**"Biljin sto" (Bilja's table):** the home page is one long, real-looking wooden kitchen table seen from above. As you scroll, the camera glides along the table and real objects move: flour falls, bread is cut, a cake gets dusted with cocoa. At every stop, the website itself (search, groups, the book) appears over the scene. At the very start, the logo is lying on the table made of real objects.

Why top-down ("flat lay"):
- It is the classic look of food photography and cookbooks, so it reads as **real, not cartoon**.
- Scrolling down = moving along the table. The motion matches your thumb, so it feels natural on a phone.
- It is the cheapest kind of photoreal scene to render (no walls, no room, short depth), which matters on this Mac (see §6).
- The same scene works for phone (tall frame) and desktop (wide frame).

---

## 2. Scroll story (storyboard)

The home page is ~7 "stations". Each one has a short animation driven by scroll, then text and buttons over it. The HTML overlay is always real text (searchable, translatable, accessible), never baked into the images.

| # | Scroll | What you see (Blender) | What appears over it (HTML) |
|---|---|---|---|
| 0 | 0–8 % | **The logo on the table.** A real rolling pin and two real loaves lie as the "B"; a real fork and knife come out of the bread as the "K". Linen cloth, a little flour dust, soft morning window light. | "Biljina Kuhinja", subtitle "Domaći recepti iz maminih svezaka", the **search bar** ("Šta danas kuvamo?"). |
| 1 | 8–22 % | The objects come alive: the rolling pin rolls away, the fork and knife slide aside, the loaves are pushed off. Under them lies **Bilja's open notebook** (textured with her real handwritten pages). A page turns. | "288 recepata, prepisanih iz sveske" + button **"Čitaj kao knjigu"** (book view). |
| 2 | 22–40 % | **Torte i kolači.** A sieve lets flour fall in a soft cloud onto eggs, sugar, butter and walnuts. The camera moves on to a finished layered cake; cocoa is dusted over it and one slice slides out. | Group chips: Torte · Kolači · Bez pečenja · Sitni kolači, with recipe counts. |
| 3 | 40–55 % | **Peciva i pite.** A dough sheet is rolled thinner by the rolling pin; next to it kiflice and a pita on a baking tray, steam rising. | Chips: Peciva · Pite. 3 example recipes as cards. |
| 4 | 55–70 % | **Slano.** A pot with a lid that lifts, steam; a cutting board with peppers, onion and a knife; a bowl of salad. | Chips: Glavna jela · Salate i predjela. |
| 5 | 70–85 % | **Zimnica i napici.** Jars of ajvar, pickles and jam, one lid twists open; a glass of homemade liqueur. | Chips: Zimnica · Kremovi · Napici. |
| 6 | 85–100 % | **Tiramisu.** The camera ends over a tiramisu; a spoon takes the first bite. The scene settles and slightly blurs. | "Šta danas kuvamo?" search again + **"Iznenadi me"** (random recipe) + link to the tiramisu video recipe. Then the normal page continues: newest/favorite recipes grid, footer. |

Rules so the animation never blocks the site:
- The **search is always one tap away** (sticky top bar, appears after the hero).
- A small **"Preskoči animaciju"** link jumps to the recipe groups.
- **Reduce motion** (phone setting), **Save-Data** or a very slow connection → the 7 stations become 7 still photos with the same text, no scrubbing.
- Total scroll length on phone: about 7–8 screen heights. Not longer, or it gets tiring.

---

## 3. Visual design of the whole site

- **Look:** "kitchen table, morning light". Linen background `#F6EFE4`, cards are like paper/cloth laid on the table `#FFFBF5`, espresso text `#3B2A20`, terracotta actions `#C0643B`, honey highlights `#E0A53C`, olive for "posno" `#7A8450`.
- **Type:** Bricolage Grotesque for everything; big, tight headlines (800), comfortable body text (17–18 px on phone, 1.55 line height).
- **Photos:** every food image on the site is in the same flat-lay style, same table, same light, so the site feels like one photo shoot (see §7).
- **Header:** logo-horizontal on the left, SR | EN, search icon. On phone the bottom bar: Početna · Pretraga · Grupe · Knjiga · Omiljeni.
- **Recipe page:** top photo (flat lay of the dish) → title, group, tags → buttons Podeli / ♥ / Kuvam / Original zapis → ingredients with tick-boxes → numbered steps → notes → "Slični recepti". Kuvam mode keeps the screen on and enlarges text.
- **Group page:** header photo of that group's table station (reused from the home animation), filter chips, recipe cards (photo, title, small tags).
- **Book view ("Čitaj kao knjigu"):** paper pages with page-curl turning (StPageFlip), printed in Bricolage (no handwriting font), cover = logo on linen.
- **Motion besides the hero:** small and quick only (cards fade up, chips pop), 150–250 ms.

---

## 4. Website — technical solution

| Part | Choice | Why |
|---|---|---|
| Framework | **Astro 5** (static), TypeScript | Every recipe is a real HTML page → good sharing previews and Google; tiny JS. |
| Styling | **Tailwind CSS 4** with the palette as CSS variables | Fast to build, consistent. |
| Scroll animation | **GSAP 3 + ScrollTrigger**, **Lenis** smooth scroll | Industry standard for scroll-scrubbed sequences; free for this use. |
| Frames on screen | `<canvas>`; images decoded with `createImageBitmap` off the main thread | Smooth on phones. |
| Search | **Fuse.js** + own normalizer (Cyrillic→Latin, č/ć/š/ž/đ folding) + synonyms + aliases | Runs on the phone, no server. |
| Book view | **StPageFlip** (`page-flip`, MIT) | Real page curl, touch support. |
| i18n | Astro i18n routing: `/` (sr), `/en/` | Same slug in both languages, `hreflang`. |
| Offline | **PWA** (Workbox via `@vite-pwa/astro`) | Recipes open in the kitchen without signal; app icon on the phone. |
| SEO | schema.org `Recipe` JSON-LD, sitemap, OG image per recipe | Shows nicely in Google and Viber/WhatsApp. |
| Hosting | GitHub Pages + GitHub Actions | Free, deploy on push. |

### Frame-sequence engine (the hero)
- Two render sets of the same Blender scene:
  - **Phone:** 1080×1920 portrait (camera sees a narrow strip of the table).
  - **Desktop:** 1920×1080 landscape (same path, wider view).
- **Frames:** about **40 per station × 7 ≈ 280 frames** per set. Scroll scrubbing does not need video frame rates; between two frames the canvas cross-fades, so it still looks smooth.
- **Format:** AVIF (quality ~45) with WebP fallback; target **≤ 60 KB per frame** → ~15 MB per set, loaded in pieces:
  1. Station 0 frames + every 8th frame of everything (~2 MB) → page usable immediately.
  2. The rest loads by station, just ahead of where you are scrolling.
  3. Phones only ever download the phone set; desktops only the desktop set.
- Loop-free: the sequence ends on a still that also serves as the background of the search section.

### Performance targets
- Lighthouse mobile ≥ 90 on recipe pages; home page LCP < 2.5 s (the first frame is a normal `<img>` with `fetchpriority=high`).
- Home page JS ≤ 60 KB gzipped (GSAP + Lenis + engine). Recipe pages ≤ 25 KB.

---

## 5. Blender pipeline (realistic, not cartoon)

**Software:** Blender 4.5 LTS (installed), rendered with **Cycles** (path tracing = photoreal light), AgX color, OpenImageDenoise. Scenes are built and changed by Python scripts (versioned in `blender/`), so every change is repeatable.

**How Fable 5.2 works on it:** Fable is a Claude model. It writes and runs the Blender scripts through the **Blender connector** (run code in Blender, take viewport screenshots, render previews), looks at the result, and adjusts. It can't render faster than Blender itself; long renders run in the background on this Mac (or a render farm, §6).

**Where realism comes from:**
- **Light:** a real HDRI of a kitchen/window (Poly Haven, CC0) + one soft area light as "window". Shallow depth of field.
- **Materials:** scanned PBR textures (Poly Haven / ambientCG, CC0): oak table, linen cloth, steel, ceramic, glass. Bread and cake get subsurface scattering and displacement (crumb, crust), flour is a particle layer.
- **Models:**
  - Simple shapes we model ourselves accurately: rolling pin, fork, knife, bowls, jars, pot, notebook, eggs, cake layers, dough sheet.
  - Organic food that is hard to model (bread loaf, walnuts, peppers, onion): CC0 photo-scans where available (Poly Haven, ambientCG, Smithsonian 3D open access). If a good CC0 scan doesn't exist, model + sculpt + photo texture, or leave that item out.
  - No assets with unclear licences. Every asset and its licence goes in `blender/ASSETS.md`.
- **Her notebook:** the open notebook in station 1 uses her real page photos as texture (only pages without personal data; never IMG_5688).
- **Effects:** flour cloud = particles, cocoa dust = particles, steam = volume (rendered once as a separate layer and reused), page turn = cloth / shape keys, objects rolling and sliding = keyframes (no heavy fluid sims).

**Workflow with check-ins:**
1. **Gray-box animatic:** whole story in simple shapes, EEVEE, low resolution, wired into the website. → You approve timing and story on your phone.
2. **Look development:** station 0 (the logo on the table) rendered photoreal as one still. → You approve the realism level.
3. **Build out stations 1–6** as stills first, then animation.
4. **Final render** of both sets, conversion to AVIF/WebP, wiring into the site.

---

## 6. Rendering on this Mac — the honest numbers

This Mac: Intel i5-8259U (4 cores), 8 GB RAM, Intel Iris Plus 655. **Cycles can't use this GPU on macOS**, so it renders on the CPU.

- Estimate for one photoreal frame (1080×1920, ~64 samples + denoise): **~2–5 min**.
- 280 frames × 2 sets ≈ 560 frames → **~20–45 hours** of rendering. That's 2–4 nights, running in the background, resumable (it can stop and continue).
- 8 GB RAM limits the scene: textures at 2K, few scans at a time, particles kept modest.

Ways to make it faster (we can mix them):
1. **Render once, crop twice:** render 1440×1920 frames that serve both phone and desktop via a wider camera (desktop sees the middle band). Saves ~40 %, but desktop gets a bit less detail.
2. **Static parts as one still:** the table and things that don't move are rendered once; only moving objects are rendered per frame and composited. Big saving, more setup.
3. **SheepIt** free community render farm: free, uses volunteers' computers, a few hours per job; the .blend file gets uploaded there.
4. **Paid render farm** (e.g. GarageFarm, RebusFarm): roughly $10–40 for this amount, done in an hour. Needs your OK and payment by you.

My suggestion: start locally (1 + 2). Use a farm only if the nights become a problem.

---

## 7. Food photos for recipe pages

The earlier decision was "generated food pictures, none added later". Options:
- **A — Blender stations:** each group gets its photo from the home-page animation (11 images). Every recipe in the group shows its group photo. Cheap and perfectly consistent, but not dish-specific.
- **B — AI image per recipe:** a photoreal flat-lay image for each of the 288 recipes, generated with an image model (e.g. via the Weave models in the Figma connector), with a fixed prompt style (same oak table, linen, window light, top-down) so they match the Blender scene. Labeled "ilustracija" in small text. Needs a check of credits/cost first, and I review every image for wrong food.
- **C — mix:** AI images for the ~60 most-viewed/most-typical recipes, group photo for the rest.

My suggestion: **C**, then fill in the rest over time.

---

## 8. Build order and check-ins

| Step | What | You check |
|---|---|---|
| 0 | Tools: `brew install ffmpeg`, `npm` deps, confirm the Blender connector talks to Blender; collect CC0 assets (list shown to you before download) | asset list |
| 1 | Site without animation: layout, recipe pages, groups, search, SR/EN, share, favorites, PWA, deploy to GitHub Pages | live link on your phone |
| 2 | Book view | on phone + desktop |
| 3 | Gray-box animatic wired into the home page | story + timing |
| 4 | Look-dev still of station 0 | realism |
| 5 | Stations 1–6 stills, then animation | each station |
| 6 | Final render (local nights / farm), AVIF/WebP, lazy loading, reduced-motion stills | home page on a real phone over mobile data |
| 7 | Food photos (option from §7) | images |
| 8 | Polish, Lighthouse, schema.org, OG images, `HOW-TO-ADD-A-RECIPE.md` | final OK, then publish |

Step 1 is useful on its own: the site works and can be shared before the animation is done.

---

## 9. Risks

- **Photoreal food is the hardest thing in 3D.** Bread, cake and flour can look great; things like walnuts or onion may look "CG". Mitigation: look-dev check at step 4, use scans, cut items that don't convince.
- **Render time on this Mac** (§6). Mitigation: fewer frames, render-once-crop-twice, static plate, farm as backup.
- **Page weight on mobile data.** Mitigation: phone set only, staged loading, still-image fallback.
- **iOS Safari quirks with scroll and canvas.** Mitigation: Lenis + ScrollTrigger tested on a real iPhone early (step 3).
- **Licences.** Only CC0 or clearly licensed assets, all listed in `blender/ASSETS.md`.

---

## 10. Open questions for Darko

1. **Story:** OK with "Biljin sto" (top-down table, 7 stations as above)? Anything to add or remove (e.g. a specific dish she is known for)?
2. **Her notebook in the animation:** OK to show her real handwritten pages (only pages without names/phone numbers)?
3. **Rendering:** local nights first, and a farm only if needed? SheepIt (free, file uploaded to volunteers) OK, or paid farm only with your OK?
4. **Food photos:** option A, B or C (§7)?
5. **Sound:** none (my suggestion), or an optional quiet kitchen sound with a mute button?

---

## 11. Build log

**2026-11-13 (evening)** — Darko: "do it", phone use comes first.
- **Site built (step 1 + 2):** Astro 7, plain CSS with palette B, Bricolage Grotesque (self-hosted). 608 pages: home, groups, 11 group pages, 288 recipe pages, search, favorites, book, each in SR and EN. Own search engine in `src/lib/search-client.ts` (Cyrillic/accents folding, typos, Serbian word endings, synonyms, ingredients; replaces Fuse.js). Book view with page-flip (`page-flip`), one page on phones, two on desktop, deep link `/knjiga/?g=torte#slug`. Share, ♥ favorites, "Kuvam" (screen stays on), tick-off ingredients, lite YouTube embed, schema.org Recipe, manifest + `public/sw.js` (offline), `.github/workflows/deploy.yml`, `HOW-TO-ADD-A-RECIPE.md`.
- **Not Tailwind / GSAP / Lenis:** plain CSS and a small own scroll engine (`src/components/Story.astro`) turned out simpler and lighter. `gsap` and `lenis` are installed but unused; remove if they stay unused.
- **Blender (step 3–4 started):** `blender/scene.py` builds the table scene fully procedurally (no downloads yet): oak table, linen cloth, rolling pin, two loaves, fork, knife, flour. `blender/anim_hero.py` renders station 0→1 (objects roll/slide away), resumable. `scripts/frames.py` converts PNG → WebP + `public/hero/m/manifest.json`. The home page switches to the scroll story automatically when that manifest exists.
- **Measured on this Mac:** 540×960, 32 samples: ~20–40 s per frame (CPU). Full 1080×1920 would be ~4× that.
- **Known gaps:** bread and cutlery are still "draft" realism (procedural); scanned CC0 assets + HDRI would lift it (needs Darko's OK to download). Stations 2–6, the notebook, desktop (landscape) frames, per-recipe photos and "Original zapis" scans are not done. Emoji are placeholders for food photos.
- **Checking pages:** `design/shots/shot.sh <path> <name> [height]` screenshots a page at phone width (dev server on :4321).
