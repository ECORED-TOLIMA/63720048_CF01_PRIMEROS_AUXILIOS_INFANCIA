export default {
  global: {
    Name: 'Principios de primeros auxilios en primera infancia',
    Description:
      'Este componente desarrolla los Principios de primeros auxilios en primera infancia, abordando la normativa, conceptos básicos, bioseguridad y gestión del riesgo. Permite reconocer situaciones de emergencia, evaluar condiciones del entorno y aplicar acciones iniciales seguras. Fortalece el rol del primer respondiente para actuar de manera oportuna, responsable y acorde con lineamientos técnicos en contextos de atención infantil.',
    imagenBannerPrincipal: '@/assets/curso/portada/ilustracion.png',
    fondoBannerPrincipal: '@/assets/curso/portada/fondo-banner.png',
    imagenesDecorativasBanner: [
      {
        clases: ['banner-principal-decorativo-1', 'd-none', 'd-lg-block'],
        imagen: '@/assets/curso/portada/decorativo-1.png',
      },
      {
        clases: ['banner-principal-decorativo-2', 'd-none', 'd-lg-block'],
        imagen: '@/assets/curso/portada/decorativo-2.png',
      },
    ],
  },
  menuPrincipal: {
    menu: [
      {
        nombreRuta: 'inicio',
        icono: 'fas fa-home',
        titulo: 'Volver al inicio',
      },
      {
        nombreRuta: 'introduccion',
        icono: 'fas fa-info-circle',
        titulo: 'Introducción',
        desarrolloContenidos: true,
      },
      {
        nombreRuta: 'tema1',
        numero: '1',
        titulo: 'Generalidades de los primeros auxilios',
        desarrolloContenidos: true,
        subMenu: [
          {
            numero: '1.1',
            titulo:
              'Importancia de los primeros auxilios en la primera infancia',
            hash: 't_1_1',
          },
          {
            numero: '1.2',
            titulo: 'Concepto, objetivos y principios',
            hash: 't_1_2',
          },
          {
            numero: '1.3',
            titulo: 'Características de la atención inicial',
            hash: 't_1_3',
          },
          {
            numero: '1.4',
            titulo: 'Principios de los primeros auxilios',
            hash: 't_1_4',
          },
        ],
      },
      {
        nombreRuta: 'tema2',
        numero: '2',
        titulo: 'Marco normativo y ético',
        desarrolloContenidos: true,
        subMenu: [
          {
            numero: '2.1',
            titulo: 'Lineamientos técnicos SDIS',
            hash: 't_2_1',
          },
          {
            numero: '2.2',
            titulo: 'Normativa en salud y emergencias',
            hash: 't_2_2',
          },
          {
            numero: '2.3',
            titulo: 'Derechos del paciente',
            hash: 't_2_3',
          },
          {
            numero: '2.4',
            titulo: 'Responsabilidad del primer respondiente',
            hash: 't_2_4',
          },
          {
            numero: '2.5',
            titulo: 'Redes de atención',
            hash: 't_2_5',
          },
        ],
      },
      {
        nombreRuta: 'tema3',
        numero: '3',
        titulo: 'Fundamentos conceptuales y gestión del riesgo',
        desarrolloContenidos: true,
        subMenu: [
          {
            numero: '3.1',
            titulo: 'Fundamentos conceptuales',
            hash: 't_3_1',
          },
          {
            numero: '3.2',
            titulo: 'Gestión del riesgo',
            hash: 't_3_2',
          },
        ],
      },
      {
        nombreRuta: 'tema4',
        numero: '4',
        titulo: 'Bioseguridad y rol del primer respondiente',
        desarrolloContenidos: true,
        subMenu: [
          {
            numero: '4.1',
            titulo: 'Concepto y normas básicas',
            hash: 't_4_1',
          },
          {
            numero: '4.2',
            titulo: 'Elementos de protección personal',
            hash: 't_4_2',
          },
          {
            numero: '4.3',
            titulo: 'Manejo de riesgos biológicos',
            hash: 't_4_3',
          },
          {
            numero: '4.4',
            titulo: 'Rol del primer respondiente',
            hash: 't_4_4',
          },
        ],
      },
      {
        nombreRuta: 'tema5',
        numero: '5',
        titulo: 'Botiquín de primeros auxilios',
        desarrolloContenidos: true,
        subMenu: [
          {
            numero: '5.1',
            titulo: 'Concepto y normativa',
            hash: 't_5_1',
          },
          {
            numero: '5.2',
            titulo: 'Clasificación y elementos del botiquín',
            hash: 't_5_2',
          },
        ],
      },
      {
        nombreRuta: 'tema6',
        numero: '6',
        titulo: 'Evaluación del escenario y toma de decisiones',
        desarrolloContenidos: true,
        subMenu: [
          {
            numero: '6.1',
            titulo: 'Tipos de emergencia',
            hash: 't_6_1',
          },
          {
            numero: '6.2',
            titulo: 'Valoración inicial',
            hash: 't_6_2',
          },
          {
            numero: '6.3',
            titulo: 'Seguridad de la escena',
            hash: 't_6_3',
          },
          {
            numero: '6.4',
            titulo: 'Activación del sistema de emergencias',
            hash: 't_6_4',
          },
          {
            numero: '6.5',
            titulo: 'Aplicación en contextos infantiles',
            hash: 't_6_5',
          },
          {
            numero: '6.6',
            titulo: 'Toma de decisiones en primeros auxilios',
            hash: 't_6_6',
          },
        ],
      },
    ],
    subMenu: [
      {
        icono: 'fas fa-sitemap',
        titulo: 'Síntesis',
        nombreRuta: 'sintesis',
        desarrolloContenidos: true,
      },
      {
        nombreRuta: 'actividad',
        icono: 'far fa-question-circle',
        titulo: 'Actividad didáctica',
        desarrolloContenidos: true,
      },
      {
        nombreRuta: 'glosario',
        icono: 'fas fa-sort-alpha-down',
        titulo: 'Glosario',
      },
      {
        icono: 'fas fa-book',
        titulo: 'Referencias bibliográficas',
        nombreRuta: 'referencias',
      },
      {
        icono: 'fas fa-file-pdf',
        titulo: 'Descargar PDF',
        download: 'downloads/dist.pdf',
      },
      {
        icono: 'fas fa-download',
        titulo: 'Descargar material',
        download: 'downloads/material.zip',
      },
      {
        icono: 'far fa-registered',
        titulo: 'Créditos',
        nombreRuta: 'creditos',
      },
    ],
  },
  glosario: [
    {
      termino: 'Atención inicial',
      significado:
        'acciones inmediatas que se realizan para proteger y asistir a una persona antes de la llegada del personal especializado.',
    },
    {
      termino: 'Bioseguridad',
      significado:
        'medidas y prácticas destinadas a prevenir la exposición a agentes biológicos y reducir los riesgos durante la atención de una emergencia.',
    },
    {
      termino: 'Botiquín de primeros auxilios',
      significado:
        'recurso que contiene elementos básicos organizados para brindar atención inicial ante lesiones o emergencias.',
    },
    {
      termino: 'Elementos de protección personal (EPP)',
      significado:
        'equipos y dispositivos que protegen al primer respondiente del contacto con sangre, fluidos corporales u otros agentes que puedan afectar su salud.',
    },
    {
      termino: 'Emergencia',
      significado:
        'situación que pone en riesgo la vida, la salud o la integridad de una persona y requiere atención oportuna.',
    },
    {
      termino: 'Evaluación del escenario',
      significado:
        'observación inicial del entorno para identificar peligros y determinar si existen condiciones seguras para acercarse y brindar atención.',
    },
    {
      termino: 'Factor de riesgo',
      significado:
        'circunstancia que aumenta la probabilidad de que ocurra un accidente, una lesión o una afectación a la salud.',
    },
    {
      termino: 'Gestión del riesgo',
      significado:
        'proceso orientado a identificar, analizar, prevenir y controlar las situaciones que pueden ocasionar daños.',
    },
    {
      termino: 'Primer respondiente',
      significado:
        'persona que brinda la atención inicial durante una emergencia mientras llega el personal especializado.',
    },
    {
      termino: 'Primeros auxilios',
      significado:
        'atención inmediata y temporal que recibe una persona lesionada o enferma repentinamente hasta la llegada de la asistencia especializada.',
    },
    {
      termino: 'Seguridad de la escena',
      significado:
        'condición que permite brindar atención sin exponer a riesgos adicionales al primer respondiente, a la persona afectada ni a quienes se encuentran en el lugar.',
    },
    {
      termino: 'Sistema de emergencias',
      significado:
        'red de entidades, recursos y servicios que intervienen de manera coordinada en la atención de urgencias y emergencias.',
    },
  ],
  referencias: [
    {
      referencia:
        'Ley 1098 de 2006. Por la cual se expide el Código de la Infancia y la Adolescencia. 8 de noviembre de 2006. Diario Oficial No. 46.446.',
      link: '',
    },
    {
      referencia:
        'Ley Estatutaria 1751 de 2015. Por medio de la cual se regula el derecho fundamental a la salud y se dictan otras disposiciones. 16 de febrero de 2015. Diario Oficial No. 49.427.',
      link: '',
    },
    {
      referencia:
        'Ministerio de Salud y Protección Social. (2012). <em>Guías básicas de atención médica prehospitalaria</em> (2.ª ed.).',
      link: '',
    },
    {
      referencia:
        'Ministerio de Salud y Protección Social. (2016, 17 de febrero). <em>Resolución 429 de 2016, por medio de la cual se adopta la Política de Atención Integral en Salud</em>.',
      link: '',
    },
    {
      referencia:
        'Ministerio de Salud y Protección Social. (2017). <em>Manual de medidas básicas para el control de infecciones asociadas a la atención en salud</em>.',
      link: '',
    },
    {
      referencia:
        'Ministerio de Salud y Protección Social. (2017, 30 de marzo). <em>Resolución 926 de 2017, por la cual se reglamenta el desarrollo y la operación del Sistema de Emergencias Médicas</em>.',
      link: '',
    },
    {
      referencia:
        'Ministerio de Salud y Protección Social. (2019, 25 de noviembre). <em>Resolución 3100 de 2019, por la cual se definen los procedimientos y las condiciones de inscripción de los prestadores de servicios de salud y de habilitación de los servicios de salud, y se adopta el Manual de Inscripción de Prestadores y Habilitación de Servicios de Salud</em>.',
      link: '',
    },
  ],
  creditos: [
    {
      titulo: 'ECOSISTEMA DE RECURSOS EDUCATIVOS DIGITALES',
      autores: [
        {
          nombre: 'Claudia Johanna Gómez Pérez ',
          cargo:
            'Profesional G06. Responsable Ecosistema Virtual de Recursos Educativos Digitales',
          centro: 'Centro Agroturístico - Regional Santander',
        },
        {
          nombre: 'Diana Rocío Possos Beltrán',
          cargo: 'Responsable de línea de producción ',
          centro: 'Centro de Comercio y Servicios - Regional Tolima',
        },
      ],
    },
    {
      titulo: 'CONTENIDO INSTRUCCIONAL',
      autores: [
        {
          nombre: 'Laura Briguitte Perea Possos',
          cargo: 'Experta temática',
          centro: 'Centro de Comercio y Servicios - Regional Tolima',
        },
        {
          nombre: 'Gloria Lida Alzate Suárez',
          cargo: 'Evaluadora instruccional',
          centro: 'Centro de Comercio y Servicios - Regional Tolima',
        },
      ],
    },
    {
      titulo: 'DISEÑO Y DESARROLLO DE RECURSOS EDUCATIVOS DIGITALES',
      autores: [
        {
          nombre: 'Juan Daniel Polanco Muñoz',
          cargo: 'Diseñador de contenidos digitales',
          centro: 'Centro de Comercio y Servicios - Regional Tolima',
        },
        {
          nombre: 'Manuel Felipe Echavarria Orozco',
          cargo: 'Desarrollador <em>full stack</em>',
          centro: 'Centro de Comercio y Servicios - Regional Tolima',
        },
        {
          nombre: 'Gilberto Junior Rodríguez Rodríguez',
          cargo: 'Animador y productor audiovisual',
          centro: 'Centro de Comercio y Servicios - Regional Tolima',
        },
      ],
    },
    {
      titulo: 'VALIDACIÓN RECURSO EDUCATIVO DIGITAL',
      autores: [
        {
          nombre: 'María Fernanda Pineda Mora',
          cargo: 'Evaluadora de contenidos inclusivos y accesibles',
          centro: 'Centro de Comercio y Servicios - Regional Tolima',
        },
        {
          nombre: 'Javier Mauricio Oviedo',
          cargo: 'Validador y vinculador de recursos educativos digitales',
          centro: 'Centro de Comercio y Servicios - Regional Tolima',
        },
      ],
    },
  ],
  creditosAdicionales: {
    imagenes:
      'Fotografías y vectores tomados de <a href="https://www.freepik.es/" target="_blank">www.freepik.es</a>, <a href="https://www.shutterstock.com/" target="_blank">www.shutterstock.com</a>, <a href="https://unsplash.com/" target="_blank">unsplash.com </a>y <a href="https://www.flaticon.com/" target="_blank">www.flaticon.com</a>',
    creativeCommons:
      'Licencia creative commons CC BY-NC-SA<br><a href="https://creativecommons.org/licenses/by-nc-sa/2.0/" target="_blank">ver licencia</a>',
  },
}
