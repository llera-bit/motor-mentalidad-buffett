---
name: query-file
description: Fila una respuesta de Query como página nueva de la wiki del cerebro Buffett, pero solo si es síntesis pura de las cartas (todo citado, sin marco personal ni de trading). Crea la página, la enlaza en index.md y registra la operación en log.md.
---

# /query-file — filar una respuesta de Query como página

Cuándo aplica: tras responder una Query cuya respuesta sea **síntesis pura de las cartas**
(todo citado, sin marco personal ni de trading).

Reglas de admisión:
- **Sí se fila:** respuesta 100% sostenida en citas de las cartas (p. ej. la evolución de
  un concepto a lo largo de los años, una comparación entre casos, una síntesis temática).
- **No se fila nunca:** cualquier respuesta que relacione las cartas con el trading, el
  riesgo personal o el contexto del usuario. Se queda en el chat.
- **Query mixta:** separar. El núcleo de síntesis pura puede filarse (despojado de todo
  marco personal); la capa de aplicación personal se queda en el chat.

Procedimiento:
1. Confirmar con el usuario antes de filar (disciplina del piloto).
2. Crear `wiki/<slug-kebab-case>.md` con el formato estándar de `CLAUDE.md`: frontmatter
   (`concepto`, `domain`, `years` = todos los años citados, `estado: borrador`,
   `actualizado`), síntesis ES + citas EN, wikilinks, sección "Cartas fuente".
3. Enlazar: añadir la página a `index.md` bajo su `domain` y wikilinks recíprocos desde
   las páginas relacionadas.
4. Registrar en `log.md`: `## [YYYY-MM-DD] query | <tema>` con la página creada.

Procedencia: una página de `/query-file` nace de una consulta, no de una sola carta; se
reconoce porque suele citar varios años. El `log.md` deja el rastro.
