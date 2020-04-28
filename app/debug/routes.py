import flask
import app.utils.serialize as json
import app.utils.errors as errors
import os.path as path
"""
    Envia la documentacion de la API generada por APIDoc
"""


def init_routes(app):

    """
    @api {get} /v1/debug/optaplanner Consultar logs de optaplanner
    @apiName Consultar las ultimas 5 lineas del optaplanner.log
    @apiGroup Debug

    @apiSuccessExample {json} Response
        HTTP/1.1 200 OK
        {
                'log'':[String]
        }
        @apiUse Errors

    """

    @app.route('/v1/debug/optaplanner', methods=['GET'])
    def consultarOptaplannerLog():
        try:
            result = {
                'log': []
            }
            count = 0
            with open('optaplanner.log','r') as log:
                for line in reversed(list(log)):
                    result['log'].append(line)
                    count += 1
                    if count > 5:
                        break
            return json.dic_to_json(result)

        except Exception as error:
            return errors.handleError(error)

    @app.route('/v1/debug/download', methods=['GET'])
    def descargarLog():
        try:
            logname = flask.request.args.get('name', '')
            if logname != '' and path.exists(logname):
                print(path.abspath('.'))
                return flask.send_from_directory(
                    app.config['BASE_PATH'], logname, as_attachment=True)

        except Exception as error:
            return errors.handleError(error)


    @app.route('/v1/debug/solver', methods=['GET'])
    def consultarSolverLog():
        try:
            result = {
                'log': []
            }
            count = 0
            with open('solver.log','r') as log:
                for line in reversed(list(log)):
                    result['log'].append(line)
                    count += 1
                    if count > 5:
                        break
            return json.dic_to_json(result)

        except Exception as error:
            return errors.handleError(error)

    return app
