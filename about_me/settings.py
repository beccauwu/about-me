"""
Django settings for about_me project.

Generated by 'django-admin startproject' using Django 4.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
import dj_database_url
from pathlib import Path
from decouple import config
from google.oauth2 import service_account

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = [
    '*'
    # 'about-me-rebecca.herokuapp.com'
]

# Application definition

INSTALLED_APPS = [
    'dal',
    'dal_select2',
    'django_addanother',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'whitenoise.runserver_nostatic',
    'client_side_image_cropping',
    'inlineedit',
    'corsheaders',
    'storages',
    'about_me',
    'accounts',
    'photography',
    'anymail',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'about_me.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'about_me.context-processors.add_account_forms',
            ],
        },
    },
]

WSGI_APPLICATION = 'about_me.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

if not DEBUG:
    DATABASES = {'default': dj_database_url.config(conn_max_age=600, ssl_require=True)}
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': config('POSTGRESQL_DATABASE'),
            'USER': config('POSTGRESQL_USER'),
            'PASSWORD': config('POSTGRESQL_PASSWORD'),
            'HOST': config('POSTGRESQL_HOST'),
            'PORT': config('POSTGRESQL_PORT'),
        }
    }

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/


# AWS s3 settings
AWS_S3_ACCESS_KEY_ID = config('AWS_S3_ACCESS_KEY_ID')
AWS_S3_SECRET_ACCESS_KEY = config('AWS_S3_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = config('AWS_S3_BUCKET_NAME')
AWS_S3_CUSTOM_DOMAIN = config('AWS_S3_DOMAIN')
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
    'ACL': 'public-read',
}
AWS_LOCATION = 'static'
STATIC_URL = "https://{}/{}/".format(AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
# GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
#         os.path.join(BASE_DIR, 'google-credentials.json')
#     )

DEFAULT_FILE_STORAGE = 'about_me.storage_backends.MediaRootS3Boto3Storage'
STATICFILES_STORAGE = "about_me.storage_backends.StaticRootS3Boto3Storage"
# GS_BUCKET_NAME = 'django-site1-b420694.appspot.com'

# STATICFILES_STORAGE = "about_me.storage_backends.StaticGCSStorage"
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATIC_LOCATION = 'static'
# STATIC_URL = 'https://storage.googleapis.com/{}/static/'.format(GS_BUCKET_NAME)
# MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafiles')
# MEDIA_LOCATION = 'media'
# MEDIA_URL = 'https://storage.googleapis.com/{}/media/'.format(GS_BUCKET_NAME)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'website_cache_table',
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
             'level': os.getenv('DJANGO_LOG_LEVEL'),
        },
    },
}


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LOGIN_REDIRECT_URL = 'apps.home'
LOGOUT_REDIRECT_URL = 'apps.home'

#email settings
ANYMAIL = {
  "MAILGUN_API_KEY": config('MAILGUN_API_KEY', default=None),
  "MAILGUN_API_URL": "https://api.eu.mailgun.net/v3",
  "MAILGUN_SENDER_DOMAIN": config('MAILGUN_DOMAIN', default=None),
}

EMAIL_BACKEND = 'anymail.backends.mailgun.EmailBackend'


INLINEEDIT_EDIT_ACCESS = lambda user, model, field: True

INLINEEDIT_ADAPTORS = {
    "formcontrol": "about_me.adaptors.FormControl",
    'textarea': 'about_me.adaptors.TextArea',
}

from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}
