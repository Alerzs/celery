from celery import shared_task
from time import sleep

@shared_task(task_rate_limit= '5/m')
def task1():
    return

@shared_task(task_rate_limit= '1/m')
def task2():
    return

@shared_task
def task3():
    return

