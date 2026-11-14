import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const bi = z.object({ sr: z.string(), en: z.string() });
const biList = z.object({ sr: z.array(z.string()), en: z.array(z.string()) });

const recipes = defineCollection({
  loader: glob({ pattern: '*.md', base: './src/content/recipes' }),
  schema: z.object({
    slug: z.string(),
    title: bi,
    category: z.string(),
    tags: z.array(z.string()).default([]),
    aliases: biList.partial().optional(),
    ingredients: z.array(z.object({ group: bi, sr: z.array(z.string()), en: z.array(z.string()) })),
    steps: biList,
    notes: bi.nullish(),
    video: z.string().optional(),
    video_credit: z.string().optional(),
  }),
});

export const collections = { recipes };
