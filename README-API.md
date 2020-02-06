<a name="top"></a>
# Lexia Scheduling Service v0.1.0



- [Calendarizacion](#calendarizacion)
	- [Solicitar Calendarizacion](#solicitar-calendarizacion)
	


# <a name='calendarizacion'></a> Calendarizacion

## <a name='solicitar-calendarizacion'></a> Solicitar Calendarizacion
[Back to top](#top)



	POST /v1/calendarizacion/



### Examples

Body

```
{
    "sala": [
        {
            'idSala':"{id de la sala}" "Integer",
            'calendarizable':"{se pueden calendarizar en esta sala} Boolean"
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
            'tipo': "{Tipo de la audiencia} String",
            'almafuerte': "{True si es en Almafuerte } Boolean",
            'boulonge_sur_mer': "{True si es en Boulonge Sur Mer} Boolean",
            'fechaSolicutud': "{Fecha en la que fue solicitada la Audiencia} String (YYYY/MM/DD),
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
            'tipo': "{Tipo de la audiencia} String",
            'almafuerte': "{True si es en Almafuerte } Boolean",
            'boulonge_sur_mer': "{True si es en Boulonge Sur Mer} Boolean",
            'fechaSolicutud': "{Fecha en la que fue solicitada la Audiencia} String (YYYY/MM/DD),
            'fechaRealizacion': "{Fecha en la que fue calendarizada la Audiencia} String (YYYY/MM/DD),
            'horaComienzo': "{Hora en la que fue calendarizada la Audiencia} String (HH:MM),
            'idSala': "{id Sala en la que fue calendarizada} Integer,
            'duracion': Integer,
            'id': Integer,
        }
    ],
    "horarioNormalJuez": [{ // No definitivo
        "idJuez":Integer,
        'dia':[{
                'diaSemana': "{1 a 5, de Lunes a Viernes} Integer" ,
                'horaInicio': "String (HH:MM)",
                'horaFin': "String (HH:MM)",
        }]
    }],
    "indisposicionJuez": [{ // No definitivo
        "idJuez": "Integer",
        "dia": [{
            'fecha': "String (YYYY/MM/DD)" ,
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
