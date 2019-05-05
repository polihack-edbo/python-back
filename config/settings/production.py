from .base import *

import os

import dj_database_url

SECRET_KEY = os.environ['SECRET_KEY']
ENVIRONMENT = 'production'
DEBUG = os.environ['DEBUG'] if 'DEBUG' in os.environ else False
ALLOWED_HOSTS = ['*']
DATABASES['default'] = dj_database_url.config(
    default='DATABASE_URL_HERE'
)