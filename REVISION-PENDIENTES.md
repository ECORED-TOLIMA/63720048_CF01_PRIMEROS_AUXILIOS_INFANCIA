# Revisión y pendientes — CF1_63720048

Lo que **no se pudo resolver desde las fuentes** (`.xd`, `.pdf`, `_DI.docx`, `_AD.docx`) y las
decisiones que tomé yo para no parar. Todo lo demás sale de las fuentes.

## Decisiones que tomé (por si hay que revertirlas)

1. **El hero y el banner de cabecera van CLAROS, no oscuros como el PDF.** El grupo del XD
   (`Enmascarar grupo 1119221`) es un degradado lavanda `#E3D7FF` → azul `#97CBFF` con la textura
   `Recurso 1` en `multiply 0.6` y una foto en `soft-light 0.7`. El exportador del PDF aplastó esos
   dos `blendMode` como si fueran normales, y por eso en el PDF el panel sale gris/violeta oscuro
   **con el texto `#12263F` del propio XD casi ilegible encima**. Me quedo con el XD: fondo claro y
   texto oscuro (quitando el `color: $white` que fuerza BASE). Mismo criterio en el banner de
   cabecera de todas las secciones, que es otro grupo (1600×220) con la misma receta.
2. ~~La paleta es la de los hex ESCRITOS de la hoja de especificación~~ → **REVERTIDO el
   2026-07-30 por hallazgo de Luis**: «los colores de los elementos background deben ser
   exactamente el color propuesto en el XD». El `fill` de cada nodo manda para ESE elemento
   (`#FFC0AC`, `#FFE6DE`, `#F4EDFE`, `#DBC2FA`, `#B8F4CE`); `remapear_paleta()` quedó como
   identidad y se regeneraron TODOS los assets. La única variable que se queda con el hex escrito
   es `$color-acento-botones: #85E336`, que él mismo corrigió en su día y no marcó ahora.
3. **Subtema 2.1 «Lineamientos técnicos SDIS»**: está en la tabla de contenidos del DI.docx, pero
   el artboard del Tema 2 **no dibuja su píldora** (el contenido arranca justo bajo el título del
   tema). Lo dejé en el menú con `hash: 't_2_1'` anclado al primer bloque del tema.

4. **El RADIO de cada caja y de cada foto se lee del XD**, no se pone a granel. Las clases `.bg-N`
   son sólo color; el radio va en `.r-0/.r-5/.r-10/.r-20` según el `r=[...]` del rect o de la
   máscara. Hay cajas **sin radio** (cuadradas del todo) y fotos **con** radio (10 o 20).
5. **A 390 px de ancho el contenido se corta por la derecha** en todas las pantallas: viene del
   ancho mínimo efectivo (~480 px) de la infraestructura del kit, no de la maquetación. A 768 px
   todo apila bien.

## Falta contenido en las fuentes

6. **La URL del video de la Introducción.** El XD dibuja «Espacio para video» (sin URL) y el
   DI.docx sólo nombra el guion (`Guion_Introduccion_Video_CF01_63720047`, que además cita el
   código **63720047**, no el 63720048 de este componente). Quedó el embed por defecto del
   scaffold.
7. **Las imágenes del cuestionario** (`src/assets/actividad/imagen1..10.png`) son las que trae el
   scaffold, **de otro curso**. El kit reserva su columna sin `v-if`, así que se quedan como
   marcador hasta que lleguen las buenas.
8. **Los textos de las dos infografías interactivas no están en ninguna fuente.** El 2.5 «Redes de
   atención ante emergencias» y el 4.3 «Manejo adecuado de los riesgos biológicos» se dibujan en el
   XD con seis etiquetas y un «+» cada una, pero la descripción que debería abrir cada punto no está
   ni en el pasteboard del XD (que sólo trae las etiquetas) ni en el DI.docx. Van maquetadas como
   **figura estática** con el render exacto del XD, para no inventar contenido.
9. **Los créditos son los del scaffold.** El DI.docx sólo nombra, en «CONTROL DEL DOCUMENTO», a
   **Laura Briguitte Perea Possos** (experta temática) y **Gloria Lida Alzate Suárez** (evaluadora
   instruccional) — ya corregidos. Los demás roles (diseño, desarrollo, validación) se quedan como
   los trae la plantilla porque el DI no los nombra.
10. **Las referencias no traen URL.** Las siete son normas y publicaciones citadas sin enlace en el
    DI.docx, así que van con `link: ''` (el componente omite el ancla).

## De `Hallazgos(5)` — lo que queda por cerrar

- **«Los fondos no salen completos»**: no lo he tocado en esta ronda. Lo que aplico ahora es el
  `margin-inline: -6.2rem` + `background-size: cover`; falta compararlo 1:1 con tu referencia.
- **«Mal la imagen»** y **«Faltó la imagen»** (imágenes 7-8 y 15-16 del documento): no he
  identificado a qué bloque se refieren. Dime el subtema y lo cierro.
- **«Los iconos con fondo negro» del Tema 3**: audité los 20 assets del tema y el render. Los
  glifos salen en los colores del XD (`#584E64`, `#59433C`, `#394F65`), el negro opaco es del 0 % y
  no hay ninguna zona negra en la pantalla. **No lo he podido reproducir**; si lo estás viendo en
  GitHub Pages puede ser del build, no del código.
- **Las posiciones de los puntos de la infografía del 2.5** las repartí yo (la ilustración no tiene
  nodos identificables por punto). Las del 4.3 sí salen de los nodos del XD.

## Revisión final de esta sesión (2026-07-30)

**Negrillas — comprobado contra el DOCX, no por criterio propio.** El `_DI.docx` tiene **214 runs en
negrilla** de 782 con texto, **2 en cursiva y 0 tachados**. Verifiqué uno a uno los términos que puse
en `b`: `Curiosidad:`, `Proteger la integridad:`, `Higiene de manos:`, `Emergencia:`, `Caídas:` van
**bold en el DOCX** → mi `b` es correcto. En cambio **`Tipo A` / `Tipo B` / `Tipo C` de la Tabla 4
NO van en negrilla en el DOCX** y yo los puse con `b`: hay que quitarlo.

**Saltos de línea.** El DOCX no tiene ningún `<w:br/>`, pero **60 nodos de texto del XD llevan salto
de línea interno**. Buena parte son listas que ya separé en `li`, pero **no los he revisado uno a
uno**: los que sean un salto real dentro de un párrafo necesitan `br`.

**Altos.** Sin resolver y sin cifra fiable: dos intentos de medirlo automáticamente midieron la
ventana, no el contenido (render = XD + 5999 exacto en los seis temas). Hay que medir por CDP el alto
de `.container.tarjeta--blanca` y compararlo con el alto del artboard.

**Negrillas corregidas**: quitada la de `Tipo A` / `Tipo B` / `Tipo C` en la Tabla 4 del Tema 5,
porque en el DOCX esos runs NO van en negrilla.

**El acordeón del Tema 6 — lo que ya comprobé y NO explica el fallo** (para no repetir el trabajo):
- los **colores y radios son idénticos** en los tres acordeones del curso: abierto `#F4EDFE` `r=20`,
  cerrados `#B8F4CE` `r=20` (`457001`+`456997..457000` en el 6.3, `456556`+`456557..456559` en el
  6.5, `456995`+`456991..` en el T1);
- el **número de ítems cuadra** con el XD en los cuatro: T1=5, T4=5, T5=3, **T6=[5, 4]**;
- el render de los dos del T6 se ve igual que los buenos (abierto lila, cerrados verdes, botón
  circular verde a la derecha).
→ Falta el dato de **qué** está mal (¿el ancho? ¿el ítem que va abierto? ¿el alto del abierto?
¿el texto?). Es lo primero que hay que aclarar; no toqué nada por no inventar una corrección.

**Lo que marcó Luis al final y NO he revisado todavía** (primero de la próxima sesión):
- **algunos colores de fondo siguen mal**: toca cruzar CADA `.bg-N` de las 7 vistas contra el
  `(fill, r)` del inventario, no solo los que salieron en los hallazgos.

## Estado

| pantalla | estado |
|---|---|
| Portada (`/`) | hecha |
| Introducción | hecha |
| Temas 1-6 | hechos |
| Síntesis | hecha |
| Actividad didáctica | hecha (20 preguntas del `_AD.docx`) |
| Glosario / Referencias | hechos (12 términos y 7 referencias del DI.docx) |
| Créditos | del scaffold, con la experta temática corregida al DI.docx |

Las 13 rutas comprobadas una a una contra el overlay de error de Vite: ninguna rota.
