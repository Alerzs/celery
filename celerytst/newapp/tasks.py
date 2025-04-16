from celerytst.celery import app

@app.task(queue='priority_queue')
def task1():
    return
