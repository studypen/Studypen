from backend.settings_comon import *

SECRET_KEY = 'zt-wymci1#aobqr-$g#8cm5+-06338$8f74l%i*p(chg$h%sse'

DEBUG = True

CORS_ALLOWED_ORIGINS = [
    "http://localhost:9000",
    "http://127.0.0.1:9000",
    "http://192.168.43.1:9000"
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'studenthut',
        'PASSWORD': 'iwillnotshare',

        'USER': 'studenthut',  # db name

        'HOST': 'localhost',  # host
        'PORT': 5432,  # port
    }
}
