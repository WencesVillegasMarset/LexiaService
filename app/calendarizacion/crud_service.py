import app.utils.database as db
import datetime


def crearSolicitud(params):

    # Actualizamos los valores validos a actualizar
    # solicitud.update(params)
    params['created'] = datetime.datetime.utcnow()
    solicitudId = db.solicitudes.insert_one(params).inserted_id

    return solicitudId
