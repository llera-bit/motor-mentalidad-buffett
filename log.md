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

## [2026-07-08] ingest | carta 2001
- **Fuente:** `raw/2001.pdf`
- **Páginas creadas:** `principios-de-suscripcion` (riesgo) — tres reglas + exposición vs. experiencia.
- **Páginas enriquecidas:** ninguna.
- **Nota:** golpe del 11-S; el error de mirar experiencia y no exposición (riesgo de agregación).
- **Estado:** borrador (todas).

## [2026-07-08] ingest | carta 2002
- **Fuente:** `raw/2002.pdf`
- **Páginas creadas:** `derivados` (riesgo) — "armas financieras de destrucción masiva".
- **Páginas enriquecidas:** `principios-de-suscripcion` (+2002: las correlaciones afloran en la
  crisis), `incentivos-alineados` (+2002: mark-to-myth favorece bonus del trader y opciones del CEO).
- **Nota:** aplicada la pauta de leer a fondo aunque el tema se repita (enriquecimientos complementarios).
- **Estado:** borrador (todas).

## [2026-07-08] ingest | carta 2003
- **Fuente:** `raw/2003.pdf`
- **Páginas creadas:** ninguna (ensayo de gobernanza/compensación).
- **Páginas enriquecidas:** `imperativo-institucional` (+2003: el "boardroom atmosphere" adormece
  los genes fiduciarios), `incentivos-alineados` (+2003: captura de comités/consultores de compensación).
- **Nota:** se omite la macro (Squanderville/Thriftville) por criterio de alcance.
- **Estado:** borrador (todas).

## [2026-07-08] ingest | carta 2004
- **Fuente:** `raw/2004.pdf`
- **Páginas creadas:** ninguna (carta de exceso de caja y dólar/macro).
- **Páginas enriquecidas:** `hiperactividad-del-mercado` (+2004: la emoción y los costes son los
  enemigos del inversor; tres causas de bajo rendimiento).
- **Nota:** se omite la macro del dólar; float y disciplina de suscripción vienen como restatement.
- **Estado:** borrador (todas).

## [2026-07-08] ingest | carta 2005
- **Fuente:** `raw/2005.pdf`
- **Páginas creadas:** ninguna.
- **Páginas enriquecidas:** `hiperactividad-del-mercado` (+2005: parábola de los Gotrocks; los
  dueños ganan menos que sus empresas por costes de fricción), `ventaja-competitiva` (+2005:
  "widening the moat" como objetivo de gestión por encima del corto plazo).
- **Estado:** borrador (todas).

## [2026-07-08] ingest | carta 2006
- **Fuente:** `raw/2006.pdf`
- **Páginas creadas:** ninguna (float restated; adquisiciones ISCAR/otras; filantropía).
- **Páginas enriquecidas:** `vientos-a-favor-vs-en-contra` (+2006: la economía en erosión vence
  al mejor gestor; "get into a good business"), `franquicia-vs-negocio` (+2006: los periódicos,
  antaño franquicias, se degradan en negocios — la predicción de 1991 cumpliéndose).
- **Estado:** borrador salvo `vientos-a-favor-vs-en-contra` (pendiente).

## [2026-07-09] ingest | re-pase carta 1990 (lectura completa)
- **Motivo:** re-pase de las cartas 1990–2001, leídas en su día en fracciones, para rescatar
  complementos que no se extrajeron. Sin duplicar contenido ya presente.
- **Fuente:** `raw/1990.pdf`
- **Páginas creadas:** ninguna.
- **Páginas enriquecidas:** `float` (+1990: medir el coste por el ratio pérdida/float, no por el
  combined ratio; "low cost = good business"; GEICO con coste negativo), `margen-de-seguridad`
  (+1990: el motto de Graham en su origen, invocado contra la manía del apalancamiento),
  `fortaleza-financiera-y-liquidez` (+1990: la daga en el volante; "plan que exige esquivar
  todos los baches es un plan para el desastre"), `riesgo-no-es-volatilidad` (+1990: "lumpy 15%
  vs smooth 12%"; aceptar resultados desiguales si la expectativa a largo plazo es superior),
  `vientos-a-favor-vs-en-contra` (+1990: en un commodity, "impossible to be smarter than your
  dumbest competitor").
- **Estado:** sin cambios (borrador salvo `vientos-a-favor-vs-en-contra`, que sigue pendiente).

## [2026-07-09] ingest | re-pase carta 1991 (lectura completa)
- **Fuente:** `raw/1991.pdf`
- **Páginas creadas:** `errores-de-omision` (los peores errores son de omisión, no de comisión;
  Fannie Mae, ~$1.4 B no ganados; chuparse el pulgar ante lo entendido y atractivo).
- **Páginas enriquecidas:** `incentivos-alineados` (+1991: comp de H.H. Brown = salario simbólico
  + % del beneficio tras un cargo por capital; no tratar el capital como gratis), `concentracion`
  (+1991: la cita de Keynes de 1934), `goodwill-economico` (+1991: See's a 20 años; comparar el
  beneficio con el capital incremental; "untapped pricing power"), `valor-y-crecimiento` (+1991:
  la matemática bob-around, de 25x a 10x al revisar la expectativa de crecimiento).
- **No duplicado:** el look-through del propio inversor y "watch the field, not the scoreboard"
  ya estaban en `beneficios-retenidos-participadas`; la franquicia vs. negocio, en su página.
- **Estado:** borrador (todas las tocadas).

## [2026-07-09] ingest | re-pase carta 1992 (lectura completa)
- **Fuente:** `raw/1992.pdf`
- **Páginas creadas:** ninguna.
- **Páginas enriquecidas:** `no-predecir-el-mercado` (+1992: "forecasts are poison"; los
  pronosticadores hacen quedar bien a los adivinos), `contra-el-mercado-eficiente` (+1992:
  mercado secundario gobernado por la locura colectiva, x por 1/2x; nueva emisión la controla
  el vendedor), `locura-de-las-adquisiciones` (+1992: el "restructuring charge"; el CEO recibe
  la educación y el accionista paga la matrícula; su propio mea culpa), `candor` (+1992: las
  opciones son un coste real; "calling a tail a leg does not make it a leg").
- **No duplicado:** JBW/DCF y "define what you don't know" ya en `valor-intrinseco` y
  `circulo-de-competencia`; margen de seguridad y valor/crecimiento, en sus páginas.
- **Estado:** borrador (todas las tocadas).

## [2026-07-09] ingest | re-pase carta 1993 (lectura completa)
- **Fuente:** `raw/1993.pdf`
- **Páginas creadas:** ninguna.
- **Páginas enriquecidas:** `mr-market` (+1993: la máquina de votar/pesar de Graham; Coca-Cola
  1919→1920 −50% → 2,1 M/acción), `candor` (+1993: no disparar y luego pintar la diana; fijar el
  objetivo por adelantado).
- **Cambio de estado:** `mr-market` pasa de `estable` a `pendiente` (era la única página estable
  y se ha modificado; queda pendiente de re-revisión).
- **No filado:** el largo tratado sobre gobierno corporativo (tres tipos de consejo) y la
  política de filantropía quedan fuera de la taxonomía del cerebro; contenido ya cubierto de
  1993 (riesgo≠volatilidad, concentración, foso, círculo) no se re-toca.

## [2026-07-09] ingest | re-pase carta 1994 (lectura completa)
- **Fuente:** `raw/1994.pdf` (una de las menos leídas en su día).
- **Páginas creadas:** ninguna.
- **Páginas enriquecidas:** `emitir-acciones-solo-a-su-valor` (+1994: rechazar deals que suben
  el BPA pero bajan el valor intrínseco por acción; "chain letter in reverse"), `circulo-de-
  competencia` (+1994: "degree-of-difficulty doesn't count"; lo difícil no se premia),
  `incentivos-alineados` (+1994: alineamiento = socio en ambas direcciones; "heads I win, tails
  you lose"), `goodwill-economico` (+1994: Scott Fetzer, la amortización del premio no es coste
  económico; el valor intrínseco crece mientras baja el valor en libros).
- **No duplicado:** la definición de valor intrínseco y la analogía de la educación ya están en
  `valor-intrinseco` (1983/1992); el float de 1994 es idéntico al 1995 ya en `float`; el "fear
  is the foe of the faddist" es el 1994 ya en `miedo-y-codicia`; la macro-agnosia, en
  `no-predecir-el-mercado`.
- **Estado:** borrador (todas las tocadas).

## [2026-07-09] ingest | re-pase carta 1995 (lectura completa)
- **Fuente:** `raw/1995.pdf`
- **Páginas creadas:** ninguna.
- **Páginas enriquecidas:** `franquicia-vs-negocio` (+1995: "have-to-be-smart-once" vs
  "have-to-be-smart-every-day"; el sobrino holgazán en una TV vs. el minorista, "to coast is to
  fail"), `locura-de-las-adquisiciones` (+1995: Drucker, "dealmaking beats working... deals that
  make no sense"; sin plan estratégico no hay precio absurdo forzado).
- **No duplicado:** float 1995 y "lumpy 15%" ya en `float` y `riesgo-no-es-volatilidad`; el moat
  de GEICO ya en `ventaja-competitiva`; la candor de la Class B (avisar de que la acción está
  cara, no explotar al comprador poco sofisticado) ya cubierta por `candor`.
- **Estado:** borrador (ambas).

## [2026-07-09] ingest | re-pase carta 1996 (lectura completa)
- **Fuente:** `raw/1996.pdf` (una de las menos leídas en su día).
- **Páginas creadas:** `predecibilidad` (los Inevitables: certeza de lo bueno sobre esperanza de
  lo grande; negocios que apenas cambian; Impostors; la pérdida de foco como mayor amenaza).
- **Páginas enriquecidas:** `fortaleza-financiera-y-liquidez` (+1996: "reverse engineer" /
  máxima invertida de Munger, "where I'm going to die so I'll never go there"; no plantar
  semillas de lo intolerable → no deuda grande), `concentracion` (+1996: la concentración surge
  al dejar correr a los ganadores; no traspasar a Michael Jordan).
- **No duplicado:** "if you aren't willing to own for ten years..." y el goal del inversor ya
  están en `holding-para-siempre`; el moat de GEICO y el círculo definitivo (1996) ya en sus
  páginas; float 1996 y "lumpy 15%" ya cubiertos.
- **Estado:** borrador (todas).

## [2026-07-09] ingest | re-pase carta 1997 (lectura completa)
- **Fuente:** `raw/1997.pdf`
- **Páginas creadas:** ninguna.
- **Páginas enriquecidas:** `mr-market` (+1997: la analogía de la hamburguesa; el ahorrador neto
  debería querer precios bajos; "disinvestors lose, investors gain"), `emitir-acciones-solo-a-su-
  valor` (+1997: la "Confesión" —emitir acciones costó dinero; ceder un bateador de .380; las dos
  condiciones para pagar prima), `disciplina-de-no-actuar` (+1997: al inversor no le cantan
  strikes; la paciencia no se penaliza), `principios-de-suscripcion` (+1997: el ejemplo de los
  dados —la ausencia de pérdidas no valida el precio; el experto sin dinero en la mesa).
- **No duplicado:** "cheery consensus / optimism is the enemy of the rational buyer" ya en
  `miedo-y-codicia` (1990); float 1997 y el círculo/criterios ya cubiertos.
- **Estado:** sin cambios de estado (mr-market y disciplina siguen pendientes; el resto borrador).

## [2026-07-09] ingest | re-pase carta 1998 (lectura completa)
- **Fuente:** `raw/1998.pdf` (una de las menos leídas en su día).
- **Páginas creadas:** ninguna.
- **Páginas enriquecidas:** `candor` (+1998: integridad contable ante la manipulación —"rather
  disappoint with earnings than accounting"; "think about what counts, not how it will be
  counted"; las opciones como coste, el ejemplo de pagar la publicidad con opciones).
- **No filado / no duplicado:** el error de vender McDonald's ya en `holding-para-siempre`; el
  float 1998 ("si el coste sube, el crecimiento es una maldición") ya en `float`; "lumpy 15%"
  (General Re) ya en `riesgo-no-es-volatilidad`; el mandato al gestor (dirigir como dueño a 100
  años) y las adquisiciones GEICO/EJA/General Re son operativos.
- **Estado:** borrador.

## [2026-07-09] ingest | re-pase carta 1999 (lectura completa)
- **Fuente:** `raw/1999.pdf` (una de las menos leídas en su día).
- **Páginas creadas:** ninguna.
- **Páginas enriquecidas:** `recompra-de-acciones` (+1999: las dos condiciones estrictas; recomprar
  por encima del valor daña al que se queda, "dollar bills for $1.10"; crítica de recomprar para
  inflar el precio o compensar opciones), `goodwill-economico` (+1999: el goodwill económico crece
  como la tierra —See's 78 años—; su amortización choca con la realidad, a diferencia de la
  depreciación).
- **No duplicado:** "comfortable business at questionable price" = el 1989 de `buen-negocio-a-precio-
  justo`; el círculo/tech ("no insights into which tech participants have durable advantage") ya en
  `circulo-de-competencia` (1999); look-through ya cubierto. La cautela sobre el nivel del mercado
  (retornos atados al PIB) queda fuera —es una llamada macro puntual, no un principio transferible.
- **Estado:** borrador (ambas).

## [2026-07-09] ingest | re-pase carta 2000 (lectura completa)
- **Fuente:** `raw/2000.pdf`
- **Páginas creadas:** ninguna.
- **Páginas enriquecidas:** `miedo-y-codicia` (+2000: la psicología de la burbuja/codicia —"nothing
  sedates rationality like large doses of effortless money"; Cenicienta; bailar donde los relojes
  no tienen agujas; su lado de la codicia estaba poco desarrollado).
- **No duplicado:** Esopo "bird in the hand" (3 preguntas) ya en `valor-intrinseco` (2000);
  "speculation... not a game we play" / "most dangerous when it looks easiest" ya en
  `valor-y-crecimiento` (2000); la crítica al EBITDA ("tooth fairy pays for capex") y la
  depreciación como coste real reformulan el 1989 de `owner-earnings`; el mea culpa de Dexter
  (pagar con acciones) es el principio de `emitir-acciones` (1997) ya cubierto; adquisiciones,
  operativo.
- **Estado:** borrador.

## [2026-07-09] ingest | re-pase carta 2001 (lectura completa)
- **Fuente:** `raw/2001.pdf` (post-11S)
- **Páginas creadas:** ninguna.
- **Páginas enriquecidas:** `principios-de-suscripcion` (dentro del 2001 ya presente: la regla de
  Noé —"Predicting rain doesn't count; building arks does"—; el error no fue de conocimiento sino
  de no convertir el pensamiento en acción). Sin nuevo año ni cambio de índice.
- **No duplicado:** los tres principios y "experience vs exposure" (2001) ya estaban; "avoid dumb
  decisions rather than brilliant ones" ya en `circulo-de-competencia`; EBITDA/"loss development"
  en `owner-earnings`/`candor`; el mea culpa de Dexter (pagar con acciones) es el principio de
  `emitir-acciones` (1997); "debt is a four-letter word" y los junk bonds ya en `fortaleza`.
- **Estado:** borrador.

## [2026-07-09] ingest | re-pase 1990–2001 COMPLETO
- **Resumen:** releídas enteras las 12 cartas 1990–2001 (que en su día se leyeron en fracciones
  por un atajo grep). Resultado: 2 páginas nuevas (`errores-de-omision`, `predecibilidad`) y ~34
  enriquecimientos en páginas existentes, todos con cita textual + año, sin duplicar. 0
  discrepancias en `check_years.py` tras cada commit. `mr-market` pasó de estable a pendiente.
- **Siguiente:** reanudar la ingesta hacia delante en 2007 (autónoma, resumen cada 5, commit por
  carta, lectura completa).

## [2026-07-09] ingest | carta 2007 (lectura completa)
- **Fuente:** `raw/2007.pdf` ("The Great, the Good and the Gruesome"). Ingesta hacia delante.
- **Páginas creadas:** `negocio-grande-bueno-pesimo` (economía del capital reinvertido: el gran
  negocio —See's— crece sin devorar capital; el bueno —FlightSafety, utilities— exige reinversión;
  el pésimo —aerolíneas— engulle capital y no gana; las tres cuentas de ahorro).
- **Páginas enriquecidas:** `ventaja-competitiva` (+2007: el foso debe ser duradero, no
  reconstruible sin cesar, ni depender de una estrella; "Roman Candles"; Mayo Clinic),
  `emitir-acciones-solo-a-su-valor` (+2007: Dexter cuantificado —400 M → 3.500 M por pagar con
  acciones—, su peor operación), `errores-de-omision` (+2007: rechazar la estación de TV
  Dallas-Fort Worth, negocio "tipo See's", >1.000 M perdidos).
- **No filado:** "helpers / passive must win" ya en `hiperactividad-del-mercado` (Gotrocks 2005);
  opciones-expensing y supuestos de pensiones = `candor`/`owner-earnings`; derivados (uso
  disciplinado: hold the money, sin riesgo de contraparte) y divisas/déficit, macro/operativo.
- **Estado:** borrador (todas las tocadas).

## [2026-07-09] ingest | carta 2008 (lectura completa)
- **Fuente:** `raw/2008.pdf` (la crisis financiera).
- **Páginas creadas:** ninguna.
- **Páginas enriquecidas:** `derivados` (+2008: las advertencias de 2002 cumpliéndose —Bear Stearns,
  la "red de dependencia mutua", la metáfora venérea—; y el uso disciplinado de Berkshire: hold the
  money → sin riesgo de contraparte, el CEO como director de riesgos), `riesgo-no-es-volatilidad`
  (+2008: "beware of geeks bearing formulas"; los modelos históricos fallan cuando el universo
  cambia; la volatilidad pasada no dice nada del valor futuro), `fallar-convencionalmente` (+2008:
  la aprobación no es el objetivo; las grandes decisiones traen bostezos, no aplausos), `fortaleza-
  financiera-y-liquidez` (+2008: "never count on the kindness of strangers"; no cambiar el sueño
  por un beneficio extra).
- **No duplicado:** "price is what you pay, value is what you get" ya en `valor-intrinseco` (1983);
  "pessimism is your friend" en `miedo-y-codicia`; el error de ConocoPhillips/bancos irlandeses y el
  análisis Clayton/hipotecas (HPA, "borrowers who shouldn't have borrowed") son casos/macro.
- **Estado:** borrador (todas las tocadas).

## [2026-07-09] ingest | carta 2009 (lectura completa)
- **Fuente:** `raw/2009.pdf` (compra de BNSF).
- **Páginas creadas:** ninguna.
- **Páginas enriquecidas:** `predecibilidad` (+2009: autos 1910 / aviones 1930 / TV 1950 —ver el
  crecimiento no basta; la competencia diezma a casi todos los que entran), `miedo-y-codicia`
  (+2009: "when it's raining gold, reach for a bucket, not a thimble"; "a climate of fear is your
  best friend"), `emitir-acciones-solo-a-su-valor` (+2009: BNSF —si no venderías la empresa entera
  a ese precio, no la vendas a trozos; la acción sobrevalorada = "counterfeit money"; los asesores
  nunca valoran lo que se entrega, "don't ask the barber").
- **No duplicado:** "invert, always invert" / kindness of strangers ya en `fortaleza` (1996/2008);
  "CEO must own risk control" en `derivados` (2008); el giro a negocios intensivos en capital
  "buenos" ya en `negocio-grande-bueno-pesimo` (2007); Clayton/hipotecas y NetJets, casos.
- **Estado:** borrador (todas las tocadas).

## [2026-07-09] lint | health-check del grafo (41 páginas)
- **Detectado:** 10 páginas huérfanas (0 enlaces entrantes), entre ellas `miedo-y-codicia`, `float`,
  `concentracion`, `derivados`, `holding-para-siempre`, `emitir-acciones-solo-a-su-valor`,
  `errores-de-omision`, `contra-el-mercado-eficiente`, `imperativo-institucional`, `arbitraje`.
  Causa: al crear/enriquecer se añadían enlaces *desde* la página, casi nunca *hacia* ella.
- **Corregido:** enlaces entrantes recíprocos añadidos en `mr-market`, `circulo-de-competencia`,
  `principios-de-suscripcion`, `fortaleza-financiera-y-liquidez`, `hiperactividad-del-mercado`,
  `recompra-de-acciones`, `disciplina-de-no-actuar`, `fallar-convencionalmente`,
  `contra-el-mercado-eficiente`, `buen-negocio-a-precio-justo`.
- **Verificado:** 0 wikilinks rotos, 0 huérfanas, 0 páginas sin salientes, media 3,0 entrantes;
  índice ↔ ficheros coherentes; `check_years` 0 discrepancias.
- **Estado:** sin cambios (añadir un enlace en "Relacionados" es cambio trivial).
- **Deuda abierta:** `check_years.py` sigue fuera del repo (en `/tmp`); 35 páginas en `borrador`
  nunca revisadas.
