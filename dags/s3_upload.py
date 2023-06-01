# import requests
# import csv
# import json
from datetime import datetime
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from airflow.providers.amazon.aws.operators.s3 import S3ListOperator
from airflow import DAG

with DAG("upload_file_s3", start_date=datetime(2021,1,1), schedule_interval="@daily", catchup=False) as dag:
    
    listFiles = S3ListOperator(
        task_id='list_objects',
        bucket='pipeline-companies-database-staging',
        aws_conn_id='CONNECT_AWS_STAGING'
    )

