from collections import Callable

from celery import Celery, Task

from Lib.actions import Action
from Lib.queues import BindingKey


def subscribe(app: Celery, queue_name: str, binding_key: BindingKey, action: Action) -> Callable:
    def wrapper(function: Callable) -> Task:
        routing_key = f"{str(binding_key)}.{str(action)}"
        return app.task(function, name=routing_key, queue=queue_name)

    return wrapper
