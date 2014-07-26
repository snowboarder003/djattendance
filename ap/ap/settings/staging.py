from .base import *

DEBUG = True
TEMPLATE_DEBUG = True

INSTALLED_APPS += ('gunicorn',
                   'debug_toolbar',)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ap',
        'USER': 'django',
        'PASSWORD': 'attend2god',
        'HOST': 'localhost',
        'PORT': '',
    }
}
