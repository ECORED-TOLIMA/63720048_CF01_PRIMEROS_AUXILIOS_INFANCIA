<template lang="pug">
  .curso-main-container.pb-3
    BannerInterno(icono="far fa-question-circle" titulo="Actividad didáctica")
    .container.tarjeta.tarjeta--blanca.p-4.p-md-5
      #Actividad
        ActividadController(:cuestionario="cuestionario")

</template>

<script>
import ActividadController from '@ecored-sena/boulder-kit/plugin/components/actividad/ActividadController.vue'

export default {
  name: 'ActividadDidactica',
  components: {
    ActividadController,
  },
  data: () => ({
    cuestionario: {
      tema: 'Ruta de protección en primera infancia.',
      titulo: 'Cuestionario',
      introduccion:
        '<b>Objetivo:</b> reconocer los principios de los primeros auxilios en primera infancia mediante la identificación de conceptos, riesgos, medidas de bioseguridad y acciones iniciales que orientan una actuación segura y responsable ante situaciones de emergencia.',
      barajarPreguntas: true,
      titulo_aprobado: '¡BUEN TRABAJO!',
      titulo_reprobado: 'VUELVA A INTENTARLO.',
      preguntas: [
        {
          id: 1,
          texto: '¿Qué son los primeros auxilios?',
          imagen: '@/assets/actividad/imagen1.png',
          barajarRespuestas: true,
          opciones: [
            {
              id: 'a',
              texto: 'Atención médica especializada.',
              esCorrecta: false,
            },
            {
              id: 'b',
              texto: 'Atención psicológica.',
              esCorrecta: false,
            },
            {
              id: 'c',
              texto: 'Atención inmediata antes del hospital.',
              esCorrecta: true,
            },
            {
              id: 'd',
              texto: 'Atención prolongada.',
              esCorrecta: false,
            },
          ],
          mensaje_correcto:
            '¡Correcto! Los primeros auxilios son la atención inmediata que se brinda antes de la llegada de la atención especializada.',
          mensaje_incorrecto:
            'Revise nuevamente el contenido del componente formativo.',
        },
        {
          id: 2,
          texto: '¿Cuál es el principal objetivo de los primeros auxilios?',
          imagen: '@/assets/actividad/imagen1.png',
          barajarRespuestas: true,
          opciones: [
            {
              id: 'a',
              texto: 'Dar medicamentos.',
              esCorrecta: false,
            },
            {
              id: 'b',
              texto: 'Preservar la vida.',
              esCorrecta: true,
            },
            {
              id: 'c',
              texto: 'Diagnosticar enfermedades.',
              esCorrecta: false,
            },
            {
              id: 'd',
              texto: 'Reemplazar al médico.',
              esCorrecta: false,
            },
          ],
          mensaje_correcto:
            '¡Correcto! El objetivo principal es proteger la vida y evitar complicaciones.',
          mensaje_incorrecto:
            'Revise nuevamente el contenido del componente formativo.',
        },
        {
          id: 3,
          texto: 'La primera acción del primer respondiente es:',
          imagen: '@/assets/actividad/imagen1.png',
          barajarRespuestas: true,
          opciones: [
            {
              id: 'a',
              texto: 'Atender a la víctima.',
              esCorrecta: false,
            },
            {
              id: 'b',
              texto: 'Llamar a la familia.',
              esCorrecta: false,
            },
            {
              id: 'c',
              texto: 'Dar agua.',
              esCorrecta: false,
            },
            {
              id: 'd',
              texto: 'Evaluar la escena.',
              esCorrecta: true,
            },
          ],
          mensaje_correcto:
            '¡Correcto! Evaluar el entorno evita riesgos adicionales para quien atiende y para la víctima.',
          mensaje_incorrecto:
            'Revise nuevamente el contenido del componente formativo.',
        },
        {
          id: 4,
          texto:
            '¿Qué principio busca evitar empeorar la condición de la víctima?',
          imagen: '@/assets/actividad/imagen1.png',
          barajarRespuestas: true,
          opciones: [
            {
              id: 'a',
              texto: 'Responsabilidad.',
              esCorrecta: false,
            },
            {
              id: 'b',
              texto: 'No causar daño.',
              esCorrecta: true,
            },
            {
              id: 'c',
              texto: 'Seguridad.',
              esCorrecta: false,
            },
            {
              id: 'd',
              texto: 'Oportunidad.',
              esCorrecta: false,
            },
          ],
          mensaje_correcto:
            '¡Correcto! El principio de no causar daño evita intervenciones inadecuadas.',
          mensaje_incorrecto:
            'Revise nuevamente el contenido del componente formativo.',
        },
        {
          id: 5,
          texto: '¿Qué caracteriza la atención inicial?',
          imagen: '@/assets/actividad/imagen2.png',
          barajarRespuestas: true,
          opciones: [
            {
              id: 'a',
              texto: 'Es inmediata.',
              esCorrecta: true,
            },
            {
              id: 'b',
              texto: 'Es especializada.',
              esCorrecta: false,
            },
            {
              id: 'c',
              texto: 'Es opcional.',
              esCorrecta: false,
            },
            {
              id: 'd',
              texto: 'Es prolongada.',
              esCorrecta: false,
            },
          ],
          mensaje_correcto:
            '¡Correcto! La inmediatez es clave para prevenir complicaciones.',
          mensaje_incorrecto:
            'Revise nuevamente el contenido del componente formativo.',
        },
        {
          id: 6,
          texto: 'En primera infancia, el riesgo es mayor porque:',
          imagen: '@/assets/actividad/imagen2.png',
          barajarRespuestas: true,
          opciones: [
            {
              id: 'a',
              texto: 'Son independientes.',
              esCorrecta: false,
            },
            {
              id: 'b',
              texto: 'Son más vulnerables.',
              esCorrecta: true,
            },
            {
              id: 'c',
              texto: 'Son más fuertes.',
              esCorrecta: false,
            },
            {
              id: 'd',
              texto: 'Tienen más experiencia.',
              esCorrecta: false,
            },
          ],
          mensaje_correcto:
            '¡Correcto! En la primera infancia, el proceso de desarrollo aumenta la vulnerabilidad frente a los accidentes.',
          mensaje_incorrecto:
            'Revise nuevamente el contenido del componente formativo.',
        },
        {
          id: 7,
          texto: '¿Qué elemento es clave en bioseguridad?',
          imagen: '@/assets/actividad/imagen2.png',
          barajarRespuestas: true,
          opciones: [
            {
              id: 'a',
              texto: 'Gasas.',
              esCorrecta: false,
            },
            {
              id: 'b',
              texto: 'Tijeras.',
              esCorrecta: false,
            },
            {
              id: 'c',
              texto: 'Guantes.',
              esCorrecta: true,
            },
            {
              id: 'd',
              texto: 'Alcohol.',
              esCorrecta: false,
            },
          ],
          mensaje_correcto:
            '¡Correcto! Los guantes protegen tanto al primer respondiente como a la víctima.',
          mensaje_incorrecto:
            'Revise nuevamente el contenido del componente formativo.',
        },
        {
          id: 8,
          texto: '¿Cuándo se debe activar el sistema de emergencias?',
          imagen: '@/assets/actividad/imagen2.png',
          barajarRespuestas: true,
          opciones: [
            {
              id: 'a',
              texto: 'Cuando la situación es grave.',
              esCorrecta: true,
            },
            {
              id: 'b',
              texto: 'Solo si hay adultos.',
              esCorrecta: false,
            },
            {
              id: 'c',
              texto: 'Siempre.',
              esCorrecta: false,
            },
            {
              id: 'd',
              texto: 'Cuando no hay riesgo.',
              esCorrecta: false,
            },
          ],
          mensaje_correcto:
            '¡Correcto! El sistema de emergencias se activa cuando existe riesgo para la vida o la salud.',
          mensaje_incorrecto:
            'Revise nuevamente el contenido del componente formativo.',
        },
        {
          id: 9,
          texto: 'La línea de emergencias en Colombia es:',
          imagen: '@/assets/actividad/imagen3.png',
          barajarRespuestas: true,
          opciones: [
            {
              id: 'a',
              texto: '123.',
              esCorrecta: true,
            },
            {
              id: 'b',
              texto: '911.',
              esCorrecta: false,
            },
            {
              id: 'c',
              texto: '111.',
              esCorrecta: false,
            },
            {
              id: 'd',
              texto: '101.',
              esCorrecta: false,
            },
          ],
          mensaje_correcto:
            '¡Correcto! La línea 123 es el canal único de atención de emergencias en Colombia.',
          mensaje_incorrecto:
            'Revise nuevamente el contenido del componente formativo.',
        },
        {
          id: 10,
          texto: '¿Qué se debe informar al llamar a emergencias?',
          imagen: '@/assets/actividad/imagen3.png',
          barajarRespuestas: true,
          opciones: [
            {
              id: 'a',
              texto: 'Solo el nombre.',
              esCorrecta: false,
            },
            {
              id: 'b',
              texto: 'Información completa del evento.',
              esCorrecta: true,
            },
            {
              id: 'c',
              texto: 'Solo el número de teléfono.',
              esCorrecta: false,
            },
            {
              id: 'd',
              texto: 'Nada.',
              esCorrecta: false,
            },
          ],
          mensaje_correcto:
            '¡Correcto! Se debe brindar información completa y clara del evento para facilitar la atención oportuna.',
          mensaje_incorrecto:
            'Revise nuevamente el contenido del componente formativo.',
        },
        {
          id: 11,
          texto: 'El botiquín sirve para:',
          imagen: '@/assets/actividad/imagen3.png',
          barajarRespuestas: true,
          opciones: [
            {
              id: 'a',
              texto: 'Hospitalización.',
              esCorrecta: false,
            },
            {
              id: 'b',
              texto: 'Curar enfermedades.',
              esCorrecta: false,
            },
            {
              id: 'c',
              texto: 'Diagnóstico.',
              esCorrecta: false,
            },
            {
              id: 'd',
              texto: 'Atención inicial.',
              esCorrecta: true,
            },
          ],
          mensaje_correcto:
            '¡Correcto! El botiquín permite brindar una atención inicial mientras llega la ayuda especializada.',
          mensaje_incorrecto:
            'Revise nuevamente el contenido del componente formativo.',
        },
        {
          id: 12,
          texto: '¿Qué NO debe hacer el primer respondiente?',
          imagen: '@/assets/actividad/imagen3.png',
          barajarRespuestas: true,
          opciones: [
            {
              id: 'a',
              texto: 'Activar emergencias.',
              esCorrecta: false,
            },
            {
              id: 'b',
              texto: 'Evaluar.',
              esCorrecta: false,
            },
            {
              id: 'c',
              texto: 'Actuar con seguridad.',
              esCorrecta: false,
            },
            {
              id: 'd',
              texto: 'Realizar procedimientos avanzados.',
              esCorrecta: true,
            },
          ],
          mensaje_correcto:
            '¡Correcto! El primer respondiente debe actuar dentro de los límites de sus competencias.',
          mensaje_incorrecto:
            'Revise nuevamente el contenido del componente formativo.',
        },
        {
          id: 13,
          texto: '¿Qué es una emergencia?',
          imagen: '@/assets/actividad/imagen4.png',
          barajarRespuestas: true,
          opciones: [
            {
              id: 'a',
              texto: 'Situación normal.',
              esCorrecta: false,
            },
            {
              id: 'b',
              texto: 'Situación que pone en riesgo la vida.',
              esCorrecta: true,
            },
            {
              id: 'c',
              texto: 'Situación leve.',
              esCorrecta: false,
            },
            {
              id: 'd',
              texto: 'Situación sin riesgo.',
              esCorrecta: false,
            },
          ],
          mensaje_correcto:
            '¡Correcto! Una emergencia es una situación que pone en riesgo la vida y requiere atención inmediata.',
          mensaje_incorrecto:
            'Revise nuevamente el contenido del componente formativo.',
        },
        {
          id: 14,
          texto: 'La valoración inicial permite:',
          imagen: '@/assets/actividad/imagen4.png',
          barajarRespuestas: true,
          opciones: [
            {
              id: 'a',
              texto: 'Medicar.',
              esCorrecta: false,
            },
            {
              id: 'b',
              texto: 'Hospitalizar.',
              esCorrecta: false,
            },
            {
              id: 'c',
              texto: 'Priorizar atención.',
              esCorrecta: true,
            },
            {
              id: 'd',
              texto: 'Diagnosticar.',
              esCorrecta: false,
            },
          ],
          mensaje_correcto:
            '¡Correcto! La valoración inicial permite priorizar la atención según la gravedad de cada caso.',
          mensaje_incorrecto:
            'Revise nuevamente el contenido del componente formativo.',
        },
        {
          id: 15,
          texto: '¿Qué se debe verificar primero en la víctima?',
          imagen: '@/assets/actividad/imagen4.png',
          barajarRespuestas: true,
          opciones: [
            {
              id: 'a',
              texto: 'Dirección.',
              esCorrecta: false,
            },
            {
              id: 'b',
              texto: 'Conciencia y respiración.',
              esCorrecta: true,
            },
            {
              id: 'c',
              texto: 'Nombre.',
              esCorrecta: false,
            },
            {
              id: 'd',
              texto: 'Edad.',
              esCorrecta: false,
            },
          ],
          mensaje_correcto:
            '¡Correcto! La conciencia y la respiración son indicadores clave de vida.',
          mensaje_incorrecto:
            'Revise nuevamente el contenido del componente formativo.',
        },
        {
          id: 16,
          texto: 'La gestión del riesgo busca:',
          imagen: '@/assets/actividad/imagen4.png',
          barajarRespuestas: true,
          opciones: [
            {
              id: 'a',
              texto: 'Identificar y controlar riesgos.',
              esCorrecta: true,
            },
            {
              id: 'b',
              texto: 'Evitar atención.',
              esCorrecta: false,
            },
            {
              id: 'c',
              texto: 'Aumentar riesgos.',
              esCorrecta: false,
            },
            {
              id: 'd',
              texto: 'Ignorar peligros.',
              esCorrecta: false,
            },
          ],
          mensaje_correcto:
            '¡Correcto! La gestión del riesgo busca identificar y controlar los riesgos para prevenir accidentes.',
          mensaje_incorrecto:
            'Revise nuevamente el contenido del componente formativo.',
        },
        {
          id: 17,
          texto: '¿Qué es bioseguridad?',
          imagen: '@/assets/actividad/imagen5.png',
          barajarRespuestas: true,
          opciones: [
            {
              id: 'a',
              texto: 'Limpieza.',
              esCorrecta: false,
            },
            {
              id: 'b',
              texto: 'Atención médica.',
              esCorrecta: false,
            },
            {
              id: 'c',
              texto: 'Protección frente a riesgos biológicos.',
              esCorrecta: true,
            },
            {
              id: 'd',
              texto: 'Diagnóstico.',
              esCorrecta: false,
            },
          ],
          mensaje_correcto:
            '¡Correcto! La bioseguridad protege frente a riesgos biológicos y reduce el contagio.',
          mensaje_incorrecto:
            'Revise nuevamente el contenido del componente formativo.',
        },
        {
          id: 18,
          texto: 'El primer respondiente debe:',
          imagen: '@/assets/actividad/imagen5.png',
          barajarRespuestas: true,
          opciones: [
            {
              id: 'a',
              texto: 'Ignorar protocolos.',
              esCorrecta: false,
            },
            {
              id: 'b',
              texto: 'Actuar con responsabilidad.',
              esCorrecta: true,
            },
            {
              id: 'c',
              texto: 'Reemplazar al médico.',
              esCorrecta: false,
            },
            {
              id: 'd',
              texto: 'Actuar sin pensar.',
              esCorrecta: false,
            },
          ],
          mensaje_correcto:
            '¡Correcto! El primer respondiente debe actuar con responsabilidad y ética.',
          mensaje_incorrecto:
            'Revise nuevamente el contenido del componente formativo.',
        },
        {
          id: 19,
          texto: 'Las redes de atención permiten:',
          imagen: '@/assets/actividad/imagen5.png',
          barajarRespuestas: true,
          opciones: [
            {
              id: 'a',
              texto: 'Reemplazar hospitales.',
              esCorrecta: false,
            },
            {
              id: 'b',
              texto: 'Reducir personal.',
              esCorrecta: false,
            },
            {
              id: 'c',
              texto: 'Continuidad del cuidado.',
              esCorrecta: true,
            },
            {
              id: 'd',
              texto: 'Evitar atención.',
              esCorrecta: false,
            },
          ],
          mensaje_correcto:
            '¡Correcto! Las redes de atención garantizan la continuidad y la articulación del cuidado.',
          mensaje_incorrecto:
            'Revise nuevamente el contenido del componente formativo.',
        },
        {
          id: 20,
          texto: 'La toma de decisiones en primeros auxilios implica:',
          imagen: '@/assets/actividad/imagen5.png',
          barajarRespuestas: true,
          opciones: [
            {
              id: 'a',
              texto: 'Esperar siempre.',
              esCorrecta: false,
            },
            {
              id: 'b',
              texto: 'Actuar sin analizar.',
              esCorrecta: false,
            },
            {
              id: 'c',
              texto: 'Analizar y actuar con criterio.',
              esCorrecta: true,
            },
            {
              id: 'd',
              texto: 'Seguir intuición.',
              esCorrecta: false,
            },
          ],
          mensaje_correcto:
            '¡Correcto! Tomar decisiones acertadas exige analizar la situación antes de actuar.',
          mensaje_incorrecto:
            'Revise nuevamente el contenido del componente formativo.',
        },
      ],
      mensaje_final_aprobado:
        '¡Excelente resultado! Se evidencia una comprensión adecuada de los principios de los primeros auxilios en la primera infancia, así como la capacidad para reconocer situaciones de riesgo y tomar decisiones oportunas frente a una emergencia.',
      mensaje_final_reprobado:
        'No ha superado la actividad. Le recomendamos volver a revisar el componente formativo e intentar nuevamente la actividad didáctica.',
    },
  }),
}
</script>
