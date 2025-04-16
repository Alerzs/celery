import os
from celery import Celery
from time import sleep
from kombu import Queue ,Exchange

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "celerytst.settings")
app = Celery("celerytst")
app.config_from_object("django.conf:settings", namespace="CELERY") 

app.conf.task_queues = [
    Queue('tasks', Exchange('tasks'), routing_key='tasks',
          queue_arguments={'x-max-priority': 10}),
]

@app.task(queue='tasks')
def task1():
    sleep(3)
    return

@app.task(queue='tasks')
def task2():
    sleep(3)
    return


app.conf.task_acks_late = True
app.conf.task_queue_max_priority = 10
app.conf.task_default_priority = 5 #default priority value 
app.conf.worker_prefetch_multiplier = 1 # how many task can worker get from message broker at once
app.conf.worker_concurrency = 1 # how many tasks can run at once

app.autodiscover_tasks()

