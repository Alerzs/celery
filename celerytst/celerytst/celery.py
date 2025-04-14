import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "celerytst.settings") #gives celery access to project settings
app = Celery("celerytst")
app.config_from_object("django.conf:settings", namespace="CELERY") #search setting for CELERY namespace where settings related to celery has it

app.conf.task_routes = {
    'newapp.tasks.task1': {'queue':'queue1'}, 
    'newapp.tasks.task2': {'queue':'queue2'},
    'newapp.tasks.task3': {'queue':'queue3'},
    } #setting queue for each task

app.autodiscover_tasks() #search for tasks.py in each app and tasks in there

