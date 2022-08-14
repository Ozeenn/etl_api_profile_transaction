from fastapi import FastAPI
import ccard
from faker import Faker
from datetime import datetime
from Config.Postgre import PostgreConfig
from Connections.Postgre import PostgreConnection
import random
from time import time

app = FastAPI()
post_conn = PostgreConnection(PostgreConfig('db_etl'))


@app.get("/profile/")
async def profile():
    card = get_random_card()
    return {
        "profile": get_random_profile(),
        "card-number": card[0],
        "card-type": card[1],
        "account": get_random_account(),
        "dat_processamento": datetime.now()
    }


def get_random_profile():
    return Faker().profile()


def get_random_card():
    return random.choice([(ccard.visa(), 'Visa'), (ccard.mastercard(), 'Mastercard')])


def get_random_account():
    account = ''
    for _ in range(6):
        account = account + str(random.randint(0, 9))
    return account


def get_random_mcc():
    mcc = ''
    for _ in range(4):
        mcc = mcc + str(random.randint(0, 9))
    return mcc


def get_random_date():
    return datetime.fromtimestamp(random.randint(1, int(time())))


async def get_random_id():
    return post_conn.return_query_list(
        'select md5(num_card || num_account) from staging.stg_profile_infos order by random() LIMIT 1')[0][0]


@app.get("/transactions/")
async def transactions():
    return {
        "id": await get_random_id(),
        "mcc": get_random_mcc(),
        "value": random.randint(0, 10000),
        "date": get_random_date(),
        "city": Faker().city(),
        "country": Faker().country()
    }
