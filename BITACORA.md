# BITÁCORA — CF1_63720048 · Principios de primeros auxilios en primera infancia

Repo propio del entregable (`ECORED-TOLIMA/pruebas-plantilla-manuel-v2`, rama `master`).
Fuentes en `fuentes/`: `CF1_63720048.xd`, `CF1_63720048.pdf`, `63720048_CF01_DI.docx`,
`63720048_CF01_AD.docx`. Servidor: `npm run serve` → http://localhost:5173/CF1_63720048/

## Reglas de trabajo de este repo

- **`commit` + `push` de CADA sección terminada**, sin esperar aprobación: la Action del repo
  despliega a **GitHub Pages al pushear a `master`**, así que el push es la forma en que Luis
  revisa. Después de cada push se comprueba que la Action pasó.
  - local: http://localhost:5173/CF1_63720048/
  - publicado: https://ecored-tolima.github.io/pruebas-plantilla-manuel-v2/
- **No se pregunta nada.** Cada bifurcación se decide desde el XD + PDF + DOCX y se anota en
  `REVISION-PENDIENTES.md` con el porqué.
- `.gitignore`: el `.xd` descomprimido (`/fuentes/CF1_63720048/`, 64 MB, lo genera `config.py`).

## Mapa artboard → pantalla → página, y offsets

Los `XD_DX`/`XD_DY` salen **directamente del `manifest` del XD** (`uxdesign#bounds`: `DX=-x`,
`DY=-y`), no hace falta medir con `offsets.py` (que además no encuentra la tarjeta blanca en la
portada porque ahí no hay). Comprobado: coincide con `offsets.py` en la Introducción y el Tema 1.

| artboard | nombre en el XD | pantalla | pág | XD_DX | XD_DY | alto |
|---|---|---|---|---|---|---|
| 75feec5f | Portada | Portada | 1 | 14030 | 11707 | 1647 |
| 15bbf878 | Introduccion | Introducción | 2 | 12274 | 11700 | 1413 |
| 4e18ab8b | Tema-1 | 1 · Generalidades de los primeros auxilios | 3 | 10506 | 11700 | 7977 |
| 4d52d5f3 | Tema-2 | 2 · Marco normativo y ético | 4 | 7761 | 11700 | 7846 |
| 043a7b89 | Tema-3 | 3 · Fundamentos conceptuales y gestión del riesgo | 5 | 4498 | 11700 | 4946 |
| 6f483d33 | Tema-4 | 4 · Bioseguridad y rol del primer respondiente | 6 | 2600 | 11700 | 7620 |
| 5a49f3ff | Tema-5 | 5 · Botiquín de primeros auxilios | 7 | −277 | 11700 | 3917 |
| 9075a584 | Tema-6 | 6 · Evaluación del escenario y toma de decisiones | 8 | −2783 | 11700 | 11411 |
| b9ed25b2 | Tablet | Tablet/Móvil — **no se maqueta** | 9 | 14044 | 9904 | 894 |
| 39c2a691 | Sintesis – PDF | Síntesis (hoja del anexo) | 10 | 14044 | 8854 | 1494 |

Aquí los **nombres de capa SÍ son fiables** (`Tema-1`..`Tema-6`), verificado contra el `h1` de
cada artboard. 10 artboards / 10 páginas, todas asignadas.

## Paleta — de la HOJA DE ESPECIFICACIÓN, no de los rects de muestra

La hoja de swatches del artboard de la portada está **desincronizada**: el rect de muestra y el
hex escrito al lado no coinciden en 3 de los 4 colores. **Manda el hex ESCRITO** (regla de Luis,
2026-07-29; el PDF pinta el rect porque se exportó con la paleta vieja).

| variable | hex escrito (**el bueno**) | rect de muestra |
|---|---|---|
| 1 · primario | `#8EC5FC` | `#8EC5FC` (coincide) |
| 2 · secundario | `#E3D7FF` | `#DBC2FA` |
| 3 · acento contenido | `#FFB866` | `#FFC0AC` |
| 4 · acento botón | `#85E336` | `#16D95E` |
| 5 · terciario | `#F6F0E8` / `#FDFCFB` | — |

Variables (VC = clara, V = variable, VO = oscura): 1 `#DDEEFE`/`#F3F9FF`/`#394F65`,
2 `#F7F3FF`/`#FCFBFF`/`#5B5666`, 3 `#FFEAD1`/`#FFF8EF`/`#594023`, 4-VC `#F3FCEA`.

## Correcciones de arranque aplicadas (hallazgos de Luis del 2026-07-29)

1. Texto de los botones → **negro** (`.boton *` en BASE lo fuerza a `$white`).
2. Número/ícono del título de tema → **negro**.
3. Fondo del hero → **el grupo del XD entero** (`Enmascarar grupo 1119221`), no capas compuestas
   a mano en PIL.
4. Ninguna nota con «barra lateral» inventada; las cajas con pestaña de 25×8 son `.cajon`.
5. `?noaos` + `html.noaos` para congelar AOS y la transición del acordeón en las capturas.

## Portada (pág 1) — hecha

- `Enmascarar grupo 1119221` = **todo** el fondo del hero: página **(136,100) 1328×559**. Ojo:
  su `transform` dice `tx=5079,ty=2649` pero su hijo `Rectángulo 455427` va **rotado 180°**
  (`a=-1,d=-1`) y lo recoloca; la posición real hay que sacarla del **bbox acumulado**, nunca del
  `tx/ty`. Dentro lleva 8 capas: el degradado (lavanda `#E3D7FF` → azul `#97CBFF`), la textura
  `Recurso 1` en **multiply 0.6**, tres grupos de adornos a 0.2/0.2/0.3, los anillos y una foto
  JPG en **soft-light 0.7**. Chrome aplica los `blendMode` él solo.
- **⚠️ El hero del PDF es un FLATTEN MALO.** En el PDF sale gris/violeta oscuro con el texto azul
  marino casi ilegible: el exportador aplastó el `multiply` y el `soft-light` como si fueran
  normales. En el XD el degradado es CLARO y el texto es `#12263F`, que sobre claro sí se lee. Se
  maquetó **según el XD** (hero claro + texto oscuro) y se quitó el `color: $white` de BASE.
  El reparto de tonos sí coincide con el PDF (azul arriba-izquierda, lila/magenta a la derecha).
- Ilustración = **composición de hermanos**: la forma crema `Trazado 1001976` (894,190 432×432)
  detrás del recorte sin fondo `Enmascarar grupo 1119222` (857,153 506×506). Se saca con
  `--rect 857 153 506 506` y `--excluir-rect` para las dos fichas flotantes, que las pone el CSS.
- Fichas flotantes: teléfono en **(857,382)** y corazón en **(1273,472)**, las dos 90×90. Se
  anclan con `right`/`bottom` en px desde la esquina inferior derecha de `.banner-principal__img`
  (que coincide con la de la tarjeta) → caen en la coordenada exacta del XD aunque el
  `.container` de bootstrap mida 1320 y no los 1328 del XD.
- `$banner-principal-img-y: 'abajo'`: en el XD la ilustración va **pegada al borde inferior** del
  hero (153+506 = 659 = borde inferior del panel).
- El ancho del texto del hero es el `col-xxl-5` que ya trae el kit (≈490, el `frameW` del XD):
  se **quitó** el override de BASE que lo ensanchaba a 58.33 %.
- `vite.config.js`: `base` `/NUEVA_BASE_TOLIMA/` → `/CF1_63720048/`.

## Introducción (pág 2) — hecha

- El banner de cabecera de las secciones es **otro grupo**: `Enmascarar grupo 1119228`, página
  **(0,70) 1600×220** (misma receta que el hero: degradado + `Recurso 1` en multiply + la foto en
  soft-light). El `BannerInterno` del kit reusa `fondoBannerPrincipal`, así que se sobreescribe
  `.banner-interno__fondo` en `_custom.sass`. En el PDF sale oscuro por lo mismo que el hero.
- Assets (correlación contra la pág 2): imagen derecha `Enmascarar grupo 1119242` (1121,316)
  292×396 → **0.9934**; ícono `Grupo 1181743` (185,573) 84×84 → **0.9429**.
- Rejilla: `.row > .col-lg-9` (texto, 915 en el XD) `+ .col-lg-3` (imagen, 292).
- El aviso es `Rectángulo 456415` 916×130 `r=10` **sin pestaña** → no es `.cajon`, es un fondo
  plano redondeado (`.bg-1`).
- La fila ícono+texto va con `.col-auto + .col` (el ícono pegado al borde, el texto a ~104px),
  igual que en CF01.
- **El video no tiene URL en ninguna fuente** (el XD dibuja «Espacio para video» y el DI sólo
  nombra `Guion_Introduccion_Video_CF01_63720047`). Se deja el embed por defecto que trae el
  scaffold y queda anotado como pendiente.

## Tema 1 (pág 3) — hecho

Artboard `4e18ab8b`, `XD_DX=10506 XD_DY=11700`, tarjeta 1328×7760. 4 subtemas.

**Assets: 25, todos verificados por correlación contra la pág 3.** Fotos enmascaradas con
`regen_fotos.py` (`f2` 0.992, `f3` 0.981, `f4` 0.991, `f5` 0.987); íconos y aviso 84
(0.94-0.98); fondos decorativos y Figura 1 con `--grupo`.

- **`f6` (la ilustración del 1.3) es una COMPOSICIÓN de hermanos**, no un grupo: forma de color
  `Trazado 1003382` + recorte `Enmascarar grupo 1119237` + adorno `Trazado 1003383`. Con
  `--grupo` daba **0.524**; con `fit_composicion.py` (que selecciona las capas por NOMBRE y busca
  escala/offset por correlación), **0.9771** — y la escala que encuentra (0.773× del nodo) es el
  `scaleX` del pattern que el pipeline ignora.
- **Tres fondos decorativos full-bleed** (`Grupo 1184123` 1328×254, `Grupo 1178002` 1328×483,
  `Grupo 1184136` 1328×254) con la receta `.row.bg-fondo-N > .col-12 > .p-5`. Su correlación sale
  ~0.00 porque en el PDF llevan ENCIMA las tarjetas y el acordeón que pone el HTML: es normal.
- **Las pestañas de 25×8 existen y son 3**: `Rectángulo 401461` (290,1142), `456434` (498,4067) y
  `456438` (186,5341) → esos tres avisos son `.cajon`, y ningún otro. Los demás son rects con
  `r=10` sin pestaña.
- **La Figura 1 SÍ tiene variante móvil en el pasteboard**: `Grupo 1183114`, 400×1130, con el
  mismo contenido apilado en vertical. Va con el `img` móvil PRIMERO
  (`d-block.d-md-none` + `d-none.d-md-block`).
- Componentes: `AcordionA(tipo="b")` para los 5 principios del 1.2 (botón = círculo del
  acento-botón a la derecha, comprobado en el PDF), `LineaTiempoD` para las 5 características del
  1.3, `SlyderF` para los 5 principios del 1.4 (el XD dibuja 3 y las flechas; los otros 2 salen
  del DI.docx).
- El **tinte del arte `#B8F4CE` es el 30 % del VIEJO `#16D95E`**; con el hex bueno (`#85E336`) el
  equivalente es **`#DAF7C3`** → `$color-4-30`. Está en la tabla de remapeo.
- 26 elementos con `data-aos`, **0 sin `aos-animate`** con el viewport cubriendo la página.

## Traducción de la paleta VIEJA del arte a la de la spec

Los nodos del XD siguen rellenos con los colores de los **rects de muestra**. Barriendo los
rellenos de los 9 artboards, la traducción es:

| en el arte del XD | va como |
|---|---|
| `#FFC0AC` | `$color-acento-contenido` `#FFB866` |
| `#FFE6DE` | 3-VC `#FFEAD1` |
| `#DBC2FA` | `$color-secundario` `#E3D7FF` |
| `#F4EDFE` | 2-VC `#F7F3FF` |
| `#16D95E` | `$color-acento-botones` `#85E336` |
| `#8EC5FC` `#DDEEFE` `#F3F9FF` `#394F65` | ya coinciden con la spec |

## Pendiente de decisión de Luis
- Subtema **2.1 «Lineamientos técnicos SDIS»**: está en la tabla de contenidos del DI.docx pero
  el artboard del Tema 2 **no dibuja la píldora del 2.1** (el contenido arranca justo bajo el
  título del tema). Va en el menú con `hash: 't_2_1'` anclado al primer bloque.


## Temas 2-6, Síntesis, Actividad y los datos de `global.js` — hechos

| pantalla | artboard / pág | assets | notas |
|---|---|---|---|
| Tema 2 · Marco normativo y ético | 4d52d5f3 / 4 | 6 fotos (0.94-0.998) + 11 íconos + 2 fondos | 2 tablas, 2 `SlyderF`, `LineaTiempoD`, pódcast, infografía de redes |
| Tema 3 · Fundamentos y gestión del riesgo | 043a7b89 / 5 | 5 fotos (0.983-0.995) + 11 íconos | Tabla 3, dos listas de 10 (1-10 y A-J) |
| Tema 4 · Bioseguridad y rol | 6f483d33 / 6 | 7 fotos (0.914-0.993) + 14 íconos + 1 fondo | `AcordionA`, 3 tarjetas de EPP, figura de riesgos |
| Tema 5 · Botiquín | 5a49f3ff / 7 | 5 fotos (0.859-0.993) | panel azul con la foto sangrando, Tabla 4 |
| Tema 6 · Evaluación del escenario | 9075a584 / 8 | 9 fotos (0.979-0.998) + 23 íconos + 3 fondos | la pantalla más larga (11.196 px), 2 `SlyderF`, 2 `AcordionA`, Tabla 5, Figura 2 |
| Síntesis | 39c2a691 / 10 | mapa 1228×900 | el artboard es la HOJA DEL ANEXO; la pantalla se maqueta con la convención del kit |
| Actividad didáctica | — (no hay artboard) | — | 20 preguntas del `_AD.docx`, el kit muestra 10 barajadas |

**Lo que hubo que descubrir en esta tanda:**

- **`ActividadController` NO está en los componentes globales del kit**
  (`GlobalComponents.js` no lo registra) → hay que importarlo en la vista o Vue avisa
  «Failed to resolve component» y la pantalla sale **vacía, sin ningún error visible**.
- **El contrato del cuestionario del kit** es `pregunta.texto` (no `pregunta`),
  `opciones: [{id, texto, esCorrecta}]`, `mensaje_correcto` / `mensaje_incorrecto` por pregunta y
  `titulo_aprobado` / `mensaje_final_aprobado` / `titulo_reprobado` / `mensaje_final_reprobado` en el
  cuestionario. El prefijo «¡Correcto!» se quita del texto del docx porque el componente ya lo pinta.
- **La misma composición de hermanos** (`Trazado 1003382` + `Enmascarar grupo 1119237` +
  `Trazado 1003383`) se repite en los temas 1, 2 y 4, siempre con `regen_fotos` dando 0.52-0.69 y
  `fit_composicion.py` subiéndolo a 0.94-0.98.
- **`regen_fotos.py` renumera y puede sobreescribir** un asset generado a mano antes con el mismo
  nombre: correr primero `regen_fotos` y después los `--grupo` puntuales, no al revés.
- Las **dos infografías interactivas** (2.5 y 4.3) van como figura estática: los textos de sus
  puntos «+» no están en el XD (el pasteboard sólo trae las etiquetas) ni en el DI.docx.
