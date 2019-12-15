import numbers
import app.utils.errors as error
import datetime
import app.utils.validator as validator

SALA_LIST_SCHEMA = {
    "id_sala": {
        "required": True,
        "type": numbers.Integral,
    },
    "calendarizable": {
        "required": True,
        "type": bool,
    }
}

SALA_SCHEMA = {
    "id_sala": {
        "required": True,
        "type": numbers.Integral,
    }
}

JUEZ_SCHEMA = {
    "id_juez": {
        "required": True,
        "type": numbers.Integral,
    }
}

DEFENSOR_SCHEMA = {
    "id_defensor": {
        "required": True,
        "type": numbers.Integral,
    }
}

FISCAL_SCHEMA = {
    "id_fiscal": {
        "required": True,
        "type": numbers.Integral,
    }
}
QUERELLANTE_SCHEMA = {
    "id_querellante": {
        "required": True,
        "type": numbers.Integral,
    }
}

ASESOR_SCHEMA = {
    "id_asesor": {
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
    'tipo': {
        "required": True,
        "type": str,
    },
    'fecha_solicutud': {
        "required": True,
        "type": str,
    },
    'duracion': {
        "required": True,
        "type": numbers.Integral,
    },
    'id_audiencia': {
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
        'fecha_solicutud': {
            "required": True,
            "type": str,
        },
        'fecha_realizacion': {
            "required": True,
            "type": str,
        },
        'hora_comienzo': {
            "required": True,
            "type": str,
        },
        'duracion': {
            "required": True,
            "type": numbers.Integral,
        },
        'id_sala': {
            "required": True,
            "type": numbers.Integral,
        },
        'id_audiencia': {
            "required": True,
            "type": str,
        }
}

SOLCITUD_SCHEMA = {
    "salas": {
        "required": True,
        "type": list,
        'minQuantity': 1,
        "childSchema": SALA_LIST_SCHEMA
    },
    "audiencias": {
        "required": True,
        "type": list,
        'minQuantity': 1,
        "childSchema": AUDIENCIA_SCHEMA
    },
    "audiencias_fijadas": {
        "required": True,
        "type": list,
        'minQuantity': 0,
        "childSchema": AUDIENCIA_FIJADA_SCHEMA
    },
    'notification_url': {
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
