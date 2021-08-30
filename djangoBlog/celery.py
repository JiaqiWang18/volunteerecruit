from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoBlog.settings')

app = Celery('djangoBlog')

app.config_from_object('django.conf:settings', namespace='CELERY')
print(app.conf)
app.autodiscover_tasks()
