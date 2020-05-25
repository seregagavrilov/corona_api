from .settings_common import *


DEBUG = False

ALLOWED_HOSTS = [
    ".osla.ru",
    ".herokuapp.com",
    "127.0.0.1",
    "0.0.0.0"
]

AWS_S3_OBJECT_PARAMETERS = {
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'CacheControl': 'max-age=94608000',
}

AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')
S3_CLOUDFRONT_DOMAIN = env('AWS_S3_HOST')

MEDIAFILES_LOCATION = 'media'
MEDIA_ROOT = '/%s/' % MEDIAFILES_LOCATION
MEDIA_URL = 'https://%s/%s/' % (S3_CLOUDFRONT_DOMAIN, MEDIAFILES_LOCATION)
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'

STATICFILES_LOCATION = 'static'
STATIC_ROOT = '/%s/' % STATICFILES_LOCATION
# STATIC_URL = 'https://%s/%s/' % (S3_CLOUDFRONT_DOMAIN, STATICFILES_LOCATION)
STATICFILES_STORAGE = 'custom_storages.StaticStorage'

# AWS_S3_REGION_NAME = env('AWS_S3_REGION_NAME')
# AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
# AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')

# celery settings
CELERY_BROKER_URL = env('CELERY_BROKER_URL', default="redis://localhost:6379/1")
CELERY_RESULT_BACKEND = 'django-db'

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [os.environ.get('CHANNELS_REDIS_URL', default='redis://localhost:6379/1')],
        },
    },
}

