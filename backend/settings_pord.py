from backend.settings_comon import *
import os

SECRET_KEY = os.environ['DJANGO_SECRET']

DEBUG = False

ALLOWED_HOSTS = [
    '.studypen.in',
    'studypen-env.eba-juigq53v.ap-south-1.elasticbeanstalk.com',

]
CORS_ALLOWED_ORIGINS = [
    'https://www.studypen.in',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['RDS_DB_NAME'],
        'USER': os.environ['RDS_USERNAME'],
        'PASSWORD': os.environ['RDS_PASSWORD'],
        'HOST': os.environ['RDS_HOSTNAME'],
        'PORT': os.environ['RDS_PORT']
    }
}
