from pathlib import Path

import django_heroku
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = '8^*+=oy+-pujem*%@5e5mb3xf=h@uw!&$k#6)5+8&8+ncpfaj)'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',

    'accounts',
    'products',
    'dashboard',
    'events',
    'filters',
    'orders',
    'carts',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'optic.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
            BASE_DIR / 'build',
        ]
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

CORS_ALLOW_ALL_ORIGINS = True
WSGI_APPLICATION = 'optic.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 's_optic',
        'USER': 'almaz',
        'PASSWORD': 'almazdb',
        'HOST': 'localhost',
        'PORT': 5432
    }
}

# DATABASES = {
#     'default': dj_database_url.config()
# }

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


LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Asia/Almaty'

USE_I18N = True

USE_L10N = True

USE_TZ = True

AUTH_USER_MODEL = 'accounts.User'
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    BASE_DIR / 'static',
    BASE_DIR / 'build' / 'static',
)
STATIC_ROOT = BASE_DIR / 'static'

##### MEDIAS
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'claytemateam@gmail.com'
EMAIL_HOST_PASSWORD = 'dujtneryirlqvdfd'

django_heroku.settings(locals())