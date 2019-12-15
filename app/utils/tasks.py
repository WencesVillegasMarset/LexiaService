# import time
import xmltodict


def parse_to_xml(data):
    # some long running task here
    with open('result.xml', 'w+') as result_file:
        result_file.write(xmltodict.unparse(data, pretty=True))
    return data
