import app.utils.database as db
import datetime
import bson
import app.utils.errors as error


def crearSolicitud(params):

    # Actualizamos los valores validos a actualizar
    # solicitud.update(params)
    params['created'] = datetime.datetime.utcnow()
    solicitudId = db.solicitudes.insert_one(params).inserted_id

    return solicitudId


def getSolicitud(solicitudId):
    try:
        result = db.solicitudes.find_one({"_id": bson.ObjectId(solicitudId)})
        if (not result):
            raise error.InvalidArgument("_id", "Solicitud does not exists")
        return result
    except Exception:
        raise error.InvalidArgument("_id", "Invalid object id")


def getSolucion(solicitudId):
    try:
        query_params = {"solicitudId": bson.ObjectId(solicitudId)}
        result = db.soluciones.find_one(query_params)
        if (not result):
            raise error.InvalidArgument("_id", "Solucion does not exists")
        return result
    except Exception:
        raise error.InvalidArgument("_id", "Invalid object id")
