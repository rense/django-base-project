#!/usr/bin/env python
import os
import sys

from django.core.management import execute_from_command_line

if __name__ == "__main__":

    with open("environment", "r") as _file:
        environment = _file.read().replace('\n', '')

    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE", "settings.%s" % environment
    )
    execute_from_command_line(sys.argv)
