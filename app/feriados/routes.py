import flask
import app.feriados.schema as restValidator
import app.utils.serialize as json
import app.utils.errors as errors
import app.feriados.crud_service as crud

"""
    Envia la documentacion de la API generada por APIDoc
"""


def init_routes(app):

    @app.route('/v1/feriados/<year>', methods=['GET'])
    def consultarFeriados(year):
        try:
            year = int(year)
            restValidator.validarAnio(year)
            feriados = crud.getFeriados(year)
            # solicitud['AudienciaSchedule'] = params
            # application.q.enqueue(parse_to_xml, solicitud)
            return json.dic_to_json(feriados)

        except Exception as error:
            return errors.handleError(error)

    @app.route('/v1/feriados/', methods=['POST'])
    def cargarFeriados():
        try:
            params = json.body_to_dic(flask.request.data)
            restValidator.validarFeriados(params)
            result = crud.crearFeriados(params)
            return json.dic_to_json(result)

        except Exception as error:
            return errors.handleError(error)

    return app
