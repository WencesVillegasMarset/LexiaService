define({ "api": [
  {
    "type": "get",
    "url": "/v1/solucion/:solicitudId",
    "title": "Solicitar Solucion",
    "name": "Consultar_resultado_de_una_Solicitud",
    "group": "Calendarizacion",
    "examples": [
      {
        "content": "@apiExample",
        "type": "json"
      }
    ],
    "success": {
      "examples": [
        {
          "title": "Response",
          "content": "HTTP/1.1 200 OK\n    {\n        \"_id\": \"{ObjectId de la Solucion}\",\n        \"audiencia\": [ // lista de audiencias calendarizadas\n            {\n                \"fijada\": \"{Boolean}\",\n                \"idSala\": \"{ID de la Sala donde se calendarizo}\",\n                \"id\": \"{ID de la Audiencia}\",\n                \"fechaAudiencia\": \"{Fecha en la que se calendarizo (YYYY-MM-DD)}\",\n                \"horaAudiencia\": \"Hora en la que se calendarizo (HH:MM)\"\n            }\n        ],\n        \"created\": \"{Datetime de Creacion}\",\n        \"solicitudId\": \"{ID de la Solicitud}\"\n    }",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "./app/calendarizacion/routes.py",
    "groupTitle": "Calendarizacion",
    "error": {
      "examples": [
        {
          "title": "400 Bad Request",
          "content": "HTTP/1.1 400 Bad Request\n{\n    \"path\" : \"{Nombre de la propiedad}\",\n    \"message\" : \"{Motivo del error}\"\n}",
          "type": "json"
        },
        {
          "title": "400 Bad Request",
          "content": "HTTP/1.1 400 Bad Request\n{\n    \"error\" : \"{Motivo del error}\"\n}",
          "type": "json"
        },
        {
          "title": "500 Server Error",
          "content": "HTTP/1.1 500 Server Error\n{\n    \"error\" : \"{Motivo del error}\"\n}",
          "type": "json"
        }
      ]
    }
  },
  {
    "type": "GET",
    "url": "/v1/solucion/:solicitudId/excel",
    "title": "Solicitar Excel de Calendarizacion",
    "name": "Descargar_Excel_de_la_Solucion_correspondiente_al_ID_de_Solicitud",
    "group": "Calendarizacion",
    "examples": [
      {
        "content": "@apiExample",
        "type": "json"
      }
    ],
    "success": {
      "examples": [
        {
          "title": "Response",
          "content": "HTTP/1.1 200 OK\nArchivo .xlsx",
          "type": "application/spreadsheetml.sheet"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "./app/calendarizacion/routes.py",
    "groupTitle": "Calendarizacion",
    "error": {
      "examples": [
        {
          "title": "400 Bad Request",
          "content": "HTTP/1.1 400 Bad Request\n{\n    \"path\" : \"{Nombre de la propiedad}\",\n    \"message\" : \"{Motivo del error}\"\n}",
          "type": "json"
        },
        {
          "title": "400 Bad Request",
          "content": "HTTP/1.1 400 Bad Request\n{\n    \"error\" : \"{Motivo del error}\"\n}",
          "type": "json"
        },
        {
          "title": "500 Server Error",
          "content": "HTTP/1.1 500 Server Error\n{\n    \"error\" : \"{Motivo del error}\"\n}",
          "type": "json"
        }
      ]
    }
  },
  {
    "type": "delete",
    "url": "/v1/solicitud/:solicitudId",
    "title": "Eliminar Solicitud",
    "name": "Eliminar_una_Solicitud_de_la_Base_de_Datos(Hard_Delete)",
    "group": "Calendarizacion",
    "examples": [
      {
        "content": "@apiExample",
        "type": "json"
      }
    ],
    "success": {
      "examples": [
        {
          "title": "Response",
          "content": "HTTP/1.1 200 OK",
          "type": "200"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "./app/calendarizacion/routes.py",
    "groupTitle": "Calendarizacion",
    "error": {
      "examples": [
        {
          "title": "400 Bad Request",
          "content": "HTTP/1.1 400 Bad Request\n{\n    \"path\" : \"{Nombre de la propiedad}\",\n    \"message\" : \"{Motivo del error}\"\n}",
          "type": "json"
        },
        {
          "title": "400 Bad Request",
          "content": "HTTP/1.1 400 Bad Request\n{\n    \"error\" : \"{Motivo del error}\"\n}",
          "type": "json"
        },
        {
          "title": "500 Server Error",
          "content": "HTTP/1.1 500 Server Error\n{\n    \"error\" : \"{Motivo del error}\"\n}",
          "type": "json"
        }
      ]
    }
  },
  {
    "type": "delete",
    "url": "/v1/solucion/:solucionId",
    "title": "Eliminar Solucion",
    "name": "Eliminar_una_Solucion_de_la_Base_de_Datos(Hard_Delete)",
    "group": "Calendarizacion",
    "examples": [
      {
        "content": "@apiExample",
        "type": "json"
      }
    ],
    "success": {
      "examples": [
        {
          "title": "Response",
          "content": "HTTP/1.1 200 OK",
          "type": "200"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "./app/calendarizacion/routes.py",
    "groupTitle": "Calendarizacion",
    "error": {
      "examples": [
        {
          "title": "400 Bad Request",
          "content": "HTTP/1.1 400 Bad Request\n{\n    \"path\" : \"{Nombre de la propiedad}\",\n    \"message\" : \"{Motivo del error}\"\n}",
          "type": "json"
        },
        {
          "title": "400 Bad Request",
          "content": "HTTP/1.1 400 Bad Request\n{\n    \"error\" : \"{Motivo del error}\"\n}",
          "type": "json"
        },
        {
          "title": "500 Server Error",
          "content": "HTTP/1.1 500 Server Error\n{\n    \"error\" : \"{Motivo del error}\"\n}",
          "type": "json"
        }
      ]
    }
  },
  {
    "type": "post",
    "url": "/v1/solicitud/",
    "title": "Solicitar Calendarizacion",
    "name": "Hacer_Solicitud_de_Calendarizacion",
    "group": "Calendarizacion",
    "examples": [
      {
        "title": "Body",
        "content": "{\n    \"sala\": [ // up to date\n        {\n            'idSala':\"{id de la sala}\" \"Integer\",\n            'calendarizable':\"{se pueden calendarizar en esta sala} Boolean\"\n            'almafuerte': \"{True si es en Almafuerte } Boolean\",\n            'boulonge_sur_mer': \"{True si es en Boulonge Sur Mer} Boolean\",\n        }\n    ],\n    \"audiencia\": [\n        {\n            \"juez\": [{\n                \"idJuez\": \"Integer\",\n            }],\n            \"defensor\": [{\n                \"idDefensor\": \"Integer\",\n            }],\n            \"fiscal\": [{\n                \"idFiscal\": \"Integer\",\n            }],\n            \"querellante\": [{\n                \"idQuerellante\": \"Integer\",\n            }],\n            \"asesor\": [{\n                \"idAsesor\": \"Integer\",\n            }],\n            'riesgosa': \"{Hay alto riesgo de que se extienda mas de la duracion estimaada?} Boolean\",\n            'detenido': \"{Tiene Detenidos?} Boolean\",\n            'tipo': {\n                'idTipo':\"{ID del tipo de la audiencia} Integer\",\n                'tiempoRealizacionMinimo':\"{Numero de dias minimo para fijacion} Integer\",\n                'tiempoRealizacionMaximo':\"{Numero de dias minimo para fijacion} Integer\",\n            },\n            'aLaTarde': \"{Indica si debe realizarse obligatoriamente a la tarde}Boolean\"\n            'almafuerte': \"{True si es en Almafuerte } Boolean\",\n            'boulonge_sur_mer': \"{True si es en Boulonge Sur Mer} Boolean\",\n            'fechaSolicitud': \"{Fecha en la que fue solicitada la Audiencia} String (YYYY-MM-DD),\n            'duracion': Integer,\n            'id': Integer,\n        }\n    ],\n    \"audienciaFijada\": [\n        {\n            \"juez\": [{\n                \"idJuez\": \"Integer\",\n            }],\n            \"defensor\": [{\n                \"idDefensor\": \"Integer\",\n            }],\n            \"fiscal\": [{\n                \"idFiscal\": \"Integer\",\n            }],\n            \"querellante\": [{\n                \"idQuerellante\": \"Integer\",\n            }],\n            \"asesor\": [{\n                \"idAsesor\": \"Integer\",\n            }],\n            'riesgosa': \"{Hay alto riesgo de que se extienda mas de la duracion estimaada?} Boolean\",\n            'detenido': \"{Tiene Detenidos?} Boolean\",\n            'externa': \"{Hay alto riesgo de que se extienda mas de la duracion estimaada?} Boolean\",\n            'tipo': {\n                'idTipo':\"{ID del tipo de la audiencia} Integer\",\n                'tiempoRealizacionMinimo':\"{Numero de dias minimo para fijacion} Integer\",\n                'tiempoRealizacionMaximo':\"{Numero de dias minimo para fijacion} Integer\",\n            }\n            'aLaTarde': \"{Indica si debe realizarse obligatoriamente a la tarde}Boolean\"\n            'almafuerte': \"{True si es en Almafuerte } Boolean\",\n            'boulonge_sur_mer': \"{True si es en Boulonge Sur Mer} Boolean\",\n            'fechaSolicitud': \"{Fecha en la que fue solicitada la Audiencia} String (YYYY-MM-DD),\n            'fechaRealizacion': \"{Fecha en la que fue calendarizada la Audiencia} String (YYYY-MM-DD),\n            'horaComienzo': \"{Hora en la que fue calendarizada la Audiencia} String (HH:MM),\n            'idSala': \"{id Sala en la que fue calendarizada} Integer,\n            'duracion': Integer,\n            'id': Integer,\n        }\n    ],\n    \"licenciaJuez\": [{ // up to date\n        \"idJuez\":Integer,\n        'fechaInicio': \"String (YYYY-MM-DD)\" ,\n        'fechaFin': \"String (YYYY-MM-DD)\" ,\n    }],\n    \"turnoTardeJuez\": [{ // up to date\n        \"fecha\": \"String (YYYY-MM-DD)\" ,\n        \"juez\": [{\n            \"idJuez\": \"Integer\",\n        }]\n    }],\n    \"indisposicionJuez\": [{ // up to date\n        \"idJuez\": \"Integer\",\n        \"dia\": [{\n            'fecha': \"String (YYYY-MM-DD)\" ,\n            'horaInicio': \"String (HH:MM)\",\n            'horaFin': \"String (HH:MM)\",\n        }]\n    }],\n    \"urlNotificacion\": \"{URL a la que se notificará cuando el Solver arroje resultados} String\"\n}",
        "type": "json"
      }
    ],
    "success": {
      "examples": [
        {
          "title": "Response",
          "content": "HTTP/1.1 200 OK\n{\n    'solicitudId' : {ObjectId}\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "./app/calendarizacion/routes.py",
    "groupTitle": "Calendarizacion",
    "error": {
      "examples": [
        {
          "title": "400 Bad Request",
          "content": "HTTP/1.1 400 Bad Request\n{\n    \"path\" : \"{Nombre de la propiedad}\",\n    \"message\" : \"{Motivo del error}\"\n}",
          "type": "json"
        },
        {
          "title": "400 Bad Request",
          "content": "HTTP/1.1 400 Bad Request\n{\n    \"error\" : \"{Motivo del error}\"\n}",
          "type": "json"
        },
        {
          "title": "500 Server Error",
          "content": "HTTP/1.1 500 Server Error\n{\n    \"error\" : \"{Motivo del error}\"\n}",
          "type": "json"
        }
      ]
    }
  },
  {
    "type": "post",
    "url": "/v1/solicitud/sandbox",
    "title": "Solicitar Calendarizacion Modo Prueba",
    "name": "Hacer_Solicitud_de_Calendarizacion_Modo_Prueba",
    "group": "Calendarizacion",
    "examples": [
      {
        "title": "Body",
        "content": "{\n    \"sala\": [ // up to date\n        {\n            'idSala':\"{id de la sala}\" \"Integer\",\n            'calendarizable':\"{se pueden calendarizar en esta sala} Boolean\"\n            'almafuerte': \"{True si es en Almafuerte } Boolean\",\n            'boulonge_sur_mer': \"{True si es en Boulonge Sur Mer} Boolean\",\n        }\n    ],\n    \"audiencia\": [\n        {\n            \"juez\": [{\n                \"idJuez\": \"Integer\",\n            }],\n            \"defensor\": [{\n                \"idDefensor\": \"Integer\",\n            }],\n            \"fiscal\": [{\n                \"idFiscal\": \"Integer\",\n            }],\n            \"querellante\": [{\n                \"idQuerellante\": \"Integer\",\n            }],\n            \"asesor\": [{\n                \"idAsesor\": \"Integer\",\n            }],\n            'riesgosa': \"{Hay alto riesgo de que se extienda mas de la duracion estimaada?} Boolean\",\n            'detenido': \"{Tiene Detenidos?} Boolean\",\n            'tipo': {\n                'idTipo':\"{ID del tipo de la audiencia} Integer\",\n                'tiempoRealizacionMinimo':\"{Numero de dias minimo para fijacion} Integer\",\n                'tiempoRealizacionMaximo':\"{Numero de dias minimo para fijacion} Integer\",\n            },\n            'aLaTarde': \"{Indica si debe realizarse obligatoriamente a la tarde}Boolean\"\n            'almafuerte': \"{True si es en Almafuerte } Boolean\",\n            'boulonge_sur_mer': \"{True si es en Boulonge Sur Mer} Boolean\",\n            'fechaSolicitud': \"{Fecha en la que fue solicitada la Audiencia} String (YYYY-MM-DD),\n            'duracion': Integer,\n            'id': Integer,\n        }\n    ],\n    \"audienciaFijada\": [\n        {\n            \"juez\": [{\n                \"idJuez\": \"Integer\",\n            }],\n            \"defensor\": [{\n                \"idDefensor\": \"Integer\",\n            }],\n            \"fiscal\": [{\n                \"idFiscal\": \"Integer\",\n            }],\n            \"querellante\": [{\n                \"idQuerellante\": \"Integer\",\n            }],\n            \"asesor\": [{\n                \"idAsesor\": \"Integer\",\n            }],\n            'riesgosa': \"{Hay alto riesgo de que se extienda mas de la duracion estimaada?} Boolean\",\n            'detenido': \"{Tiene Detenidos?} Boolean\",\n            'externa': \"{Hay alto riesgo de que se extienda mas de la duracion estimaada?} Boolean\",\n            'tipo': {\n                'idTipo':\"{ID del tipo de la audiencia} Integer\",\n                'tiempoRealizacionMinimo':\"{Numero de dias minimo para fijacion} Integer\",\n                'tiempoRealizacionMaximo':\"{Numero de dias minimo para fijacion} Integer\",\n            },\n            'aLaTarde': \"{Indica si debe realizarse obligatoriamente a la tarde}Boolean\"\n            'almafuerte': \"{True si es en Almafuerte } Boolean\",\n            'boulonge_sur_mer': \"{True si es en Boulonge Sur Mer} Boolean\",\n            'fechaSolicitud': \"{Fecha en la que fue solicitada la Audiencia} String (YYYY-MM-DD),\n            'fechaRealizacion': \"{Fecha en la que fue calendarizada la Audiencia} String (YYYY-MM-DD),\n            'horaComienzo': \"{Hora en la que fue calendarizada la Audiencia} String (HH:MM),\n            'idSala': \"{id Sala en la que fue calendarizada} Integer,\n            'duracion': Integer,\n            'id': Integer,\n        }\n    ],\n    \"licenciaJuez\": [{ // up to date\n        \"idJuez\":Integer,\n        'fechaInicio': \"String (YYYY-MM-DD)\" ,\n        'fechaFin': \"String (YYYY-MM-DD)\" ,\n    }],\n    \"turnoTardeJuez\": [{ // up to date\n        \"fecha\": \"String (YYYY-MM-DD)\" ,\n        \"juez\": [{\n            \"idJuez\": \"Integer\",\n        }]\n    }],\n    \"indisposicionJuez\": [{ // up to date\n        \"idJuez\": \"Integer\",\n        \"dia\": [{\n            'fecha': \"String (YYYY-MM-DD)\" ,\n            'horaInicio': \"String (HH:MM)\",\n            'horaFin': \"String (HH:MM)\",\n        }]\n    }],\n    \"urlNotificacion\": \"{URL a la que se notificará cuando el Solver arroje resultados} String\"\n    \"fechaSolicitud\": \"{Fecha en la que se correrá la simulacion. e.g:\n                        Simulamos para las audiencias que llegaron el 10 Nov 2018 => 2018-11-10} String\"\n\n}",
        "type": "json"
      }
    ],
    "success": {
      "examples": [
        {
          "title": "Response",
          "content": "HTTP/1.1 200 OK\n{\n    'solicitudId' : {ObjectId}\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "./app/calendarizacion/routes.py",
    "groupTitle": "Calendarizacion",
    "error": {
      "examples": [
        {
          "title": "400 Bad Request",
          "content": "HTTP/1.1 400 Bad Request\n{\n    \"path\" : \"{Nombre de la propiedad}\",\n    \"message\" : \"{Motivo del error}\"\n}",
          "type": "json"
        },
        {
          "title": "400 Bad Request",
          "content": "HTTP/1.1 400 Bad Request\n{\n    \"error\" : \"{Motivo del error}\"\n}",
          "type": "json"
        },
        {
          "title": "500 Server Error",
          "content": "HTTP/1.1 500 Server Error\n{\n    \"error\" : \"{Motivo del error}\"\n}",
          "type": "json"
        }
      ]
    }
  },
  {
    "type": "post",
    "url": "/v1/feriados/",
    "title": "Crear Feriados",
    "name": "Cargar_todos_los_feriados_de_un_Año_dado",
    "group": "Feriados",
    "examples": [
      {
        "title": "Body",
        "content": "{\n    \"feriadoList\": [ \n        {\n            'dia':\"{Numero del Dia [1-31]} Integer\",\n            'mes':\"{Numero del Mes [1-12]} Integer\"\n            'motivo': \"{Descripcion Opcional} String\",\n        }\n    ],\n    \"anio\": {\"Año en el que acontecen los feriados\" Integer}\n}",
        "type": "json"
      }
    ],
    "success": {
      "examples": [
        {
          "title": "Response",
          "content": "HTTP/1.1 200 OK\n{\n    \"feriadoList\": [ \n        {\n            'dia':\"{Numero del Dia [1-31]} Integer\",\n            'mes':\"{Numero del Mes [1-12]} Integer\"\n            'motivo': \"{Descripcion Opcional} String\",\n        }\n    ],\n    \"anio\": \"{Año en el que acontecen los feriados} Integer\",\n    \"created\": \"{Date}\"\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "./app/feriados/routes.py",
    "groupTitle": "Feriados",
    "error": {
      "examples": [
        {
          "title": "400 Bad Request",
          "content": "HTTP/1.1 400 Bad Request\n{\n    \"path\" : \"{Nombre de la propiedad}\",\n    \"message\" : \"{Motivo del error}\"\n}",
          "type": "json"
        },
        {
          "title": "400 Bad Request",
          "content": "HTTP/1.1 400 Bad Request\n{\n    \"error\" : \"{Motivo del error}\"\n}",
          "type": "json"
        },
        {
          "title": "500 Server Error",
          "content": "HTTP/1.1 500 Server Error\n{\n    \"error\" : \"{Motivo del error}\"\n}",
          "type": "json"
        }
      ]
    }
  },
  {
    "type": "get",
    "url": "/v1/feriados/:anio",
    "title": "Consultar Feriados",
    "name": "Consultar_todos_los_feriados_de_un_Año_dado_(anio)",
    "group": "Feriados",
    "success": {
      "examples": [
        {
          "title": "Response",
          "content": "HTTP/1.1 200 OK\n[\n    {\n        dia':\"{Numero del Dia [1-31]} Integer\",\n        'mes':\"{Numero del Mes [1-12]} Integer\"\n        'motivo': \"{Descripcion Opcional} String\",\n    }\n]",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "./app/feriados/routes.py",
    "groupTitle": "Feriados",
    "error": {
      "examples": [
        {
          "title": "400 Bad Request",
          "content": "HTTP/1.1 400 Bad Request\n{\n    \"path\" : \"{Nombre de la propiedad}\",\n    \"message\" : \"{Motivo del error}\"\n}",
          "type": "json"
        },
        {
          "title": "400 Bad Request",
          "content": "HTTP/1.1 400 Bad Request\n{\n    \"error\" : \"{Motivo del error}\"\n}",
          "type": "json"
        },
        {
          "title": "500 Server Error",
          "content": "HTTP/1.1 500 Server Error\n{\n    \"error\" : \"{Motivo del error}\"\n}",
          "type": "json"
        }
      ]
    }
  },
  {
    "type": "patch",
    "url": "/v1/scores/:scoresId/activar",
    "title": "Activar Scores",
    "name": "Activar_configuracion_de_pesos",
    "group": "Scores",
    "success": {
      "examples": [
        {
          "title": "Response",
          "content": "HTTP/1.1 200 OK\n{\n    \"_id\": \"{ObjectId}\",\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "./app/scores/routes.py",
    "groupTitle": "Scores",
    "error": {
      "examples": [
        {
          "title": "400 Bad Request",
          "content": "HTTP/1.1 400 Bad Request\n{\n    \"path\" : \"{Nombre de la propiedad}\",\n    \"message\" : \"{Motivo del error}\"\n}",
          "type": "json"
        },
        {
          "title": "400 Bad Request",
          "content": "HTTP/1.1 400 Bad Request\n{\n    \"error\" : \"{Motivo del error}\"\n}",
          "type": "json"
        },
        {
          "title": "500 Server Error",
          "content": "HTTP/1.1 500 Server Error\n{\n    \"error\" : \"{Motivo del error}\"\n}",
          "type": "json"
        }
      ]
    }
  },
  {
    "type": "post",
    "url": "/v1/scores/",
    "title": "Crear Scores",
    "name": "Cargar_configuracion_de_pesos",
    "group": "Scores",
    "examples": [
      {
        "title": "Body",
        "content": "{\n    \"constraintConfiguration\": [\n        {\n            'nombreRestriccion':\"{Nombre de la restriccion} String\",\n            'pesosRestriccion':\"{Pesos de la restriccion (X => Entero)[XX/XX/XX/XX/XX]} String\"\n        }\n    ]\n}",
        "type": "json"
      }
    ],
    "success": {
      "examples": [
        {
          "title": "Response",
          "content": "HTTP/1.1 200 OK\n{\n    \"constraintConfiguration\": [\n        {\n            'nombreRestriccion':\"{Nombre de la restriccion} String\",\n            'pesosRestriccion':\"{Pesos de la restriccion (X => Entero)[XX/XX/XX/XX/XX]} String\"\n        }\n    ],\n    \"activo\": False,\n    \"_id\": \"{ObjectId}\",\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "./app/scores/routes.py",
    "groupTitle": "Scores",
    "error": {
      "examples": [
        {
          "title": "400 Bad Request",
          "content": "HTTP/1.1 400 Bad Request\n{\n    \"path\" : \"{Nombre de la propiedad}\",\n    \"message\" : \"{Motivo del error}\"\n}",
          "type": "json"
        },
        {
          "title": "400 Bad Request",
          "content": "HTTP/1.1 400 Bad Request\n{\n    \"error\" : \"{Motivo del error}\"\n}",
          "type": "json"
        },
        {
          "title": "500 Server Error",
          "content": "HTTP/1.1 500 Server Error\n{\n    \"error\" : \"{Motivo del error}\"\n}",
          "type": "json"
        }
      ]
    }
  },
  {
    "type": "post",
    "url": "/v1/scores/:scoresId",
    "title": "Consultar Scores",
    "name": "Consultar_configuracion_de_pesos",
    "group": "Scores",
    "success": {
      "examples": [
        {
          "title": "Response",
          "content": "HTTP/1.1 200 OK\n{\n    \"constraintConfiguration\": [\n        {\n            'nombreRestriccion':\"{Nombre de la restriccion} String\",\n            'pesosRestriccion':\"{Pesos de la restriccion (X => Entero)[XX/XX/XX/XX/XX]} String\"\n        }\n    ],\n    \"activo\": \"Boolean\",\n    \"_id\": \"{ObjectId}\",\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "./app/scores/routes.py",
    "groupTitle": "Scores",
    "error": {
      "examples": [
        {
          "title": "400 Bad Request",
          "content": "HTTP/1.1 400 Bad Request\n{\n    \"path\" : \"{Nombre de la propiedad}\",\n    \"message\" : \"{Motivo del error}\"\n}",
          "type": "json"
        },
        {
          "title": "400 Bad Request",
          "content": "HTTP/1.1 400 Bad Request\n{\n    \"error\" : \"{Motivo del error}\"\n}",
          "type": "json"
        },
        {
          "title": "500 Server Error",
          "content": "HTTP/1.1 500 Server Error\n{\n    \"error\" : \"{Motivo del error}\"\n}",
          "type": "json"
        }
      ]
    }
  },
  {
    "type": "patch",
    "url": "/v1/scores/:scoresId/desactivar",
    "title": "Desactivar Scores",
    "name": "Desactivar_configuracion_de_pesos",
    "group": "Scores",
    "success": {
      "examples": [
        {
          "title": "Response",
          "content": "HTTP/1.1 200 OK\n{\n    \"_id\": \"{ObjectId}\",\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "./app/scores/routes.py",
    "groupTitle": "Scores",
    "error": {
      "examples": [
        {
          "title": "400 Bad Request",
          "content": "HTTP/1.1 400 Bad Request\n{\n    \"path\" : \"{Nombre de la propiedad}\",\n    \"message\" : \"{Motivo del error}\"\n}",
          "type": "json"
        },
        {
          "title": "400 Bad Request",
          "content": "HTTP/1.1 400 Bad Request\n{\n    \"error\" : \"{Motivo del error}\"\n}",
          "type": "json"
        },
        {
          "title": "500 Server Error",
          "content": "HTTP/1.1 500 Server Error\n{\n    \"error\" : \"{Motivo del error}\"\n}",
          "type": "json"
        }
      ]
    }
  }
] });
