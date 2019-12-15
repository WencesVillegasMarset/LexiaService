from flask import Flask
import os
from rq import Queue
from redis import Redis
from app.calendarizacion import routes


app = Flask(__name__, static_folder=os.path.join('..', 'public'))
# inicializo rutas de la app
app = routes.init_routes(app)
# inicializo el task queue
redis_conn = Redis()
q = Queue(connection=redis_conn)
