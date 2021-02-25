import os

CELERY_BROKER_URL = os.getenv('CELERY_BROKER', 'redis://localhost:6379')
CELERY_RESULT_BACKEND = os.getenv('CELERY_BROKER', 'redis://localhost:6379')
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Europe/London'
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"
