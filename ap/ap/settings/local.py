from .base import *

ADMINS += (
    ('Sarah Rumbley', 'srumbley@mit.edu')
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'C:/Users/Scrumbley/attendanceplus/ap/database.db',                      # Or path to database file if using sqlite3.
    }
}

TEMPLATE_DIRS = (
    'C:/Users/Scrumbley/attendanceplus/ap/templates'
)

INSTALLED_APPS += (
    'terms',
    'django.contrib.admin',
)

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    'C:/Users/Scrumbley/attendanceplus/ap/static',
)
