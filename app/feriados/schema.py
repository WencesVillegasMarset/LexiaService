import numbers
import app.utils.errors as error
import datetime
import app.utils.validator as validator

DIA_SCHEMA = {
    'dia': {
        "required": True,
        "type": numbers.Integral,
    },
    'mes': {
        "required": True,
        "type": numbers.Integral,
    },
    'motivo': {
        "required": False,
        "type": str,
    }
}

FERIADO_SCHEMA = {
    "anio": {
        "required": True,
        "type": numbers.Integral,
    },
    "feriadoList": {
        "required": True,
        "type": list,
        'minQuantity': 0,
        "childSchema": DIA_SCHEMA
    }
}


def validarFeriados(documento):
    err = validator.validateSchema(FERIADO_SCHEMA, documento)

    if (len(err) > 0):
        raise error.MultipleArgumentException(err)


def validarAnio(anio):
    if anio > 0 and len(str(anio)) == 4:
        return True
    else:
        raise error.InvalidArgument('anio', 'Formato de año invalido')


def newFeriado():
    return {
        "feriadoList": [],
        "anio": '',
        "created": datetime.datetime.utcnow()
    }
