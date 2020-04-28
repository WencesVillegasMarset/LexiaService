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


def crearSolucion(params, solicitudId):

    # Actualizamos los valores validos a actualizar
    # solicitud.update(params)
    params['created'] = datetime.datetime.utcnow()
    params['solicitudId'] = solicitudId
    solucionId = db.soluciones.insert_one(params).inserted_id

    return solucionId


def getSolicitud(solicitudId):
    try:
        result = db.solicitudes.find_one({"_id": bson.ObjectId(solicitudId)})
        if (not result):
            raise error.InvalidArgument("_id", "Solicitud does not exists")
        return result
    except Exception:
        raise error.InvalidArgument("_id", "Invalid object id")


def getSolicitudList(url, start, pagesize):
    # try:
    result = {}
    result['total'] = db.solicitudes.count_documents(filter={})
    if result['total'] < start:
        raise error.InvalidArgument("start", "Invalid start number")
    if start == 0:
        result['results'] = list(db.solicitudes.find(projection={}).limit(pagesize))
        result['previous'] = ''
    else:
        result['results'] = list(db.solicitudes.find(projection={}).skip(start).limit(pagesize))
        result['previous'] = url + '?start={}'.format(start-pagesize)

    if result['total'] > start + pagesize:
        result['next'] = url + '?start={}'.format(start+pagesize)
    else:
        result['next'] = ''

    return result

    # except Exception:
        

def getSolucion(solicitudId):
    try:
        query_params = {"solicitudId": bson.ObjectId(solicitudId)}
        result = db.soluciones.find_one(query_params)
        if (not result):
            raise error.InvalidArgument("_id", "Solucion does not exists")
        return result
    except Exception:
        raise error.InvalidArgument("_id", "Invalid object id")


def deleteSolicitud(solicitudId):
    try:
        query_params = {"_id": bson.ObjectId(solicitudId)}
        result = db.solicitudes.delete_one(query_params)
        if (result.deleted_count == 0):
            raise error.InvalidArgument("_id", "Solucion does not exists")
        return result
    except Exception:
        raise error.InvalidArgument("_id", "Invalid object id")


def deleteSolucion(solucionId):
    try:
        query_params = {"_id": bson.ObjectId(solucionId)}
        result = db.soluciones.delete_one(query_params)
        if (result.deleted_count == 0):
            raise error.InvalidArgument("_id", "Solucion does not exists")
        return result
    except Exception:
        raise error.InvalidArgument("_id", "Invalid object id")
