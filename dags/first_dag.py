from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import pandas as pd


def first_function_execute():
  print("hello world")
  return "hello world"

with DAG(
    dag_id="first_dag",
    schedule_interval="@daily",
    default_args={
      "owner":"airflow",
      "retries":1,
      "retry_delay":timedelta(minutes=5),
      "start_date":datetime(2023,1,28)
    },
    catchup=False,
) as f:
.
first_function_execute=PythonOperator(
  task_id="first_function_execute",
  python_callable=first_function_execute,
)
  
