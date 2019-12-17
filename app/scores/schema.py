import app.utils.errors as error
import datetime
import app.utils.validator as validator


SINGLE_SCORE_SCHEMA = {
    "nombreRestriccion": {
        "required": True,
        "type": str,
    },
    "pesosRestriccion": {
        "required": True,
        "type": str,
    }
}

SCORES_SCHEMA = {
    "constraintConfiguration": {
        "required": True,
        "minQuantity": 1,
        "type": list,
        "childSchema": SINGLE_SCORE_SCHEMA
    }
}


def validarScores(documento):
    err = validator.validateSchema(SCORES_SCHEMA, documento)

    if (len(err) > 0):
        raise error.MultipleArgumentException(err)


def newScores():
    return {
        "scoreList": [],
        "created": datetime.datetime.utcnow()
    }
