from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.models import Variable

import os
from airflow.utils.task_group import TaskGroup
from airflow.models import Variable
from datetime import datetime, timedelta


now_stamp = datetime.now()

# constants in Variables
MY_NAME = Variable.get("my_name")
MY_AGE = Variable.get("my_age")
CURR = Variable.get("currency")
URL_BTC = Variable.get("url_bitcoin")
SELL_OR_BUY = Variable.get("sell_buy")
PHONE = Variable.get("phone")


def extract_currencies(curr, ti):
    import requests
    import json
    res_btc = requests.get(URL_BTC)
    response_btc = json.loads(res_btc.text)
    NEW_SNAP = response_btc[CURR][SELL_OR_BUY]
    # PUSHED Xcom
    ti.xcom_push(
        key=curr, value=f"{NEW_SNAP} - {now_stamp} -- {extract_currencies.__name__} -- {MY_NAME} -- {PHONE}")


def put_to_db(curr, ti):
    pulled_data = ti.xcom_pull(key=curr)
    ti.xcom_push(key="Latest_XCOM_PUSH", value=pulled_data)
    for_bash = f"Extracted BTC value is:{pulled_data}"
    print(f"Extracted BTC value is:{pulled_data}")


def explore_data(curr, ti):
    pulled_data = ti.xcom_pull(key=f"Latest_XCOM_PUSH")
    print(f"I've done all tasks: {pulled_data}")
    ti.xcom_push(
        key=curr, value=f"{pulled_data} - {now_stamp} - {explore_data.__name__}")


with DAG(
    dag_id="extract_currencies",
    start_date=datetime(2023, 1, 4),
    schedule_interval=None,  # timedelta(minutes=1),
    catchup=False,
    tags=["currency extractor"],
    default_args={
        "owner": MY_NAME,
        "retries": 1,
        "retry_delay": timedelta(minutes=1)
    },
    doc_md="The DAG that makes something super useful for all humanity !"
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


task1 >> task2 >> task3
