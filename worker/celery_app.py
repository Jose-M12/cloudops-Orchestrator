from celery import Celery

app = Celery("cloudops", broker="redis://redis:6379/0", backend="redis://redis:6379/1")
app.conf.update(task_acks_late=True, worker_prefetch_multiplier=1, broker_transport_options={"visibility_timeout": 3600})
