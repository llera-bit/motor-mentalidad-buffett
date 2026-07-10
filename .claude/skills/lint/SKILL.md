---
name: lint
description: Pase de salud (health-check) de la wiki del cerebro Buffett — contradicciones/evolución, páginas huérfanas, conceptos sin página, cross-references, rigor de citas, frontmatter y consistencia índice/log. No aplica el perfil de trading del usuario.
---

# /lint — pase de salud de la wiki (cerebro Buffett)

Objetivo: revisar la salud de `wiki/` y proponer arreglos. Respeta la **regla de rigor**
(toda afirmación con cita de una carta; sin conocimiento externo) y el **alcance del
perfil** (no se relaciona nada con el trading del usuario). No usa búsqueda web.

## Paso 0 — comprobaciones automáticas (obligatorias)

Antes de nada, y **también antes de cada commit de ingest**, ejecutar desde la raíz del repo:

```
python .claude/skills/lint/check_years.py    # años: frontmatter == Cartas fuente == index; cada año con cita
python .claude/skills/lint/graph_audit.py    # wikilinks rotos, páginas huérfanas, simetría con index.md
```

Ambos salen con código 1 si encuentran algo. Cubren automáticamente los puntos 3, 7 y 8 de
abajo; si alguno falla, arreglar antes de seguir con la revisión manual. Estos scripts
cazan el fallo más común: un `Edit` que actualiza el frontmatter pero no inserta la cita en
el cuerpo, dejando una página que reclama un año que no cita.

## Revisión manual

Revisa:
1. **Contradicciones / evolución:** afirmaciones que chocan entre páginas, o cambios de
   matiz de un concepto entre cartas de años distintos → señalar para revisión del usuario.
2. **Afirmaciones caducas:** algo que una carta posterior matiza o supera.
3. **Páginas huérfanas:** sin enlaces entrantes `[[...]]` desde otras páginas ni desde
   `index.md` (automatizado en `graph_audit.py`). Toda página nueva nace con enlaces
   entrantes, no solo salientes.
4. **Conceptos sin página:** ideas citadas en varias páginas que merecerían página propia.
5. **Cross-references que faltan:** páginas que deberían enlazarse entre sí y no lo hacen.
6. **Rigor:** toda afirmación con su cita y año; cita que no aparezca en la carta = bug.
7. **Frontmatter:** `domain` válido, `years` ordenado y completo, `actualizado` al día,
   `estado` coherente (automatizado en parte en `check_years.py`).
8. **Consistencia índice/log:** cada página en `index.md` bajo su `domain`; operaciones
   registradas en `log.md`.
9. **Duplicación:** la misma cita textual no puede vivir en dos páginas. Si un concepto
   reaparece, se enlaza (Opción A), no se copia.

Salida: informe de hallazgos agrupado por tipo, con propuestas concretas. Arreglar solo
los triviales e inequívocos; para el resto, esperar visto bueno. Registrar el pase en
`log.md`: `## [YYYY-MM-DD] lint | <resumen>`.
