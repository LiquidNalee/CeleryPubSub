from collections import Callable

from celery import Celery, Task

from Lib.actions import Action
from Lib.queues import BindingKey


def subscribe(app: Celery, binding_key: BindingKey, action: Action) -> Callable:
    def wrapper(function: Callable) -> Task:
        routing_key = f"{str(binding_key)}.{str(action)}"
        return app.task(function, name=routing_key)

    return wrapper
