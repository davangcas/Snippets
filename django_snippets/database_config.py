import os
import dj_database_url
from decouple import config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

HEROKU = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}

LOCAL_POSTGRES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'snippets',
        'USER': 'postgres',
        'PASSWORD': '0518',
        'HOST': '127.0.0.1',
        'DATABASE_PORT': '5432',
    }
}