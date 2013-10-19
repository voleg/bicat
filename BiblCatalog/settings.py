# coding: utf-8
__author__ = 'voleg'
import os, platform
from django.core.exceptions import ImproperlyConfigured
try:
    from .local import *
except ImportError:
    raise ImproperlyConfigured('can\'t get local settings')

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
hostname = platform.node()

# remote host VirtualBox Vm
test1_msql_host = '192.168.198.3'
test1_msql_port = '3019'
# localhost VirtualBox Vm
test2_msql_host = '192.168.56.3'
test2_msql_port = '3019'
# Production DB Server (hostname = 'res')
production_msql_host = '192.168.1.252'
production_msql_port = '4538'

TESTING = 2

if hostname == 'res' or TESTING == 0:
    MSSQL_HOST = production_msql_host
    MSSQL_PORT = production_msql_port

    # DSN's
    b_cat = 'SERV3BCAT'
    b_kart = 'SERV3BKART'
    b_uml = 'SERV3BUML'

    default_db = {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bicat',
        'USER': 'bicat',
        'PASSWORD': 'J8jPJ1Fv',
        'HOST': '192.168.0.242',
        'PORT': '',
    }

    DEBUG = False
elif TESTING == 1:
    MSSQL_HOST = production_msql_host
    MSSQL_PORT = production_msql_port

    # DSN's
    b_cat = 'SERV3BCAT'
    b_kart = 'SERV3BKART'
    b_uml = 'SERV3BUML'

    default_db = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_PATH, '../dev.db'),
    }

    DEBUG = True
else:
    MSSQL_HOST = test2_msql_host
    MSSQL_PORT = test2_msql_port

    # DSN's
    b_cat = 'TEST2SERV3BCAT'
    b_kart = 'TEST2SERV3BKART'
    b_uml = 'TEST2SERV3BUML'

    default_db = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_PATH, '../dev.db'),
    }

    DEBUG = True

TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': default_db,
    'bikart': {
        'display_name': u'Периодика',
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'B_KART',
        'USER': 'biblioteka',
        'PASSWORD': '250bibl052',
        'HOST': MSSQL_HOST,
        'PORT': MSSQL_PORT,
        'COLLATION': 'Cyrillic_General_CI_AS',
        'OPTIONS': {'driver': 'TDS',
                    'dsn': b_kart,
                    'host_is_server': True,
                    'extra_params': 'TDS_VERSION=8.0'}
    },
    'bicat': {
        'display_name': u'Книги',
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'B_CAT',
        'USER': 'biblioteka',
        'PASSWORD': '250bibl052',
        'HOST': MSSQL_HOST,
        'PORT': MSSQL_PORT,
        'COLLATION': 'Cyrillic_General_CI_AS',
        'OPTIONS': {'driver': 'TDS',
                    'dsn': b_cat,
                    'host_is_server': True,
                    'extra_params': 'TDS_VERSION=8.0'}
    },
    'biuml': {
        'display_name': u'Учебно методическая литература',
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'B_uml',
        'USER': 'biblioteka',
        'PASSWORD': '250bibl052',
        'HOST': MSSQL_HOST,
        'PORT': MSSQL_PORT,
        'COLLATION': 'Cyrillic_General_CI_AS',
        'OPTIONS': {'driver': 'TDS',
                    'dsn': b_uml,
                    'host_is_server': True,
                    'extra_params': 'TDS_VERSION=8.0'}
    }
}

DATABASE_ROUTERS = ['apps.router.BiRouter']

# Тег в поле `db`/DOC.Item который не нужно разрезать по разделителю (`,` или `;`)
DO_NOT_SPLIT_TAGS = ['254']

TIME_ZONE = 'Europe/Moscow'
LANGUAGE_CODE = 'ru-ru'

SITE_ID = 1

USE_I18N = True
USE_L10N = True
USE_TZ = False

MEDIA_ROOT = os.path.join(PROJECT_PATH, '../sitemedia/media/')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_PATH, '../sitemedia/static/')
STATIC_URL = '/static/'

STATICFILES_DIRS = ()

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #     'django.template.loaders.eggs.Loader',
)

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

TEMPLATE_DIRS = (os.path.join(PROJECT_PATH, '../templates/'),)

TEMPLATE_CONTEXT_PROCESSORS = (
    # default template context processors
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    # required by django-admin-tools
    'django.core.context_processors.request',
    'apps.prefs.context_processors.context_prefs',
)

INSTALLED_APPS = (
    'django_extensions',
    #    'admin_tools',
    #    'admin_tools.theming',
    #    'admin_tools.menu',
    #    'admin_tools.dashboard',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.markup',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    'django_markdown',
    'south',
    'south_admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
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
