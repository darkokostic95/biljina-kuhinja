import glob, re, os, sys
B = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "work/batches")
docs = {}  # slug -> (file, text)
order = {}
for p in sorted(glob.glob(B + "/*.yaml")):
    parts = open(p, encoding="utf-8").read().split("\n---\n")
    order[p] = []
    for d in parts:
        m = re.search(r"^slug: (\S+)", d, re.M)
        docs[m.group(1)] = [p, d]; order[p].append(m.group(1))
errors = []
def rep(slug, old, new, count=1):
    d = docs[slug][1]
    if old not in d: errors.append(f"{slug}: not found: {old[:70]}"); return
    docs[slug][1] = d.replace(old, new, count)
def setdoc(slug, text, newslug=None):
    p = docs[slug][0]; ns = newslug or slug
    docs[ns] = [p, text.strip("\n")]
    if ns != slug:
        order[p][order[p].index(slug)] = ns; del docs[slug]
def delete(slug):
    p = docs[slug][0]; order[p].remove(slug); del docs[slug]
def title(slug, sr, en=None):
    d = docs[slug][1]
    m = re.search(r"^title: \{sr: (.*?), en: (.*)\}$", d, re.M)
    docs[slug][1] = d.replace(m.group(0), f"title: {{sr: {sr}, en: {en or m.group(2)}}}")
def save():
    for p, slugs in order.items():
        out = []
        for s in slugs:
            d = docs[s][1]
            d = re.sub(r"^uncertain: .*\n?", "", d, flags=re.M).rstrip("\n")
            out.append(d)
        open(p, "w", encoding="utf-8").write("\n---\n".join(out) + "\n")
    for e in errors: print("ERR", e)
    print("saved", sum(len(v) for v in order.values()), "docs;", len(errors), "errors")
