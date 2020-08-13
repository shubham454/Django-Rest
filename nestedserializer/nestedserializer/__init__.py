from __future__ import absolute_import

# this will take sure the app is always importt when
# Django starts so that shared _task  will use this app

from .celery import app as celery_app

