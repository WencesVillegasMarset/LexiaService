import re


def validateSchema(schema, document):
    """
    Valida un documento contra un esquema dado
    schema: Documento con validaciones
        {
            "strProperty": {
                "required": True,
                "type": str,
                },
            "numberProperty": {
                "required": False,
                "type": numbers.Integral | numbers.Real,
                },...
        }
    retorna: Lista de errores
    """

    errors = {}
    for (schema_key, schema_prop) in schema.items():
        # print((schema_key, schema_prop))
        # print(document)
        if schema_prop['required'] and schema_key not in document:
            errors[schema_key] = "Requerido"
        if schema_key in document:
            document_field = document[schema_key]
            if not isinstance(document_field, schema_prop['type']):
                errors[schema_key] = "Tipo invalido"
                continue
            if schema_prop['type'] is dict:
                sub_errors = validateSchema(
                    schema_prop['child'], document_field)
                errors = {**errors, **sub_errors}
                continue
            if schema_prop['type'] is list:
                if (not schema_prop['required']) and (document_field is None):
                    continue
                if schema_prop['minQuantity'] > len(document_field):
                    msg = "Cantidad de objetos minima: "
                    errors[schema_key] = msg + str(schema_prop['minQuantity'])
                    continue
                if len(document_field) > 0:
                    sub_errors = validateSchemaList(
                        schema_prop['childSchema'], document_field)
                    errors = {**errors, **sub_errors}
                    continue
            if schema_prop['type'] is str:
                sub_errors = validateStringField(schema_key, document_field)
                errors = {**errors, **sub_errors}

    return errors


def validateSchemaList(schema, document):

    errors = {}

    for item in document:
        sub_errors = validateSchema(schema, item)
        errors = {**errors, **sub_errors}

    return errors


def validateStringField(key_name, field_value):

    errors = {}

    KEY_PREFIXES = {
        'fecha': __valFecha,
        'hora': __valHora,
        'pesos': __valPesos
    }
    for prefix in KEY_PREFIXES.keys():
        if key_name.startswith(prefix):
            func = KEY_PREFIXES[prefix]
            if not func(field_value):
                errors[key_name] = "Invalid Format"
                break
            break
    return errors


def __valFecha(value):
    res = re.search(r"(19|20)\d\d[-.](0[1-9]|1[012])[-.](0[1-9]|[12][0-9]|3[01])", value)
    if res is None:
        return False
    return True


def __valHora(value):
    res = re.search(r"^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$", value)
    if res is None:
        return False
    return True


def __valPesos(value):
    res = re.search(r"^\d*[0-9]*/\d*[0-9]*/\d*[0-9]*/\d*[0-9]*/\d*[0-9]+$", value)
    if res is None:
        return False
    return True
