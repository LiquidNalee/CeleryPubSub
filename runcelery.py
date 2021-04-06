#!/usr/bin/env python3

"""Run Celery workers

Bypass the standard bin/celery script installed by setuptools
automatically on install, since we're not using a virtualenv
anymore.
This is the content of the created script, with an import of
`appengine_config` to append the vendors/ folder to sys.path.

This script takes the same arguments as the `celery`.
"""

import sys

from pkg_resources import load_entry_point


if __name__ == "__main__":
    sys.exit(load_entry_point("celery", "console_scripts", "celery")())
