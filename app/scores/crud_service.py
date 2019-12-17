import app.utils.database as db
import datetime
import bson
import app.utils.errors as error


def crearScores(data):

    # Actualizamos los valores validos a actualizar
    # solicitud.update(params)
    data['created'] = datetime.datetime.utcnow()
    data['_id'] = db.scores.insert_one(data).inserted_id

    return data


def getScores(scoresId):

    try:
        result = db.scores.find_one({"_id": bson.ObjectId(oid=scoresId)},
            sort=[('created', db.pymongo.DESCENDING)])
        if (not result):
            raise error.InvalidArgument("id", "No hay scores con ese id")
        return result
    except Exception:
        raise error.InvalidArgument("id", "Invalid ID")


def getLatestScores():
    try:
        result = db.scores.find_one(sort=[('created', db.pymongo.DESCENDING)])
        if (not result):
            raise error.InvalidArgument("created", "No hay scores")
        return result

    except Exception:
        raise error.InvalidArgument("Created", "Scores")
