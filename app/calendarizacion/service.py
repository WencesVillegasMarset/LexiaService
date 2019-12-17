import app.scores.crud_service as scores
import app.utils.errors as errors


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
    room_list = []
    possible_rooms_list = [] 
    for sala in data['sala']:
        if sala["calendarizable"]:
            del sala["calendarizable"]
            possible_rooms_list.append(sala)
        else:
            del sala["calendarizable"]
        room_list.append(sala)

    data['salaList'] = {
        'room': room_list,
    }
    data['possibleRooms'] = {
        'room': possible_rooms_list,
    }
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
    try:
        res = scores.getLatestScores()
        data['constraintConfiguration'] = res['constraintConfiguration']
        temp = {}
        for constraint in data['constraintConfiguration']:
            temp[constraint['nombreRestriccion']] = constraint['pesosRestriccion']
        data['constraintConfiguration'] = temp
    except Exception as err:
        errors.handleUnknown(err)
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


def xmlSolutionToDict():
    pass
