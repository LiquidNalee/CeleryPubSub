import logging

from celery import Celery

from Lib.actions import Action
from Lib.celery_consumer import subscribe
from Lib.celery_event_bus import CeleryEventBus
from Lib.queues import BindingKey

app = Celery('tasks2', broker="pyamqp://guest:guest@localhost//")


@subscribe(app=app, binding_key=BindingKey.ESTIMA, action=Action.CREATION)
def on_estima_creation(body):
    print("Estima created but add a lil bit of spice")
    print(body)


@subscribe(app=app, binding_key=BindingKey.LEAD, action=Action.CREATION)
def on_lead_creation(body):
    print("Lead created")
    print(body)
