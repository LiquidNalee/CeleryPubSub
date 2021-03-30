from pubsub_tasks import subscribe, SubscriptionRequest
from tasks import on_rabbit, on_animal

subscribe.delay("animals.#")
