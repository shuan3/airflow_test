from airflow import DAG

from airflow.operators.python_operator import PythonOperator
from pandas import DataFrame
from airflow.utils.dates import days_ago

from datetime import datetime

import requests
import pandas as pd


def ingest_data()->DataFrame:

    d = {'col1': [1, 2], 'col2': [3, 4]}
    df = pd.DataFrame(data=d)
    return df



def transform_df(df)->DataFrame:
    import pandas as pd

    from datetime import datetime
    print('Today is {}'.format(datetime.today().date()))
    print(df)
    # df=pd.DataFrame(df)
    # df['updated_date']= datetime.today().strftime('%Y-%m-%d')
    df['updated_date']= 'lol'
    return df



def final_step():

    response = requests.get('https://api.quotable.io/random')

    quote = response.json()['content']

    print('Quote of the day: "{}"'.format(quote))



dag = DAG(

    'fetch_data',

    default_args={'start_date': days_ago(1)},

    schedule_interval='0 23 * * *',

    catchup=False

)



ingest_data = PythonOperator(

    task_id='ingest_data',

    python_callable=ingest_data,

    dag=dag

)



transform_df = PythonOperator(

    task_id='transform_df',

    python_callable=transform_df,

    dag=dag,
    op_kwargs={"df": "{{ ti.xcom_pull(task_ids='ingest_data') }}"}
    # op_kwargs={"df_dict": "{{ ti.xcom_pull(task_ids='read_file') }}"}
)



final_step = PythonOperator(

    task_id='final_step',

    python_callable=final_step,

    dag=dag

)


ingest_data>>transform_df>>final_step