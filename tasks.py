from celery import Celery
import logging

app = Celery('tasks', broker="pyamqp://guest:guest@localhost//")
logger = logging.getLogger(__name__)


@app.task
def on_animal(body):
    print("It's an animal")
    print(body)


@app.task
def on_rabbit(body):
    print("It'a rabbit")
    print(body)

