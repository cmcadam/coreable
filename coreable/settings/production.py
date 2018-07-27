from coreable.settings.base import *
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = [*]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD'os.environ['DB_PASSWORD'],
        'HOST': 'localhost',
        'PORT': '',
    }
}

try:
    from coreable.settings.local import *
except:
    pass