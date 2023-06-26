import json

faculties =     ('fbme', 'ipp', 'fl', 'fel', 'its', 'ipt', 'imi', 'fbt', 'fsl', 'fam', 'tef', 'imz')
faculties_ukr = ('ФБМІ', 'ВПІ', 'ФЛ', 'ФЕЛ', 'ІТС', 'ФТІ', 'ММІ', 'ФБТ', 'ФСП', 'ФПМ', 'ІАТЕ', 'ІМЗ')

global BOT_TOKEN
global DATABASE_URL
global ANTIFLOOD_RATE

def _get_data():
    with open('settings.json', 'r') as file:
        global DATABASE_URL

        py_data = json.load(file)
        DATABASE_URL = py_data['DATABASE_URL']


        print(DATABASE_URL)


try:
    _get_data()
except FileNotFoundError:
    import os
    os.chdir('../..')
    _get_data()
except Exception as e:
    print(e)
