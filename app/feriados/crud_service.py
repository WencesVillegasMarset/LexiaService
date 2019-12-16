import app.utils.database as db
import datetime
# import bson
import app.utils.errors as error


def crearFeriados(data):

    # Actualizamos los valores validos a actualizar
    # solicitud.update(params)
    data['created'] = datetime.datetime.utcnow()
    data['_id'] = db.feriados.insert_one(data).inserted_id

    return data


def getFeriados(anio):

    try:
        result = db.feriados.find_one(
            {
                "anio": anio,
            },
            sort=[('created', db.pymongo.DESCENDING)])
        if (not result):
            raise error.InvalidArgument("anio", "No hay feriadso para ese año")
        return result['feriadoList']

    except Exception:
        raise error.InvalidArgument("anio", "Año invalido")
