"""
@author: patrick_alan
@created_date: 14/08/2022
"""

from urllib3 import PoolManager
import json
from Config.Postgre import PostgreConfig
from Connections.Postgre import PostgreConnection
from datetime import datetime

###########################
# Instanciando configurações
https = PoolManager()
post_conn = PostgreConnection(PostgreConfig('db_etl'))
###########################


def request_transactions():
    return json.loads(https.request('GET', url='http://127.0.0.1:8000/transactions/').data.decode('utf-8'))


def insert_postgre():
    data_request = request_transactions()
    post_conn.insert_into(
        table='staging.stg_transactions',
        data=[
            [
                data_request['id'],
                data_request['mcc'],
                data_request['value'],
                data_request['date'],
                data_request['city'],
                data_request['country']
            ]
        ],
        flg_trunc_before=False
    )


def get_transactions():
    for _ in range(1000):
        print('     ' + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + f" - Inserindo dados - {_}")
        try:
            insert_postgre()
        except:
            continue


def call_procs():
    print('     ' + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " - Chamandos procedures")
    post_conn.call_proc(
        'proc_insert_tb_transactions'
    )


if __name__ == '__main__':
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " - Iniciando script")
    get_transactions()
    call_procs()
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " - Finalizando script")
