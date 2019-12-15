
def toSolverFormat(data):
    final_structure = _extractLists(data)
    return toXMLKeys(final_structure)


def toXMLKeys(dictionary):
    return dictionary


def _extractLists(data):
    ACTOR_LIST = ['juez', 'fiscal', 'asesor', 'querellante', 'defensor']

    for actor in ACTOR_LIST:
        temp = set()
        for audiencia in data['audiencias']:
            if actor not in audiencia.keys():
                continue
            for act in audiencia[actor]:
                temp.add(act['id_' + actor])

        for audiencia in data['audiencias_fijadas']:
            if actor not in audiencia.keys():
                continue
            for act in audiencia[actor]:
                temp.add(act['id_' + actor])
        temp = list(temp)
        for idx in range(len(temp)):
            temp[idx] = {
                actor: {
                    'id_'+actor: temp[idx]
                }
            }

        data[actor + '_list'] = temp
    return data
