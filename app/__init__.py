from flask import Flask
import os
from tasks.tasks import make_celery
from calendarizacion import routes
app = Flask(__name__, static_folder=os.path.join('..', 'public'))
app.config.update(
    CELERY_BROKER_URL='pyamqp://',
    CELERY_RESULT_BACKEND='redis://localhost:6379'
)
celery = make_celery(app)

app = routes.init_routes(app)
