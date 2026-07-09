# CLAUDE.md — Cerebro Warren Buffett

## Propósito
Cerebro de conocimiento sobre la filosofía de inversión de Warren Buffett, extraído
exclusivamente de sus cartas anuales a los accionistas de Berkshire Hathaway.

## Arquitectura (tres capas)
- `raw/` — cartas anuales en PDF (1977–2024). **Solo lectura. Nunca modificar.**
- `wiki/` — páginas de concepto interconectadas que creo y mantengo yo.
- `CLAUDE.md` — este esquema de reglas.
- `index.md` — índice de la wiki, agrupado por `domain`.
- `log.md` — registro cronológico de ingestas y cambios.

## Regla de rigor (NO NEGOCIABLE)
Toda afirmación de la wiki debe salir de una carta en `raw/`, con cita textual y año.
- Prohibido completar con conocimiento externo sobre Buffett o sobre inversión.
- Si algo no aparece en las cartas, no se incluye.
- Cada síntesis se apoya en al menos una cita literal atribuida a su año.
- Una afirmación sin cita es un bug: se corrige o se elimina.

## Perfil del usuario (contexto general)
Opera mercados de forma sistemática e intradía, con gestión de riesgo estructurada.
Este perfil **no** prioriza dominios ni orienta la cobertura de la wiki.
- Regla de proporcionalidad: extraer proporcionalmente a lo que cada carta enfatiza,
  sin peso añadido por interés personal del usuario.
Su aplicación está acotada por el bloque «Alcance del perfil» de abajo.

## Operaciones (flujo de trabajo)
- **Ingest** (procesar una carta): leer, extraer conceptos, crear páginas y **enriquecer
  las existentes** cuando reaparece un concepto (Opción A: cita + año en `years`, no duplicar). Actualizar `index.md`, `log.md`, `actualizado`.
- **Query** (responder contra la wiki): buscar en `index.md`, leer y sintetizar con citas. Filar síntesis pura → skill `query-file` (`/query-file`).
- **Lint** (health-check de la wiki) → skill `lint` (`/lint`).

## Alcance del perfil (SEPARADO DE LAS OPERACIONES, NO NEGOCIABLE)
El perfil de trading del usuario es contexto personal y NO se aplica por defecto:
- En **Ingest** y **Lint**: prohibido señalar, comentar o relacionar el contenido con el
  trading, el riesgo personal o cualquier contexto del usuario — ni en páginas ni en chat.
- En **Query**: único modo en que se aplica el perfil, y solo si el usuario lo pregunta
  explícitamente. Las respuestas con marco de trading NO se filan en `wiki/`.

## Idioma
Cita textual en inglés (palabras exactas de Buffett) + síntesis en español.

## Formato de página `wiki/`
Nombre de archivo: `kebab-case.md` (ej. `mr-market.md`).
Frontmatter:
```
---
concepto: <nombre legible>
domain: <ver taxonomía>
years: [<años de las cartas citadas>]
estado: borrador | pendiente | estable
actualizado: YYYY-MM-DD
---
```
Cuerpo:
- Síntesis en español apoyada en citas.
- Citas textuales en bloque con atribución de año:
  > "<texto exacto en inglés>" — 1987
- Enlaces internos con wikilinks al slug del archivo: `[[mr-market]]`.
- Sección final "Cartas fuente" con los años citados.

## Taxonomía de `domain`
- `psicologia` — temperamento, Mr. Market, miedo/codicia, no pronosticar.
- `riesgo` — margen de seguridad, apalancamiento, preservación de capital.
- `modelos-mentales` — círculo de competencia, valor intrínseco, coste de oportunidad.
- `valoracion` — owner earnings, valor intrínseco, look-through earnings.
- `contabilidad` — GAAP vs. realidad económica, goodwill, métricas.
- `casos` — empresas concretas (See's, GEICO, textil, seguros/float).

## Estados
- `borrador` — recién creada por Ingest; nunca revisada.
- `pendiente` — página `estable` que se modificó (cambio sustantivo); pendiente de re-revisión.
- `estable` — revisada y aprobada; sin cambios pendientes.
Ingest→`borrador`; aprobar→`estable`; modificar `estable`→`pendiente`; re-aprobar→`estable`. Enriquecer una `borrador` la deja igual; los cambios triviales no cambian el estado.

## Mantenimiento
- Antes de ingerir en masa, proponer y esperar visto bueno (regla del piloto).
- `log.md` es append-only; prefijo `## [YYYY-MM-DD] <op> | <detalle>` (op: ingest|query|lint).
