from .base import *

DEBUG = False
TEMPLATE_DEBUG = False

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES = {'default' : dj_database_url.config()}

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
import os
BASE_DIR = os.path.dirname(os.path.abspath(__name__))
STATIC_ROOT = os.path.join(BASE_DIR, 'ap/static')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'ap/static'),
)

BOOTSTRAP3 = {
    'jquery_url': STATIC_ROOT + 'js/jquery-1.11.1.min.js',
    'base_url': None,
    'css_url': STATIC_ROOT + 'css/bootstrap.min.css',
    'theme_url': None,
    'javascript_url': STATIC_ROOT + 'js/bootstrap.min.js',
    'horizontal_label_class': 'col-md-2',
    'horizontal_field_class': 'col-md-4',
}