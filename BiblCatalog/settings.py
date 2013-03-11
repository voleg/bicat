# Django settings for BiblCatalog project.
import os, platform

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

TESTING = 1

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
elif TESTING == 1 :
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

    DEBUG = True

TEMPLATE_DEBUG = DEBUG

ADMINS = (
     ('Voleg', 'ffrooty@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': default_db,
    'bikart': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'B_KART',
        'USER': 'biblioteka',
        'PASSWORD': '250bibl052',
        'HOST': MSSQL_HOST,
        'PORT': MSSQL_PORT,
        'COLLATION': 'Cyrillic_General_CI_AS',
        'OPTIONS':  {   'driver': 'TDS',
                        'dsn':  b_kart,
                        'host_is_server': True,
                        'extra_params': 'TDS_VERSION=8.0' }
    },
    'bicat': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'B_CAT',
        'USER': 'biblioteka',
        'PASSWORD': '250bibl052',
        'HOST': MSSQL_HOST,
        'PORT': MSSQL_PORT,
        'COLLATION': 'Cyrillic_General_CI_AS',
        'OPTIONS':  {   'driver': 'TDS',
                        'dsn':  b_cat,
                        'host_is_server': True,
                        'extra_params': 'TDS_VERSION=8.0' }
    },
    'biuml': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'B_uml',
        'USER': 'biblioteka',
        'PASSWORD': '250bibl052',
        'HOST': MSSQL_HOST,
        'PORT': MSSQL_PORT,
        'COLLATION': 'Cyrillic_General_CI_AS',
        'OPTIONS':  {   'driver': 'TDS',
                        'dsn':  b_uml,
                        'host_is_server': True,
                        'extra_params': 'TDS_VERSION=8.0' }
    }
}

DATABASE_ROUTERS = ['apps.router.BiRouter']

DO_NOT_SPLIT_TAGS = ['254']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Moscow'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'ru-ru'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = False

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_PATH, '../sitemedia/media/')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PROJECT_PATH, '../sitemedia/static/')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'a1_vu9e1ty(adt8af!d8y@l=7r#w2^pgbfjrlk#^)yj_no_imq'

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

ROOT_URLCONF = 'BiblCatalog.urls'

# Python dotted path to the WSGI application used by Django's runserver.
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
#    'sorl.thumbnail'
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
