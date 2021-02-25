import os

from django.conf import settings

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(settings.OUTSIDE_PROJECT_DIR, 'static')
STATICFILES_DIRS = ["templates/static"]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(settings.OUTSIDE_PROJECT_DIR, 'media')
