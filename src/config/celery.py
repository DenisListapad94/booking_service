import os
from celery.schedules import crontab
from celery import Celery
from celery import shared_task
# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks([
    "config.tasks",
    "booking_app.tasks"
])




@shared_task
def debug_task(second: int):
    from time import sleep
    sleep(second)
    return f'we sleep {second}'

app.conf.beat_schedule = {
    # Executes every 1 minutes
    'sleep some seconds': {
        'task': 'config.celery.debug_task',
        'schedule': crontab(minute="*/1"),
        'args': (10,),
    },
}