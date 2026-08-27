<template lang="pug">
.curso-main-container.introduccion.pb-3
  BannerInterno
  .container.tarjeta.tarjeta--blanca.p-4.p-md-5.mb-5

    .titulo-principal.color-acento-contenido
      .titulo-principal__numero
        span i
      h1 Introducción

    .row
      .col-lg-9
        p(data-aos="fade-down") Los primeros auxilios son la respuesta inmediata, provisional y organizada que se brinda ante una emergencia o urgencia. En la primera infancia, etapa de alta vulnerabilidad, esta actuación oportuna puede marcar la diferencia entre proteger la vida de niñas y niños o agravar una situación de riesgo.

        .bg-1.r-10.p-4.mt-4(data-aos="fade-down")
          p.mb-0 A lo largo de este componente formativo, encontrará los fundamentos que le permitirán actuar con seguridad como primer respondiente: el marco normativo vigente, los conceptos esenciales, las medidas de bioseguridad y la gestión del riesgo en entornos infantiles. Estos saberes fortalecerán su capacidad para evaluar el entorno, tomar decisiones acertadas y activar los servicios de emergencia, tanto en su rol laboral como en la vida cotidiana.

        .row.align-items-start.mt-4(data-aos="fade-down")
          .col-auto.mb-3.mb-lg-0
            figure
              img(src="@/assets/curso/temas/intro/2.png" alt="" style="width: 84px")
          .col
            p.mb-0 Los contenidos se abordan desde un enfoque práctico y adaptado a las características de la primera infancia, con ejemplos aplicados a contextos de atención infantil que orientan el paso a paso de una actuación segura, responsable y humanizada. Por ello, el estudio de este componente se complementa con un recurso audiovisual que contextualiza los temas abordados, facilita la comprensión de su relevancia en situaciones reales y orienta el proceso de aprendizaje desde una perspectiva práctica. Para acceder a este recurso, se recomienda consultar el material audiovisual que acompaña esta sección.

      .col-lg-3.d-none.d-lg-block
        figure
          img(src="@/assets/curso/temas/intro/1.png" alt="" style="width: 292px").m-auto

    .row.justify-content-center.align-items-center.mt-5
      .col-lg-12
        figure(data-aos="fade-down")
          .video
            iframe(width="560" height="315" src="https://www.youtube.com/embed/DC1CjF8waro?si=KnKx32zBBlHGeM2k" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen)


</template>

<script>
export default {
  name: 'Introduccion',
}
</script>

<style lang="sass"></style>
