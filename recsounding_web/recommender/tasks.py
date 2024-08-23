from celery import Celery

app = Celery('recommender')

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(10.0, my task.s(), name='add evey 10 seconds')
    
@app.task
def my_task():
    print('Tarefa periódica executada.')