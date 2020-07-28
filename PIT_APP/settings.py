"""
Django settings for PIT_APP project.

Generated by 'django-admin startproject' using Django 3.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from socket import gethostname, gethostbyname

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STAT=os.path.join(BASE_DIR,'static')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%p&m@r)=8pm!zczh1v+&yfk=-g)txrypl!oo8vqx2d4ixwx(p6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [gethostname(), gethostbyname(gethostname()), 'localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'channels',
    'survey.apps.SurveyConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    #for dashboard
    'channels_redis',
    'django_plotly_dash.apps.DjangoPlotlyDashConfig',
    # Form conditions
    'formtools',
    # Debug page loading perf.
    'debug_toolbar',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'PIT_APP.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'PIT_APP.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASE_ENGINE = os.getenv('DATABASE_ENGINE')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3' if DATABASE_ENGINE is None else DATABASE_ENGINE,
    }
}

if DATABASES['default']['ENGINE'] == 'django.db.backends.sqlite3':
    if os.getenv('DATABASE_NAME') is None:
        DATABASES['default']['NAME'] = os.path.join(BASE_DIR, 'db.sqlite3')
    else:
        DATABASES['default']['NAME'] = os.getenv('DATABASE_NAME')
else:
    DATABASES['default']['NAME'] = os.getenv('DATABASE_NAME')
    DATABASES['default']['USER'] = os.getenv('DATABASE_USER')
    DATABASES['default']['PASSWORD'] = os.getenv('DATABASE_PASSWORD')
    DATABASES['default']['HOST'] = os.getenv('DATABASE_HOST')
    DATABASES['default']['PORT'] = int(os.getenv('DATABASE_PORT'))


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Etc/GMT+4'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    STAT,
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

#for dashboard
ASGI_APPLICATION = 'PIT_APP.routing.applications'

X_FRAME_OPTIONS = 'SAMEORIGIN'

CHANNEL_LAYERS = {
    'default' : {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG' : {
            'hosts' : [('localhost', 6379),],
        }
    }
}

PLOTLY_COMPONENTS = [
    'dash_core_components',
    'dash_html_components',
    'dash_renderer',
    'dpd_components'
]

# Redirect to home URL after login (Default redirects to /accounts/profile/)
LOGIN_REDIRECT_URL = '/'

LOGIN_URL = '/login'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INTERNAL_IPS = [
  '127.0.0.1',
]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"