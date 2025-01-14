import os

from celery import Celery
from django.utils import timezone

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'check_inactive_users_every_30_seconds': {
        'task': 'lms_app.tasks.check_inactive_users',  # Путь к вашей задаче
        'schedule': timezone.timedelta(days=30) # Интервал выполнения
    },
}
# Load task modules from all registered Django apps.
app.autodiscover_tasks()