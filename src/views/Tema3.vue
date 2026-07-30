<template lang="pug">
.curso-main-container.pb-3
  BannerInterno
  .container.tarjeta.tarjeta--blanca.p-4.p-md-5.mb-5

    .titulo-principal.color-acento-contenido
      .titulo-principal__numero
        span 3
      h1 Fundamentos conceptuales y gestión del riesgo

    .row.align-items-start.justify-content-center(data-aos="fade-down")
      .col-lg-4.mb-4.mb-lg-0
        figure
          img(src="@/assets/curso/temas/t3/f1.png" alt="" style="width: 396px").m-auto
      .col-lg-8
        p Este eje temático integra los conceptos básicos de primeros auxilios y las acciones necesarias para identificar, analizar y controlar los factores de riesgo. Su comprensión permite interpretar una emergencia, emplear la terminología adecuada y orientar una respuesta inicial segura y oportuna.
        .bg-3.r-10.p-4.mt-4
          .row.align-items-center
            .col-auto
              figure.mb-0
                img(src="@/assets/curso/temas/t3/i1.png" alt="" style="width: 84px")
            .col
              p.mb-0 En el contexto de la primera infancia, la comprensión de estos fundamentos adquiere especial relevancia debido a la vulnerabilidad de las niñas y los niños frente a los riesgos del entorno. Para orientar una respuesta inicial segura y oportuna, se deben reconocer los siguientes conceptos:

    .row.justify-content-center.mt-5(data-aos="fade-down")
      .col-md-6.col-lg-3
        .tarjeta.bg-4.r-20.tarjeta--icono-arriba
          figure
            img(src="@/assets/curso/temas/t3/i3.png" alt="")
          p.text-center.mb-2(style="font-size:1.125em")
            b Emergencia
          p.text-center.mb-0 Situación crítica que amenaza la vida y requiere atención inmediata de servicios especializados.
      .col-md-6.col-lg-3
        .tarjeta.bg-4.r-20.tarjeta--icono-arriba
          figure
            img(src="@/assets/curso/temas/t3/i4.png" alt="")
          p.text-center.mb-2(style="font-size:1.125em")
            b Urgencia
          p.text-center.mb-0 Situación que necesita atención pronta, aunque no representa peligro vital inmediato para alguien.
      .col-md-6.col-lg-3
        .tarjeta.bg-4.r-20.tarjeta--icono-arriba
          figure
            img(src="@/assets/curso/temas/t3/i5.png" alt="")
          p.text-center.mb-2(style="font-size:1.125em")
            b Peligro
          p.text-center.mb-0 Fuente, condición o acción con capacidad de causar lesiones, daños o afectaciones graves.
      .col-md-6.col-lg-3
        .tarjeta.bg-4.r-20.tarjeta--icono-arriba
          figure
            img(src="@/assets/curso/temas/t3/i6.png" alt="")
          p.text-center.mb-2(style="font-size:1.125em")
            b Riesgo
          p.text-center.mb-0 Probabilidad de que un peligro cause daño, según la exposición y vulnerabilidad existentes.

    p.mt-5(data-aos="fade-down") La diferenciación de estos conceptos permite interpretar rápidamente lo ocurrido, tomar decisiones responsables y evitar actuaciones improvisadas que puedan agravar la situación.

    .row.justify-content-center.mt-4(data-aos="fade-down")
      .col-lg-10
        .cajon.color1.p-4
          p.mb-0 Asimismo, la gestión del riesgo aporta una mirada preventiva que complementa la atención inicial. Identificar y controlar de manera anticipada los factores de riesgo presentes en hogares, jardines infantiles y centros de desarrollo integral contribuye a reducir la ocurrencia de accidentes y a proteger la vida de la población infantil.

    p.mt-4(data-aos="fade-down") De esta manera, los fundamentos conceptuales y la gestión del riesgo se articulan como la base sobre la cual se construye una respuesta segura, organizada y oportuna.

    separador

    //- ─────────────────────────────── 3.1
    #t_3_1.titulo-segundo.color-acento-contenido
      h2 3.1 Fundamentos conceptuales

    p(data-aos="fade-down") Los fundamentos conceptuales permiten comprender los términos básicos necesarios para la atención en primeros auxilios, facilitando la identificación de situaciones de emergencia, la valoración del riesgo y la toma de decisiones adecuadas. Estos conceptos son esenciales para actuar de manera organizada, segura y coherente frente a eventos que puedan afectar la salud, especialmente en la primera infancia.

    p.mt-4(data-aos="fade-down") A continuación, se presentan los principales conceptos aplicados en primeros auxilios:

    .row.justify-content-center.mt-4(data-aos="fade-down")
      .col-lg-10
        .titulo-sexto.color-acento-contenido.mb-3
          h5 Tabla 3.
          span Conceptos básicos en primeros auxilios
        .tabla-a.tabla--normativa.color-acento-contenido
          table
            thead
              tr
                th Concepto
                th Definición
                th Aplicación en primeros auxilios
            tbody
              tr
                td
                  b Emergencia
                td Situación que pone en riesgo la vida de una persona y requiere atención inmediata.
                td Permite priorizar la atención y actuar de forma urgente para preservar la vida.
              tr
                td
                  b Urgencia
                td Situación que requiere atención rápida, pero no compromete de manera inmediata la vida.
                td Permite organizar la atención según la gravedad del caso.
              tr
                td
                  b Negligencia
                td Falta de cuidado o de atención ante una situación que lo requiere.
                td Evitar omitir acciones necesarias en la atención de la persona afectada.
              tr
                td
                  b Imprudencia
                td Actuar sin precaución o sin considerar los riesgos.
                td Evitar acciones apresuradas que puedan generar daño.
              tr
                td
                  b Impericia
                td Falta de conocimiento o habilidad para realizar una acción.
                td No realizar procedimientos para los cuales no se está capacitado.
              tr
                td
                  b Peligro
                td Situación o condición con potencial de causar daño.
                td Identificar riesgos en el entorno antes de intervenir.
              tr
                td
                  b Riesgo
                td Probabilidad de que un peligro cause daño.
                td Evaluar la posibilidad de afectación para tomar decisiones.
              tr
                td
                  b Accidente
                td Evento inesperado que causa lesión o daño.
                td Reconocer situaciones que requieren atención inmediata.
              tr
                td
                  b Factor de riesgo
                td Condición que aumenta la probabilidad de un accidente.
                td Identificar condiciones inseguras en entornos infantiles.

    p.mt-4(data-aos="fade-down") Estos conceptos permiten al primer respondiente interpretar adecuadamente las situaciones que se presentan, diferenciando entre niveles de gravedad y reconociendo los riesgos asociados al entorno. Su comprensión facilita una actuación más segura, evitando errores como la negligencia, la imprudencia o la impericia.

    p.mt-4(data-aos="fade-down") En el contexto de la primera infancia, la aplicación de estos fundamentos permite:

    .row.justify-content-center.mt-4(data-aos="fade-down")
      .col-lg-10
        .bg-3.p-4
          .row.align-items-center
            .col-lg-7
              ol.lista-ol--cuadro.lista-numerada--cuadro.mb-0
                li
                  span.lista-ol--cuadro__vineta
                    span 1
                  |  Identificar los factores de riesgo presentes en el entorno.
                li
                  span.lista-ol--cuadro__vineta
                    span 2
                  |  Diferenciar una urgencia de una emergencia.
                li
                  span.lista-ol--cuadro__vineta
                    span 3
                  |  Reconocer situaciones que requieren atención inmediata.
                li
                  span.lista-ol--cuadro__vineta
                    span 4
                  |  Prevenir accidentes frecuentes.
                li
                  span.lista-ol--cuadro__vineta
                    span 5
                  |  Valorar las condiciones de seguridad antes de intervenir.
                li
                  span.lista-ol--cuadro__vineta
                    span 6
                  |  Tomar decisiones oportunas y responsables.
                li
                  span.lista-ol--cuadro__vineta
                    span 7
                  |  Evitar actuaciones que puedan agravar la situación.
                li
                  span.lista-ol--cuadro__vineta
                    span 8
                  |  Aplicar medidas básicas de prevención y protección.
                li
                  span.lista-ol--cuadro__vineta
                    span 9
                  |  Solicitar apoyo especializado cuando sea necesario.
                li
                  span.lista-ol--cuadro__vineta
                    span 10
                  |  Fortalecer la protección integral de niñas y niños.
            .col-lg-5.d-none.d-lg-block
              figure.mb-0
                img(src="@/assets/curso/temas/t3/f2.png" alt="" style="width: 366px").r-10.m-auto

    .row.align-items-start.mt-4(data-aos="fade-down")
      .col-auto
        figure.mb-0
          img(src="@/assets/curso/temas/t3/i2.png" alt="" style="width: 84px")
      .col
        p.mb-0 La aplicación de estos fundamentos favorece la prevención de accidentes y orienta una actuación inicial segura, organizada y acorde con las necesidades de la primera infancia.
        p.mt-3.mb-0 A partir del reconocimiento de los conceptos y factores de riesgo, es necesario comprender las acciones orientadas a identificar, analizar y controlar las condiciones que pueden ocasionar daños. Por ello, a continuación, se aborda la gestión del riesgo.

    separador

    //- ─────────────────────────────── 3.2
    #t_3_2.titulo-segundo.color-acento-contenido
      h2 3.2 Gestión del riesgo

    .row.align-items-start(data-aos="fade-down")
      .col-lg-3.d-none.d-lg-block
        figure
          img(src="@/assets/curso/temas/t3/f3.png" alt="" style="width: 292px").r-10.m-auto
      .col-lg-9
        p La gestión del riesgo en primeros auxilios corresponde al conjunto de acciones orientadas a identificar, analizar y controlar los factores que pueden generar daño en una situación de emergencia. En el contexto de la primera infancia, su aplicación es fundamental debido a la mayor vulnerabilidad de niñas y niños frente a condiciones inseguras en su entorno.
        .cajon.color1.p-4.mt-4
          p.mb-0 Este proceso inicia con la identificación de los riesgos presentes en el lugar, los cuales pueden ser de tipo físico, biológico, ambiental o humano. Posteriormente, se realiza un análisis del riesgo, valorando la probabilidad de que ocurra un evento adverso y las posibles consecuencias para la persona afectada. Esta valoración permite priorizar las acciones de atención y establecer medidas de control adecuadas.

    p.mt-4(data-aos="fade-down") La gestión del riesgo también incluye la implementación de acciones preventivas orientadas a reducir la ocurrencia de accidentes. Estas acciones pueden involucrar la eliminación de peligros, la adecuación de espacios seguros y la supervisión constante, especialmente en entornos donde se encuentran niñas y niños.

    .row.justify-content-center.mt-5(data-aos="fade-down")
      .col-lg-10
        .tarjeta.bg-6.tarjeta--badge-arriba.px-4.pb-4
          figure
            img(src="@/assets/curso/temas/t3/i7.png" alt="")
          p.text-center.mb-0 En el marco de los primeros auxilios, es fundamental que el primer respondiente evalúe el entorno antes de intervenir, identificando posibles peligros que puedan afectar tanto a la víctima como a sí mismo.

    p.mt-4(data-aos="fade-down") La gestión del riesgo se desarrolla mediante acciones relacionadas que permiten reconocer los peligros, valorar sus posibles consecuencias y establecer medidas de protección. A continuación, se presentan las principales acciones que orientan este proceso:

    .row.justify-content-center.mt-4(data-aos="fade-down")
      .col-sm-6.col-lg-3.mb-4.mb-lg-0
        .tarjeta--boton.color-1.p-4.h-100
          .row.justify-content-center.mb-3
            .col-7
              figure
                img.icono(src="@/assets/curso/temas/t3/i8.png" alt="")
                img.icono-hover(src="@/assets/curso/temas/t3/o1.png" alt="")
          h3.text-center Identificación del peligro
          p.text-small.text-center.mb-0 Reconoce las condiciones, los objetos o las acciones que pueden causar daño.
      .col-sm-6.col-lg-3.mb-4.mb-lg-0
        .tarjeta--boton.color-1.p-4.h-100
          .row.justify-content-center.mb-3
            .col-7
              figure
                img.icono(src="@/assets/curso/temas/t3/i9.png" alt="")
                img.icono-hover(src="@/assets/curso/temas/t3/o2.png" alt="")
          h3.text-center Análisis del riesgo
          p.text-small.text-center.mb-0 Valora la probabilidad de que ocurra un evento y sus posibles consecuencias.
      .col-sm-6.col-lg-3.mb-4.mb-sm-0
        .tarjeta--boton.color-1.p-4.h-100
          .row.justify-content-center.mb-3
            .col-7
              figure
                img.icono(src="@/assets/curso/temas/t3/i10.png" alt="")
                img.icono-hover(src="@/assets/curso/temas/t3/o3.png" alt="")
          h3.text-center Control del riesgo
          p.text-small.text-center.mb-0 Aplica medidas para eliminar el peligro o reducir sus posibles efectos.
      .col-sm-6.col-lg-3
        .tarjeta--boton.color-1.p-4.h-100
          .row.justify-content-center.mb-3
            .col-7
              figure
                img.icono(src="@/assets/curso/temas/t3/i11.png" alt="")
                img.icono-hover(src="@/assets/curso/temas/t3/o4.png" alt="")
          h3.text-center Prevención
          p.text-small.text-center.mb-0 Implementa acciones anticipadas para evitar accidentes y proteger a la primera infancia.

    p.mt-4(data-aos="fade-down") La aplicación articulada de estas acciones permite reducir la exposición a situaciones peligrosas y fortalecer la seguridad en los entornos de atención a la primera infancia.

    p.mt-4(data-aos="fade-down") Este proceso orienta la toma de decisiones del primer respondiente y favorece una actuación organizada ante situaciones de emergencia. En la primera infancia, permite anticipar condiciones que pueden afectar la vida y la integridad. Para su aplicación, se consideran las siguientes acciones:

    .row.justify-content-center.mt-4(data-aos="fade-down")
      .col-lg-10
        .bg-3.p-4
          .row.align-items-center
            .col-lg-7
              ol.lista-ol--cuadro.lista-numerada--cuadro.mb-0
                li
                  span.lista-ol--cuadro__vineta
                    span A
                  |  Identificar los peligros presentes en el entorno.
                li
                  span.lista-ol--cuadro__vineta
                    span B
                  |  Analizar las situaciones que pueden ocasionar daños.
                li
                  span.lista-ol--cuadro__vineta
                    span C
                  |  Valorar las posibles consecuencias.
                li
                  span.lista-ol--cuadro__vineta
                    span D
                  |  Establecer medidas preventivas.
                li
                  span.lista-ol--cuadro__vineta
                    span E
                  |  Eliminar o reducir las condiciones peligrosas.
                li
                  span.lista-ol--cuadro__vineta
                    span F
                  |  Verificar la seguridad del lugar.
                li
                  span.lista-ol--cuadro__vineta
                    span G
                  |  Priorizar las necesidades de atención.
                li
                  span.lista-ol--cuadro__vineta
                    span H
                  |  Aplicar los protocolos establecidos.
                li
                  span.lista-ol--cuadro__vineta
                    span I
                  |  Solicitar apoyo especializado.
                li
                  span.lista-ol--cuadro__vineta
                    span J
                  |  Verificar la efectividad de las medidas implementadas.
            .col-lg-5.d-none.d-lg-block
              figure.mb-0
                img(src="@/assets/curso/temas/t3/f4.png" alt="" style="width: 282px").r-10.m-auto

    .row.align-items-center.mt-4(data-aos="fade-down")
      .col-lg-3.d-none.d-lg-block
        figure
          img(src="@/assets/curso/temas/t3/f5.png" alt="" style="width: 292px").r-10.m-auto
      .col-lg-9
        p La aplicación ordenada de estas acciones facilita la toma de decisiones y fortalece la protección integral de las niñas y los niños, de acuerdo con los protocolos institucionales y las rutas de atención establecidas en Colombia.
        p.mt-4 En la primera infancia, la gestión del riesgo requiere especial atención debido a la curiosidad, la movilidad y la dependencia del cuidado adulto. La consideración de estas características permite anticipar situaciones peligrosas, establecer medidas preventivas y proteger la vida y la integridad de las niñas y los niños.
        p.mb-0.mt-4 Una vez reconocidas las acciones para gestionar los riesgos del entorno, es necesario considerar las medidas que protegen al primer respondiente y a la persona afectada durante la atención.

</template>

<script>
export default {
  name: 'Tema3',
  mounted() {
    this.$nextTick(() => {
      this.$aosRefresh()
    })
  },
  updated() {
    this.$aosRefresh()
  },
}
</script>

<style lang="sass"></style>
