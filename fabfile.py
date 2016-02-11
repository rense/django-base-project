import os

from contextlib import contextmanager
from fabric.api import task, local
from fabric.context_managers import settings as fabric_settings

with open('environment', 'r') as _file:
    environment = _file.read().replace('\n', '')

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE', 'settings.%s' % environment
)

from django.conf import settings

manage_file = os.path.join(settings.BASE_DIR, 'manage.py')

gunicorn_pid_file = os.path.join(
    settings.BASE_DIR, settings.PID_DIR, 'gunicorn.pid'
)

@contextmanager
def _continue():
    with fabric_settings(warn_only=True):
        yield

@task
def clean():
    local('find %s -name "*.pyc" -exec rm {} \;' % settings.BASE_DIR)

@task
def run():
    clean()
    local(
        '%s runserver_plus 0.0.0.0:8000 -v 2 --threaded' % (manage_file,)
    )

@task
def shell():
    local(
        '%s shell_plus' % (manage_file,)
    )

@task
def test():
    clean()
    local(
        '%s test -v 2' % (manage_file,)
    )

@task
def pip():
    local('pip-compile requirements.in')
    local('pip-sync requirements.txt')
