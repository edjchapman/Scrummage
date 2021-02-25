"""
Django settings for Scrummage project.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from .partial_settings.allowed_hosts import *
from .partial_settings.apps import *
from .partial_settings.celery import *
from .partial_settings.db import *
from .partial_settings.logging import *
from .partial_settings.middleware import *
from .partial_settings.password_validators import *
from .partial_settings.rest_framework import *
from .partial_settings.smtp import *
from .partial_settings.static_media import *
from .partial_settings.templates import *
from .partial_settings.timezone import *
from .partial_settings.vars import *
