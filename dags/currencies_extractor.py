from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
import datetime
import requests
import json
import os
from airflow.utils.task_group import TaskGroup
from airflow.models import Variable


from datetime import datetime, timedelta

from include.models import Snapshot

# constants
MY_NAME = "IVAN"
MY_AGE = 43
CURRENCIES = {
    "usa": "USD",
    "canada": "CAD",
    "europe": "EUR",
    "britain": "GBP",
    "new_zeland": "NZD",
    "turkey": "TRY",
    "brazil": "BRL",
    "china": "CNY",
    "russia": "RUB"
}
URL_CURR = 'https://open.er-api.com/v6/latest/'
URL_BTC = 'https://blockchain.info/ticker'
RATIO_CURRENCY = 'RUB'


def extract_currencies(currencies):
    cont = []
    for i in currencies:
        response = requests.get(URL_CURR+currencies[i])
        res_btc = requests.get(URL_BTC)
        response_btc = json.loads(res_btc.text)
        res = json.loads(response.text)
        row = {
            currencies[i]: f"{res['rates'][RATIO_CURRENCY]} | {response_btc[currencies[i]]['sell']}"}
        cont.append(row)
    new_snapshot = Snapshot(
        usa=cont[0]['USD'],
        canada=cont[1]['CAD'],
        europe=cont[2]['EUR'],
        britain=cont[3]['GBP'],
        new_zeland=cont[4]['NZD'],
        turkey=cont[5]['TRY'],
        brazil=cont[6]['BRL'],
        china=cont[7]['CNY'],
        russia=cont[8]['RUB'],
    )
    return new_snapshot


def put_to_db(new_snapshot):
    print(new_snapshot)


with DAG(
    dag_id="simple_test_dag",
    start_date=datetime(2022, 7, 28),
    schedule_interval=timedelta(minutes=30),
    catchup=False,
    tags=["currency extractor"],
    default_args={
        "owner": MY_NAME,
        "retries": 2,
        "retry_delay": timedelta(minutes=5)
    }
) as dag:

    task1 = PythonOperator(
        task_id="extract currencies from API",
        python_callable=extract_currencies,
        op_kwargs={"currencies": CURRENCIES}      # Passes args to callable
    )
    task2 = PythonOperator(
        task_id="put data to db",
        python_callable=put_to_db,
        op_kwargs=new_snapshot     # Passes args to callable
    )


task1 >> task2
