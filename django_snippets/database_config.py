import os
import dj_database_url
import decouple

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

HEROKU = {
    'default': dj_database_url.config(
        default=decouple.config('DATABASE_URL')
    )
}