export type Lang = 'sr' | 'en';
export const LANGS: Lang[] = ['sr', 'en'];

const BASE = import.meta.env.BASE_URL.replace(/\/$/, '');

export const CATEGORIES: { id: string; sr: string; en: string; icon: string; tint: string }[] = [
  { id: 'torte', sr: 'Torte', en: 'Cakes', icon: '🎂', tint: '#F3D9C8' },
  { id: 'kolaci', sr: 'Kolači', en: 'Bakes & bars', icon: '🍰', tint: '#F6E3BC' },
  { id: 'bez-pecenja', sr: 'Bez pečenja', en: 'No-bake', icon: '🍫', tint: '#E9D5C3' },
  { id: 'sitni-kolaci', sr: 'Sitni kolači', en: 'Cookies', icon: '🍪', tint: '#F4DFB5' },
  { id: 'pite', sr: 'Pite', en: 'Pies', icon: '🥧', tint: '#F1D7B4' },
  { id: 'peciva', sr: 'Peciva', en: 'Breads & pastries', icon: '🥐', tint: '#F5DDAF' },
  { id: 'glavna-jela', sr: 'Glavna jela', en: 'Main dishes', icon: '🍲', tint: '#EBCDB9' },
  { id: 'salate-predjela', sr: 'Salate i predjela', en: 'Salads & starters', icon: '🥗', tint: '#DDE3C4' },
  { id: 'zimnica', sr: 'Zimnica', en: 'Preserves', icon: '🫙', tint: '#EFC9B4' },
  { id: 'kremovi-sladoledi', sr: 'Kremovi i sladoledi', en: 'Creams & ice cream', icon: '🍨', tint: '#F3E6D2' },
  { id: 'napici', sr: 'Napici', en: 'Drinks', icon: '🥤', tint: '#E6DCC6' },
];
export const catById = (id: string) => CATEGORIES.find((c) => c.id === id)!;

export const TAGS: Record<string, { sr: string; en: string }> = {
  posno: { sr: 'posno', en: 'lenten (vegan)' },
  'bez-pecenja': { sr: 'bez pečenja', en: 'no-bake' },
  cokolada: { sr: 'čokolada', en: 'chocolate' },
  orasi: { sr: 'orasi', en: 'walnuts' },
  keks: { sr: 'keks', en: 'biscuits' },
  plazma: { sr: 'plazma', en: 'Plazma biscuits' },
  voce: { sr: 'voće', en: 'fruit' },
  kokos: { sr: 'kokos', en: 'coconut' },
  jabuke: { sr: 'jabuke', en: 'apples' },
  kvasac: { sr: 'kvasac', en: 'yeast' },
  praznicno: { sr: 'praznično', en: 'festive' },
  brzo: { sr: 'brzo', en: 'quick' },
  sir: { sr: 'sir', en: 'cheese' },
  meso: { sr: 'meso', en: 'meat' },
  piletina: { sr: 'piletina', en: 'chicken' },
  povrce: { sr: 'povrće', en: 'vegetables' },
  lesnik: { sr: 'lešnik', en: 'hazelnut' },
  kikiriki: { sr: 'kikiriki', en: 'peanuts' },
  banane: { sr: 'banane', en: 'bananas' },
  jagode: { sr: 'jagode', en: 'strawberries' },
  med: { sr: 'med', en: 'honey' },
  mak: { sr: 'mak', en: 'poppy seeds' },
  susam: { sr: 'susam', en: 'sesame' },
  oblanda: { sr: 'oblanda', en: 'wafer sheets' },
  video: { sr: 'video', en: 'video' },
};
export const tagLabel = (t: string, lang: Lang) => TAGS[t]?.[lang] ?? t;

export const UI = {
  sr: {
    site: 'Biljina Kuhinja',
    tagline: 'Domaći recepti iz maminih svezaka',
    desc: 'Biljina Kuhinja: 288 domaćih recepata iz maminih svezaka. Torte, kolači, peciva, pite, zimnica i glavna jela.',
    searchPlaceholder: 'Šta danas kuvamo?',
    searchHint: 'Probajte: „orasi čokolada“, „posno“, „kiflice“',
    home: 'Početna', search: 'Pretraga', groups: 'Grupe', book: 'Knjiga', favorites: 'Omiljeni',
    allRecipes: 'Svi recepti', recipes: 'recepata', recipe1: 'recept',
    groupsTitle: 'Grupe recepata',
    surprise: 'Iznenadi me',
    readAsBook: 'Čitaj kao knjigu',
    bookLead: 'Listajte recepte kao pravu kuvaricu, stranu po stranu.',
    featured: 'Probajte danas',
    videoRecipe: 'Video recept',
    ingredients: 'Sastojci', steps: 'Priprema', notes: 'Napomena',
    share: 'Podeli', copied: 'Link je kopiran', save: 'Sačuvaj', saved: 'Sačuvano',
    cook: 'Kuvam', cookOn: 'Ekran ostaje upaljen',
    similar: 'Slični recepti',
    noFavs: 'Još nema sačuvanih recepata. Dodirnite ♥ na receptu da ga sačuvate ovde.',
    noResults: 'Nema tačnog pogotka. Možda tražite:',
    results: 'rezultata',
    filterAll: 'Sve',
    recent: 'Nedavno traženo',
    back: 'Nazad',
    watchVideo: 'Pusti video',
    videoBy: 'Video: ',
    bookPick: 'Izaberite grupu',
    bookOpen: 'Otvori recept',
    bookHint: 'Prevucite ili dodirnite ivicu strane',
    prev: 'Prethodna', next: 'Sledeća',
    footer: 'Recepti iz Biljinih svezaka, prepisani s ljubavlju.',
    offline: 'Radi i bez interneta kada jednom otvorite recept.',
    skip: 'Preskoči na recepte',
    step: 'Korak',
    langSwitch: 'English',
  },
  en: {
    site: 'Biljina Kuhinja',
    tagline: "Home recipes from mom's notebooks",
    desc: "Biljina Kuhinja (Bilja's Kitchen): 288 Serbian home recipes from mom's notebooks. Cakes, bakes, breads, pies, preserves and main dishes.",
    searchPlaceholder: 'What are we cooking today?',
    searchHint: 'Try: "walnuts chocolate", "vegan", "kiflice"',
    home: 'Home', search: 'Search', groups: 'Groups', book: 'Book', favorites: 'Favorites',
    allRecipes: 'All recipes', recipes: 'recipes', recipe1: 'recipe',
    groupsTitle: 'Recipe groups',
    surprise: 'Surprise me',
    readAsBook: 'Read as a book',
    bookLead: 'Flip through the recipes like a real cookbook, page by page.',
    featured: 'Try today',
    videoRecipe: 'Video recipe',
    ingredients: 'Ingredients', steps: 'Method', notes: 'Note',
    share: 'Share', copied: 'Link copied', save: 'Save', saved: 'Saved',
    cook: 'Cooking', cookOn: 'Screen stays on',
    similar: 'Similar recipes',
    noFavs: 'No saved recipes yet. Tap ♥ on a recipe to keep it here.',
    noResults: 'No exact match. Maybe you are looking for:',
    results: 'results',
    filterAll: 'All',
    recent: 'Recent searches',
    back: 'Back',
    watchVideo: 'Play video',
    videoBy: 'Video: ',
    bookPick: 'Pick a group',
    bookOpen: 'Open recipe',
    bookHint: 'Swipe or tap the page edge',
    prev: 'Previous', next: 'Next',
    footer: "Recipes from Bilja's notebooks, copied with love.",
    offline: 'Works offline once you have opened a recipe.',
    skip: 'Skip to recipes',
    step: 'Step',
    langSwitch: 'Srpski',
  },
} as const;
export const t = (lang: Lang) => UI[lang];

type Route = 'home' | 'recipes' | 'category' | 'recipe' | 'search' | 'favorites' | 'book';
const SEG: Record<Lang, Record<Exclude<Route, 'home'>, string>> = {
  sr: { recipes: 'recepti', category: 'recepti', recipe: 'recept', search: 'pretraga', favorites: 'omiljeni', book: 'knjiga' },
  en: { recipes: 'recipes', category: 'recipes', recipe: 'recipe', search: 'search', favorites: 'favorites', book: 'book' },
};
export function url(lang: Lang, route: Route, param?: string): string {
  const pre = lang === 'en' ? '/en' : '';
  if (route === 'home') return `${BASE}${pre}/`;
  const seg = SEG[lang][route];
  return `${BASE}${pre}/${seg}/${param ? param + '/' : ''}`;
}
export const asset = (p: string) => `${BASE}/${p.replace(/^\//, '')}`;
export const plural = (n: number, lang: Lang) =>
  lang === 'en' ? `${n} ${n === 1 ? 'recipe' : 'recipes'}` : `${n} ${n % 10 === 1 && n % 100 !== 11 ? 'recept' : n % 10 >= 2 && n % 10 <= 4 && (n % 100 < 10 || n % 100 >= 20) ? 'recepta' : 'recepata'}`;
