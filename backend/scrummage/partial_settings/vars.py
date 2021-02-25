import os

APPENV = os.getenv('APP_SETTINGS_ENV', "LOCAL")

DEBUG = APPENV != "PRODUCTION"

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

OUTSIDE_PROJECT_DIR = os.path.dirname(BASE_DIR)

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'aPmJynQS9C44Hn3GoKQHte84igYNqb35gr7thTFY')

ROOT_URLCONF = 'scrummage.urls'

WSGI_APPLICATION = 'scrummage.wsgi.application'

ASGI_APPLICATION = "scrummage.routing.application"
