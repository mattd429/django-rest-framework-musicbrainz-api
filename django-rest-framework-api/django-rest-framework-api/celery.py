import os
from celery import Celery

# Set the default Django, settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django-rest-framework-api.settings.base')

from django.conf import settings

# Pointing to the instance of the library
app = Celery('django-rest-framework-api')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# Will dump its own request information.
@app.task(bind=True)
def debug_true(self):
    print('Request: {0!r}'.format(self.request))
