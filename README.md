# Cerebro Warren Buffett

Cerebro de conocimiento personal sobre la filosofía de inversión de Warren
Buffett, construido siguiendo el patrón de tres capas de Karpathy
(`raw` → `wiki` → `schema`).

## Estructura

- `raw/` — cartas anuales a los accionistas de Berkshire Hathaway, en PDF. Fuente original, solo lectura.
- `wiki/` — páginas de concepto interconectadas (psicología, riesgo, modelos mentales, valoración, contabilidad, casos).
- `CLAUDE.md` — esquema de reglas que rige cómo se construye y mantiene la wiki.
- `index.md` — índice de la wiki, agrupado por dominio.
- `log.md` — registro cronológico de ingestas y cambios.
- `.claude/skills/` — `lint` (audita citas y grafo de la wiki) y `query-file` (fila respuestas de consulta como páginas nuevas).

## Estado actual

48 cartas ingeridas (1977–2024), 56 páginas en `wiki/`, organizadas en 6 dominios.

## Cómo se usa

Abrir esta carpeta en [Claude Code](https://claude.com/claude-code) y preguntar
directamente contra la wiki — por ejemplo, "¿qué dice Buffett sobre el float
de los seguros?".

## Regla de rigor

Toda afirmación de la wiki sale de una carta real, con cita textual y año.
Nada de conocimiento externo sobre Buffett o inversión.
