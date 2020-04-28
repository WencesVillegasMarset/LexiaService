import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    DATABASE_PORT = os.environ.get('DATABASE_PORT') or 27017
    DATABASE_URL = os.environ.get('DATABASE_URL') or 'localhost'
    SOLUTION_PATH = os.environ.get('SOLUTION_PATH') or '/home/wences/Documents/repos/LexiaService/ogap-solver/optaplanner_examples_jar/data/xml'
    DATA_PATH = os.environ.get('DATA_PATH') or '/home/wences/Documents/repos/LexiaService/ogap-solver/optaplanner_examples_jar/data'
    BASE_PATH = os.environ.get('BASE_PATH') or 'C:\\Users\\wence\\Documents\\Documents\\repos\\LexiaService'
    CLIENT_XLSX = os.environ.get('CLIENT_XLSX') or '/home/wences/Documents/repos/LexiaService/ogap-solver/optaplanner_examples_jar/data/excel/'

