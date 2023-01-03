from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

from datetime import datetime, timedelta


# constants
MY_NAME = "IVAN"
MY_AGE = 43


def multiply_by_23(number):
    """Multiplies a number by 23 and prints the results to Airflow logs."""
    result = number * 23
    print(result)


with DAG(
    dag_id="simple_test_dag",
    start_date=datetime(2022, 7, 28),
    schedule_interval=timedelta(minutes=30),
    catchup=False,
    tags=["lesson 1"],
    default_args={
        "owner": MY_NAME,
        "retries": 2,
        "retry_delay": timedelta(minutes=5)
    }
) as dag:
    task1 = BashOperator(
        task_id="say_my_name",
        bash_command=f"echo {MY_NAME}"
    )
    task2 = PythonOperator(
        task_id="multiply_my_number_by_23",
        python_callable=multiply_by_23,
        op_kwargs={"number": MY_AGE}      # Passes args to callable
    )


task1 >> task2
