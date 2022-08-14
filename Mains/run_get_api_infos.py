from urllib3 import PoolManager
import json
from Config.Postgre import PostgreConfig
from Connections.Postgre import PostgreConnection
from datetime import datetime

https = PoolManager()
post_conn = PostgreConnection(PostgreConfig('db_etl'))


def request_profile_infos():
    return json.loads(https.request('GET', url='http://127.0.0.1:8000/profile/').data.decode('utf-8'))


def insert_postgre():
    data_request = request_profile_infos()
    post_conn.insert_into(
        table='staging.stg_profile_infos',
        data=[
            [
                data_request['profile']['job'],
                data_request['profile']['company'],
                data_request['profile']['ssn'],
                data_request['profile']['residence'],
                data_request['profile']['current_location'][0],
                data_request['profile']['current_location'][1],
                data_request['profile']['blood_group'],
                data_request['profile']['username'],
                data_request['profile']['name'],
                data_request['profile']['sex'],
                data_request['profile']['address'],
                data_request['profile']['mail'],
                data_request['profile']['birthdate'],
                data_request['card-number'],
                data_request['card-type'],
                data_request['account'],
                data_request['dat_processamento']

            ]
        ],
        flg_trunc_before=False
    )


def get_profile_infos():
    for _ in range(50):
        print('     ' + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + f" - Inserindo dados - {_}")
        try:
            insert_postgre()
        except:
            continue


def call_procs():
    print('     ' + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " - Chamandos procedures")
    post_conn.call_proc(
        'proc_insert_tb_profile_infos'
    )


if __name__ == '__main__':
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " - Iniciando script")
    get_profile_infos()
    call_procs()
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " - Finalizando script")
