from collections import Callable

from celery import Celery, Task

from Lib.actions import Action
from Lib.queues import BindingKey


def subscribe(app: Celery, binding_key: BindingKey, action: Action) -> Callable:
    def wrapper(function: Callable) -> Task:
        routing_key = f"{str(binding_key)}.{str(action)}"
        app.conf.task_routes[f"{function.__module__}.{function.__name__}"] = {
            "queue": str(binding_key),
            "routing_key": routing_key,
        }
        return app.task(function)

    return wrapper
