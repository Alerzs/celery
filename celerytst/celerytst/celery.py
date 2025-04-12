import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "celerytst.settings") #gives celery access to project settings

app = Celery("celerytst") #creating a new celery instance using name of the project
app.config_from_object("django.conf:settings", namespace="CELERY") #search setting for CELERY namespace where settings related to celery has it

app.autodiscover_tasks() #search for tasks.py in each app and tasks in there
