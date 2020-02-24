import flask
import app.feriados.schema as restValidator
import app.utils.serialize as json
import app.utils.errors as errors
import app.feriados.crud_service as crud

"""
    Envia la documentacion de la API generada por APIDoc
"""


def init_routes(app):

    """
    @api {get} /v1/feriados/:anio Consultar Feriados
    @apiName Consultar todos los feriados de un Año dado (anio)
    @apiGroup Feriados

    @apiSuccessExample {json} Response
        HTTP/1.1 200 OK
        [
            {
                dia':"{Numero del Dia [1-31]} Integer",
                'mes':"{Numero del Mes [1-12]} Integer"
                'motivo': "{Descripcion Opcional} String",
            }
        ]
        @apiUse Errors

    """

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

    """
    @api {post} /v1/feriados/ Crear Feriados
    @apiName Cargar todos los feriados de un Año dado
    @apiGroup Feriados

    @apiExample {json} Body
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
    @apiSuccessExample {json} Response
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
        @apiUse Errors
    """

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
