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

## [2026-07-08] ingest | carta 1979
- **Fuente:** `raw/1979.pdf`
- **Páginas creadas:** `roe-vs-beneficio-por-accion` (contabilidad),
  `buen-negocio-a-precio-justo` (modelos-mentales), `inflacion-enemigo-del-inversor` (riesgo).
- **Páginas enriquecidas:** `disciplina-de-no-actuar` (+1979: reducir volumen, rareza de la
  disciplina), `beneficios-retenidos-participadas` (+1979: un dólar retenido → un dólar de valor).
- **Estado:** borrador (nuevas) / pendiente + borrador (enriquecidas).

## [2026-07-08] ingest | carta 1980
- **Fuente:** `raw/1980.pdf`
- **Páginas creadas:** `recompra-de-acciones` (valoracion), `ventaja-competitiva`
  (modelos-mentales), `fortaleza-financiera-y-liquidez` (riesgo).
- **Páginas enriquecidas:** `beneficios-retenidos-participadas` (+1980: iceberg/árbol, "el
  acto, no el actor"), `inflacion-enemigo-del-inversor` (+1980: hamburguesas, impuesto al
  capital), `buen-negocio-a-precio-justo` (+1980: reputación del negocio),
  `no-predecir-el-mercado` (+1980: pronósticos inútiles).
- **Estado:** borrador (ninguna aprobada aún).

## [2026-07-08] ingest | carta 1981
- **Fuente:** `raw/1981.pdf`
- **Páginas creadas:** `locura-de-las-adquisiciones` (psicologia), `retener-o-repartir`
  (valoracion).
- **Páginas enriquecidas:** `inflacion-enemigo-del-inversor` (+1981: tenia corporativa),
  `concentracion` (+1981: evitar compromisos pequeños).
- **Estado:** borrador (ninguna aprobada aún).

## [2026-07-08] ingest | carta 1982
- **Fuente:** `raw/1982.pdf`
- **Páginas creadas:** `emitir-acciones-solo-a-su-valor` (valoracion).
- **Páginas enriquecidas:** `ventaja-competitiva` (+1982: ventaja en costes amplia y
  duradera), `vientos-a-favor-vs-en-contra` (+1982: ecuación del negocio de materia prima),
  `locura-de-las-adquisiciones` (+1982: adrenalina vs intelecto, Pascal).
- **Estado:** borrador salvo `vientos-a-favor-vs-en-contra`, que sigue `pendiente`.
