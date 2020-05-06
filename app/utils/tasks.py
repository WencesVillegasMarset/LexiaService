# import time
import subprocess
import logging
import requests
import app.calendarizacion.service as calendarizacion
import json
import app.utils.config as config
import datetime
import app.calendarizacion.crud_service as crud
import os


SOLUTION_PATH = config.Config.SOLUTION_PATH
DATA_PATH = config.Config.DATA_PATH

def run_solver(data, solicitudId):
    logging.basicConfig(filename='solver.log',
                        filemode='a', level=logging.DEBUG,
                        format='%(asctime)s %(levelname)-8s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    today = datetime.datetime.today()
    if len(data) == 5:
        solicitud_filename = '{}-{}-{}.xml'.format(
            today.year, today.month, today.day)
    else:
        solicitud_filename = '{}.xml'.format(data[5])

    with open(os.path.join(DATA_PATH, 'unsolved', solicitud_filename), 'w+') as result_file:
        result_file.write(data[0])

    with open(os.path.join(DATA_PATH, 'JuezTimeGrainAfternoon.xml'), 'w+') as result_file:
        result_file.write(data[1])

    with open(os.path.join(DATA_PATH, 'JuezTimeGrainLicence.xml'), 'w+') as result_file:
        result_file.write(data[2])

    with open(os.path.join(DATA_PATH, 'JuezTimeGrainSpecial.xml'), 'w+') as result_file:
        result_file.write(data[3])

    with subprocess.Popen(
            ["java", "-jar", "optaplanner-examples.jar", 'short'],
            stdout=subprocess.PIPE,
            cwd='./ogap-solver/optaplanner_examples_jar') as proc:
        logging.info(proc.stdout.read())
    try:
        logging.debug(os.path.exists(os.path.join(SOLUTION_PATH, 'Result.xml')))
        solucion = calendarizacion.xmlSolutionToDict(
            os.path.join(SOLUTION_PATH, 'Result.xml'))
        solucion_id = crud.crearSolucion(solucion, solicitudId)
        logging.debug(solucion_id)
        response = {
            "solicitudId": solicitudId,
            'success': True,
        }
        try:
            requests.post(data[4], data=response)
        except Exception:
            logging.error("Error sending POST notification")
    except FileNotFoundError:
        response = {
            "solicitudId": solicitudId,
            'success': False,
        }
        try:
            requests.post(data[4], data=response)
        except Exception:
            logging.error("Error sending POST notification")
        return
    # eliminar xml de resultados
    try:
        os.remove(os.path.join(DATA_PATH, 'unsolved', solicitud_filename))
    except FileNotFoundError:
        pass
    os.rename(
            os.path.join(os.path.split(SOLUTION_PATH)[0],
                         'excel', 'Result.xlsx'),
            os.path.join(os.path.split(SOLUTION_PATH)[0],
                         'excel', str(solicitudId) + '.xlsx'))
    return data
