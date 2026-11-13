import { allRecipes, sortFor } from '../../../lib/recipes';
import { CATEGORIES, type Lang } from '../../../lib/i18n';

export function getStaticPaths() {
  return (['sr', 'en'] as Lang[]).flatMap((lang) => CATEGORIES.map((c) => ({ params: { lang, category: c.id } })));
}
// Everything the book view needs for one group in one language.
export async function GET({ params }: { params: { lang: Lang; category: string } }) {
  const { lang, category } = params;
  const list = sortFor((await allRecipes()).filter((r) => r.category === category), lang).map((r) => ({
    s: r.slug,
    t: r.title[lang],
    i: r.ingredients.map((g) => ({ g: r.ingredients.length > 1 ? g.group[lang] : '', l: g[lang] })),
    p: r.steps[lang],
    n: r.notes?.[lang] ?? '',
  }));
  return new Response(JSON.stringify(list), { headers: { 'Content-Type': 'application/json' } });
}
