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
Le interesa la disciplina y psicología de Buffett tanto como su stock-picking.
Este perfil orienta qué dominios de las cartas priorizar en su cobertura:
- Núcleo: psicología/disciplina, gestión de riesgo, modelos mentales/checklists.
- Apoyo: casos de empresas y contabilidad como ilustración, no como fin en sí.
Su aplicación está acotada por el bloque «Modos de operación» de abajo.

## Modos de operación — alcance del perfil (REGLA SEPARADA, NO NEGOCIABLE)
El perfil de trading de arriba es contexto personal y NO se aplica por defecto. Solo
se activa en un modo:
- **Ingest** (crear/editar páginas): únicamente síntesis de las cartas con cita.
  Prohibido señalar, comentar o relacionar el contenido con el trading, el riesgo
  personal o cualquier contexto del usuario — ni en las páginas ni en el chat.
- **Lint** (revisar rigor / mantenimiento): igual que Ingest. Sin marco personal.
- **Query** (el usuario pregunta explícitamente cómo se relaciona algo de las cartas
  con su trading): único modo en que se aplica el perfil personal.
Si durante Ingest o Lint aparece una conexión con el trading, no la menciones ni la
guardes en ningún sitio: espera a un Query explícito del usuario.

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
estado: borrador | revision | estable
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
`borrador` (recién ingerida) → `revision` (revisada por el usuario) → `estable`.

## Mantenimiento
- Al crear/editar una página: actualizar `index.md` (bajo su `domain`) y el campo
  `actualizado`.
- Registrar cada ingesta en `log.md`: fecha, carta(s) y páginas creadas/editadas.
- Antes de ingerir en masa, proponer y esperar visto bueno (regla del piloto).
