import app.utils.errors as error
import datetime
import app.utils.validator as validator

SINGLE_SCORE_SCHEMA = {
    "nombreRestriccion": {
        "required": True,
        "type": str,
    },
    "valorScore": {
        "required": True,
        "type": str,
    }
}

SCORES_SCHEMA = {
    "scoreList": {
        "required": True,
        "minQuantity": 1,
        "type": list,
        "child_schema": SINGLE_SCORE_SCHEMA
    }
}


def validarScores(documento):
    err = validator.validateSchema(SCORES_SCHEMA, documento)

    if (len(err) > 0):
        raise error.MultipleArgumentException(err)


def validarScore(score):
    if score:
        pass
    else:
        raise error.InvalidArgument('anio', 'Formato de año invalido')


def newScores():
    return {
        "scoreList": [],
        "created": datetime.datetime.utcnow()
    }
