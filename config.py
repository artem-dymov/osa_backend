import json

faculties =     ('fbme', 'tef')
faculties_ukr = ('ФБМІ', 'ІАТЕ')

global DATABASE_URL
global HOST

def _get_data():
    with open('settings.json', 'r') as file:
        global DATABASE_URL
        global HOST

        py_data = json.load(file)
        DATABASE_URL = py_data['DATABASE_URL']
        HOST = py_data['HOST']


try:
    _get_data()
except FileNotFoundError:
    import os
    os.chdir('../..')
    _get_data()
except Exception as e:
    print(e)
