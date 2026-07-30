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
