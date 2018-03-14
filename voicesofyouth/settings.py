"""
Django settings for {} project..format(PROJECT_NAME)

Generated by 'django-admin startproject' using Django 1.11.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

import dj_database_url
from decouple import config
from unipath import Path

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).absolute().parent
PROJECT_NAME = BASE_DIR.name

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default='%3)=j$(#mt8!$t+kps2y8&2v*x63lb%hjjyw6k3desjg2*#5^#')
GEOS_LIBRARY_PATH=config('GEOS_LIBRARY_PATH', '/usr/lib/x86_64-linux-gnu/libgeos_c.so')  # Ubuntu default path
GDAL_LIBRARY_PATH=config('GDAL_LIBRARY_PATH', '/usr/lib/libgdal.so')  # Ubuntu default path
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)
DEBUG_TOOLBAR = config('DEBUG_TOOLBAR', default=False, cast=bool)

ALLOWED_HOSTS = ['127.0.0.1', 'localhost'] + config('ALLOWED_HOSTS',
                                                    cast=lambda v: [h for h in v.split(',')],
                                                    default='')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.gis',
    'django.contrib.postgres',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'smartmin',
    'rest_framework',
    'rest_framework_gis',
    'rest_framework.authtoken',
    'corsheaders',
    'django_filters',
    'crispy_forms',
    'taggit',
    'compressor',
    'sass_processor',
    'qurl_templatetag',
    'leaflet',
    'docs',
    'voicesofyouth.core',
    'voicesofyouth.user',
    'voicesofyouth.project',
    'voicesofyouth.tag',
    'voicesofyouth.theme',
    'voicesofyouth.report',
    'voicesofyouth.api',
    'voicesofyouth.translation',
    'voicesofyouth.voyadmin',
    'graphene_django'
]

GRAPHENE = {
    'SCHEMA': 'voicesofyouth.api.graphql.schema.schema',
    'MIDDLEWARE': [
        'graphene_django.debug.DjangoDebugMiddleware',
    ]
}

if DEBUG:
    from voicesofyouth.core.model_mommy import MOMMY_SPATIAL_FIELDS
    MOMMY_CUSTOM_FIELDS_GEN = MOMMY_SPATIAL_FIELDS

INSTALLED_APPS.append('django_extensions')
INSTALLED_APPS.append('model_mommy')
INSTALLED_APPS.append('mommy_spatial_generators')
INTERNAL_IPS = ('127.0.0.1', 'localhost')

DOCS_ROOT = os.path.join(BASE_DIR, '../docs/users/build/html')
# DOCS_ACCESS = 'staff'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

LOGIN_URL = '/admin/login/'

if DEBUG_TOOLBAR:
    INSTALLED_APPS.append('debug_toolbar')
    MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')

CORS_ORIGIN_WHITELIST = (
    'localhost:8000',
    '127.0.0.1:8000',
    'localhost:8080',
    '127.0.0.1:8080',
)

CORS_ALLOW_CREDENTIALS = True

ROOT_URLCONF = '{}.urls'.format(PROJECT_NAME)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'voicesofyouth.core.context_processors.notifications',
            ],
        },
    },
]

WSGI_APPLICATION = '{}.wsgi.application'.format(PROJECT_NAME)

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASE_NAME = 'db.sqlite3'
DEFAULT_DATABASE = config('DEFAULT_DATABASE', default='postgis://postgres:development@localhost:5432/voydev')
DATABASES = {}
DATABASES['default'] = dj_database_url.config(default=DEFAULT_DATABASE)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

AUTH_USER_MODEL = 'user.VoyUser'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = Path('/media/')
PIN_URL = MEDIA_URL.child('pins') + '/'
PIN_ROOT = MEDIA_ROOT.child('pins')
SASS_PROCESSOR_INCLUDE_FILE_PATTERN = r'^.+\.scss$'
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'sass_processor.finders.CssFinder',
]
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static_dev"),
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',)
}

# Default pagination items per page.
ITEMS_PER_PAGE = 10

LEAFLET_CONFIG = {
    'RESET_VIEW': False
}
