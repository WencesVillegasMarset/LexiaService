import pymongo

import app.utils.config as config

client = pymongo.MongoClient(
    config.Config.DATABASE_URL,
    config.Config.DATABASE_PORT)

db = client['calendarizaciones']

solicitudes = db.solicitudes
soluciones = db.soluciones
feriados = db.feriados
scores = db.scores
