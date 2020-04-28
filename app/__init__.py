from flask import Flask
from rq import Queue
from redis import Redis
import app.calendarizacion.routes as calendarizacion
import app.feriados.routes as feriados
import app.scores.routes as scores
import app.debug.routes as debug

import app.utils.config as config


app = Flask(__name__, static_folder='../public')
# inicializo rutas de la app
app = calendarizacion.init_routes(app)
app = feriados.init_routes(app)
app = scores.init_routes(app)
app = debug.init_routes(app)
app.config["CLIENT_XLSX"] = config.Config.CLIENT_XLSX
# inicializo el task queue
redis_conn = Redis()
q = Queue(connection=redis_conn)
