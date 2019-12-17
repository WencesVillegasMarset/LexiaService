# import time
import xmltodict
import subprocess
import logging
import requests


def parse_to_xml(data):
    logging.basicConfig(filename='solver.log', filemode='a', level=logging.DEBUG)
    # some long running task here
    with open('solicitud.xml', 'w+') as result_file:
        result_file.write(xmltodict.unparse(data, pretty=True))
    with subprocess.Popen(["git", "status"], stdout=subprocess.PIPE) as proc:
        logging.info(proc.stdout.read())
    json = {
        "errors": "None"
    }
    requests.post(data['AudienciaSchedule']['urlNotificacion'], data=json)
    return data
