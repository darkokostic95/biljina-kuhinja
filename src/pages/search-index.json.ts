import { allRecipes } from '../lib/recipes';
import { words } from '../lib/normalize';
import { CATEGORIES, TAGS } from '../lib/i18n';

// Small search index: one row per recipe, words already normalized.
export async function GET() {
  const rows = (await allRecipes()).map((r) => {
    const cat = CATEGORIES.find((c) => c.id === r.category)!;
    const uniq = (a: string[]) => [...new Set(a)];
    return {
      s: r.slug,
      ts: r.title.sr,
      te: r.title.en,
      c: r.category,
      g: r.tags,
      v: r.video ? 1 : 0,
      t: uniq(words(r.title.sr + ' ' + r.title.en)),
      a: uniq(words([...(r.aliases?.sr ?? []), ...(r.aliases?.en ?? [])].join(' '))),
      k: uniq(words([cat.sr, cat.en, ...r.tags.flatMap((x) => [TAGS[x]?.sr ?? x, TAGS[x]?.en ?? ''])].join(' '))),
      i: uniq(words(r.ingredients.flatMap((g) => [...g.sr, ...g.en]).join(' '))),
    };
  });
  return new Response(JSON.stringify(rows), { headers: { 'Content-Type': 'application/json' } });
}
