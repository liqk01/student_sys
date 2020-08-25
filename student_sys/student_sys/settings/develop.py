from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        'ENGINE': 'django.db.backends.mysql',
        'PORT': 3306,
        'NAME': 'student',
        'USER': 'root',
        'PASSWORD': '*******',
        'HOST': 'localhost',
        'TEST':{
            'NAME': 'student_test'
        }
    }
}
