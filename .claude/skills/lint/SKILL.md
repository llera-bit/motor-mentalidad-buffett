---
name: lint
description: Pase de salud (health-check) de la wiki del cerebro Buffett — contradicciones/evolución, páginas huérfanas, conceptos sin página, cross-references, rigor de citas, frontmatter y consistencia índice/log. No aplica el perfil de trading del usuario.
---

# /lint — pase de salud de la wiki (cerebro Buffett)

Objetivo: revisar la salud de `wiki/` y proponer arreglos. Respeta la **regla de rigor**
(toda afirmación con cita de una carta; sin conocimiento externo) y el **alcance del
perfil** (no se relaciona nada con el trading del usuario). No usa búsqueda web.

Revisa:
1. **Contradicciones / evolución:** afirmaciones que chocan entre páginas, o cambios de
   matiz de un concepto entre cartas de años distintos → señalar para revisión del usuario.
2. **Afirmaciones caducas:** algo que una carta posterior matiza o supera.
3. **Páginas huérfanas:** sin enlaces entrantes `[[...]]` desde otras páginas ni desde
   `index.md`.
4. **Conceptos sin página:** ideas citadas en varias páginas que merecerían página propia.
5. **Cross-references que faltan:** páginas que deberían enlazarse entre sí y no lo hacen.
6. **Rigor:** toda afirmación con su cita y año; cita que no aparezca en la carta = bug.
7. **Frontmatter:** `domain` válido, `years` ordenado y completo, `actualizado` al día,
   `estado` coherente.
8. **Consistencia índice/log:** cada página en `index.md` bajo su `domain`; operaciones
   registradas en `log.md`.

Salida: informe de hallazgos agrupado por tipo, con propuestas concretas. Arreglar solo
los triviales e inequívocos; para el resto, esperar visto bueno. Registrar el pase en
`log.md`: `## [YYYY-MM-DD] lint | <resumen>`.
