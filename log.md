# Log de ingestas

_Registro append-only. Prefijo por entrada: `## [YYYY-MM-DD] <op> | <detalle>`
(op: `ingest` | `query` | `lint`). Últimas entradas: `grep "^## \[" log.md | tail -5`._

## [2026-07-07] ingest | carta 1987 (piloto)
- **Fuente:** `raw/1987.pdf`
- **Páginas creadas:**
  - `wiki/mr-market.md` (psicologia)
  - `wiki/volatilidad-y-venta-forzada.md` (riesgo)
  - `wiki/analista-de-negocios.md` (modelos-mentales)
- **Estado:** piloto aprobado por el usuario; commit `a1ebc23`.

## [2026-07-08] ingest | carta 1977
- **Fuente:** `raw/1977.pdf`
- **Páginas creadas:**
  - `wiki/criterios-de-seleccion.md` (modelos-mentales)
  - `wiki/disciplina-de-no-actuar.md` (psicologia)
  - `wiki/vientos-a-favor-vs-en-contra.md` (modelos-mentales)
- **Páginas enriquecidas:**
  - `wiki/analista-de-negocios.md` — añadida cita de 1977; `years: [1977, 1987]` (Opción A).
- **Estado:** aprobada por el usuario; commit `b7e5ade`.

## [2026-07-08] ingest | carta 1978
- **Fuente:** `raw/1978.pdf`
- **Páginas creadas:** `no-predecir-el-mercado` (psicologia), `concentracion`
  (modelos-mentales), `beneficios-retenidos-participadas` (valoracion).
- **Páginas enriquecidas:** `criterios-de-seleccion` (+1978: cuatro filtros y comprador
  neto), `vientos-a-favor-vs-en-contra` (+1978: economía de bienes indiferenciados).
- **Estado:** borrador (nuevas) / pendiente (enriquecidas).
