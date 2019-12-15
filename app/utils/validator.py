
# import re


def validateSchema(schema, document):
    """
    Valida un documento contra un esquema dado
    schema: Documento con validaciones
        {
            "strProperty": {
                "required": True,
                "type": str,
                "minLen": 60
                "maxLen": 60
                },
            "numberProperty": {
                "required": False,
                "type": numbers.Integral | numbers.Real,
                "min": 0
                "max": 0
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
            # if schema_prop['type'] is str:
            # TODO : Definir validadores para fechas
            # y otras strings especificas

    return errors


def validateSchemaList(schema, document):

    errors = {}

    for item in document:
        sub_errors = validateSchema(schema, item)
        errors = {**errors, **sub_errors}

    return errors
