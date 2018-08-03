from settings import *

DEBUG = True

SECRET_KEY = 'development-nonsense-key'

CORS_ORIGIN_ALLOW_ALL = True

DATABASE_DEFAULT = {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'django-base-project',
    'USER': 'dbp-user',
    'PASSWORD': 'dbp-password',

    'HOST': '127.0.0.1',
    'PORT': '3306',
    'OPTIONS': {
        'init_command': "SET sql_mode='STRICT_ALL_TABLES'",
        'charset': 'utf8mb4'
    }
}

DATABASES = {
    'default': DATABASE_DEFAULT
}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['console'],
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        }
    }
}

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] += (
    'rest_framework.renderers.BrowsableAPIRenderer',
)

PID_DIR = '/tmp/'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

