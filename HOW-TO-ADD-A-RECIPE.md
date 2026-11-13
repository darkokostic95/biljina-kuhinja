# How to add a recipe

1. Copy any file in `src/content/recipes/` (for example `vanilice.md`) and rename it. The file name is the link: `moj-kolac.md` becomes `/recept/moj-kolac/`. Use only small letters, numbers and dashes (no č, ć, š, ž, đ in the file name).
2. Change the contents:
   - `slug`: the same as the file name, without `.md`.
   - `title`: the name in Serbian (`sr`) and English (`en`).
   - `category`: one of `torte`, `kolaci`, `bez-pecenja`, `sitni-kolaci`, `pite`, `peciva`, `glavna-jela`, `salate-predjela`, `zimnica`, `kremovi-sladoledi`, `napici`.
   - `tags`: any of `posno`, `brzo`, `bez-pecenja`, `cokolada`, `orasi`, `keks`, `plazma`, `voce`, `kokos`, `jabuke`, `kvasac`, `praznicno`, `sir`, `meso`, `piletina`, `povrce`, `lesnik`, `kikiriki`, `banane`, `jagode`, `med`, `mak`, `susam`, `oblanda`.
   - `ingredients`: one or more groups. Each group has a name (`group`) and the same number of lines in `sr` and `en`.
   - `steps`: the same number of steps in `sr` and `en`.
   - `notes` and `aliases` (other names people might search for) are optional.
3. Check it on your computer: `npm run dev`, then open http://localhost:4321/biljina-kuhinja/
4. Commit and push to `main`. GitHub builds and publishes the site in about a minute. Search, groups, the book view and the sitemap update on their own.

The search finds recipes by title, other names (`aliases`), group, tags and ingredient words, in both languages.
