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

FILER_STORAGES = {
    'public': {
        'main': {
            'ENGINE': 'filer.storage.PublicFileSystemStorage',
            'OPTIONS': {
                'location': os.path.join(MEDIA_ROOT, 'images'),
                'base_url': os.path.join(MEDIA_URL, 'images')
            },
            'UPLOAD_TO': 'filer.utils.generate_filename.randomized',
            'UPLOAD_TO_PREFIX': '',
        },
        'thumbnails': {
            'ENGINE': 'filer.storage.PublicFileSystemStorage',
            'OPTIONS': {
                'location': os.path.join(MEDIA_ROOT, 'images', 'thumbnails'),
                'base_url': os.path.join(MEDIA_URL, 'images', 'thumbnails')
            },
        },
    }
}

FILER_DEBUG = True
FILER_ENABLE_LOGGING = True

THUMBNAIL_HIGH_RESOLUTION = True


REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] += (
    'rest_framework.renderers.BrowsableAPIRenderer',
)

PID_DIR = '/tmp/'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

