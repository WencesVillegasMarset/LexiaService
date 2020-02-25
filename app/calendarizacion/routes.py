import flask
from app.utils.tasks import run_solver
import app as application
import app.calendarizacion.schema as restValidator
import app.utils.serialize as json
import app.utils.errors as errors
import app.calendarizacion.crud_service as crud
import app.calendarizacion.service as service

"""
    Envia la documentacion de la API generada por APIDoc
"""


def init_routes(app):

    @app.route('/<path:path>')
    def api_index(path):
        return flask.send_from_directory('../public', path)

    @app.route('/', methods=['GET'])
    def index():
        return flask.send_from_directory('../public', "index.html")

    """
    @api {post} /v1/calendarizacion/ Solicitar Calendarizacion
    @apiName Hacer Solicitud de Calendarizacion
    @apiGroup Calendarizacion

    @apiExample {json} Body
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
    @apiSuccessExample {json} Response
        HTTP/1.1 200 OK
        {
            'solicitudId' : {ObjectId}
        }
        @apiUse Errors

    """
    @app.route('/v1/solicitud/', methods=['POST'])
    def solicitarCalendarizacion():
        try:
            params = json.body_to_dic(flask.request.data)
            restValidator.validarSolicitud(params)
            solicitudId = crud.crearSolicitud(params)
            audiencias_data, juez_data = service.toSolverFormat(params)
            solicitud = (
                audiencias_data,
                juez_data['afternoon'],
                juez_data['license'],
                juez_data['special'],
                params['urlNotificacion']
            )
            application.q.enqueue(
                run_solver, solicitud, solicitudId, job_timeout=3600)

            return json.dic_to_json({'solicitudId': solicitudId})

        except Exception as error:
            return errors.handleError(error)

    @app.route('/v1/solicitud/<solicitudId>', methods=['GET'])
    def consultarSolicitud(solicitudId):
        try:
            solicitud = crud.getSolicitud(solicitudId)
            return json.dic_to_json(solicitud)

        except Exception as error:
            return errors.handleError(error)
    """
    @api {delete} /v1/solicitud/:solicitudId Eliminar Solicitud
    @apiName Eliminar una Solicitud de la Base de Datos(Hard Delete)
    @apiGroup Calendarizacion

    @apiExample
    @apiSuccessExample {200} Response
        HTTP/1.1 200 OK
        @apiUse Errors

    """

    @app.route('/v1/solicitud/<solicitudId>', methods=['DELETE'])
    def eliminarSolicitud(solicitudId):
        try:
            crud.deleteSolicitud(solicitudId)
            return flask.make_response('', 200)

        except Exception as error:
            return errors.handleError(error)

    """
    @api {post} /v1/calendarizacion/sandbox Solicitar Calendarizacion Modo Prueba
    @apiName Hacer Solicitud de Calendarizacion Modo Prueba
    @apiGroup Calendarizacion

    @apiExample {json} Body
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
    @apiSuccessExample {json} Response
        HTTP/1.1 200 OK
        {
            'solicitudId' : {ObjectId}
        }
        @apiUse Errors

    """
    @app.route('/v1/solicitud/sandbox', methods=['POST'])
    def solicitarCalendarizacionSandbox():
        try:
            params = json.body_to_dic(flask.request.data)
            restValidator.validarSolicitudSandbox(params)
            solicitudId = crud.crearSolicitud(params)
            audiencias_data, juez_data = service.toSolverFormat(params)
            solicitud = (
                audiencias_data,
                juez_data['afternoon'],
                juez_data['license'],
                juez_data['special'],
                params['urlNotificacion'],
                params['fechaSolicitud']
            )
            application.q.enqueue(
                run_solver, solicitud, solicitudId, job_timeout=3600)

            return json.dic_to_json({'solicitudId': solicitudId})

        except Exception as error:
            return errors.handleError(error)

    """
    @api {get} /v1/calendarizacion/:solicitudId Solicitar Solucion
    @apiName Consultar resultado de una Solicitud
    @apiGroup Calendarizacion

    @apiExample
    @apiSuccessExample {json} Response
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
        @apiUse Errors

    """

    @app.route('/v1/solucion/<solicitudId>', methods=['GET'])
    def consultarCalendarizacion(solicitudId):
        try:
            solucion = crud.getSolucion(solicitudId)
            return json.dic_to_json(solucion)

        except Exception as error:
            return errors.handleError(error)
    """
    @api {GET} /v1/solucion/:solicitudId/excel Solicitar Excel de Calendarizacion
    @apiName Descargar Excel de la Solucion correspondiente al ID de Solicitud
    @apiGroup Calendarizacion

    @apiExample
    @apiSuccessExample {application/spreadsheetml.sheet} Response
        HTTP/1.1 200 OK
        Archivo .xlsx
        @apiUse Errors
    """
    @app.route('/v1/solucion/<solicitudId>/excel', methods=['GET'])
    def excelCalendarizacion(solicitudId):
        try:
            if crud.getSolucion(solicitudId):
                return flask.send_from_directory(
                    app.config['CLIENT_XLSX'],
                    '{}.xlsx'.format(str(solicitudId)),
                    as_attachment=True)

        except Exception as error:
            return errors.handleError(error)

    """
    @api {delete} /v1/solucion/:solucionId Eliminar Solucion
    @apiName Eliminar una Solucion de la Base de Datos(Hard Delete)
    @apiGroup Calendarizacion

    @apiExample
    @apiSuccessExample {200} Response
        HTTP/1.1 200 OK
        @apiUse Errors

    """

    @app.route('/v1/solucion/<solucionId>', methods=['DELETE'])
    def eliminarCalendarizacion(solucionId):
        try:
            crud.deleteSolucion(solucionId)
            return flask.make_response('', 200)

        except Exception as error:
            return errors.handleError(error)

    return app
