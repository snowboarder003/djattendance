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

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] =  dj_database_url.config(default='postgres://django:attend2god@localhost/ap')

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
import os
BASE_DIR = os.path.dirname(os.path.abspath(__name__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/ap/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'ap/static'),
)