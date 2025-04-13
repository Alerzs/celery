from celery import Celery

app = Celery('task')
app.config_from_object('celeryconfig') # takes settings from celeryconfig.py file
app.conf.imports = ('newapp.tasks') # import tasks from tasks.py file
app.autodiscover_tasks()