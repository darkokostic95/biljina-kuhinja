"""Split work/batches/*.yaml (multi-document) into src/content/recipes/<slug>.md and validate."""
import sys, glob, os, yaml, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATS = ["torte", "kolaci", "bez-pecenja", "sitni-kolaci", "pite", "peciva",
        "glavna-jela", "salate-predjela", "zimnica", "kremovi-sladoledi", "napici"]
TAGS = {"posno", "bez-pecenja", "cokolada", "orasi", "keks", "plazma", "voce", "kokos",
        "jabuke", "kvasac", "praznicno", "brzo", "sir", "meso", "piletina", "povrce",
        "lesnik", "kikiriki", "banane", "jagode", "med", "mak", "susam", "oblanda", "video"}

LIST_LINE = re.compile(r'^(\s+)(sr|en): \[(.*)\]\s*$')
STEP_SPLIT = re.compile(r'(?<=[.!?"])\s*,\s+(?=["A-ZČĆŠŽĐ0-9])')

def _q(item):
    item = item.strip()
    if len(item) >= 2 and item[0] == '"' and item[-1] == '"':
        item = item[1:-1]
    return '"' + item.replace('\\', '\\\\').replace('"', '\\"') + '"'

def preprocess(text):
    """Authoring shorthand: `sr: [a, b, c]` lists. Ingredient items split on ', ';
    step items split only on ', ' that follows end punctuation and precedes a capital."""
    out, section = [], None
    for line in text.splitlines():
        m = re.match(r'^([a-z_]+):', line)
        if m:
            section = m.group(1)
        um = re.match(r'^uncertain: \[(.*)\]\s*$', line)
        if um:
            out.append("uncertain:")
            out.append("- " + _q(um.group(1)))
            continue
        lm = LIST_LINE.match(line)
        if lm and section in ("ingredients", "steps"):
            ind, lang, body = lm.groups()
            items = STEP_SPLIT.split(body) if section == "steps" else body.split(", ")
            out.append(f"{ind}{lang}:")
            out += [f"{ind}- {_q(i)}" for i in items if i.strip()]
        else:
            out.append(line)
    return "\n".join(out)

def main():
    out = os.path.join(ROOT, "src/content/recipes")
    seen, errors = {}, []
    for path in sorted(glob.glob(os.path.join(ROOT, "work/batches/*.yaml"))):
        for doc in yaml.safe_load_all(preprocess(open(path, encoding="utf-8").read())):
            if not doc:
                continue
            s = doc.get("slug", "?")
            where = f"{os.path.basename(path)}:{s}"
            if not re.fullmatch(r"[a-z0-9-]+", s): errors.append(f"bad slug {where}")
            if s in seen: errors.append(f"duplicate slug {where} (also {seen[s]})")
            seen[s] = where
            if doc.get("category") not in CATS: errors.append(f"bad category {where}: {doc.get('category')}")
            for t in doc.get("tags", []):
                if t not in TAGS: errors.append(f"unknown tag {where}: {t}")
            for k in ("title", "ingredients", "steps"):
                if k not in doc: errors.append(f"missing {k} {where}")
            t = doc.get("title", {})
            if not (t.get("sr") and t.get("en")): errors.append(f"title needs sr+en {where}")
            for g in doc.get("ingredients", []):
                if len(g.get("sr", [])) != len(g.get("en", [])):
                    errors.append(f"ingredient sr/en length mismatch {where} group={g.get('group')}")
            st = doc.get("steps", {})
            if len(st.get("sr", [])) != len(st.get("en", [])):
                errors.append(f"steps sr/en length mismatch {where}")
            with open(os.path.join(out, s + ".md"), "w", encoding="utf-8") as fh:
                fh.write("---\n")
                fh.write(yaml.safe_dump(doc, allow_unicode=True, sort_keys=False, width=1000))
                fh.write("---\n")
    for e in errors: print("ERROR", e)
    print(f"{len(seen)} recipes written, {len(errors)} errors")
    return 1 if errors else 0

if __name__ == "__main__":
    sys.exit(main())
