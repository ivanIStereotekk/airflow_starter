# from airflow import DAG
# from airflow.operators.python import PythonOperator
# from airflow.operators.bash import BashOperator

# from datetime import datetime, timedelta


# # constants
# MY_NAME = "IVAN"
# MY_AGE = 43


# def multiply_by_23(number):
#     """Multiplies a number by 23 and prints the results to Airflow logs."""
#     result = number * 23
#     print(result)


# with DAG(
#     dag_id="simple_test_dag",
#     start_date=datetime(2022, 7, 28),
#     schedule_interval=timedelta(minutes=30),
#     catchup=False,
#     tags=["lesson 1"],
#     default_args={
#         "owner": MY_NAME,
#         "retries": 2,
#         "retry_delay": timedelta(minutes=5)
#     }
# ) as dag:
#     task1 = BashOperator(
#         task_id="say_my_name",
#         bash_command=f"echo {MY_NAME}"
#     )
#     task2 = PythonOperator(
#         task_id="multiply_my_number_by_23",
#         python_callable=multiply_by_23,
#         op_kwargs={"number": MY_AGE}      # Passes args to callable
#     )


# task1 >> task2


############################# NO WORKING DAG #######################


# from airflow import DAG
# from airflow.operators.python import PythonOperator
# from airflow.operators.bash import BashOperator
# import datetime

# import os
# from airflow.utils.task_group import TaskGroup
# from airflow.models import Variable
# from datetime import datetime, timedelta


# # constants
# MY_NAME = "IVAN"
# MY_AGE = 43
# CURRENCIES = {
#     "usa": "USD",
#     "canada": "CAD",
#     "europe": "EUR",
#     "britain": "GBP",
#     "new_zeland": "NZD",
#     "turkey": "TRY",
#     "brazil": "BRL",
#     "china": "CNY",
#     "russia": "RUB"
# }
# URL_CURR = 'https://open.er-api.com/v6/latest/'
# URL_BTC = 'https://blockchain.info/ticker'
# RATIO_CURRENCY = 'RUB'
# NEW_SNAP = None


# def extract_currencies(currencies):
#     from include.models import Snapshot_Json
#     import requests
#     import json
#     cont = []
#     for i in currencies:
#         response = requests.get(URL_CURR+currencies[i])
#         res_btc = requests.get(URL_BTC)
#         response_btc = json.loads(res_btc.text)
#         res = json.loads(response.text)
#         row = {
#             currencies[i]: f"{res['rates'][RATIO_CURRENCY]} | {response_btc[currencies[i]]['sell']}"}
#         cont.append(row)
#     NEW_SNAP = Snapshot_Json(
#         usa=cont[0]['USD'],
#         canada=cont[1]['CAD'],
#         europe=cont[2]['EUR'],
#         britain=cont[3]['GBP'],
#         new_zeland=cont[4]['NZD'],
#         turkey=cont[5]['TRY'],
#         brazil=cont[6]['BRL'],
#         china=cont[7]['CNY'],
#         russia=cont[8]['RUB'],
#     )
#     print("this is snap:", type(NEW_SNAP))
#     return f'snap = {type(NEW_SNAP)}'


# def put_to_db(NEW_SNAP):
#     print(NEW_SNAP)


# with DAG(
#     dag_id="extract_currencies_1",
#     start_date=datetime(2023, 1, 4),
#     schedule_interval=None,  # timedelta(minutes=1),
#     catchup=False,
#     tags=["currency extractor"],
#     default_args={
#         "owner": MY_NAME,
#         "retries": 2,
#         "retry_delay": timedelta(minutes=1)
#     }
# ) as dag:

#     task1 = PythonOperator(
#         task_id="extract_api",
#         python_callable=extract_currencies,
#         op_kwargs={"currencies": CURRENCIES}      # Passes args to callable
#     )
#     task2 = PythonOperator(
#         task_id="put_data_to_db",
#         python_callable=put_to_db,
#         op_kwargs={"snapshot": NEW_SNAP}     # Passes args to callable
#     )
#     task3 = BashOperator(
#         task_id="result_print",
#         bash_command=f"echo {NEW_SNAP}"
#     )


# task1 >> task2 >> task3
