# yourvenv/cfehome/celery.py
from __future__ import absolute_import, unicode_literals # for python2

import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
# this is also used in manage.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fastIT.settings')


## Get the base REDIS URL, default to redis' default
broker_url = 'amqp://guest:guest@localhost:5672/celery'

app = Celery('fastIT')

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.broker_url = broker_url

# this allows you to schedule items in the Django admin.
app.conf.beat_scheduler = 'django_celery_beat.schedulers.DatabaseScheduler'
app.conf.task_default_queue = 'celery'

#PERIODIC TASKS
from celery.schedules import crontab
app.conf.beat_schedule = {
    'get_all_jobs': {
        'task': 'scrap_jobs',
        'schedule': crontab(minute="*/3"),
    },
}
app.conf.timezone = 'UTC'
