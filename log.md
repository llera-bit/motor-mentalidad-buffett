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

## [2026-07-08] ingest | carta 1988
- **Fuente:** `raw/1988.pdf`
- **Páginas creadas:** `holding-para-siempre` (psicologia), `arbitraje` (modelos-mentales).
- **Páginas enriquecidas:** `concentracion` (+1988: Mae West, muy pocas empresas),
  `contra-el-mercado-eficiente` (+1988: "frequently" vs "always" efficient; 63 años de arbitraje).
- **Estado:** borrador (todas).

## [2026-07-08] ingest | carta 1989
- **Fuente:** `raw/1989.pdf`
- **Páginas creadas:** `imperativo-institucional` (psicologia), `circulo-de-competencia`
  (modelos-mentales).
- **Páginas enriquecidas:** `buen-negocio-a-precio-justo` (+1989: wonderful company at fair
  price, colilla de puro, tiempo amigo/enemigo), `fortaleza-financiera-y-liquidez` (+1989: 99:1,
  la ruina no se compensa), `owner-earnings` (+1989: crítica a EBITDA).
- **Nota:** carta faro (ensayo "Mistakes of the First Twenty-Five Years").
- **Estado:** borrador (todas).

## [2026-07-08] ingest | carta 1990
- **Fuente:** `raw/1990.pdf`
- **Páginas creadas:** ninguna (carta de conceptos en acción).
- **Páginas enriquecidas:** `miedo-y-codicia` (+1990: pesimismo amigo/optimismo enemigo,
  pensar no encuestar), `circulo-de-competencia` (+1990: Watson "smart in spots"),
  `imperativo-institucional` (+1990: banqueros lemming).
- **Nota:** compra de Wells Fargo en el pánico bancario, como ilustración.
- **Estado:** borrador (todas).

## [2026-07-08] ingest | carta 1991
- **Fuente:** `raw/1991.pdf`
- **Páginas creadas:** `franquicia-vs-negocio` (modelos-mentales).
- **Páginas enriquecidas:** `beneficios-retenidos-participadas` (+1991: definición formal de
  look-through earnings; mirar al campo, no al marcador).
- **Nota:** ensayo "franquicia vs. negocio" (3 condiciones; la franquicia tolera mala gestión).
- **Estado:** borrador (todas).

## [2026-07-08] ingest | carta 1992
- **Fuente:** `raw/1992.pdf`
- **Páginas creadas:** `valor-y-crecimiento` (valoracion), `margen-de-seguridad` (riesgo).
- **Páginas enriquecidas:** `valor-intrinseco` (+1992: fórmula de John Burr Williams, DCF),
  `circulo-de-competencia` (+1992: delimitar lo que no sabes; evitar errores grandes).
- **Nota:** valor y crecimiento "joined at the hip"; margin of safety = piedra angular (Graham).
- **Estado:** borrador (todas).

## [2026-07-08] ingest | carta 1993
- **Fuente:** `raw/1993.pdf`
- **Páginas creadas:** `riesgo-no-es-volatilidad` (riesgo).
- **Páginas enriquecidas:** `concentracion` (+1993: concentrar reduce riesgo para el que
  entiende), `ventaja-competitiva` (+1993: foso alrededor del castillo, Coke/Gillette),
  `circulo-de-competencia` (+1993: el que no sabe, que indexe).
- **Nota:** ensayo faro sobre el riesgo (beta vs. pérdida de poder adquisitivo; 5 factores).
- **Estado:** borrador (todas).

## [2026-07-08] ingest | carta 1994
- **Fuente:** `raw/1994.pdf`
- **Páginas creadas:** ninguna (carta de aplicación de principios).
- **Páginas enriquecidas:** `no-predecir-el-mercado` (+1994: ignorar la macro; los shocks no
  hacen mella), `miedo-y-codicia` (+1994: fear, friend of the fundamentalist),
  `disciplina-de-no-actuar` (+1994: la "zona feliz" de Ted Williams).
- **Nota:** enrichment-only; la macro y el miedo como distracción vs. oportunidad.
- **Estado:** borrador salvo `disciplina-de-no-actuar`, que sigue `pendiente`.

## [2026-07-08] ingest | carta 1995
- **Fuente:** `raw/1995.pdf`
- **Páginas creadas:** `float` (casos) — primera página del dominio `casos`.
- **Páginas enriquecidas:** `ventaja-competitiva` (+1995: "economic castles protected by
  unbreachable moats", GEICO al 100%).
- **Nota:** compra del 100% de GEICO; definición de float y su coste.
- **Estado:** borrador (todas).

## [2026-07-08] ingest | carta 1996
- **Fuente:** `raw/1996.pdf`
- **Páginas creadas:** ninguna (carta "owner's manual", restatement).
- **Páginas enriquecidas:** `circulo-de-competencia` (+1996: conocer los límites del círculo es
  lo vital), `holding-para-siempre` (+1996: si no lo tendrías 10 años, ni 10 minutos),
  `disciplina-de-no-actuar` (+1996: la inactividad es inteligente; más dinero roncando).
- **Nota:** corregida deriva en el frontmatter `years` de `circulo-de-competencia` (faltaban
  1992/1993/1996; ya cuadra con cuerpo, Cartas fuente e índice).
- **Estado:** borrador salvo `disciplina-de-no-actuar` (pendiente).

## [2026-07-08] ingest | carta 1997
- **Fuente:** `raw/1997.pdf`
- **Páginas creadas:** ninguna.
- **Páginas enriquecidas:** `float` (+1997: ironía contable, vale más que fondos propios
  equivalentes), `criterios-de-seleccion` (+1997: parábola de las hamburguesas / comprador neto
  prefiere precios bajos).
- **Estado:** borrador (`float`) / pendiente (`criterios-de-seleccion`).

## [2026-07-08] ingest | carta 1998
- **Fuente:** `raw/1998.pdf`
- **Páginas creadas:** ninguna (carta corta; año de General Re, Dairy Queen, Executive Jet).
- **Páginas enriquecidas:** `float` (+1998: lo que cuenta es el coste; crecer float caro es
  maldición), `holding-para-siempre` (+1998: vender McDonald's fue un error; el trasiego restó).
- **Estado:** borrador (todas).

## [2026-07-08] ingest | carta 1999
- **Fuente:** `raw/1999.pdf`
- **Páginas creadas:** ninguna (peor año relativo; disciplina en la burbuja puntocom).
- **Páginas enriquecidas:** `circulo-de-competencia` (+1999: reconocer el perímetro; no comprar
  tecnología por falta de insight sobre ventajas duraderas; no cambiar razón por esperanza).
- **Estado:** borrador (todas).

## [2026-07-08] ingest | carta 2000
- **Fuente:** `raw/2000.pdf`
- **Páginas creadas:** ninguna.
- **Páginas enriquecidas:** `valor-intrinseco` (+2000: Esopo, "pájaro en mano", las tres
  preguntas), `valor-y-crecimiento` (+2000: especulación = mirar lo que pagará el siguiente; más
  peligrosa cuando parece fácil).
- **Nota:** ensayo de Esopo (600 a.C.) sobre valoración; crítica a la burbuja puntocom.
- **Estado:** borrador (todas).
