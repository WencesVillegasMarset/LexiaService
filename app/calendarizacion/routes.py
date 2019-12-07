import flask


"""
    Envia la documentacion de la API generada por APIDoc
"""


def init_routes(app):

    @app.route('/', methods=['GET'])
    def index():
        return flask.send_from_directory('../public', "index.html")

    """"""
    @app.route('/v1/calendarizacion/<calendarId>', methods=['GET'])
    def solicitarCalendarizacion(calendarId):
        # try:
        # params = json.body_to_dic(flask.request.data)
        # params = restValidator.validateData(params)
        # guardar calendarizacion en base de datos
        # correr background task
        # retornar respuesta sobre exito o fracaso
        return "Hello, World!"
        # except Exception as error:
        #     return errors.handleError(error)
    return app

