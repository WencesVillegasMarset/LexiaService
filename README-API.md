<a name="top"></a>
# Lexia Scheduling Service v0.1.0



- [Calendarizacion](#calendarizacion)
	- [Solicitar Solucion](#solicitar-solucion)
	- [Solicitar Excel de Calendarizacion](#solicitar-excel-de-calendarizacion)
	- [Eliminar Solicitud](#eliminar-solicitud)
	- [Eliminar Solucion](#eliminar-solucion)
	- [Solicitar Calendarizacion](#solicitar-calendarizacion)
	- [Solicitar Calendarizacion Modo Prueba](#solicitar-calendarizacion-modo-prueba)
	
- [Feriados](#feriados)
	- [Crear Feriados](#crear-feriados)
	- [Consultar Feriados](#consultar-feriados)
	
- [Scores](#scores)
	- [Activar Scores](#activar-scores)
	- [Crear Scores](#crear-scores)
	- [Consultar Scores](#consultar-scores)
	- [Desactivar Scores](#desactivar-scores)
	


# <a name='calendarizacion'></a> Calendarizacion

## <a name='solicitar-solucion'></a> Solicitar Solucion
[Back to top](#top)



	GET /v1/calendarizacion/:solicitudId



### Examples

undefined

```
@apiExample
```


### Success Response

Response

```
HTTP/1.1 200 OK
    {
        "_id": "{ObjectId de la Solucion}",
        "audiencia": [ // lista de audiencias calendarizadas
            {
                "fijada": "{Boolean}",
                "idSala": "{ID de la Sala donde se calendarizo}",
                "id": "{ID de la Audiencia}",
                "fechaAudiencia": "{Fecha en la que se calendarizo (YYYY-MM-DD)}",
                "horaAudiencia": "Hora en la que se calendarizo (HH:MM)"
            }
        ],
        "created": "{Datetime de Creacion}",
        "solicitudId": "{ID de la Solicitud}"
    }
```


### Error Response

400 Bad Request

```
HTTP/1.1 400 Bad Request
{
    "path" : "{Nombre de la propiedad}",
    "message" : "{Motivo del error}"
}
```
400 Bad Request

```
HTTP/1.1 400 Bad Request
{
    "error" : "{Motivo del error}"
}
```
500 Server Error

```
HTTP/1.1 500 Server Error
{
    "error" : "{Motivo del error}"
}
```
## <a name='solicitar-excel-de-calendarizacion'></a> Solicitar Excel de Calendarizacion
[Back to top](#top)



	GET /v1/solucion/:solicitudId/excel



### Examples

undefined

```
@apiExample
```


### Success Response

Response

```
HTTP/1.1 200 OK
Archivo .xlsx
```


### Error Response

400 Bad Request

```
HTTP/1.1 400 Bad Request
{
    "path" : "{Nombre de la propiedad}",
    "message" : "{Motivo del error}"
}
```
400 Bad Request

```
HTTP/1.1 400 Bad Request
{
    "error" : "{Motivo del error}"
}
```
500 Server Error

```
HTTP/1.1 500 Server Error
{
    "error" : "{Motivo del error}"
}
```
## <a name='eliminar-solicitud'></a> Eliminar Solicitud
[Back to top](#top)



	DELETE /v1/solicitud/:solicitudId



### Examples

undefined

```
@apiExample
```


### Success Response

Response

```
HTTP/1.1 200 OK
```


### Error Response

400 Bad Request

```
HTTP/1.1 400 Bad Request
{
    "path" : "{Nombre de la propiedad}",
    "message" : "{Motivo del error}"
}
```
400 Bad Request

```
HTTP/1.1 400 Bad Request
{
    "error" : "{Motivo del error}"
}
```
500 Server Error

```
HTTP/1.1 500 Server Error
{
    "error" : "{Motivo del error}"
}
```
## <a name='eliminar-solucion'></a> Eliminar Solucion
[Back to top](#top)



	DELETE /v1/solucion/:solucionId



### Examples

undefined

```
@apiExample
```


### Success Response

Response

```
HTTP/1.1 200 OK
```


### Error Response

400 Bad Request

```
HTTP/1.1 400 Bad Request
{
    "path" : "{Nombre de la propiedad}",
    "message" : "{Motivo del error}"
}
```
400 Bad Request

```
HTTP/1.1 400 Bad Request
{
    "error" : "{Motivo del error}"
}
```
500 Server Error

```
HTTP/1.1 500 Server Error
{
    "error" : "{Motivo del error}"
}
```
## <a name='solicitar-calendarizacion'></a> Solicitar Calendarizacion
[Back to top](#top)



	POST /v1/calendarizacion/



### Examples

Body

```
{
    "sala": [ // up to date
        {
            'idSala':"{id de la sala}" "Integer",
            'calendarizable':"{se pueden calendarizar en esta sala} Boolean"
            'almafuerte': "{True si es en Almafuerte } Boolean",
            'boulonge_sur_mer': "{True si es en Boulonge Sur Mer} Boolean",
        }
    ],
    "audiencia": [
        {
            "juez": [{
                "idJuez": "Integer",
            }],
            "defensor": [{
                "idDefensor": "Integer",
            }],
            "fiscal": [{
                "idFiscal": "Integer",
            }],
            "querellante": [{
                "idQuerellante": "Integer",
            }],
            "asesor": [{
                "idAsesor": "Integer",
            }],
            'riesgosa': "{Hay alto riesgo de que se extienda mas de la duracion estimaada?} Boolean",
            'detenido': "{Tiene Detenidos?} Boolean",
            'tipo': "{ID del tipo de la audiencia} Integer",
            'almafuerte': "{True si es en Almafuerte } Boolean",
            'boulonge_sur_mer': "{True si es en Boulonge Sur Mer} Boolean",
            'fechaSolicitud': "{Fecha en la que fue solicitada la Audiencia} String (YYYY-MM-DD),
            'duracion': Integer,
            'id': Integer,
        }
    ],
    "audienciaFijada": [
        {
            "juez": [{
                "idJuez": "Integer",
            }],
            "defensor": [{
                "idDefensor": "Integer",
            }],
            "fiscal": [{
                "idFiscal": "Integer",
            }],
            "querellante": [{
                "idQuerellante": "Integer",
            }],
            "asesor": [{
                "idAsesor": "Integer",
            }],
            'riesgosa': "{Hay alto riesgo de que se extienda mas de la duracion estimaada?} Boolean",
            'detenido': "{Tiene Detenidos?} Boolean",
            'externa': "{Hay alto riesgo de que se extienda mas de la duracion estimaada?} Boolean",
            'tipo': {
                'idTipo':"{ID del tipo de la audiencia} Integer",
                'tiempoRealizacionMinimo':"{Numero de dias minimo para fijacion} Integer",
                'tiempoRealizacionMaximo':"{Numero de dias minimo para fijacion} Integer",
            }
            'almafuerte': "{True si es en Almafuerte } Boolean",
            'boulonge_sur_mer': "{True si es en Boulonge Sur Mer} Boolean",
            'fechaSolicitud': "{Fecha en la que fue solicitada la Audiencia} String (YYYY-MM-DD),
            'fechaRealizacion': "{Fecha en la que fue calendarizada la Audiencia} String (YYYY-MM-DD),
            'horaComienzo': "{Hora en la que fue calendarizada la Audiencia} String (HH:MM),
            'idSala': "{id Sala en la que fue calendarizada} Integer,
            'duracion': Integer,
            'id': Integer,
        }
    ],
    "licenciaJuez": [{ // up to date
        "idJuez":Integer,
        'fechaInicio': "String (YYYY-MM-DD)" ,
        'fechaFin': "String (YYYY-MM-DD)" ,
    }],
    "turnoTardeJuez": [{ // up to date
        "fecha": "String (YYYY-MM-DD)" ,
        "juez": [{
            "idJuez": "Integer",
        }]
    }],
    "indisposicionJuez": [{ // up to date
        "idJuez": "Integer",
        "dia": [{
            'fecha': "String (YYYY-MM-DD)" ,
            'horaInicio': "String (HH:MM)",
            'horaFin': "String (HH:MM)",
        }]
    }],
    "urlNotificacion": "{URL a la que se notificará cuando el Solver arroje resultados} String"
}
```


### Success Response

Response

```
HTTP/1.1 200 OK
{
    'solicitudId' : {ObjectId}
}
```


### Error Response

400 Bad Request

```
HTTP/1.1 400 Bad Request
{
    "path" : "{Nombre de la propiedad}",
    "message" : "{Motivo del error}"
}
```
400 Bad Request

```
HTTP/1.1 400 Bad Request
{
    "error" : "{Motivo del error}"
}
```
500 Server Error

```
HTTP/1.1 500 Server Error
{
    "error" : "{Motivo del error}"
}
```
## <a name='solicitar-calendarizacion-modo-prueba'></a> Solicitar Calendarizacion Modo Prueba
[Back to top](#top)



	POST /v1/calendarizacion/sandbox



### Examples

Body

```
{
    "sala": [ // up to date
        {
            'idSala':"{id de la sala}" "Integer",
            'calendarizable':"{se pueden calendarizar en esta sala} Boolean"
            'almafuerte': "{True si es en Almafuerte } Boolean",
            'boulonge_sur_mer': "{True si es en Boulonge Sur Mer} Boolean",
        }
    ],
    "audiencia": [
        {
            "juez": [{
                "idJuez": "Integer",
            }],
            "defensor": [{
                "idDefensor": "Integer",
            }],
            "fiscal": [{
                "idFiscal": "Integer",
            }],
            "querellante": [{
                "idQuerellante": "Integer",
            }],
            "asesor": [{
                "idAsesor": "Integer",
            }],
            'riesgosa': "{Hay alto riesgo de que se extienda mas de la duracion estimaada?} Boolean",
            'detenido': "{Tiene Detenidos?} Boolean",
            'tipo': "{ID del tipo de la audiencia} Integer",
            'almafuerte': "{True si es en Almafuerte } Boolean",
            'boulonge_sur_mer': "{True si es en Boulonge Sur Mer} Boolean",
            'fechaSolicitud': "{Fecha en la que fue solicitada la Audiencia} String (YYYY-MM-DD),
            'duracion': Integer,
            'id': Integer,
        }
    ],
    "audienciaFijada": [
        {
            "juez": [{
                "idJuez": "Integer",
            }],
            "defensor": [{
                "idDefensor": "Integer",
            }],
            "fiscal": [{
                "idFiscal": "Integer",
            }],
            "querellante": [{
                "idQuerellante": "Integer",
            }],
            "asesor": [{
                "idAsesor": "Integer",
            }],
            'riesgosa': "{Hay alto riesgo de que se extienda mas de la duracion estimaada?} Boolean",
            'detenido': "{Tiene Detenidos?} Boolean",
            'externa': "{Hay alto riesgo de que se extienda mas de la duracion estimaada?} Boolean",
            'tipo': {
                'idTipo':"{ID del tipo de la audiencia} Integer",
                'tiempoRealizacionMinimo':"{Numero de dias minimo para fijacion} Integer",
                'tiempoRealizacionMaximo':"{Numero de dias minimo para fijacion} Integer",
            }
            'almafuerte': "{True si es en Almafuerte } Boolean",
            'boulonge_sur_mer': "{True si es en Boulonge Sur Mer} Boolean",
            'fechaSolicitud': "{Fecha en la que fue solicitada la Audiencia} String (YYYY-MM-DD),
            'fechaRealizacion': "{Fecha en la que fue calendarizada la Audiencia} String (YYYY-MM-DD),
            'horaComienzo': "{Hora en la que fue calendarizada la Audiencia} String (HH:MM),
            'idSala': "{id Sala en la que fue calendarizada} Integer,
            'duracion': Integer,
            'id': Integer,
        }
    ],
    "licenciaJuez": [{ // up to date
        "idJuez":Integer,
        'fechaInicio': "String (YYYY-MM-DD)" ,
        'fechaFin': "String (YYYY-MM-DD)" ,
    }],
    "turnoTardeJuez": [{ // up to date
        "fecha": "String (YYYY-MM-DD)" ,
        "juez": [{
            "idJuez": "Integer",
        }]
    }],
    "indisposicionJuez": [{ // up to date
        "idJuez": "Integer",
        "dia": [{
            'fecha': "String (YYYY-MM-DD)" ,
            'horaInicio': "String (HH:MM)",
            'horaFin': "String (HH:MM)",
        }]
    }],
    "urlNotificacion": "{URL a la que se notificará cuando el Solver arroje resultados} String"
    "fechaSolicitud": "{Fecha en la que se correrá la simulacion. e.g:
                        Simulamos para las audiencias que llegaron el 10 Nov 2018 => 2018-11-10} String"

}
```


### Success Response

Response

```
HTTP/1.1 200 OK
{
    'solicitudId' : {ObjectId}
}
```


### Error Response

400 Bad Request

```
HTTP/1.1 400 Bad Request
{
    "path" : "{Nombre de la propiedad}",
    "message" : "{Motivo del error}"
}
```
400 Bad Request

```
HTTP/1.1 400 Bad Request
{
    "error" : "{Motivo del error}"
}
```
500 Server Error

```
HTTP/1.1 500 Server Error
{
    "error" : "{Motivo del error}"
}
```
# <a name='feriados'></a> Feriados

## <a name='crear-feriados'></a> Crear Feriados
[Back to top](#top)



	POST /v1/feriados/



### Examples

Body

```
{
    "feriadoList": [ 
        {
            'dia':"{Numero del Dia [1-31]} Integer",
            'mes':"{Numero del Mes [1-12]} Integer"
            'motivo': "{Descripcion Opcional} String",
        }
    ],
    "anio": {"Año en el que acontecen los feriados" Integer}
}
```


### Success Response

Response

```
HTTP/1.1 200 OK
{
    "feriadoList": [ 
        {
            'dia':"{Numero del Dia [1-31]} Integer",
            'mes':"{Numero del Mes [1-12]} Integer"
            'motivo': "{Descripcion Opcional} String",
        }
    ],
    "anio": "{Año en el que acontecen los feriados} Integer",
    "created": "{Date}"
}
```


### Error Response

400 Bad Request

```
HTTP/1.1 400 Bad Request
{
    "path" : "{Nombre de la propiedad}",
    "message" : "{Motivo del error}"
}
```
400 Bad Request

```
HTTP/1.1 400 Bad Request
{
    "error" : "{Motivo del error}"
}
```
500 Server Error

```
HTTP/1.1 500 Server Error
{
    "error" : "{Motivo del error}"
}
```
## <a name='consultar-feriados'></a> Consultar Feriados
[Back to top](#top)



	GET /v1/feriados/:anio





### Success Response

Response

```
HTTP/1.1 200 OK
[
    {
        dia':"{Numero del Dia [1-31]} Integer",
        'mes':"{Numero del Mes [1-12]} Integer"
        'motivo': "{Descripcion Opcional} String",
    }
]
```


### Error Response

400 Bad Request

```
HTTP/1.1 400 Bad Request
{
    "path" : "{Nombre de la propiedad}",
    "message" : "{Motivo del error}"
}
```
400 Bad Request

```
HTTP/1.1 400 Bad Request
{
    "error" : "{Motivo del error}"
}
```
500 Server Error

```
HTTP/1.1 500 Server Error
{
    "error" : "{Motivo del error}"
}
```
# <a name='scores'></a> Scores

## <a name='activar-scores'></a> Activar Scores
[Back to top](#top)



	PATCH /v1/scores/:scoresId/activar





### Success Response

Response

```
HTTP/1.1 200 OK
{
    "_id": "{ObjectId}",
}
```


### Error Response

400 Bad Request

```
HTTP/1.1 400 Bad Request
{
    "path" : "{Nombre de la propiedad}",
    "message" : "{Motivo del error}"
}
```
400 Bad Request

```
HTTP/1.1 400 Bad Request
{
    "error" : "{Motivo del error}"
}
```
500 Server Error

```
HTTP/1.1 500 Server Error
{
    "error" : "{Motivo del error}"
}
```
## <a name='crear-scores'></a> Crear Scores
[Back to top](#top)



	POST /v1/scores/



### Examples

Body

```
{
    "constraintConfiguration": [
        {
            'nombreRestriccion':"{Nombre de la restriccion} String",
            'pesosRestriccion':"{Pesos de la restriccion (X => Entero)[XX/XX/XX/XX/XX]} String"
        }
    ]
}
```


### Success Response

Response

```
HTTP/1.1 200 OK
{
    "constraintConfiguration": [
        {
            'nombreRestriccion':"{Nombre de la restriccion} String",
            'pesosRestriccion':"{Pesos de la restriccion (X => Entero)[XX/XX/XX/XX/XX]} String"
        }
    ],
    "activo": False,
    "_id": "{ObjectId}",
}
```


### Error Response

400 Bad Request

```
HTTP/1.1 400 Bad Request
{
    "path" : "{Nombre de la propiedad}",
    "message" : "{Motivo del error}"
}
```
400 Bad Request

```
HTTP/1.1 400 Bad Request
{
    "error" : "{Motivo del error}"
}
```
500 Server Error

```
HTTP/1.1 500 Server Error
{
    "error" : "{Motivo del error}"
}
```
## <a name='consultar-scores'></a> Consultar Scores
[Back to top](#top)



	POST /v1/scores/:scoresId





### Success Response

Response

```
HTTP/1.1 200 OK
{
    "constraintConfiguration": [
        {
            'nombreRestriccion':"{Nombre de la restriccion} String",
            'pesosRestriccion':"{Pesos de la restriccion (X => Entero)[XX/XX/XX/XX/XX]} String"
        }
    ],
    "activo": "Boolean",
    "_id": "{ObjectId}",
}
```


### Error Response

400 Bad Request

```
HTTP/1.1 400 Bad Request
{
    "path" : "{Nombre de la propiedad}",
    "message" : "{Motivo del error}"
}
```
400 Bad Request

```
HTTP/1.1 400 Bad Request
{
    "error" : "{Motivo del error}"
}
```
500 Server Error

```
HTTP/1.1 500 Server Error
{
    "error" : "{Motivo del error}"
}
```
## <a name='desactivar-scores'></a> Desactivar Scores
[Back to top](#top)



	PATCH /v1/scores/:scoresId/desactivar





### Success Response

Response

```
HTTP/1.1 200 OK
{
    "_id": "{ObjectId}",
}
```


### Error Response

400 Bad Request

```
HTTP/1.1 400 Bad Request
{
    "path" : "{Nombre de la propiedad}",
    "message" : "{Motivo del error}"
}
```
400 Bad Request

```
HTTP/1.1 400 Bad Request
{
    "error" : "{Motivo del error}"
}
```
500 Server Error

```
HTTP/1.1 500 Server Error
{
    "error" : "{Motivo del error}"
}
```
