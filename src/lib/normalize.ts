// Shared by the build (search index) and the browser (query).
const CYR: Record<string, string> = {
  а:'a',б:'b',в:'v',г:'g',д:'d',ђ:'dj',е:'e',ж:'z',з:'z',и:'i',ј:'j',к:'k',л:'l',љ:'lj',м:'m',н:'n',њ:'nj',о:'o',п:'p',р:'r',с:'s',т:'t',ћ:'c',у:'u',ф:'f',х:'h',ц:'c',ч:'c',џ:'dz',ш:'s',
};
export function norm(s: string): string {
  let out = '';
  for (const ch of s.toLowerCase()) out += CYR[ch] ?? ch;
  return out
    .replace(/đ/g, 'dj')
    .normalize('NFD').replace(/[̀-ͯ]/g, '')
    .replace(/[^a-z0-9]+/g, ' ')
    .trim();
}
const STOP = new Set(['i','ili','sa','s','za','od','na','u','po','se','da','je','a','g','kg','dl','l','ml','dkg','kom','the','of','and','with','for','to','in','a','an','or','tbsp','tsp','cup','cups','kasika','kasike','kasicica','kasicice','solja','solje','malo','oko','pola','kesica','kesice','pakovanje']);
export function words(s: string): string[] {
  return norm(s).split(' ').filter((w) => w.length > 1 && !/^\d+$/.test(w) && !STOP.has(w));
}
