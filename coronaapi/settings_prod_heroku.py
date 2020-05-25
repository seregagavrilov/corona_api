from .settings_prod import *

import dj_database_url


IS_HEROKU_HOST = True

DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = [
    "*"
]

DATABASES = {
    'default': {
    }
}

DATABASES['default'].update(dj_database_url.config())

def get_cache():
    return {
        'default': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
            'TIMEOUT': None,
            'OPTIONS': {
                'MAX_ENTRIES': 0
            }
        }
    }


CACHES = get_cache()

# BASE_HOST = os.environ.get("BASE_HOST", "https://dev.osla.ru")

# Static files (CSS, JavaScript, Images)
STATIC_ROOT = os.path.join(BASE_DIR, 'static')  # Important for Heroku
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),  # Important for Heroku
)
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
MEDIA_ROOT = ''
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
# AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
AWS_S3_HOST = os.environ['AWS_S3_HOST']
AWS_S3_ENDPOINT_URL = os.environ['AWS_S3_ENDPOINT_URL']
AWS_S3_REGION_NAME = os.environ['AWS_S3_REGION_NAME']
AWS_QUERYSTRING_AUTH = False
AWS_DEFAULT_ACL = None

# django-dbbackup
DBBACKUP_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# DBBACKUP_STORAGE_OPTIONS = {
#     'access_key': os.environ['S3_ACCESS_KEY'],
#     'secret_key': os.environ['S3_SECRET_KEY'],
#     'bucket_name': os.environ['S3_BUCKET_NAME'],
#     'host':  os.environ['S3_HOST_NAME'],
#     'default_acl':  os.environ['S3_DEFAULT_ACL']
# }


# celery settings
CELERY_BROKER_URL = os.environ['REDIS_URL']
CELERY_RESULT_BACKEND = 'django-db'

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [os.environ.get('CHANNELS_REDIS_URL', 'redis://localhost:6379')],
        },
    },
}


