#===========================================================================
#Program Name           :        Airflow_template.py
#Date                   :        01-Oct-2021
#Version                :        1.0
#Author                 :        Manish
#Description            :        Sample Creation
#Revision History
#===========================================================================
#Author              Date            Version Change Description
#===========================================================================
#Manish              01-Oct-2021     1.0     Gave Life    
#===========================================================================


from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.email_operator import EmailOperator

#email_list = Variable.get("EMAIL_LIST")
default_args = {
    'owner': 'Manish',
    #'email': email_list,
    'email_on_failure': False,
    'email_on_retry': False,

}
    
dag= DAG (
    'Manish',
    description='Testing',
    default_args = default_args,

)

t1 = BashOperator(
        task_id='print_date',
        bash_command='date',
 )
 #Email Notification need to config in helps.py
'''Email_Process= EmailOperator(
        task_id='Email Notification',
        to=email,
        subject='Airflow Alert',
        html_content=""" <h3>Email Test</h3> """,
        dag=dag

)'''

t1 
