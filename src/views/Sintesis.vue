<template lang="pug">
.curso-main-container.pb-3
  BannerInterno(icono="fas fa-sitemap" titulo="Síntesis")
  .container.tarjeta.tarjeta--blanca.p-4.p-md-5.mb-5

    p(data-aos="fade-down") El componente formativo aborda de manera integral los fundamentos de los primeros auxilios en la primera infancia, articulando el marco normativo, los conceptos esenciales, la gestión del riesgo, las medidas de bioseguridad y el rol del primer respondiente. Desde esta perspectiva, se fortalecen las competencias para reconocer situaciones de emergencia, valorar el entorno de forma segura y ejecutar acciones iniciales oportunas que protejan la vida.

    p.mt-4(data-aos="fade-down") De igual forma, se promueve una cultura de prevención orientada a la reducción de riesgos y a la actuación responsable frente a eventos adversos, así como la adecuada activación del sistema de emergencias. Todo ello con el propósito de garantizar una atención articulada, segura y centrada en la protección integral de la vida, la salud y el bienestar de niñas y niños en los diferentes contextos de cuidado.

    p.mt-4.mb-0(data-aos="fade-down") A continuación, el mapa conceptual organiza de manera visual los ejes temáticos del componente formativo y las relaciones que los articulan.

    figure.mt-4(data-aos="fade-down")
      img(src="@/assets/curso/sintesis.svg" alt="El mapa conceptual &quot;Principios de primeros auxilios en primera infancia&quot; organiza los contenidos del componente en seis ejes: generalidades, marco normativo y ético, fundamentos conceptuales y gestión del riesgo, bioseguridad y rol del primer respondiente, botiquín, y evaluación del escenario y toma de decisiones, con sus subtemas. Así, evidencia que la atención inicial es un proceso integral orientado a proteger la vida e integridad de niñas y niños en Colombia. " style="width: 1228px").m-auto

    .row.justify-content-center.mt-5
      .col-auto
        a.anexo(:href="obtenerLink('/downloads/Sintesis.pdf')" target="_blank")
          .anexo__icono
            img(src="@/assets/bullets/icono-pdf.svg")
          .anexo__texto
            p Anexo. Síntesis
</template>

<script>
export default {
  name: 'Sintesis',
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
