# coding: utf-8
import os, platform
from django.core.exceptions import ImproperlyConfigured
try:
    from .local import *
except ImportError:
    raise ImproperlyConfigured('Please place your local settings near settings.py!')

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
path = lambda *args: os.path.join(PROJECT_PATH, *args)

if PRODUCTION_BRANCH in PROJECT_PATH and 'Linux' in platform.system():
    DEBUG = False
    MSSQL_HOST = PRODUCTION_MSSQL_HOST
    MSSQL_PORT = PRODUCTION_MSSQL_PORT
    MSSQL_USER = PRODUCTION_MSSQL_USER
    MSSQL_PASS = PRODUCTION_MSSQL_PASS
    DEFAULT_DB = PRODUCTION_DB
else:
    DEBUG = True
    MSSQL_HOST = DEV_MSSQL_HOST
    MSSQL_PORT = DEV_MSSQL_PORT
    MSSQL_USER = DEV_MSSQL_USER
    MSSQL_PASS = DEV_MSSQL_PASS
    DEFAULT_DB = STAGING_DB
    DEBUG = True

TEMPLATE_DEBUG = DEBUG

odbc_dsn_connector = lambda db_name, display_name: dict(
    display_name=display_name,
    ENGINE='sql_server.pyodbc',
    NAME=db_name,
    USER=MSSQL_USER,
    PASSWORD=MSSQL_PASS,
    HOST=MSSQL_HOST,
    PORT=MSSQL_PORT,
    OPTIONS=dict(
        host_is_server=True,
        extra_params='tds_version=8.0;ClientCharset=UTF8',
    )
)

DATABASES = {
    'default': DEFAULT_DB,
    'bikart': odbc_dsn_connector('B_KART', u'Периодика'),
    'bicat': odbc_dsn_connector('B_CAT', u'Книги'),
    'biuml': odbc_dsn_connector('B_uml', u'Учебно методическая литература')
}

DATABASE_ROUTERS = ['apps.router.BiRouter']

# Тег в поле `db`/DOC.Item который не нужно разрезать по разделителю (`,` или `;`)
DO_NOT_SPLIT_TAGS = ['254']

TIME_ZONE = 'Europe/Moscow'
LANGUAGE_CODE = 'ru-RU'

SITE_ID = 1

USE_I18N = True
USE_L10N = True
USE_TZ = False

MEDIA_ROOT = path('..', 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = path('..', 'static')
STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), '..', 'templates').replace('\\','/'),)

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',                # кешируем весь сайт целиком
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',             # кешируем весь сайт целиком
)

ROOT_URLCONF = 'BiblCatalog.urls'
WSGI_APPLICATION = 'BiblCatalog.wsgi.application'

TEMPLATE_CONTEXT_PROCESSORS = (
    # default template context processors
    'django.core.context_processors.debug',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
    # required by django-admin-tools
    'apps.prefs.context_processors.context_prefs',
)

INSTALLED_APPS = (
    'django_extensions',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.markup',
    'django.contrib.admin',
    'django_markdown',
    'south',
    'south_admin',
    'apps.blog',
    'apps.marc15',
    'apps.marc15.BiCat',
    'apps.marc15.BiKart',
    'apps.marc15.BiUML',
    'apps.marc15.search',
    'sitemedia',
    'apps.prefs',
    #    'sorl.thumbnail'
    'crispy_forms'
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

### REDIS
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379

# Используем REDIS в качестве KVS для кеширования на боевой ноде
# на локальной машине также можно использовать REDIS
#   brew install redis      # установка на OSX
#   redis-server            # запуск демона

REDIS_CACHES = {
   'default': {
       'BACKEND': 'redis_cache.RedisCache',
       'LOCATION': '127.0.0.1:6379',
       'TIMEOUT': 60,
       'MAX_ENTRIES': 10000,
       'OPTIONS': {
           'DB': 3,
           },
       },
   }

DUMMY_CACHES = {
     'default': {
         'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
     }
}

if DEBUG:
    CACHES=DUMMY_CACHES
else:
    CACHES=DUMMY_CACHES
