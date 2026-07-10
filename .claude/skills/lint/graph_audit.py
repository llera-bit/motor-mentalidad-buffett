"""Audita el grafo de la wiki: wikilinks rotos, páginas huérfanas, simetría con index.md.

Uso (desde la raíz del repo):
    python .claude/skills/lint/graph_audit.py

Informa de:
  - rotos:     `[[slug]]` que apunta a una página inexistente
  - huerfanas: páginas sin ningún enlace entrante desde otra página
  - idx-diff:  diferencia simétrica entre los .md de wiki/ y los enlazados en index.md
  - estado:    reparto de borrador / pendiente / estable

Sale con código 1 si hay rotos, huérfanas o desajuste con el índice.
"""
import re, os, collections, sys

wiki = "wiki"
files = sorted(f for f in os.listdir(wiki) if f.endswith(".md"))
slugs = {f[:-3] for f in files}
links = collections.defaultdict(set)
estado = collections.Counter()

for f in files:
    txt = open(os.path.join(wiki, f), encoding="utf-8").read()
    for m in re.findall(r"\[\[([^\]]+)\]\]", txt):
        links[f[:-3]].add(m.strip())
    estado[re.search(r"^estado:\s*(\S+)", txt, re.M).group(1)] += 1

broken = [(s, t) for s, ts in links.items() for t in ts if t not in slugs]
orphans = sorted(slugs - {t for ts in links.values() for t in ts})
index = open("index.md", encoding="utf-8").read()
in_index = set(re.findall(r"\(wiki/([a-z0-9\-]+)\.md\)", index))
idx_diff = sorted(slugs ^ in_index)

print(f"paginas={len(files)}")
print(f"rotos={broken}")
print(f"huerfanas={orphans}")
print(f"idx-diff={idx_diff}")
print(f"estado={dict(estado)}")
sys.exit(1 if (broken or orphans or idx_diff) else 0)
