<template lang="pug">
.curso-main-container.pb-3
  BannerInterno
  .container.tarjeta.tarjeta--blanca.p-4.p-md-5.mb-5

    .titulo-principal.color-acento-contenido
      .titulo-principal__numero
        span 5
      h1 Botiquín de primeros auxilios

    .row.align-items-start.justify-content-center(data-aos="fade-down")
      .col-lg-4.mb-4.mb-lg-0
        figure
          img(src="@/assets/curso/temas/t5/f1.png" alt="" style="width: 396px").m-auto
      .col-lg-8
        p El botiquín de primeros auxilios es un conjunto organizado de elementos, insumos y materiales básicos destinados a brindar atención inmediata ante situaciones de emergencia o urgencia. Su disponibilidad y adecuado mantenimiento son fundamentales para garantizar una respuesta oportuna y efectiva, especialmente en entornos donde se atiende población infantil.
        .bg-2.p-4.mt-4
          p.mb-0 En el contexto de la primera infancia, el botiquín debe estar adaptado a las necesidades de niñas y niños, asegurando la presencia de elementos básicos que permitan atender lesiones frecuentes como caídas, heridas, golpes o quemaduras leves. Asimismo, debe ubicarse en un lugar accesible, visible y seguro, evitando el acceso directo por parte de los niños y garantizando su uso por personal capacitado.

    p.mt-4(data-aos="fade-down") Para comprender su adecuada conformación y uso, es necesario reconocer el concepto de botiquín y las disposiciones que orientan su disponibilidad en los diferentes entornos. En este sentido, se presentan estos fundamentos y su aplicación en la atención de emergencias relacionadas con la primera infancia.

    separador

    //- ─────────────────────────────── 5.1
    #t_5_1.titulo-segundo.color-acento-contenido
      h2 5.1 Concepto y normativa

    p(data-aos="fade-down") El botiquín de primeros auxilios se define como el conjunto organizado de recursos básicos destinados a brindar atención inicial a una persona lesionada o en situación de emergencia, mientras se accede a servicios de atención médica especializada. Su adecuada dotación y disponibilidad permiten una respuesta oportuna que puede disminuir riesgos, complicaciones y consecuencias derivadas de eventos adversos.

    .row.bg-4.mx-0.mt-4.align-items-center(data-aos="fade-down")
      .col-lg-auto.px-0
        figure.m-0
          img(src="@/assets/curso/temas/t5/f2.png" alt="" style="width: 614px")
      .col-lg.p-4
        .tarjeta.tarjeta--blanca.p-4
          p.mb-0 En Colombia, su uso y disposición se enmarcan en los lineamientos del Sistema de Seguridad y Salud en el Trabajo, así como en las condiciones de habilitación de los servicios de salud establecidas en la Resolución 3100 de 2019, la cual fija estándares de calidad y seguridad en la atención. De igual manera, en los entornos de atención a la primera infancia, los lineamientos de la Secretaría Distrital de Integración Social (SDIS) establecen la obligatoriedad de contar con botiquines adecuados, accesibles y en condiciones óptimas para la atención de emergencias (Ministerio de Salud y Protección Social, 2019).

    p.mt-4(data-aos="fade-down") En Colombia, la disponibilidad y el adecuado manejo del botiquín en los entornos de atención a la primera infancia se sustentan en un conjunto de disposiciones que buscan garantizar condiciones seguras. Estas normas orientan tanto la dotación como el mantenimiento del botiquín, de modo que responda a las necesidades propias de esta población. Entre las principales se encuentran:

    .row.justify-content-center.mt-4
      .col-lg-10
        AcordionA.acordion--principios(tipo="b")
          .row(titulo="A. Resolución 3100 de 2019")
            .col-12
              p.mb-0 Define las condiciones de habilitación y los estándares de calidad y seguridad de los servicios de salud en Colombia, y establece la disponibilidad de insumos básicos para la atención inicial de urgencias en los diferentes entornos de atención a la población.
          .row(titulo="B. Sistema de Gestión de Seguridad y Salud en el Trabajo (SG-SST)")
            .col-12
              p.mb-0 Reglamentado por el Decreto 1072 de 2015, exige que los lugares de trabajo, incluidos jardines y centros infantiles, dispongan de botiquines dotados y accesibles para responder de forma oportuna ante accidentes o situaciones de emergencia.
          .row(titulo="C. Lineamientos técnicos de la SDIS")
            .col-12
              p.mb-0 Establecen la obligatoriedad de contar con botiquines adecuados, accesibles y en condiciones óptimas en los servicios de educación inicial dirigidos a la primera infancia, como parte de los estándares de calidad para la atención integral de niñas y niños.

    p.mt-4(data-aos="fade-down") El cumplimiento de estas disposiciones garantiza que los espacios de atención dispongan de condiciones mínimas de seguridad, permitiendo actuar de manera eficaz ante situaciones que puedan afectar la salud y el bienestar de niñas y niños, y contribuyendo a la protección integral de esta población.

    separador

    //- ─────────────────────────────── 5.2
    #t_5_2.titulo-segundo.color-acento-contenido
      h2 5.2 Clasificación y elementos del botiquín

    .row.align-items-start(data-aos="fade-down")
      .col-lg-9
        p La clasificación del botiquín depende de las características del entorno, el número de personas atendidas y los riesgos identificados. En los espacios destinados a la primera infancia, su dotación debe facilitar la atención inicial y permitir una respuesta organizada mientras se determina la necesidad de asistencia especializada.
        p.mt-4 En hogares, jardines infantiles y centros de desarrollo infantil, la selección de los elementos debe considerar las lesiones que pueden presentarse con mayor frecuencia:
        .bg-3.p-4.mt-4
          ul.lista-ul.lista-ul--compacta.mb-0
            li
              i.fas.fa-heart
              b  Caídas:
              |  pueden ocasionar raspaduras, heridas, golpes o lesiones en diferentes partes del cuerpo.
            li
              i.fas.fa-heart
              b  Heridas:
              |  producen ruptura de la piel y pueden generar sangrado o riesgo de contaminación.
            li
              i.fas.fa-heart
              b  Golpes:
              |  pueden causar dolor, inflamación, hematomas o limitación temporal del movimiento.
            li
              i.fas.fa-heart
              b  Quemaduras leves:
              |  afectan superficialmente la piel por contacto con objetos calientes, líquidos u otras fuentes de calor.
      .col-lg-3.mt-4.mt-lg-0
        figure
          img(src="@/assets/curso/temas/t5/f3.png" alt="" style="width: 292px").m-auto

    p.mt-4(data-aos="fade-down") El reconocimiento de estas situaciones permite seleccionar y organizar los elementos básicos del botiquín de acuerdo con las necesidades del entorno. Asimismo, su contenido debe revisarse periódicamente para verificar el estado, la limpieza, la integridad y la fecha de vencimiento de los productos.

    p.mt-4(data-aos="fade-down") La siguiente tabla presenta la clasificación general de los botiquines, sus características, los entornos en los que pueden utilizarse y sus elementos principales.

    .row.justify-content-center.mt-4(data-aos="fade-down")
      .col-lg-10
        .titulo-sexto.color-acento-contenido.mb-3
          h5 Tabla 4.
          span Clasificación y elementos del botiquín de primeros auxilios
        .tabla-a.tabla--normativa.color-acento-contenido
          table
            thead
              tr
                th Tipo de botiquín
                th Características
                th Uso recomendado
                th Elementos principales
            tbody
              tr
                td
                  b Tipo A
                td Botiquín básico para atención inicial en entornos de bajo riesgo.
                td Jardines infantiles, hogares, oficinas.
                td Gasas, vendas, esparadrapo, solución salina, guantes, tijeras, termómetro.
              tr
                td
                  b Tipo B
                td Botiquín intermedio con mayor dotación para atención de eventos más complejos.
                td Instituciones con mayor número de personas o riesgos moderados.
                td Incluye elementos del tipo A más inmovilizadores, apósitos especiales, entre otros.
              tr
                td
                  b Tipo C
                td Botiquín avanzado para atención de emergencias más complejas.
                td Ambientes de alto riesgo o brigadas especializadas.
                td Incluye equipos más completos para atención avanzada (uso restringido).

    p.mt-4(data-aos="fade-down") La selección del botiquín debe responder a los riesgos identificados y a las características del lugar. Sus elementos permiten brindar atención básica; sin embargo, no sustituyen la valoración del personal de salud cuando la lesión requiere atención especializada.

    p.mt-4(data-aos="fade-down") Para garantizar su disponibilidad y uso seguro, es necesario mantener el botiquín organizado y verificar periódicamente las condiciones de sus elementos. Con este propósito, se deben considerar los siguientes aspectos:

    .row.justify-content-center.mt-4(data-aos="fade-down")
      .col-lg-10
        .bg-3.p-4
          .row.align-items-center
            .col-lg-8
              ol.lista-ol--cuadro.lista-numerada--cuadro.mb-0
                li
                  span.lista-ol--cuadro__vineta
                    span 1
                  |  Mantener el botiquín limpio, ordenado y en buen estado.
                li
                  span.lista-ol--cuadro__vineta
                    span 2
                  |  Revisar periódicamente los productos para identificar aquellos vencidos o deteriorados.
                li
                  span.lista-ol--cuadro__vineta
                    span 3
                  |  Reponer oportunamente los elementos después de utilizarlos.
                li
                  span.lista-ol--cuadro__vineta
                    span 4
                  |  Ubicarlo en un lugar visible y accesible para las personas responsables.
                li
                  span.lista-ol--cuadro__vineta
                    span 5
                  |  Mantenerlo fuera del alcance de las niñas y los niños.
            .col-lg-4.d-none.d-lg-block
              figure.mb-0
                img(src="@/assets/curso/temas/t5/f4.png" alt="" style="width: 292px").m-auto

    p.mt-4(data-aos="fade-down") El cumplimiento de estas condiciones permite conservar adecuadamente los elementos del botiquín y disponer de ellos de manera oportuna durante una emergencia.

    .row.align-items-center.mt-4(data-aos="fade-down")
      .col-lg-3.d-none.d-lg-block
        figure
          img(src="@/assets/curso/temas/t5/f5.png" alt="" style="width: 292px").m-auto
      .col-lg-9
        p El botiquín de primeros auxilios constituye un recurso esencial que facilita la atención inicial en situaciones de emergencia, permitiendo al primer respondiente actuar de manera oportuna y organizada. Su adecuada dotación y uso se articulan con la bioseguridad y la gestión del riesgo, fortaleciendo la capacidad de respuesta en entornos de atención a la primera infancia.
        .bg-1.p-4.mt-4
          p.mb-0 La disponibilidad de un botiquín organizado complementa las medidas necesarias para brindar una atención inicial segura. Sin embargo, antes de utilizar sus elementos, el primer respondiente debe analizar las condiciones del lugar, identificar los peligros presentes y establecer las acciones prioritarias. En este sentido, se aborda la evaluación del escenario y la toma de decisiones.

</template>

<script>
export default {
  name: 'Tema5',
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
