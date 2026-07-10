"""Comprueba la consistencia de años de cada página de wiki/.

Para cada página verifica tres cosas:
  1. frontmatter `years` == la lista de "## Cartas fuente"
  2. frontmatter `years` == el tag `[...]` de esa página en index.md
  3. todo año del frontmatter tiene al menos una cita "— YYYY" en el cuerpo

Uso (desde la raíz del repo):
    python .claude/skills/lint/check_years.py

Sale con código 1 si hay páginas con problemas, 0 si está todo limpio.
"""
import re, glob, os, sys

index = open('index.md', encoding='utf-8').read()
problems = 0
for f in sorted(glob.glob('wiki/*.md')):
    txt = open(f, encoding='utf-8').read()
    parts = txt.split('---')
    fm = parts[1] if len(parts) > 2 else ''
    body = txt[txt.find('---', 3) + 3:] if txt.count('---') >= 2 else txt
    m = re.search(r'^years:\s*\[([0-9,\s]*)\]', fm, re.M)
    fy = set(re.findall(r'\d{4}', m.group(1))) if m else set()
    cf = body.split('## Cartas fuente')[-1] if '## Cartas fuente' in body else ''
    cfy = set(re.findall(r'^\s*-\s*(\d{4})', cf, re.M))
    body_no_cf = body.split('## Cartas fuente')[0]
    cited = set(re.findall(r'—\s*(\d{4})', body_no_cf))   # atribuciones "— YYYY"
    base = os.path.basename(f)
    im = re.search(r'\(' + re.escape('wiki/' + base) + r'\)[^`]*`\[([0-9,\s]*)\]`', index)
    iy = set(re.findall(r'\d{4}', im.group(1))) if im else None
    errs = []
    if fy != cfy:
        errs.append(f"front!=cartas {sorted(fy)} vs {sorted(cfy)}")
    if iy is not None and fy != iy:
        errs.append(f"front!=index {sorted(fy)} vs {sorted(iy)}")
    missing = fy - cited
    if missing:
        errs.append(f"anos sin cita en cuerpo: {sorted(missing)}")
    if errs:
        problems += 1
        print(f"{base}: " + " | ".join(errs))

print(f"--- paginas con problemas: {problems} ---")
sys.exit(1 if problems else 0)
