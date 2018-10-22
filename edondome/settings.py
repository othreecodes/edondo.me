"""
Django settings for edondome project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%#28eszcedox(07bqb0w(opckl&fx+ac*)ypc%9b&po5ib07od'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ENV = os.environ

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'social_django',
    'el_pagination',
    'rest_framework',
    'app',
    'firebase_auth'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'edondome.urls'

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
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'edondome.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': ENV['DB_NAME'],
        'USER': ENV['DB_USER'],
        'PORT': ENV['DB_PORT'],
        'PASSWORD': ENV['DB_PASS'],
        'HOST': ENV['DB_HOST'],

    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

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
AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookAppOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'django.contrib.auth.backends.ModelBackend',
)
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Lagos'

USE_I18N = True

USE_L10N = True

USE_TZ = True
ACCOUNT_USE_OPENID = False
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
SOCIAL_AUTH_TWITTER_KEY = 'QAZQTBkn9njp6cG54uJZ5nELw'
SOCIAL_AUTH_TWITTER_SECRET = 'FDR1YLDhtibMtNOwqdp73clr1NayOwgjnPFSvj0hHvinDIFrMl'
LOGIN_REDIRECT_URL = '/'

SOCIAL_AUTH_FACEBOOK_KEY = '1783444311970266'
SOCIAL_AUTH_FACEBOOK_SECRET = '3467a3f900d52e65c7a610321ea87ba5'
SOCIAL_AUTH_FACEBOOK_APP_NAMESPACE = 'edondome'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_API_VERSION = '2.9'

EL_PAGINATION_PER_PAGE = 12

# SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '793466574970-8ib5im5ufi13qq28gcuf4b7mdau3tkt2.apps.googleusercontent.com'
# SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'jzFh8TUAAw0Vj7wzt3RsUH7Z'
#
# SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
#     "profile",
#     "email"
# ]
# SOCIAL_AUTH_GOOGLE_OAUTH2_USE_DEPRECATED_API = True
# SOCIAL_AUTH_GOOGLE_PLUS_USE_DEPRECATED_API = True
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')

SOCIAL_AUTH_REDIRECT_IS_HTTPS = True

# Force https redirect
SECURE_SSL_REDIRECT = True
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ('firebase_auth.authentication.FirebaseAuthentication', ),
    'DATETIME_FORMAT': "%Y-%m-%d %H:%M",
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 50,
    
}

APPEND_SLASH = False
KEYFILES_DIR = os.path.join(BASE_DIR, 'keyfiles')
FIREBASE_KEY = 'edondome-165419-firebase-adminsdk-nxf5m-53cce390fd.json'