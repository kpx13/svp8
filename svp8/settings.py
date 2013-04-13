# -*- coding: utf-8 -*-
import os
from os.path import abspath, join, dirname

DEBUG = False
TEMPLATE_DEBUG = False

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS
PROJECT_ROOT = abspath(join(dirname(__file__), "../"))
LOGIN_URL = '/login'

DATE_FORMAT = '%d.%m.%Y'
DATETIME_FORMAT = '%d.%m.%Y'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'svp8',   # Or path to database file if using sqlite3.
        'USER': 'svp8',                      # Not used with sqlite3.
        'PASSWORD': 'svp8',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Asia/Dubai'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'Ru-ru'

SITE_ID = 3

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = PROJECT_ROOT + '/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = STATICFILES_ROOT = PROJECT_ROOT + '/static/'


# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".

STATIC_URL = STATICFILES_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'site_static'),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

ADMIN_MEDIA_PREFIX = STATIC_URL + "grappelli/"
MEDIA_PATH = PATH_FILEBROWSER_MEDIA = MEDIA_ROOT + 'uploads/'

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'g!nh@9(-vt+ac_)zrf+1vks(6dj+sqv96eb8=fq^xg3c*rr=@)'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'svp8.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'svp8.wsgi.application'

TEMPLATE_DIRS = (
    PROJECT_ROOT + '/templates',
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'grappelli',
    'filebrowser',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'ckeditor',
    'taggit',
    
    'pages',
    'subscribe',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

FILE_UPLOAD_MAX_MEMORY_SIZE = 7864320
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar':
           [
                ['Source', '-', 'Templates'],
                ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord'],
                ['Undo', 'Redo', ],
                ['NumberedList','BulletedList','-','Outdent','Indent','Blockquote'],
                ['JustifyLeft','JustifyCenter','JustifyRight','JustifyBlock'],
                ['Image','Flash','Table','HorizontalRule','Smiley','SpecialChar'],
                ['RemoveFormat', 'Bold','Italic','Underline','Strike','-','Subscript','Superscript'],
                ['Styles','Format','FontSize', 'TextColor','BGColor'],
                ['Link','Unlink',],
                ['Maximize', 'ShowBlocks'],
            ],
        'width': 1056,
        'height': 200,
        'toolbarCanCollapse': True,
        'resize_enabled': True
    }
}

CKEDITOR_UPLOAD_PATH = os.path.join(MEDIA_ROOT, 'uploads')
CKEDITOR_MEDIA_PREFIX = '/media/ckeditor/'
GRAPPELLI_ADMIN_TITLE = u'SVP8.ru - Спасаем мир, блеать!'
SEND_ALERT_EMAIL = ['annkpx@gmail.com']
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'noreply@webgenesis.ru'
EMAIL_HOST_PASSWORD = 'noreply13'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

try:
    from dev import *
except:
    pass
