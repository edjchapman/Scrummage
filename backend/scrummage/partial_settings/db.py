import os

DATABASES = {
    'default': {
        'ENGINE': os.getenv('DJANGO_DEFAULT_DB_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': os.getenv('DJANGO_DEFAULT_DB_NAME', 'db.sqlite3'),
        'HOST': os.getenv('DJANGO_DEFAULT_DB_HOST'),
        'PORT': os.getenv('DJANGO_DEFAULT_DB_PORT'),
        'USER': os.getenv('DJANGO_DEFAULT_DB_USER'),
        'PASSWORD': os.getenv('DJANGO_DEFAULT_DB_PASSWORD'),
    },
}

if 'postgres' in DATABASES['default']['ENGINE']:
    DATABASES['default']['OPTIONS'] = {'options': '-c search_path=scrummage,scrummage'}
