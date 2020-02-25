import app.scores.crud_service as scores
import app.utils.errors as errors
import xmltodict
import os


ACTOR_LIST = ['juez', 'fiscal', 'asesor', 'querellante', 'defensor']


def toSolverFormat(data):
    '''
        Generar solver_data
            Lista de Audiencias, Lista de Rooms y ConstraintConfiguration
        Generar xml jueces
            JuezTimeGrainAfternoon, JuezTimeGrainLicense, JuezTimeGrainSpecial
    '''
    juez_data = {
        'afternoon': _juezAfternoonParser(data['turnoTardeJuez']),
        'license': _juezLicenseParser(data['licenciaJuez']),
        'special': _juezSpecialParser(data['indisposicionJuez'])
    }
    solver_data = _audienciaScheduleParser(data)

    return solver_data, juez_data


def _juezAfternoonParser(data):
    sub_schema = []
    for fecha in data:
        fecha['date'] = fecha.pop('fecha')
        temp = {'Juez': fecha.pop('juez')}
        for item in temp['Juez']:
            item['id'] = item.pop('idJuez')
        fecha['Jueces'] = temp
        sub_schema.append(fecha)
    xml_structure = {
        'Days': {
            'Day': sub_schema
        }
    }
    return xmltodict.unparse(xml_structure, pretty=True)


def _juezLicenseParser(data):
    sub_schema = []
    for juez in data:
        juez['id'] = juez.pop('idJuez')
        juez['dayfrom'] = juez.pop('fechaInicio')
        juez['dayto'] = juez.pop('fechaFin')
        sub_schema.append(juez)

    xml_structure = {
        'Jueces': {
            'Juez': sub_schema
        }
    }
    return xmltodict.unparse(xml_structure, pretty=True)


def _juezSpecialParser(data):

    sub_schema = []
    for juez in data:
        juez['id'] = juez.pop('idJuez')
        juez['day'] = juez.pop('dia')
        for item in juez['day']:
            item['date'] = item.pop('fecha')
            item['startingTime'] = item.pop('horaInicio')
            item['endingTime'] = item.pop('horaFin')
        sub_schema.append(juez)

    xml_structure = {
        'Jueces': {
            'Juez': sub_schema
        }
    }
    return xmltodict.unparse(xml_structure, pretty=True)


def _audienciaScheduleParser(data):
    data.pop('turnoTardeJuez')
    data.pop('licenciaJuez')
    data.pop('indisposicionJuez')
    room_dict = {}
    for room in data['sala']:
        room['almaFuerte'] = room.pop('almafuerte')
        room['usable'] = room.pop('calendarizable')
        room['idRoom'] = room.pop('idSala')
        room['boulogne'] = room.pop('boulonge_sur_mer')
        room_dict[room['idRoom']] = room

    audiencia_list = []
    for audiencia in data['audiencia']:
        temp = {}
        temp['id'] = audiencia.pop('id')
        temp['audiencia'] = audiencia
        temp['audiencia']['externa'] = False
        temp['pinned'] = False

        audiencia_list.append(temp)

    for audiencia in data['audienciaFijada']:
        temp = {}
        temp['hora_comienzo'] = audiencia.pop('horaComienzo')
        temp['id'] = audiencia.pop('id')
        temp['audiencia'] = audiencia
        temp['audiencia'][
            'fechaRealizacion'] = audiencia.pop('fechaRealizacion')

        temp['room'] = room_dict[audiencia.pop('idSala')]
        temp['pinned'] = True

        audiencia_list.append(temp)
    for audiencia in audiencia_list:
        audiencia['audiencia']['boulogne'] = audiencia['audiencia'].pop('boulonge_sur_mer')
        audiencia['audiencia']['durationMinutes'] = audiencia['audiencia'].pop('duracion')
        audiencia['audiencia']['fechaPedido'] = audiencia['audiencia'].pop('fechaSolicitud')
        audiencia['audiencia']['almaFuerte'] = audiencia['audiencia'].pop('almafuerte')
        audiencia['audiencia']['idAudiencia'] = audiencia['id']
        if audiencia['pinned']:
            audiencia['audiencia']['startingMinuteOfDay'] = __getStartingMinuteofDay(
                audiencia.pop('hora_comienzo'))
        else:
            audiencia['audiencia']['startingMinuteOfDay'] = 0
        for actor in ACTOR_LIST:
            if actor in audiencia['audiencia'].keys():
                temp_actor = []
                for id_actor in audiencia['audiencia'].pop(actor):
                    temp_actor.append(id_actor)
                audiencia['audiencia'][actor+'List'] = {
                    actor.capitalize(): temp_actor
                    }

    try:
        constraint_conf = scores.getLatestScores()
        if constraint_conf['activo']:
            temp = {}
            for constraint in constraint_conf['constraintConfiguration']:
                temp[constraint['nombreRestriccion']] = constraint[
                    'pesosRestriccion']
            constraint_conf = temp
    except Exception as err:
        constraint_conf = None

    xml_structure = {
        'AudienciaSchedule': {
            'audienciaAssignmentList': {
                    'AudienciaAssignment': audiencia_list
                },
            'roomList': {
                'Room': room_dict.values(),
            },
        }
    }
    if constraint_conf and 'activo' not in constraint_conf.keys():
        xml_structure['AudienciaSchedule'][
            'constraintConfiguration'] = constraint_conf

    return xmltodict.unparse(xml_structure, pretty=True)


def xmlSolutionToDict(xml_path):
    final_format = {
        'audiencia': [],
    }
    if not os.path.exists(xml_path):
        raise FileNotFoundError
    with open(xml_path) as fd:
        res = xmltodict.parse(fd.read())
    for key, audiencias in res['AudienciaSchedule']['audienciaAssignmentList'].items():
        if key != 'AudienciaAssignment':
            continue
        for audiencia in audiencias:
            if audiencia['pinned'] == 'false':
                aud = {
                    'fijada': audiencia['pinned'],
                    'idSala': audiencia['room']['idRoom'],
                    'id': audiencia['id'],
                    'fechaAudiencia':  audiencia['startingTimeGrain']['day']['date'],
                    'horaAudiencia':  audiencia['startingTimeGrain']['startingMinuteOfDay']
                }
                aud['horaAudiencia'] = __decimalToHs(int(aud['horaAudiencia'])/60)
                final_format['audiencia'].append(aud)

    return final_format


def __decimalToHs(hours):
    hours = round(hours, 2)
    int_dec = str(hours).split('.')
    int_dec[0] = int(int_dec[0])
    int_dec[1] = int(int(int_dec[1])/10*6)
    if int_dec[0] < 10:
        int_dec[0] = '0{}'.format(int_dec[0])
    if int_dec[1] < 10:
        int_dec[1] = '0{}'.format(int_dec[1])
    return '{}:{}'.format(int_dec[0], int_dec[1])


def __getStartingMinuteofDay(time):
    hours, minutes = time.split(':')
    return int(hours) * 60 + int(minutes)


if __name__ == "__main__":
    res = __decimalToHs(610/60)
    print(res)
