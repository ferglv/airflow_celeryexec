from airflow import DAG
from datetime import datetime, timedelta

from airflow.operators.bash import BashOperator

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
    "batch_sample",
    schedule_interval="0 0 * * *",
    catchup=False,
    default_args=default_args,
)

create_command = "echo $(hostname)"

t1 = BashOperator(
    task_id="task_for_q1", bash_command=create_command, queue="queue_1", dag=dag
)

t2 = BashOperator(
    task_id="task_for_q2", bash_command=create_command, queue="queue_2", dag=dag
)

t1 >> t2
