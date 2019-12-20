# import time
import xmltodict
import subprocess
import logging
import requests
import app.calendarizacion.service as calendarizacion
import json
import app.utils.config as config

def run_solver(data, id):
    logging.basicConfig(filename='solver.log',
                            filemode='a', level=logging.DEBUG,
                            format='%(asctime)s %(levelname)-8s %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S')
    # some long running task here
    with open('solicitud.xml', 'w+') as result_file:
        result_file.write(xmltodict.unparse(data, pretty=True))
    with subprocess.Popen(["git", "status"], stdout=subprocess.PIPE) as proc:
        logging.info(proc.stdout.read())

    result_path = config.Config.SOLUTION_PATH
    solucion = calendarizacion.xmlSolutionToDict(result_path)
    with open('solucion.json', 'w+') as res:
        res.write(json.dumps(solucion))
    response = {
        "solicitudId": id
    }
    requests.post(data['AudienciaSchedule']['urlNotificacion'], data=response)
    return data
