from celery import shared_task
from time import sleep

@shared_task
def task1():
    sleep(1)
    return

@shared_task
def task2():
    sleep(1)
    return

@shared_task
def task3():
    return

