from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import pandas as pd


def first_function_execute():
  print("hello world")
  return "hello world"

with DAG(
   dag_id="my_first_dag",
    schedule_interval="0 10 * * *",
    start_date=pendulum.datetime(2023, 1, 1, tz="US/Pacific"),
    catchup=False,
) as dag:
  
