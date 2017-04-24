import os

from contextlib import contextmanager
from fabric.api import task, local
from fabric.context_managers import settings as fabric_settings

from environment import base_dir, environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.%s' % environment)

manage_file = os.path.join(base_dir, 'manage.py')

@contextmanager
def _continue():
    with fabric_settings(warn_only=True):
        yield

@task
def clean():
    local('find %s -name "*.pyc" -exec rm {} \;' % base_dir)


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
