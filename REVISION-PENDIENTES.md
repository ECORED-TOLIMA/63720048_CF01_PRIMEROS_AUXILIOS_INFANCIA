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
2. **La paleta es la de los hex ESCRITOS de la hoja de especificación**, no la de los rects de
   muestra, que están desincronizados. Y **todo el arte del XD sigue relleno con la paleta vieja**,
   así que se traduce (tabla en `BITACORA.md`): `#FFC0AC`→`#FFB866`, `#FFE6DE`→`#FFEAD1`,
   `#DBC2FA`→`#E3D7FF`, `#F4EDFE`→`#F7F3FF`, `#16D95E`→`#85E336`.
3. **Subtema 2.1 «Lineamientos técnicos SDIS»**: está en la tabla de contenidos del DI.docx, pero
   el artboard del Tema 2 **no dibuja su píldora** (el contenido arranca justo bajo el título del
   tema). Lo dejé en el menú con `hash: 't_2_1'` anclado al primer bloque del tema.

## Falta contenido en las fuentes

4. **La URL del video de la Introducción.** El XD dibuja «Espacio para video» (sin URL) y el
   DI.docx sólo nombra el guion (`Guion_Introduccion_Video_CF01_63720047`, que además cita el
   código **63720047**, no el 63720048 de este componente). Quedó el embed por defecto del
   scaffold.
5. **Las imágenes del cuestionario** (`src/assets/actividad/imagen1..10.png`) son las que trae el
   scaffold, **de otro curso**. El kit reserva su columna sin `v-if`, así que se quedan como
   marcador hasta que lleguen las buenas.
6. **`public/downloads/Sintesis.pdf`** es el del scaffold; se regenerará recortando la página 10
   del PDF de diseño al cerrar la Síntesis.

## Estado

| pantalla | estado |
|---|---|
| Portada (`/`) | hecha |
| Introducción | hecha |
| Temas 1-6 | pendientes |
| Síntesis | pendiente |
| Actividad didáctica | pendiente |
| Glosario / Referencias | pendientes (del DI.docx a `global.js`) |
| Créditos | los del scaffold, por confirmar contra el DI.docx |

Las 13 rutas comprobadas una a una contra el overlay de error de Vite: ninguna rota.
