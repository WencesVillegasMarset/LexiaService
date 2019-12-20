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

    @app.route('/', methods=['GET'])
    def index():
        return flask.send_from_directory('../public', "index.html")

    """
    @api {post} /v1/calendarizacion/ Solicitar Calendarizacion
    @apiName Hacer Solicitud de Calendarizacion
    @apiGroup Calendarizacion

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
            params = service.toSolverFormat(params)
            solicitud = {}
            solicitud['AudienciaSchedule'] = params
            application.q.enqueue(run_solver, solicitud, solicitudId)
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

    @app.route('/v1/solicitud/sandbox', methods=['POST'])
    def solicitarCalendarizacionSandbox():
        return json.dic_to_json({'error': 'Not Implemented'})

    @app.route('/v1/solucion/<solicitudId>', methods=['GET'])
    def consultarCalendarizacion(solicitudId):
        try:
            solucion = crud.getSolucion(solicitudId)
            return json.dic_to_json(solucion)

        except Exception as error:
            return errors.handleError(error)

    return app
