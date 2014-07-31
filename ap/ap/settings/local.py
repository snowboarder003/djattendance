from .base import *

DEBUG = True
TEMPLATE_DEBUG = True

INSTALLED_APPS += ('django_extensions',
                   'debug_toolbar',
                   'django_nose',)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ap',
        'USER': 'ap',
        'PASSWORD': '',
        'HOST': 'localhost',  # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',  # Set to empty string for default.
    }
}

INTERNAL_IPS = ('127.0.0.1',)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

DEBUG_TOOLBAR_CONFIG = {
    'JQUERY_URL': '',  # use local jquery (for offline development)
}

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = '/Library/WebServer/Documents/djattendance/ap/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

MAX_UPLOAD_SIZE = 20971520  # 20MB
CONTENT_TYPES = ['application/pdf', 'image/jpeg', 'image/png', 'image/jpg']  # .pdf, .jpeg and .png
