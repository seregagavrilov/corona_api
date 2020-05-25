from .settings_common import *

DEBUG = True
THUMBNAIL_DEBUG = True

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

INTERNAL_IPS = (
    '127.0.0.1',
    '192.168.1.141'
)

EMAIL_BACKEND = "djmail.backends.async.EmailBackend"

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

CELERY_BROKER_URL = env('REDIS_URL', default='redis://localhost:6379')

