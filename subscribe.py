from pubsub_tasks import subscribe, SubscriptionRequest
from tasks import on_rabbit, on_animal

sub_request = SubscriptionRequest()\
    .on("animals.rabbit", on_rabbit.delay)\
    .all(on_animal.delay)
subscribe.delay("animals.#", sub_request)
