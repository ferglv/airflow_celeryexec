from airflow import DAG
from datetime import datetime, timedelta

from airflow.operators.python import PythonOperator

from pipes.banxico_api.banxico_get_data import get_banxico_data

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2021, 1, 15),
    "email": ["airflow@example.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

dag = DAG(
    "banxico_api",
    schedule_interval="0 0 * * *",
    catchup=False,
    default_args=default_args,
)

get_data = PythonOperator(
    task_id="task_banxico_get_data",
    python_callable=get_banxico_data,
    queue="queue_1",
    dag=dag,
)

get_data
