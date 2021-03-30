from pubsub_tasks import publish

publish("animals.rabbit", {"id": 42})
publish("animals.cat", {"id": 23})
