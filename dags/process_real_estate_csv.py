from airflow import DAG
from airflow.operators.python_operator import PythonOperator 
from datetime import datetime, timedelta
import os

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}


dag = DAG(
    'process_real_estate_csv',
    default_args=default_args,
    description='Process real estate CSV files every minute',
    schedule_interval='* * * * *',  # Executes every minute
)

process_files_task = PythonOperator(
    task_id='process_files',
    python_callable=process_files,  
    dag=dag,
)

process_files_task

