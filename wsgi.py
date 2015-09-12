import os

with open("environment", "r") as _file:
    environment = _file.read().replace('\n', '')

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "settings.%s" % environment
)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
