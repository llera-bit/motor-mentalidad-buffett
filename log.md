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

## [2026-07-08] ingest | carta 1983
- **Fuente:** `raw/1983.pdf`
- **Páginas creadas:** `valor-intrinseco` (valoracion), `goodwill-economico` (contabilidad),
  `candor` (psicologia), `hiperactividad-del-mercado` (psicologia).
- **Páginas enriquecidas:** `fortaleza-financiera-y-liquidez` (+1983: rechazar oportunidades
  antes que sobreapalancar), `retener-o-repartir` (+1983: test del dólar, ventana de 5 años).
- **Nota:** carta faro (principios del propietario + apéndice sobre goodwill económico).
- **Estado:** borrador (todas).

## [2026-07-08] ingest | carta 1984
- **Fuente:** `raw/1984.pdf`
- **Páginas creadas:** `fallar-convencionalmente` (psicologia).
- **Páginas enriquecidas:** `retener-o-repartir` (+1984: dividendos, beneficio restringido
  vs no restringido), `recompra-de-acciones` (+1984: 2 dólares por 1, señal), `concentracion`
  (+1984: harén de Billy Rose), `disciplina-de-no-actuar` (+1984: no hacer nada es lo más
  difícil), `analista-de-negocios` (+1984: Graham "most businesslike").
- **Estado:** borrador; `analista-de-negocios` pasa de estable a pendiente.

## [2026-07-08] ingest | carta 1985
- **Fuente:** `raw/1985.pdf`
- **Páginas creadas:** `contra-el-mercado-eficiente` (modelos-mentales), `incentivos-alineados`
  (modelos-mentales).
- **Páginas enriquecidas:** `vientos-a-favor-vs-en-contra` (+1985: en qué barco te subes vs
  cómo remas; barco que hace agua; parade/tiptoes), `goodwill-economico` (+1985: subasta
  textil, goodwill de rutas de periódico > activos tangibles).
- **Nota:** carta del cierre del negocio textil y del ensayo sobre opciones/incentivos.
- **Estado:** borrador; `vientos-a-favor-vs-en-contra` sigue pendiente.

## [2026-07-08] ingest | carta 1986
- **Fuente:** `raw/1986.pdf`
- **Páginas creadas:** `miedo-y-codicia` (psicologia), `owner-earnings` (valoracion).
- **Páginas enriquecidas:** `ventaja-competitiva` (+1986: foso alrededor del castillo, GEICO),
  `hiperactividad-del-mercado` (+1986: el accionista en conjunto rinde menos que sus empresas).
- **Nota:** apéndice de 1986 define owner earnings (a+b−c) y la falacia del cash flow.
- **Estado:** borrador (todas).
