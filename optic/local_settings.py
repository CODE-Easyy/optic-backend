from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = '8^*+=oy+-pujem*%@5e5mb3xf=h@uw!&$k#6)5+8&8+ncpfaj)'

DEBUG = True

ALLOWED_HOSTS = ['195.210.47.31', 's-optic.kz']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'optic',
        'USER': 'optic',
        'PASSWORD': 'optic',
        'HOST': '127.0.0.1',
        'PORT': 5432
    }
}


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'claytemateam@gmail.com'
EMAIL_HOST_PASSWORD = 'dujtneryirlqvdfd'
