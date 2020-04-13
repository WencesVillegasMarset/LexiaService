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
    },
    'almafuerte': {
        "required": True,
        "type": bool,
    },
    'boulonge_sur_mer': {
        "required": True,
        "type": bool,
    }
}

TIPO_SCHEMA = {
    "idTipo": {
        "required": True,
        "type": numbers.Integral,
    },
    "tiempoRealizacionMinimo": {
        "required": True,
        "type": numbers.Integral,
    },
    "tiempoRealizacionMaximo": {
        "required": True,
        "type": numbers.Integral,
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
    'aLaTarde': {
        "required": True,
        "type": bool,
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
        "type": dict,
        "childSchema": TIPO_SCHEMA
    },
    'almafuerte': {
        "required": True,
        "type": bool,
    },
    'boulonge_sur_mer': {
        "required": True,
        "type": bool,
    },
    'fechaSolicitud': {
        "required": True,
        "type": str,
    },
    'duracion': {
        "required": True,
        "type": numbers.Integral,
    },
    'id': {
        "required": True,
        "type": numbers.Integral,
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
        "type": dict,
        "childSchema": TIPO_SCHEMA
    },
    'aLaTarde': {
        "required": True,
        "type": bool,
    },
    'almafuerte': {
        "required": True,
        "type": bool,
    },
    'boulonge_sur_mer': {
        "required": True,
        "type": bool,
    },
    'riesgosa': {
        "required": True,
        "type": bool,
    },
    'detenido': {
        "required": True,
        "type": bool,
    },
    'externa': {
        "required": True,
        "type": bool,
    },
    'fechaSolicitud': {
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
        "type": numbers.Integral,
    }
}


WORKDAY_SPECIAL_SCHEMA = {
    'fecha': {
        "required": True,
        "type": str,
    },
    'horaInicio': {
        "required": True,
        "type": str,
    },
    'horaFin': {
        "required": True,
        "type": str,
    }
}

JUEZ_TIME_LICENSE_SCHEMA = {
    'fechaInicio': {
        "required": True,
        "type": str,
    },
    'fechaFin': {
        "required": True,
        "type": str,
    },
    'idJuez': {
        "required": True,
        "type": int,
    }
}

JUEZ_TIME_AFTERNOON_SCHEMA = {
    'fecha': {
        "required": True,
        "type": str,
    },
    'juez': {
        "required": True,
        "type": list,
        'minQuantity': 1,
        "childSchema": JUEZ_SCHEMA
    }
}

JUEZ_TIME_SPECIAL_SCHEMA = {
    'idJuez': {
        "required": True,
        "type": int,
    },
    'dia': {
        "required": True,
        "type": list,
        'minQuantity': 1,
        "childSchema": WORKDAY_SPECIAL_SCHEMA
    }
}


SOLCITUD_SCHEMA = {
    "sala": {
        "required": True,
        "type": list,
        'minQuantity': 1,
        "childSchema": SALA_LIST_SCHEMA
    },
    'turnoTardeJuez': {
        "required": True,
        "type": list,
        'minQuantity': 1,
        "childSchema": JUEZ_TIME_AFTERNOON_SCHEMA
    },
    'licenciaJuez': {
        "required": True,
        "type": list,
        'minQuantity': 1,
        "childSchema": JUEZ_TIME_LICENSE_SCHEMA
    },
    'indisposicionJuez': {
        "required": True,
        "type": list,
        'minQuantity': 0,
        "childSchema": JUEZ_TIME_SPECIAL_SCHEMA
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
    'urlNotificacion': {
        "required": True,
        "type": str,
    }
}

SOLCITUD_SANDBOX_SCHEMA = {
    "sala": {
        "required": True,
        "type": list,
        'minQuantity': 1,
        "childSchema": SALA_LIST_SCHEMA
    },
    'turnoTardeJuez': {
        "required": True,
        "type": list,
        'minQuantity': 1,
        "childSchema": JUEZ_TIME_AFTERNOON_SCHEMA
    },
    'licenciaJuez': {
        "required": True,
        "type": list,
        'minQuantity': 1,
        "childSchema": JUEZ_TIME_LICENSE_SCHEMA
    },
    'indisposicionJuez': {
        "required": True,
        "type": list,
        'minQuantity': 0,
        "childSchema": JUEZ_TIME_SPECIAL_SCHEMA
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
    'urlNotificacion': {
        "required": True,
        "type": str,
    },
    'fechaSolicitud': {
        "required": True,
        "type": str,
    }
}


def validarSolicitud(documento):
    err = validator.validateSchema(SOLCITUD_SCHEMA, documento)

    if (len(err) > 0):
        raise error.MultipleArgumentException(err)


def validarSolicitudSandbox(documento):
    err = validator.validateSchema(SOLCITUD_SANDBOX_SCHEMA, documento)

    if (len(err) > 0):
        raise error.MultipleArgumentException(err)


def newSolicitud():
    return {
        "sala": [],
        "audiencia": [],
        "audienciaFijada": [],
        'created': datetime.datetime.utcnow(),
        'urlNotificacion': '',
    }
