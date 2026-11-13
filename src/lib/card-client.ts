import { CATEGORIES, TAGS, url, type Lang } from './i18n';
import { icon } from './icons';
import type { Row } from './search-client';

const esc = (s: string) => s.replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' })[c]!);

export function cardHTML(r: Row, lang: Lang): string {
  const c = CATEGORIES.find((x) => x.id === r.c)!;
  const tags = r.g.filter((g) => g === 'posno' || g === 'brzo' || g === 'video').slice(0, 2)
    .map((g) => `<span class="tag t-${g}">${esc(TAGS[g]?.[lang] ?? g)}</span>`).join('');
  return `<a class="card" href="${url(lang, 'recipe', r.s)}">
    <span class="thumb" style="background:${c.tint}">${c.icon}</span>
    <span class="body"><span class="ttl">${esc(lang === 'en' ? r.te : r.ts)}</span>
    <span class="meta"><span>${esc(c[lang])}</span>${tags}</span></span>${icon('chev', 'chev')}</a>`;
}
