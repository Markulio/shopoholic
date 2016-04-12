import os
from celery import Celery
from django.conf import settings


# Default Django settings module for the celery.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shopoholic.settings')


app = Celery('shopoholic')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
