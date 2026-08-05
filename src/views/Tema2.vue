<template lang="pug">
.curso-main-container.pb-3
  BannerInterno
  .container.tarjeta.tarjeta--blanca.p-4.p-md-5.mb-5

    .titulo-principal.color-acento-contenido
      .titulo-principal__numero
        span 2
      h1 Marco normativo y ético

    //- ─────────────────────────────── 2.1 Lineamientos técnicos SDIS
    .row.align-items-start.justify-content-center(data-aos="fade-down")
      .col-lg-8
        p La atención en primeros auxilios en la primera infancia se sustenta en un marco normativo y ético que orienta la actuación del primer respondiente, garantizando intervenciones seguras, responsables y acordes con la protección integral de niñas y niños. Este marco establece los lineamientos que regulan la atención en salud, los derechos del paciente y las condiciones mínimas para una respuesta oportuna ante situaciones de emergencia.
        .bg-2.r-10.p-4.mt-4
          p.mb-0 El conocimiento del componente normativo permite al primer respondiente comprender el alcance y los límites de su actuación, así como las responsabilidades asociadas a la atención inicial. A su vez, el componente ético orienta la conducta durante la intervención, promoviendo una atención basada en el respeto por la dignidad humana, la protección de la vida y la no generación de daño adicional.
      .col-lg-4.mt-4.mt-lg-0
        figure
          img(src="@/assets/curso/temas/t2/f2.png" alt="" style="width: 396px").m-auto

    p.mt-4 En este sentido, la actuación en primeros auxilios no solo implica saber qué hacer, sino actuar conforme a principios legales y éticos que aseguren una atención adecuada, especialmente en la primera infancia, donde se requiere un enfoque diferencial y de especial protección.

    separador
    #t_2_1.titulo-segundo.color-acento-contenido
      h2 2.1 Lineamientos técnicos SDIS

    .row.align-items-center.mt-4.justify-content-center(data-aos="fade-down")
      .col-lg-4.d-none.d-lg-block
        figure
          img(src='@/assets/curso/temas/t2/9.png', alt='', style="width: 390px").m-auto
      .col-lg-8
        p Los lineamientos técnicos establecidos por la Secretaría Distrital de Integración Social (SDIS) orientan la prestación de los servicios dirigidos a la primera infancia, especialmente en jardines infantiles y otros entornos de atención integral. Estas orientaciones buscan promover condiciones seguras, prevenir situaciones de riesgo y proteger la vida, la integridad y el bienestar de la población infantil.

        p.bg-1.r-10.p-4.mt-4.mb-0 En este marco, el talento humano debe contar con conocimientos básicos de primeros auxilios, reconocer los factores de riesgo presentes en el entorno y actuar oportunamente ante una emergencia. Esta preparación permite brindar una respuesta inicial segura, activar las rutas institucionales y articular la atención con los servicios de salud y emergencia del Distrito.

    .row.justify-content-center.mt-5(data-aos="fade-down")
      .col-lg-10
        .tarjeta.bg-6.tarjeta--badge-arriba.px-4.pb-4
          figure
            img(src="@/assets/curso/temas/t2/i1.png" alt="")
          p.text-center.mb-0 La gestión del riesgo permite identificar peligros y prevenir accidentes. También favorece la supervisión permanente y la creación de entornos seguros para la primera infancia.

    p.mt-4(data-aos="fade-down") La aplicación de estas orientaciones requiere integrar acciones preventivas y procedimientos básicos de respuesta. A continuación, se presentan los principales aspectos que debe considerar el talento humano en los servicios de atención a la primera infancia:

    .row.bg-fondo-4.mt-4
      .col-12
        .p-5
          .row.justify-content-center
            .col-11
              SlyderF.slyder--principios(columnas="col-md-6 col-lg-4")
                .tarjeta.bg-4.r-20.p-4.h-100
                  figure
                    img(src="@/assets/curso/temas/t2/i2.png" alt="" style="width: 128px").m-auto
                  p.text-center.mt-3.mb-2(style="font-size:1.125em")
                    b Prevención
                  p.text-center.mb-0 Consiste en identificar los peligros presentes en los espacios de atención y aplicar medidas que disminuyan la posibilidad de accidentes. Incluye supervisar las actividades, conservar los elementos peligrosos fuera de alcance y promover prácticas de cuidado acordes con la edad y el desarrollo de la población infantil.
                .tarjeta.bg-4.r-20.p-4.h-100
                  figure
                    img(src="@/assets/curso/temas/t2/i3.png" alt="" style="width: 128px").m-auto
                  p.text-center.mt-3.mb-2(style="font-size:1.125em")
                    b Seguridad del entorno
                  p.text-center.mb-0 Implica verificar las condiciones del lugar antes de brindar ayuda. Se deben reconocer riesgos como fuego, electricidad, sustancias tóxicas, objetos inestables o tránsito vehicular, y restringir el ingreso al área afectada cuando sea seguro hacerlo.
                .tarjeta.bg-4.r-20.p-4.h-100
                  figure
                    img(src="@/assets/curso/temas/t2/i4.png" alt="" style="width: 128px").m-auto
                  p.text-center.mt-3.mb-2(style="font-size:1.125em")
                    b Respuesta inicial
                  p.text-center.mb-0 Corresponde a los cuidados inmediatos y provisionales que se brindan ante un accidente o una enfermedad repentina. Comprende valorar el estado general y aplicar únicamente acciones conocidas y seguras, mientras se solicita la intervención del personal especializado.
                .tarjeta.bg-4.r-20.p-4.h-100
                  figure
                    img(src="@/assets/curso/temas/t2/1.svg" alt="" style="width: 128px").m-auto
                  p.text-center.mt-3.mb-2(style="font-size:1.125em")
                    b Protección integral
                  p.text-center.mb-0 Comprende el cuidado de la integridad física y del bienestar emocional durante la emergencia. Requiere mantener una comunicación calmada, proteger la privacidad, evitar intervenciones que puedan causar daños y considerar las características propias de la primera infancia.
                .tarjeta.bg-4.r-20.p-4.h-100
                  figure
                    img(src="@/assets/curso/temas/t2/2.svg" alt="" style="width: 128px").m-auto
                  p.text-center.mt-3.mb-2(style="font-size:1.125em")
                    b Activación de la ruta de emergencia
                  p.text-center.mb-0 Consiste en solicitar oportunamente el apoyo especializado cuando la situación supera la capacidad de actuación del primer respondiente. Se debe activar la línea 123, proporcionar información clara, comunicar la ubicación exacta y seguir las indicaciones recibidas.

    .row.align-items-start.mt-4(data-aos="fade-down")
      .col-auto
        figure.mb-0
          img(src="@/assets/curso/temas/t2/i5.png" alt="" style="width: 84px")
      .col
        p.mb-0 La integración de estos aspectos favorece la prevención de accidentes y una actuación organizada. Su aplicación debe articularse con los protocolos, el plan de emergencias y las rutas de atención definidas en cada servicio de la SDIS.
        p.mt-3.mb-0 Para sustentar estas actuaciones y garantizar la protección integral de la primera infancia, a continuación, se presentan las principales disposiciones normativas aplicables en materia de salud y emergencias.

    separador

    //- ─────────────────────────────── 2.2
    #t_2_2.titulo-segundo.color-acento-contenido
      h2 2.2 Normativa en salud y emergencias

    .row.align-items-center.justify-content-center(data-aos="fade-down")
      .col-lg-4.mb-4.mb-lg-0
        figure
          img(src="@/assets/curso/temas/t2/f3.png" alt="" style="width: 396px").m-auto
      .col-lg-8
        p La atención en primeros auxilios en Colombia se enmarca en disposiciones que reconocen el derecho fundamental a la salud y la protección integral de la primera infancia. La Ley Estatutaria 1751 de 2015 garantiza el acceso oportuno, eficaz y con calidad a los servicios de salud; por su parte, la Ley 1098 de 2006 reconoce a las niñas y los niños como sujetos de especial protección. Estas disposiciones orientan una respuesta oportuna, segura y sin barreras ante situaciones que puedan afectar su vida e integridad (Ley 1098 de 2006; Ley Estatutaria 1751 de 2015).
        p.mb-0.mt-4 A continuación, se presentan las principales normas que sustentan la atención en primeros auxilios y emergencias en el contexto colombiano:

    .row.justify-content-center.mt-4(data-aos="fade-down")
      .col-lg-10
        .titulo-sexto.color-acento-contenido.mb-3
          h5 Tabla 1.
          span Normativa en salud y emergencias aplicable a primeros auxilios
        .tabla-a.tabla--normativa.color-acento-contenido
          table
            thead
              tr
                th Norma
                th Año
                th Descripción
                th Aplicación en primeros auxilios
            tbody
              tr
                td
                  b Ley 1751
                td 2015
                td Establece la salud como derecho fundamental y garantiza el acceso a servicios de salud sin barreras.
                td Obliga a brindar atención inmediata en urgencias, priorizando la vida y la integridad.
              tr
                td
                  b Ley 1098 (Código de Infancia y Adolescencia)
                td 2006
                td Reconoce a niñas y niños como sujetos de especial protección.
                td Exige actuación oportuna para proteger la vida, salud e integridad de la infancia.
              tr
                td
                  b Resolución 3100
                td 2019
                td Define las condiciones de habilitación y calidad de los servicios de salud en Colombia.
                td Garantiza que la atención de urgencias se realice bajo estándares de calidad y seguridad.
              tr
                td
                  b Resolución 3280
                td 2018
                td Establece el modelo de atención integral en salud con enfoque preventivo y diferencial.
                td Orienta la atención con enfoque en promoción, prevención y atención integral en infancia.
              tr
                td
                  b Sistema General de Seguridad Social en Salud (SGSSS)
                td Vigente
                td Regula la prestación de servicios de salud en Colombia.
                td Garantiza la atención inicial de urgencias sin importar afiliación.
              tr
                td
                  b Sistema de Emergencias Médicas (SEM)
                td Vigente
                td Organiza la respuesta ante emergencias mediante redes articuladas de atención.
                td Permite activar servicios de emergencia a través de la línea 123 para respuesta oportuna.

    p.mt-4(data-aos="fade-down") Este marco normativo orienta la atención en primeros auxilios hacia una actuación responsable, oportuna y centrada en la protección de derechos, especialmente en la primera infancia. Su conocimiento permite al primer respondiente actuar con mayor seguridad, articulando la atención inicial con los servicios de salud y garantizando una respuesta adecuada ante situaciones de emergencia.

    p.mt-4(data-aos="fade-down") El conocimiento del marco normativo permite orientar la actuación del primer respondiente y proteger integralmente a la primera infancia. A partir de estas disposiciones, es necesario reconocer los derechos que deben respetarse durante la prestación de los primeros auxilios.

    separador

    //- ─────────────────────────────── 2.3
    #t_2_3.titulo-segundo.color-acento-contenido
      h2 2.3 Derechos del paciente

    .row.align-items-start(data-aos="fade-down")
      .col-lg-9
        p En la atención de primeros auxilios es fundamental garantizar el respeto por los derechos del paciente, especialmente en el caso de niñas y niños, quienes son sujetos de especial protección. Estos derechos orientan la actuación del primer respondiente hacia una atención digna, segura y centrada en la persona, evitando prácticas que vulneren su integridad física, emocional o psicológica.
        .bg-1.p-4.mt-4
          p.mb-0 En el contexto colombiano, los derechos del paciente están respaldados por la Ley 1751 de 2015, que reconoce la salud como un derecho fundamental autónomo, y por la Ley 1098 de 2006 – Código de la Infancia y la Adolescencia, que establece la protección integral de niñas, niños y adolescentes como un deber del Estado, la familia y la sociedad. En este sentido, toda intervención en primeros auxilios debe realizarse conforme a estos principios, incluso en situaciones de emergencia, garantizando el respeto por la dignidad humana y el interés superior del niño.
      .col-lg-3.mt-4.mt-lg-0
        figure
          img(src="@/assets/curso/temas/t2/f4.png" alt="" style="width: 292px").r-10.m-auto

    p.mt-4(data-aos="fade-down") El respeto por los derechos del paciente orienta una actuación humanizada, segura y responsable durante la prestación de los primeros auxilios. A continuación, se presentan estos derechos mediante definiciones breves y ejemplos que facilitan su aplicación en situaciones relacionadas con la primera infancia.

    .row.align-items-center.justify-content-center.mt-4
      .col-lg-4.d-none.d-lg-block
        figure(data-aos="fade-up")
          img(src="@/assets/curso/temas/t2/f5.png" alt="" style="width: 397px").m-auto
      .col-lg-6
        LineaTiempoD.linea-tiempo--caracteristicas.linea-bold
          .row(numero="1" titulo="Derecho a la vida y a la integridad personal")
            .col-12
              p.mb-0 Garantiza que toda actuación proteja la vida y evite daños físicos o emocionales. Por ejemplo, ante una caída, se mantiene al niño en una posición segura y no se realizan movimientos que puedan agravar una posible lesión.
          .row(numero="2" titulo="Derecho a recibir atención oportuna")
            .col-12
              p.mb-0 Permite brindar ayuda inmediata ante una situación que pueda comprometer la salud o la vida. Por ejemplo, si una niña presenta dificultad para respirar, se activa la ruta de emergencia y se aplican acciones básicas seguras.
          .row(numero="3" titulo="Derecho a la confidencialidad")
            .col-12
              p.mb-0 Protege la información personal y médica conocida durante la atención, evitando divulgarla sin autorización. Por ejemplo, los datos sobre el accidente de un niño se comunican únicamente a sus responsables y al personal autorizado que brinda apoyo.
          .row(numero="4" titulo="Derecho al consentimiento informado")
            .col-12
              p.mb-0 Permite explicar las acciones que se realizarán y solicitar autorización cuando las circunstancias lo permitan. Por ejemplo, antes de revisar una lesión leve, se informa al responsable del niño sobre el procedimiento y su finalidad de manera clara.
          .row(numero="5" titulo="Derecho a no ser abandonado")
            .col-12
              p.mb-0 Garantiza acompañamiento continuo hasta que la atención quede a cargo de una persona responsable o del servicio especializado. Por ejemplo, el primer respondiente permanece junto a la niña, la tranquiliza y espera la llegada del apoyo solicitado.

    p.mt-4(data-aos="fade-down") El respeto de estos derechos permite brindar una atención humanizada, segura y centrada en el bienestar de la primera infancia. A partir de este enfoque, es necesario reconocer las responsabilidades que orientan la actuación del primer respondiente durante una emergencia.

    separador

    //- ─────────────────────────────── 2.4
    #t_2_4.titulo-segundo.color-acento-contenido
      h2 2.4 Responsabilidad del primer respondiente

    p El primer respondiente es la persona que brinda atención inicial en una situación de emergencia o urgencia antes de la llegada de los servicios de salud. Su actuación implica una responsabilidad fundamental orientada a proteger la vida, reducir riesgos y garantizar una atención adecuada dentro de sus capacidades.

    .row.align-items-start(data-aos="fade-down")
      .col-lg-9
        
        .bg-1.p-4.mt-4
          p.mb-0 En el contexto de la primera infancia, esta responsabilidad adquiere mayor relevancia debido a la condición de vulnerabilidad de niñas y niños, quienes requieren una atención oportuna, segura y respetuosa de sus derechos. Por ello, el primer respondiente debe actuar con criterio, prudencia y responsabilidad, evitando intervenciones que puedan generar daño o agravar la situación.

        p.mt-4(data-aos="fade-down") El primer respondiente debe reconocer las responsabilidades que orientan su actuación durante una emergencia. Estas permiten organizar la atención inicial, proteger a las personas involucradas y actuar dentro de los límites de su formación. A continuación, se presentan las principales responsabilidades y su alcance:
      .col-lg-3.mt-4.mt-lg-0
        figure
          img(src="@/assets/curso/temas/t2/f6.png" alt="" style="width: 292px").r-10.m-auto

    

    .row.bg-fondo-5.mt-4
      .col-12
        .p-5
          .row.justify-content-center
            .col-11
              SlyderF.slyder--principios(columnas="col-md-6 col-lg-4")
                .tarjeta.bg-4.r-20.p-4.h-100
                  figure
                    img(src="@/assets/curso/temas/t2/i7.png" alt="" style="width: 128px").m-auto
                  p.text-center.mt-3.mb-2(style="font-size:1.125em")
                    b Actuar de manera oportuna
                  p.text-center.mb-0 Consiste en responder sin demoras injustificadas ante una emergencia, después de verificar que el entorno sea seguro. Requiere reconocer las necesidades prioritarias, tomar decisiones responsables y brindar la ayuda inicial necesaria, de acuerdo con la situación y las capacidades del primer respondiente en ese momento.
                .tarjeta.bg-4.r-20.p-4.h-100
                  figure
                    img(src="@/assets/curso/temas/t2/i8.png" alt="" style="width: 128px").m-auto
                  p.text-center.mt-3.mb-2(style="font-size:1.125em")
                    b Garantizar la seguridad
                  p.text-center.mb-0 Implica proteger al primer respondiente, a la persona afectada y a quienes se encuentran cerca. Exige identificar peligros, controlar riesgos cuando sea posible y evitar acciones que puedan ocasionar nuevas lesiones o agravar las condiciones presentes durante la atención inicial de la situación de emergencia.
                .tarjeta.bg-4.r-20.p-4.h-100
                  figure
                    img(src="@/assets/curso/temas/t2/i9.png" alt="" style="width: 128px").m-auto
                  p.text-center.mt-3.mb-2(style="font-size:1.125em")
                    b Proteger la vida
                  p.text-center.mb-0 Consiste en priorizar las acciones orientadas a conservar las funciones vitales y prevenir el agravamiento de la persona afectada. Requiere valorar su estado general, reconocer signos de alarma y brindar únicamente la atención inicial necesaria mientras llega el apoyo especializado solicitado oportunamente.
                .tarjeta.bg-4.r-20.p-4.h-100
                  figure
                    img(src="@/assets/curso/temas/t2/3.svg" alt="" style="width: 128px").m-auto
                  p.text-center.mt-3.mb-2(style="font-size:1.125em")
                    b Activar el sistema de emergencias
                  p.text-center.mb-0 Implica solicitar apoyo especializado cuando la situación supera las capacidades del primer respondiente. Requiere comunicar claramente lo ocurrido, proporcionar la ubicación exacta, describir el estado de la persona afectada y seguir las instrucciones suministradas por el personal encargado del servicio de emergencias.
                .tarjeta.bg-4.r-20.p-4.h-100
                  figure
                    img(src="@/assets/curso/temas/t2/4.svg" alt="" style="width: 128px").m-auto
                  p.text-center.mt-3.mb-2(style="font-size:1.125em")
                    b Evaluar la situación
                  p.text-center.mb-0 Consiste en observar cuidadosamente el entorno y valorar el estado general de la persona afectada antes de intervenir. Permite identificar peligros, reconocer necesidades prioritarias, determinar la ayuda requerida y tomar decisiones seguras, evitando actuaciones apresuradas que puedan aumentar los riesgos existentes durante la emergencia.
                .tarjeta.bg-4.r-20.p-4.h-100
                  figure
                    img(src="@/assets/curso/temas/t2/5.svg" alt="" style="width: 128px").m-auto
                  p.text-center.mt-3.mb-2(style="font-size:1.125em")
                    b Actuar dentro de sus competencias
                  p.text-center.mb-0 Implica realizar únicamente procedimientos conocidos, seguros y acordes con la formación recibida. El primer respondiente debe reconocer sus límites, evitar maniobras para las cuales no está capacitado y solicitar ayuda especializada cuando las necesidades de atención superen su capacidad de actuación durante la emergencia.
                .tarjeta.bg-4.r-20.p-4.h-100
                  figure
                    img(src="@/assets/curso/temas/t2/6.svg" alt="" style="width: 128px").m-auto
                  p.text-center.mt-3.mb-2(style="font-size:1.125em")
                    b Brindar acompañamiento
                  p.text-center.mb-0 Consiste en permanecer junto a la persona afectada, transmitir tranquilidad y mantener una comunicación respetuosa durante la atención. También requiere observar posibles cambios en su estado, proteger su privacidad y facilitar la entrega de información al personal especializado cuando asuma la atención de la emergencia.

    p.mt-4(data-aos="fade-down") El cumplimiento de estas responsabilidades favorece una atención inicial organizada, segura y centrada en la protección de la vida. Su aplicación permite actuar con criterio, respetar los límites de intervención y facilitar la continuidad de la atención por parte del personal especializado.

    .row.justify-content-center.mt-4(data-aos="fade-down")
      .col-lg-10
        .cajon.color1.p-4
          p.mb-0 Para fortalecer la comprensión de estos contenidos, se presenta un recurso de audio sobre la actuación del primer respondiente ante una emergencia en primera infancia. En este se explican sus responsabilidades, los límites de su intervención y la importancia de actuar con seguridad, ética y serenidad mientras llega la atención especializada.

    .row.justify-content-center.mt-4(data-aos="fade-down")
      .col-lg-10
        //- La imagen va A SANGRE sobre el panel: en el XD la imagen (1020x227) y el panel
        //- (1020x160) tienen el MISMO ancho y no hay padding lateral. El `.p-4` sólo envuelve la
        //- tarjeta blanca de dentro, como en el ejemplo del catálogo.
        figure.mb-0
          img(src="@/assets/curso/temas/t2/f7.png" alt="").w-100
        .bg-4.p-4
          .tarjeta.bg-white.p-4
            TarjetaAudio.tarjeta-audio--podcast(
              texto="Pódcast"
              tiempo
              :audio="require_src('@/assets/curso/temas/t2/audios/63720048_CF01_Guion_podcast.mp3')")

    p.mt-4(data-aos="fade-down") La actuación responsable del primer respondiente contribuye a proteger la vida, prevenir complicaciones y brindar apoyo inicial a la niña o al niño afectado. Sin embargo, esta atención requiere la articulación con instituciones y servicios especializados; por ello, a continuación, se presentan las redes de atención y su importancia en la respuesta oportuna ante una emergencia.

    separador

    //- ─────────────────────────────── 2.5
    #t_2_5.titulo-segundo.color-acento-contenido
      h2 2.5 Redes de atención

    .row.align-items-start(data-aos="fade-down")
      .col-lg-9
        p Las redes de atención en salud corresponden al conjunto organizado de servicios, instituciones y actores que intervienen de manera articulada para dar respuesta oportuna, continua y eficaz ante una situación de emergencia. Estas redes permiten coordinar acciones desde la atención inicial brindada por el primer respondiente hasta la intervención especializada en los servicios de salud, garantizando la continuidad del cuidado y la protección de la vida.
        .row.align-items-start.mt-4
          .col-auto
            figure.mb-0
              img(src="@/assets/curso/temas/t2/i6.png" alt="" style="width: 84px")
          .col
            p.mb-0 El reconocimiento de los actores que conforman las redes de atención permite comprender cómo se coordinan durante una emergencia. A continuación, se presenta un recurso infográfico que explica sus funciones y su aporte a la atención oportuna y a la continuidad del cuidado.
      .col-lg-3.mt-4.mt-lg-0
        figure
          img(src="@/assets/curso/temas/t2/7.svg" alt="" style="width: 290px").m-auto

    .row.justify-content-center.mt-4
      .col-lg-10
        ImagenInfografica.color-acento-botones.d-none.d-md-block
          template(v-slot:imagen)
            figure
              img(src="@/assets/curso/temas/t2/info-redes.svg" alt="").w-100
          .tarjeta.color-primario.p-3(x="11%" y="30%" numero="+")
            .h5.mb-2 1. Articulación entre niveles
            p.mb-0 Integra los niveles de atención para garantizar respuestas organizadas, oportunas y continuas durante cada emergencia.
          .tarjeta.color-primario.p-3(x="11%" y="56%" numero="+")
            .h5.mb-2 2. Servicios de emergencia
            p.mb-0 Atienden situaciones urgentes, activan recursos disponibles y coordinan inicialmente la respuesta según las necesidades identificadas.
          .tarjeta.color-primario.p-3(x="11%" y="80%" numero="+")
            .h5.mb-2 3. Instituciones de salud
            p.mb-0 Brindan valoración, tratamiento y seguimiento especializado para favorecer la recuperación integral de la persona afectada.
          .tarjeta.color-primario.p-3(x="89%" y="30%" numero="+")
            .h5.mb-2 4. Organismos de socorro
            p.mb-0 Apoyan el rescate, la atención inicial y el traslado mediante acciones coordinadas con otros servicios disponibles.
          .tarjeta.color-primario.p-3(x="89%" y="56%" numero="+")
            .h5.mb-2 5. Entidades de protección
            p.mb-0 Activan rutas institucionales y brindan acompañamiento cuando existen situaciones que afectan la integridad de la infancia.
          .tarjeta.color-primario.p-3(x="89%" y="80%" numero="+")
            .h5.mb-2 6. Coordinación integral
            p.mb-0 Articula los servicios para atender la emergencia y garantizar la continuidad del cuidado hasta la recuperación. 

            
        figure.d-md-none
          img(src="@/assets/curso/temas/t2/8.svg" alt="").w-100

    p.mt-5(data-aos="fade-down") En el contexto de la primera infancia, las redes de atención adquieren especial relevancia, ya que permiten activar rutas de atención prioritaria que responden a las necesidades específicas de niñas y niños, garantizando una intervención rápida, segura y adecuada a su condición. Además, contribuyen a fortalecer la articulación entre los entornos de cuidado, como jardines infantiles y centros educativos, con los servicios de salud y protección.

    p.mt-4(data-aos="fade-down") A continuación, se presentan los principales actores de las redes de atención y su función en el contexto de los primeros auxilios.

    .row.justify-content-center.mt-4(data-aos="fade-down")
      .col-lg-10
        .titulo-sexto.color-acento-contenido.mb-3
          h5 Tabla 2.
          span Redes de atención en emergencias
        .tabla-a.tabla--redes.color-acento-contenido
          table
            thead
              tr
                th Actor / Servicio
                th Función
                th Aplicación en primeros auxilios
            tbody
              tr
                td Línea 123
                td Canal de atención de emergencias a nivel nacional.
                td Permite activar de manera inmediata los servicios de emergencia.
              tr
                td Servicios de Emergencias Médicas (SEM)
                td Coordinan la respuesta prehospitalaria y traslado de pacientes.
                td Garantiza la atención oportuna y traslado seguro a centros de salud.
              tr
                td IPS (Instituciones Prestadoras de Servicios de Salud)
                td Brindan atención médica especializada.
                td Recibe y continúa la atención iniciada por el primer respondiente.
              tr
                td Bomberos
                td Atención de incendios, rescates y manejo de incidentes.
                td Apoya en situaciones de riesgo como atrapamientos o incendios.
              tr
                td Defensa Civil
                td Apoyo en emergencias, rescate y atención comunitaria.
                td Interviene en situaciones de desastre o emergencias masivas.
              tr
                td Cruz Roja
                td Atención prehospitalaria y apoyo humanitario.
                td Brinda primeros auxilios y apoyo en la atención de víctimas.
              tr
                td Policía Nacional
                td Apoyo en seguridad y control de la escena.
                td Facilita el acceso y la seguridad durante la atención de la emergencia.

    .row.align-items-center.mt-4(data-aos="fade-down")
      .col-lg-9
        p La adecuada activación de estas redes es fundamental para garantizar una respuesta integral, oportuna y segura, especialmente en la primera infancia. El primer respondiente debe reconocer cuándo la situación supera su capacidad de intervención y activar de manera inmediata los servicios de emergencia, proporcionando información clara y precisa. De esta manera, se asegura la continuidad del proceso de atención y la protección de la vida e integridad de niñas y niños.
        .cajon.color1.p-4.mt-4
          p.mb-0 La articulación de las redes de atención favorece la continuidad del cuidado y la protección de la primera infancia. Para avanzar en este proceso, es necesario comprender los conceptos básicos de primeros auxilios y las acciones relacionadas con la identificación, el análisis y el control de los riesgos.
      .col-lg-3.d-none.d-lg-block
        figure
          img(src="@/assets/curso/temas/t2/i11.png" alt="" style="width: 292px").m-auto

</template>

<script>
export default {
  name: 'Tema2',
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
