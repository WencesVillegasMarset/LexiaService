import flask
from app.utils.tasks import parse_to_xml
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
            application.q.enqueue(parse_to_xml, solicitud)
            return json.dic_to_json({'solicitudId': solicitudId})

        except Exception as error:
            return errors.handleError(error)

    @app.route('/v1/solicitud/<solicitudId>', methods=['GET'])
    def consultarSolicitud(solicitudId):
        pass


    @app.route('/v1/solicitud/sandbox', methods=['POST'])
    def solicitarCalendarizacionSandbox():
        pass


    @app.route('/v1/solucion/<solicitudId>', methods=['GET'])
    def consultarCalendarizacionSandbox(solicitudId):
        pass

    return app
