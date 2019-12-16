import flask
import app.scores.schema as restValidator
import app.utils.serialize as json
import app.utils.errors as errors
import app.scores.crud_service as crud


def init_routes(app):

    @app.route('/v1/scores/<scoresId>', methods=['GET'])
    def consultarScores(scoresId):
        try:
            feriados = crud.getScores(scoresId)
            # solicitud['AudienciaSchedule'] = params
            # application.q.enqueue(parse_to_xml, solicitud)
            return json.dic_to_json(feriados)

        except Exception as error:
            return errors.handleError(error)

    @app.route('/v1/scores/', methods=['POST'])
    def cargarScores():
        try:
            params = json.body_to_dic(flask.request.data)
            restValidator.validarScores(params)
            result = crud.crearScores(params)
            return json.dic_to_json(result)

        except Exception as error:
            return errors.handleError(error)

    return app
