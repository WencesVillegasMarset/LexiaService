XML_TAG_MAPPINGS = {
    'sala': 'room',
    'salaList': 'roomList',
    'idSala': "idRoom"
}

ACTOR_LIST = ['juez', 'fiscal', 'asesor', 'querellante', 'defensor']


def toSolverFormat(data):
    data = _extractLists(data)
    final_structure = toXMLStructure(data)
    return toXMLKeys(final_structure)


def toXMLStructure(data):
    for actor in ACTOR_LIST:
        for audiencia in data['audiencia']:
            if actor not in audiencia.keys():
                continue
            audiencia[actor+'List'] = {
                actor: audiencia[actor]
            }
            del audiencia[actor]
        for audiencia in data['audienciaFijada']:
            if actor not in audiencia.keys():
                continue
            audiencia[actor+'List'] = {
                actor: audiencia[actor]
            }
            del audiencia[actor]

    temp = {
        'sala': data['sala']
    }
    data['salaList'] = temp
    del data['sala']
    temp = {
        'audiencia': data['audiencia']
    }
    data['audienciaList'] = temp
    del data['audiencia']
    temp = {
        'audienciaFijada': data['audienciaFijada']
    }
    data['audienciaFijadaList'] = temp
    del data['audienciaFijada']

    return data


def toXMLKeys(dictionary):
    new_dict = {}
    for key in dictionary.keys():
        new_key = XML_TAG_MAPPINGS.get(key, key)
        if isinstance(dictionary[key], dict):
            new_dict[new_key] = toXMLKeys(dictionary[key])
        else:
            new_dict[new_key] = dictionary[key]
    return new_dict


def _extractLists(data):
    for actor in ACTOR_LIST:
        temp = set()
        for audiencia in data['audiencia']:
            if actor not in audiencia.keys():
                continue
            for act in audiencia[actor]:
                temp.add(act['id' + actor.capitalize()])

        for audiencia in data['audienciaFijada']:
            if actor not in audiencia.keys():
                continue
            for act in audiencia[actor]:
                temp.add(act['id' + actor.capitalize()])
        temp = list(temp)
        for idx in range(len(temp)):
            temp[idx] = {
                    'id'+actor.capitalize(): temp[idx]
                }
        data[actor + 'List'] = {
            actor: temp
        }
    return data
