import { getCollection } from 'astro:content';
import type { Lang } from './i18n';

export interface Recipe {
  slug: string;
  title: { sr: string; en: string };
  category: string;
  tags: string[];
  aliases?: { sr?: string[]; en?: string[] };
  ingredients: { group: { sr: string; en: string }; sr: string[]; en: string[] }[];
  steps: { sr: string[]; en: string[] };
  notes?: { sr: string; en: string } | null;
  video?: string;
  video_credit?: string;
}

let cache: Recipe[] | null = null;
export async function allRecipes(): Promise<Recipe[]> {
  if (cache) return cache;
  const entries = await getCollection('recipes');
  cache = entries
    .map((e) => ({ ...(e.data as any), slug: (e.data as any).slug ?? e.id }) as Recipe)
    .sort((a, b) => a.title.sr.localeCompare(b.title.sr, 'sr'));
  return cache;
}
export const sortFor = (list: Recipe[], lang: Lang) =>
  [...list].sort((a, b) => a.title[lang].localeCompare(b.title[lang], lang));

export function similar(r: Recipe, all: Recipe[], n = 4): Recipe[] {
  return all
    .filter((o) => o.slug !== r.slug)
    .map((o) => ({ o, s: (o.category === r.category ? 2 : 0) + o.tags.filter((x) => r.tags.includes(x)).length }))
    .filter((x) => x.s > 1)
    .sort((a, b) => b.s - a.s || a.o.slug.localeCompare(b.o.slug))
    .slice(0, n)
    .map((x) => x.o);
}
