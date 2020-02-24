import flask
import app.scores.schema as restValidator
import app.utils.serialize as json
import app.utils.errors as errors
import app.scores.crud_service as crud


def init_routes(app):

    """
    @api {post} /v1/scores/:scoresId Consultar Scores
    @apiName Consultar configuracion de pesos
    @apiGroup Scores

    @apiSuccessExample {json} Response
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
        @apiUse Errors
    """

    @app.route('/v1/scores/<scoresId>', methods=['GET'])
    def consultarScores(scoresId):
        try:
            feriados = crud.getScores(scoresId)
            # solicitud['AudienciaSchedule'] = params
            # application.q.enqueue(parse_to_xml, solicitud)
            return json.dic_to_json(feriados)

        except Exception as error:
            return errors.handleError(error)

    """
    @api {post} /v1/scores/ Crear Scores
    @apiName Cargar configuracion de pesos
    @apiGroup Scores

    @apiExample {json} Body
        {
            "constraintConfiguration": [
                {
                    'nombreRestriccion':"{Nombre de la restriccion} String",
                    'pesosRestriccion':"{Pesos de la restriccion (X => Entero)[XX/XX/XX/XX/XX]} String"
                }
            ]
        }
    @apiSuccessExample {json} Response
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
        @apiUse Errors
    """

    @app.route('/v1/scores/', methods=['POST'])
    def cargarScores():
        try:
            params = json.body_to_dic(flask.request.data)
            restValidator.validarScores(params)
            result = crud.crearScores(params)
            return json.dic_to_json(result)

        except Exception as error:
            return errors.handleError(error)

    """
    @api {patch} /v1/scores/:scoresId/activar Activar Scores
    @apiName Activar configuracion de pesos
    @apiGroup Scores

    @apiSuccessExample {json} Response
        HTTP/1.1 200 OK
        {
            "_id": "{ObjectId}",
        }
        @apiUse Errors
    """

    @app.route('/v1/scores/<scoresId>/activar', methods=['PATCH'])
    def activarScores(scoresId):
        try:
            result = crud.updateScores(scoresId, {'activo': True})
            return json.dic_to_json(result)

        except Exception as error:
            return errors.handleError(error)

    """
    @api {patch} /v1/scores/:scoresId/desactivar Desactivar Scores
    @apiName Desactivar configuracion de pesos
    @apiGroup Scores

    @apiSuccessExample {json} Response
        HTTP/1.1 200 OK
        {
            "_id": "{ObjectId}",
        }
        @apiUse Errors
    """

    @app.route('/v1/scores/<scoresId>/desactivar', methods=['PATCH'])
    def desactivarScores(scoresId):
        try:
            result = crud.updateScores(scoresId, {'activo': False})
            return json.dic_to_json(result)

        except Exception as error:
            return errors.handleError(error)
    return app
