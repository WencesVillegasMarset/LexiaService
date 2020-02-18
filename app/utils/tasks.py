# import time
import xmltodict
import subprocess
import logging
import requests
import app.calendarizacion.service as calendarizacion
import json
import app.utils.config as config
import datetime
import app.calendarizacion.crud_service as crud


SOLUTION_PATH = config.Config.SOLUTION_PATH


def run_solver(data, solicitudId):
    logging.basicConfig(filename='solver.log',
                        filemode='a', level=logging.DEBUG,
                        format='%(asctime)s %(levelname)-8s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    today = datetime.datetime.today()
    solicitud_filename = '{}-{}-{}.xml'.format(
        today.year, today.month, today.day)

    with open(solicitud_filename, 'w+') as result_file:
        result_file.write(data[0])
    with open('juezTimeGrainAfternoon.xml', 'w+') as result_file:
        result_file.write(data[1])
    with open('juezTimeGrainLicense.xml', 'w+') as result_file:
        result_file.write(data[2])
    with open('juezTimeGrainSpecial.xml', 'w+') as result_file:
        result_file.write(data[3])

    with subprocess.Popen(
            ["java", "-jar", "optaplanner-examples.jar", 'short'],
            stdout=subprocess.PIPE,
            cwd='./ogap-solver/optaplanner_examples_jar') as proc:
        logging.info(proc.stdout.read())

    solucion = calendarizacion.xmlSolutionToDict(SOLUTION_PATH)
    with open('solucion.json', 'w+') as res:
        res.write(json.dumps(solucion))
    crud.crearSolucion(solucion, solicitudId)
    response = {
        "solicitudId": id
    }
    requests.post(data[4], data=response)
    return data
