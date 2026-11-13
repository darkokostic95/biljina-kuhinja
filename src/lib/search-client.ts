import { norm } from './normalize';

export interface Row { s: string; ts: string; te: string; c: string; g: string[]; v: number; t: string[]; a: string[]; k: string[]; i: string[] }

const BASE = import.meta.env.BASE_URL.replace(/\/$/, '');
let rows: Promise<Row[]> | null = null;
export function loadIndex(): Promise<Row[]> {
  rows ??= fetch(`${BASE}/search-index.json`).then((r) => r.json());
  return rows;
}

// Words that mean the same thing (already normalized: no accents, latin).
const SYN: string[][] = [
  ['keks', 'keksi', 'biskvit', 'kolacici', 'cookie', 'cookies', 'biscuit', 'biscuits'],
  ['torta', 'torte', 'tortu', 'cake', 'cakes'],
  ['kolac', 'kolaci', 'kolace', 'slatkis', 'slatkisi', 'slatko', 'dessert', 'desert', 'sweet', 'sweets'],
  ['posno', 'posna', 'posni', 'posne', 'vegan', 'veganski', 'vegansko', 'lenten', 'fasting'],
  ['kifle', 'kiflice', 'kifla', 'rolls', 'crescent'],
  ['piletina', 'pile', 'pilece', 'pileci', 'chicken'],
  ['meso', 'meat', 'svinjetina', 'junetina', 'pork', 'beef', 'mleveno'],
  ['sir', 'sirom', 'sira', 'cheese'],
  ['orasi', 'orah', 'oraha', 'orasima', 'walnut', 'walnuts', 'nuts'],
  ['cokolada', 'cokolade', 'cokoladna', 'cokoladni', 'cokoladne', 'cokoladom', 'chocolate', 'coko'],
  ['hleb', 'hleba', 'bread', 'pogaca', 'lepinja', 'lepinje'],
  ['pita', 'pite', 'pitu', 'pie', 'pies', 'gibanica', 'burek'],
  ['zimnica', 'zimnicu', 'tursija', 'preserves', 'pickles', 'pickled'],
  ['sladoled', 'icecream', 'ice', 'gelato'],
  ['brzo', 'brza', 'brzi', 'brze', 'quick', 'fast', 'easy', 'lako', 'lagano'],
  ['jabuka', 'jabuke', 'jabukama', 'apple', 'apples'],
  ['jagoda', 'jagode', 'jagodama', 'strawberry', 'strawberries'],
  ['kokos', 'kokosom', 'coconut'],
  ['lesnik', 'lesnici', 'lesnika', 'hazelnut', 'hazelnuts'],
  ['banana', 'banane', 'bananama', 'bananas'],
  ['med', 'medom', 'medeni', 'medena', 'medenjaci', 'honey'],
  ['salata', 'salate', 'salatu', 'salad', 'salads'],
  ['supa', 'corba', 'soup', 'stew'],
  ['krompir', 'krompira', 'potato', 'potatoes'],
  ['paprika', 'paprike', 'paprika', 'pepper', 'peppers'],
  ['napitak', 'napici', 'pice', 'drink', 'drinks', 'sok', 'liker', 'liqueur', 'juice'],
  ['krem', 'krema', 'fil', 'cream', 'filling', 'custard'],
  ['oblanda', 'oblande', 'oblandi', 'wafer', 'wafers'],
  ['predjelo', 'predjela', 'starter', 'starters', 'appetizer', 'meze'],
  ['rucak', 'vecera', 'glavno', 'main', 'dinner', 'lunch'],
  ['kvasac', 'kvasca', 'yeast'],
  ['mak', 'makom', 'poppy'],
  ['susam', 'susamom', 'sesame'],
  ['visnje', 'visnja', 'visnjama', 'cherry', 'cherries'],
  ['kafa', 'kafe', 'neskafa', 'coffee'],
  ['slag', 'pavlaka', 'whipped'],
  ['bezjaja', 'eggless'],
  ['tiramisu', 'tiramizu'],
];
const synOf = new Map<string, string[]>();
for (const g of SYN) for (const w of g) synOf.set(w, g);

function editWithin(a: string, b: string, max: number): boolean {
  if (Math.abs(a.length - b.length) > max) return false;
  let prev = Array.from({ length: b.length + 1 }, (_, i) => i);
  for (let i = 1; i <= a.length; i++) {
    const cur = [i];
    let best = i;
    for (let j = 1; j <= b.length; j++) {
      const v = Math.min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (a[i - 1] === b[j - 1] ? 0 : 1));
      cur.push(v);
      if (v < best) best = v;
    }
    if (best > max) return false;
    prev = cur;
  }
  return prev[b.length] <= max;
}

// How well one query token matches one indexed word: 0..1
function wordScore(q: string, w: string): number {
  if (q === w) return 1;
  if (w.startsWith(q)) return q.length >= 3 ? 0.85 : 0.5;
  if (q.length >= 4 && w.includes(q)) return 0.6;
  // Serbian case endings: same stem, different ending (orasi / oraha, cokolada / cokolade)
  const min = Math.min(q.length, w.length);
  if (min >= 4) {
    let p = 0;
    while (p < min && q[p] === w[p]) p++;
    if (p >= Math.max(4, min - 2) && Math.abs(q.length - w.length) <= 3) return 0.7;
  }
  if (q.length >= 4 && editWithin(q, w, q.length >= 7 ? 2 : 1)) return 0.5;
  return 0;
}
function bestIn(q: string, list: string[]): number {
  let b = 0;
  for (const w of list) {
    const s = wordScore(q, w);
    if (s > b) { b = s; if (b === 1) break; }
  }
  return b;
}
function tokenScore(tok: string, r: Row): number {
  const variants = synOf.get(tok) ?? [tok];
  let best = 0;
  for (const v of variants) {
    const own = v === tok ? 1 : 0.9;
    const s = Math.max(bestIn(v, r.t) * 10, bestIn(v, r.a) * 8, bestIn(v, r.k) * 6, bestIn(v, r.i) * 3) * own;
    if (s > best) best = s;
  }
  return best;
}

export interface Hit { row: Row; score: number }
export interface Result { hits: Hit[]; exact: boolean }

export function search(all: Row[], query: string, limit = 40): Result {
  const toks = norm(query).split(' ').filter(Boolean);
  if (!toks.length) return { hits: [], exact: true };
  const scored = all.map((row) => {
    const per = toks.map((tk) => tokenScore(tk, row));
    return { row, per, score: per.reduce((a, b) => a + b, 0) };
  });
  // every word must match somewhere
  let hits = scored.filter((x) => x.per.every((p) => p > 0));
  let exact = true;
  if (!hits.length) {
    exact = false;
    hits = scored.filter((x) => x.score > 0); // any word
  }
  hits.sort((a, b) => b.score - a.score || a.row.ts.localeCompare(b.row.ts));
  return { hits: hits.slice(0, limit).map(({ row, score }) => ({ row, score })), exact };
}

// ---- favorites (kept on this phone only) ----
const KEY = 'bk:favs';
export function favs(): string[] {
  try { return JSON.parse(localStorage.getItem(KEY) || '[]'); } catch { return []; }
}
export function toggleFav(slug: string): boolean {
  const f = favs();
  const i = f.indexOf(slug);
  if (i >= 0) f.splice(i, 1); else f.unshift(slug);
  try { localStorage.setItem(KEY, JSON.stringify(f)); } catch {}
  return i < 0;
}
