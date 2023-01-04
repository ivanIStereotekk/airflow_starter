from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
import datetime

import os
from airflow.utils.task_group import TaskGroup
from airflow.models import Variable
from datetime import datetime, timedelta


# constants
MY_NAME = "IVAN"
MY_AGE = 43
CURR = 'RUB'

URL_BTC = 'https://blockchain.info/ticker'


def extract_currencies(curr, ti):
    import requests
    import json
    URL_BTC = 'https://blockchain.info/ticker'

    res_btc = requests.get(URL_BTC)
    response_btc = json.loads(res_btc.text)
    NEW_SNAP = response_btc['RUB']['buy']
    ti.xcom_push(key=curr, value=NEW_SNAP)  # PUSHED Xcom


def put_to_db(curr, ti):
    pulled_data = ti.xcom_pull(key=curr, task_ids='put_data_to_db')
    ti.xcom_push(key="Latest_XCOM_PUSH", value=pulled_data)
    for_bash = f"Extracted BTC value is:{pulled_data}"
    print(f"Extracted BTC value is:{pulled_data}")


def explore_data(curr, ti):
    data = ti.xcom_pull(key="Latest_XCOM_PUSH", task_ids='explore_data')
    print(f"I've done all tasks: {data}")


with DAG(
    dag_id="extract_currencies_1",
    start_date=datetime(2023, 1, 4),
    schedule_interval=None,  # timedelta(minutes=1),
    catchup=False,
    tags=["currency extractor"],
    default_args={
        "owner": MY_NAME,
        "retries": 1,
        "retry_delay": timedelta(minutes=1)
    }
) as dag:

    task1 = PythonOperator(
        task_id="extract_api",
        python_callable=extract_currencies,
        op_kwargs={'curr': CURR}

    )
    task2 = PythonOperator(
        task_id="put_data_to_db",
        python_callable=put_to_db,
        op_kwargs={'curr': CURR}

    )
    task3 = PythonOperator(
        task_id="explore_data",
        python_callable=explore_data,
        op_kwargs={'curr': CURR}

    )


task1 >> [task2, task3]
