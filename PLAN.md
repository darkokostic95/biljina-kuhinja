# Biljina Kuhinja — build plan

A recipe website for Bilja's handwritten recipes. Serbian Latin by default, English as a second language, built for phones first, hosted free on GitHub Pages. You add recipes later by adding a file to the code. There is no database and no admin panel.

---

## 0. What we're starting from

- `recipies/` has **182 photos** (181 HEIC + 1 JPG, 656 MB), named IMG_5543 to IMG_5725.
- From the pages I sampled:
  - The notes are **handwritten, in both Cyrillic and Latin**, sometimes in block capitals and sometimes in cursive. Some are on grid notebook paper, some on loose slips taped into the notebook.
  - Many photos are **rotated** 90° or 180°.
  - **One page often holds 2–3 recipes**, and some recipes **continue onto the next photo**.
  - Some recipes name who they came from (e.g. "Anđelka", "Bilja").
  - Some are **numbered variants** ("Bakin kolač 1" / "Bakin kolač 2"). Those are variants, not duplicates.
  - Many are marked **posno** (Lenten/vegan).
  - So far it's mostly cakes, tortes and pastries.
- My rough guess is **200–350 recipes** before duplicates are removed. The real number comes out of Phase 1.

---

## Phase 1 — Transcribe and organize the recipes (before any website code)

This is the biggest and most important part. The result is plain text files you can read and check before anything is built.

### 1.1 Prepare the photos
- Convert HEIC to JPG with `sips` (it's built into macOS) into `work/pages/`. Originals stay untouched.
- Fix the rotation of every page so it reads upright.
- Find **duplicate shots** of the same page. I'll match them with an image-similarity hash and then compare the text. For each duplicate group I keep the sharpest photo.

### 1.2 Transcribe every page, word for word
- I read every photo and write `work/transcripts/IMG_xxxx.md` exactly as written: original alphabet, original spelling, crossed-out words marked.
- Anything I can't read is marked `[?nečitko?]` instead of guessed. All of those go into one list for you and Bilja to check.

### 1.3 Split into recipes and join recipes that run across pages
- Build `work/index.md`, a table of **photo → recipes on it**. It marks:
  - **Continued**: a recipe that ends mid-sentence or mid-list and picks up on the next photo. These get merged into one recipe.
  - **Duplicate**: the same recipe written down twice (same name, or nearly the same ingredients). I keep the most complete version and note the other photo as a second source.
  - **Variant**: the same name with different amounts. These stay as one recipe with "Varijanta 1 / 2", or as separate recipes if they're really different.

### 1.4 Write the clean recipes
Each recipe becomes one file, `src/content/recipes/<slug>.md`:

```yaml
slug: bakin-kolac
title: { sr: "Bakin kolač", en: "Grandma's Cake" }
category: kolaci                 # see 1.5
tags: [posno, brzo, bez-pecenja, cokolada, orasi]
aliases: { sr: [kolač od jogurta, kuglof], en: [yogurt cake, bundt cake] }   # used by search
servings: null                   # only if the page says
time: null                       # only if the page says
ingredients:
  - group: { sr: "Kora", en: "Base" }
    items:
      - { qty: "5", unit: "", sr: "jaja", en: "eggs" }
      - { qty: "2", unit: "čaše", sr: "jogurta", en: "cups of yogurt" }
steps:
  sr: ["Umutiti jaja sa šećerom…", "…"]
  en: ["Beat the eggs with the sugar…", "…"]
notes: { sr: "Električni kalup.", en: "Electric baking mould." }
sources: [IMG_5680]              # original photos, shown on the page as "Original zapis"
uncertain: []                    # anything still unclear
```

- Cyrillic is converted to **Latin**. Spelling is lightly cleaned up. Amounts and the method stay exactly as Bilja wrote them; nothing gets "improved".
- The English is translated by me. Measures like "šolja", "čaša" and "kocka kvasca" are kept with a short explanation ("cup (~200 ml)", "1 cube of fresh yeast (42 g)").

### 1.5 Groups (draft, to confirm once everything is transcribed)
| Serbian | English |
|---|---|
| Torte | Tortes & layer cakes |
| Kolači | Cakes & bars (šnite, kocke) |
| Sitni kolači | Cookies & small pastries |
| Posni kolači | Lenten / vegan desserts |
| Pite i peciva | Pies, pastries, kifle |
| Hleb i testa | Bread & doughs |
| Glavna jela | Main dishes |
| Supe i čorbe | Soups & stews |
| Salate i prilozi | Salads & sides |
| Zimnica | Preserves & pickles |
| Deserti u čaši / kremovi | Creams & no-bake desserts |

"Posno", "Bez pečenja", "Brzo" and "Praznično" are **tags**, not groups, so a Lenten torte still lives under Torte.

### 1.6 The tiramisu video
- Video: *"Kako napraviti Tiramisu za manje od 10 minuta"* by **Pekar Pekarica**, https://youtu.be/GQC9kjZxR4g
- Transcript: first I try the YouTube captions (`youtube-transcript-api` via pip). If there are none, I download the audio with `yt-dlp` and transcribe it locally with Whisper. That needs `brew install ffmpeg` first.
- From the transcript I write a normal recipe (ingredients + steps, sr + en) in our own words. The recipe page embeds the video and credits the channel. The raw transcript stays in `work/` only. We don't republish someone else's script word for word.
- File: `src/content/recipes/tiramisu.md` with `video: GQC9kjZxR4g`.

### Phase 1 deliverables (you review these before Phase 2)
- `work/index.md`: every photo → which recipes, with duplicates and continuations marked
- `src/content/recipes/*.md`: all clean recipes
- `work/REVIEW.md`: unreadable words and doubtful amounts, to go through with Bilja
- A summary with the number of recipes per group

---

## Phase 2 — Brand: logo and look

### Logo — final (Darko, 2026-11-13): S3a
- **B** = rolling pin with two loaves of bread; a **fork (up) and knife (down)** come out of the bread's "waist" and form the **K**. One connected mark, flat illustrated style with espresso outlines.
- Files in `public/brand/`: `mark.svg` (colour), `mark-flat.svg` (no outlines, for terracotta/dark), `favicon.svg` + `public/favicon.ico`, `logo-horizontal.svg` (+ `-light`), `logo-stacked.svg`, `icon-192/512.png`, `apple-touch-icon.png`, `icon-maskable-512.png`, `og-image.png` (1200×630 share image). Wordmark text is outlined to paths, so it renders the same everywhere.
- Explorations kept in `design/` (logo-concepts, palettes, fonts, monogram-*.html). Generator: `design/monogram-s3.html` (parts + `FK`).

### Visual direction: "Mamina sveska" (mom's notebook)
- Background textures taken from the real notebook: **grid paper** and cream paper with ink-blue handwriting accents. The site looks like her notebook brought to life.
- Palette **B · Seoska kuhinja** (Darko, 2026-11-13): linen `#F6EFE4`, espresso `#3B2A20`, terracotta `#C0643B`, honey `#E0A53C`, olive `#7A8450`, card paper `#FFFBF5`, soft tint `#EED9C4`.
- Fonts: **Bricolage Grotesque** for everything (Darko, 2026-11-13), no handwriting fonts. Google Fonts, Latin Extended (č ć š ž đ).
- Every recipe page has an **"Original zapis"** toggle that shows Bilja's handwritten page, compressed to WebP.

### Food pictures
We have no photos of the finished dishes, only the notebook pages. Options (your choice, see Open questions):
- **A (default):** one illustrated icon per group plus the handwriting scan. Honest and consistent.
- **B:** AI-generated food images, clearly decorative.
- **C:** you add real photos over time. The design leaves a slot for one per recipe.

---

## Phase 3 — Website

> **Superseded in detail by [`WEBSITE-PLAN.md`](WEBSITE-PLAN.md) (2026-11-13)**: "Biljin sto" photoreal Blender scroll story, tech stack, render pipeline. Where the two differ, WEBSITE-PLAN.md wins.

### Tech stack
- **Astro** (static site generator). Every recipe becomes its own real HTML page. That matters for sharing: Viber, WhatsApp and Facebook show a proper preview card with the recipe name and image.
- Recipes stay as Markdown/YAML files ("content collections"). To add a recipe later, you add one file and push.
- **Tailwind CSS** for styling, and **GSAP + ScrollTrigger** for the scroll animation.
- **GitHub Actions** builds and deploys to GitHub Pages on every push.
- No backend, no database, no tracking.

### Pages and URLs
| Page | Serbian | English |
|---|---|---|
| Home (animation + search) | `/` | `/en/` |
| All recipes / a group | `/recepti/`, `/recepti/torte/` | `/en/recipes/`, `/en/recipes/torte/` |
| One recipe | `/recept/bakin-kolac/` | `/en/recipe/bakin-kolac/` |
| Favorites (saved on the phone) | `/omiljeni/` | `/en/favorites/` |

- The language switch (SR | EN) keeps you on the same recipe.
- Pages carry `hreflang` tags, and `localStorage` remembers the chosen language.

### Smart search (the main feature)
Everything runs on the phone with no server. A small search index is built along with the site.
1. **Letter-insensitive matching**: "kolac", "kolač", "колач" and "kolach" all find *kolač*. Cyrillic is converted to Latin, accents are stripped, and ć/č→c, đ→dj, š→s, ž→z.
2. **Typo tolerance**: fuzzy matching with Fuse.js, so "tirmisu" finds *Tiramisu*.
3. **Synonyms and similar dishes**: a hand-made dictionary. For example: *keks / biskvit / kolačići / cookies*, *torta / kolač / cake*, *šnite / kocke / bars*, *posno / vegan / bez jaja*, *kifle / kiflice / rolls*. On top of that, each recipe has its own `aliases` written in Phase 1. So searching "cookies" in Serbian finds *sitni kolači*.
4. **Ingredient search**: "orasi čokolada" ranks recipes that use both. A "Šta imam u kući?" chip mode lets you tap ingredients you have.
5. **Both languages at once**: an English word typed on the Serbian site still finds the recipe.
6. **Never an empty screen**: if nothing matches, it shows "Možda tražite…" with the closest recipes and groups.
7. **UX**:
   - The search bar is the hero on the home page and a sticky search button on every page.
   - Results update instantly as you type (no Enter).
   - Category chips and Posno / Bez pečenja / Brzo filters sit right under the bar.
   - Recent searches are remembered on the phone.
- *Optional later:* a true "meaning" search with a small multilingual model loaded only when there are no results. It's about 30 MB, so it's not the default on mobile data.

### Recipe page (mobile)
- Title, group, tags and the generated food image.
- **Share button**: opens the phone's own share sheet (Viber, WhatsApp, SMS…). On desktop it falls back to copy-link plus WhatsApp/Viber links.
- **Ingredients you tick off** while cooking.
- **Numbered steps** in large text.
- **"Kuvam" mode**: keeps the screen from turning off (Wake Lock) and enlarges the text.
- ♥ Favorite (saved on the phone), print-friendly layout, and the "Original zapis" image.
- The tiramisu page also has the YouTube video. It uses a lightweight embed that only loads YouTube when tapped.
- Google Recipe structured data (schema.org), so the recipe can show up nicely in Google.

### "Čitaj kao knjigu" — book view (Darko, 2026-11-13)
- A second way to read the recipes: **as a real cookbook with page-turning**. A "Knjiga" button on the home page and on every group opens it.
- **Desktop/tablet:** an open book with two pages side by side. Drag a page corner or use the arrows/keyboard and the page curls and turns. **Phone:** one page at a time, swipe to turn, same page-curl animation.
- Book layout: cover with the logo → table of contents by group (tap a group to jump) → a divider page per group → one recipe per page (title, ingredients, steps in handwriting-style font on notebook paper). Long recipes continue on the next page.
- The book can be opened for one group only (e.g. only "Torte") or the whole collection. Each page has its own link (`/knjiga/torte#<recept>`), so a shared link opens the book at that recipe, and "Otvori recept" on a page goes to the normal recipe page.
- Pages are made only when you reach them (the 2 pages around the current one), so the 288-recipe book stays fast on phones.
- Built with **StPageFlip** (`page-flip`, MIT, ~40 KB, works with touch). Paper sound on turn is optional and off by default. With "reduce motion" on, pages slide instead of curling.

### Mobile-first details
- Designed at 375 px first, with thumb-reachable bottom navigation (Početna · Pretraga · Grupe · Omiljeni).
- Lighthouse target ≥ 90 on mobile. Images are WebP at several sizes and lazy-loaded.
- **Works offline (PWA)**: a recipe opened once still opens in the kitchen without signal. "Dodaj na početni ekran" puts the app icon on Bilja's phone.
- Respects "reduce motion": the animation becomes a still picture.

---

## Phase 4 — Home page scroll animation

> Replaced by `WEBSITE-PLAN.md` §2, §5, §6 (realistic Cycles render, not stylized clay).

### Concept: "Od sveske do tanjira" (from the notebook to the plate)
As you scroll:
1. Bilja's notebook lies open and the handwriting glows.
2. Ingredients **lift off the page**: eggs, flour, sugar, a block of butter, walnuts.
3. They fall into a **mixing bowl** and a whisk spins.
4. The batter pours into a pan, which slides into an **oven** that glows warm.
5. A finished **cake** comes out steaming, the chef's hat from the logo drops on top, and a slice is cut.
6. The scene settles behind the search bar: **"Šta danas kuvamo?"**

### How it's made
- **Blender** (installed on this Mac) with the Blender connector. The scene is built by script with simple, stylized clay/toon materials, which read better and are lighter than photoreal. It's rendered as an **image sequence** (about 120 frames, portrait 720×1280 for phones and landscape for desktop) and converted to WebP, about 3–4 MB in total.
- On the page the frames are drawn on a `<canvas>` and **scrubbed by scroll** with GSAP ScrollTrigger, the same technique Apple product pages use. Every 4th frame loads first, so it starts fast on mobile data.
- A lighter 2D layer in SVG/CSS covers the hand-drawn bits (steam, sparkles, the notebook doodles).
- **About Fable 5.2:** Fable is a Claude model. It can write and run the Blender scripts and the animation code, but it can't produce video files by itself. If we want an AI-generated video clip instead of Blender, we'd use a video-generation tool (e.g. the Weave models available through the Figma connector) and scrub that video. Blender is my recommendation: we control every frame, it loops cleanly, it matches the logo, and there are no licensing questions.
- **Fallback:** if the Blender render doesn't look good enough, the same story is done fully in 2D SVG + GSAP.

---

## Phase 5 — Publishing

- Repo **`biljina-kuhinja`** on your GitHub. The address would be **https://darkokostic95.github.io/biljina-kuhinja/** (no domain purchase).
- **The original 656 MB of photos are not committed.** Only the compressed WebP versions used by "Original zapis" go in (about 25 MB). The `recipies/` and `work/` folders are kept out by `.gitignore`.
- A GitHub Actions workflow builds and deploys on every push to `main`.
- `HOW-TO-ADD-A-RECIPE.md`: copy a template file, fill it in, drop the photo in `public/originals/`, push. Search, groups and the sitemap update automatically.

---

## Folder layout

```
portfolio/bilja-cooking/
├── PLAN.md
├── recipies/              # original phone photos (not in git)
├── work/                  # pages, transcripts, index, REVIEW.md (not in git)
├── blender/               # .blend file + render script
├── src/
│   ├── content/recipes/   # one .md per recipe  ← the data
│   ├── i18n/              # sr.json, en.json (interface text)
│   ├── lib/search/        # normalize.ts, synonyms.ts, search.ts
│   ├── components/        # SearchBar, RecipeCard, ShareButton, ScrollStory…
│   └── pages/             # routes for sr + en
├── public/
│   ├── originals/         # compressed handwriting scans (WebP)
│   ├── story/             # animation frames
│   └── logo/, icons/
└── .github/workflows/deploy.yml
```

---

## Order of work and check-ins

| # | Step | You check |
|---|---|---|
| 1 | Convert, rotate and de-duplicate the photos; transcribe every page | — |
| 2 | Index, merges and clean recipe files; REVIEW list | **Recipe list + groups + doubtful spots** |
| 3 | Tiramisu transcript → recipe | together with step 2 |
| 4 | 3 logo concepts | **Pick one** |
| 5 | Site skeleton: design, recipe pages, sr/en, share | **Preview on your phone** |
| 6 | Smart search + filters + favorites + offline | Try searching |
| 7 | Blender scene → frames → scroll animation | **Animation preview** |
| 8 | SEO, link previews, performance pass, GitHub Pages deploy | **Final OK before it goes public** |

## Status (2026-11-13)
- **Phase 1 done.** All 182 photos are transcribed and checked by Darko. There are 288 recipes in `src/content/recipes/`: 57 torte, 28 kolači, 60 bez pečenja, 18 sitni kolači, 19 pite, 36 peciva, 24 glavna jela, 24 salate i predjela, 12 zimnica, 6 kremovi i sladoledi, 4 napici. 43 are tagged posno.
- The tiramisu video has no speech, only music. The recipe was read from the on-screen captions and the ingredient card at the end, and is credited to Pekar Pekarica.
- Recipe source of truth from now on: `src/content/recipes/*.md` (one file per recipe; add new ones by copying an existing file). `work/batches/` + `scripts/build_recipes.py` were only used for the first conversion.
- **Next: Phase 2 (logo) and Phase 3 (website).**

## Decisions (Darko, 2026-11-11)
1. **Food pictures**: generated images (option B), one per recipe. No real photos will be added later.
2. **Names** like "Anđelka": not shown anywhere on the site. The `from` field is dropped.
3. **Repo/URL**: `darkokostic95.github.io/biljina-kuhinja/` is fine. The git repo lives in `portfolio/bilja-cooking/`.
4. **No "O Bilji" page.**
