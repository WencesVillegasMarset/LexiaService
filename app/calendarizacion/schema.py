import numbers
import app.utils.errors as error
import datetime
import app.utils.validator as validator

SALA_LIST_SCHEMA = {
    "idSala": {
        "required": True,
        "type": numbers.Integral,
    },
    "calendarizable": {
        "required": True,
        "type": bool,
    }
}

SALA_SCHEMA = {
    "idSala": {
        "required": True,
        "type": numbers.Integral,
    }
}

JUEZ_SCHEMA = {
    "idJuez": {
        "required": True,
        "type": numbers.Integral,
    }
}

DEFENSOR_SCHEMA = {
    "idDefensor": {
        "required": True,
        "type": numbers.Integral,
    }
}

FISCAL_SCHEMA = {
    "idFiscal": {
        "required": True,
        "type": numbers.Integral,
    }
}
QUERELLANTE_SCHEMA = {
    "idQuerellante": {
        "required": True,
        "type": numbers.Integral,
    }
}

ASESOR_SCHEMA = {
    "idAsesor": {
        "required": True,
        "type": numbers.Integral,
    }
}

AUDIENCIA_SCHEMA = {
    "juez": {
        "required": True,
        "type": list,
        'minQuantity': 1,
        "childSchema": JUEZ_SCHEMA
    },
    "defensor": {
        "required": True,
        "type": list,
        'minQuantity': 1,
        "childSchema": DEFENSOR_SCHEMA
    },
    "fiscal": {
        "required": True,
        "type": list,
        'minQuantity': 1,
        "childSchema": FISCAL_SCHEMA
    },
    "querellante": {
        "required": False,
        "type": list,
        'minQuantity': 0,
        "childSchema": QUERELLANTE_SCHEMA
    },
    "asesor": {
        "required": False,
        "type": list,
        'minQuantity': 0,
        "childSchema": DEFENSOR_SCHEMA
    },
    'riesgosa': {
        "required": True,
        "type": bool,
    },
    'detenido': {
        "required": True,
        "type": bool,
    },
    'tipo': {
        "required": True,
        "type": str,
    },
    'fechaSolicutud': {
        "required": True,
        "type": str,
    },
    'duracion': {
        "required": True,
        "type": numbers.Integral,
    },
    'id': {
        "required": True,
        "type": str,
    }
}

AUDIENCIA_FIJADA_SCHEMA = {
        "juez": {
            "required": True,
            "type": list,
            'minQuantity': 1,
            "childSchema": JUEZ_SCHEMA
        },
        "defensor": {
            "required": True,
            "type": list,
            'minQuantity': 1,
            "childSchema": DEFENSOR_SCHEMA
        },
        "fiscal": {
            "required": True,
            "type": list,
            'minQuantity': 1,
            "childSchema": FISCAL_SCHEMA
        },
        "querellante": {
            "required": False,
            "type": list,
            'minQuantity': 1,
            "childSchema": QUERELLANTE_SCHEMA
        },
        "asesor": {
            "required": False,
            "type": list,
            'minQuantity': 1,
            "childSchema": DEFENSOR_SCHEMA
        },
        'tipo': {
            "required": True,
            "type": str,
        },
        'riesgosa': {
            "required": True,
            "type": bool,
        },
        'detenido': {
            "required": True,
            "type": bool,
        },
        'fechaSolicutud': {
            "required": True,
            "type": str,
        },
        'fechaRealizacion': {
            "required": True,
            "type": str,
        },
        'horaComienzo': {
            "required": True,
            "type": str,
        },
        'duracion': {
            "required": True,
            "type": numbers.Integral,
        },
        'idSala': {
            "required": True,
            "type": numbers.Integral,
        },
        'id': {
            "required": True,
            "type": str,
        }
}

SOLCITUD_SCHEMA = {
    "sala": {
        "required": True,
        "type": list,
        'minQuantity': 1,
        "childSchema": SALA_LIST_SCHEMA
    },
    "audiencia": {
        "required": True,
        "type": list,
        'minQuantity': 1,
        "childSchema": AUDIENCIA_SCHEMA
    },
    "audienciaFijada": {
        "required": True,
        "type": list,
        'minQuantity': 0,
        "childSchema": AUDIENCIA_FIJADA_SCHEMA
    },
    'notificationUrl': {
        "required": True,
        "type": str,
    }
}


def validarSolicitud(documento):
    err = validator.validateSchema(SOLCITUD_SCHEMA, documento)

    if (len(err) > 0):
        raise error.MultipleArgumentException(err)


def newSolicitud():
    return {
        "jueces": [],
        "defensores": [],
        "fiscales": [],
        "querellantes": [],
        "asesores": [],
        "salas": [],
        "audiencias": [],
        'created': datetime.datetime.utcnow(),
        'notification_url': '',
    }
