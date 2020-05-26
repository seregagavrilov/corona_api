import os
import environ


ROOT_DIR = environ.Path(__file__) - 2
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

IS_HEROKU_HOST = False
env = environ.Env()
env.read_env(str(ROOT_DIR.path(".env")))

SECRET_KEY = '1g03(1a&49j93lk3b*e#xz@25v)5i=b0i+z6=8re9ftoy3e7(g'

DEBUG = True

ALLOWED_HOSTS = ['*']

# VIRUS_API_URL = 'https://coronavirus-tracker-api.herokuapp.com/v2/locations/'
VIRUS_API_URL = 'https://coronavirus-tracker-api.herokuapp.com/v2/locations/?timelines=true'

INSTALLED_APPS = [
    'jet.dashboard',
    'jet',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'django_extensions',
    'django_celery_results',
    'django_celery_beat',
    'storages',
    'corsheaders',
]

PROJECT_APPS = [
    'apps.country',
]

INSTALLED_APPS.extend(PROJECT_APPS)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',

]

ROOT_URLCONF = 'coronaapi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, "static")
]


WSGI_APPLICATION = 'coronaapi.wsgi.application'

CORS_ORIGIN_ALLOW_ALL = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env("POSTGRES_DB", default='virus'),
        'USER': env("POSTGRES_USER", default='sergey'),
        'PASSWORD': env("POSTGRES_PASSWORD", default='Qwerty123'),
        'HOST': env("POSTGRES_HOST", default='localhost'),
        'PORT': env("POSTGRES_PORT", default=5432),
        'CLIENT_ENCODING': 'UTF8',
        'ATOMIC_REQUESTS': True,
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

JET_SIDE_MENU_COMPACT = True

JET_SIDE_MENU_ITEMS = [
    {'label': 'Страны', 'items': [
        {'name': 'country.country'},
        {'name': 'country.countrystatistic'},
    ]},
    {'label': 'Периодические задачи', 'items': [
        {'name': 'django_celery_beat.periodictask', 'label': 'Запланированные задачи'},
        {'name': 'django_celery_results.taskresult', 'label': 'Результат выполнения'},
        {'name': 'django_celery_beat.intervalschedule', 'label': 'Временные интервалы'},
        {'name': 'django_celery_beat.crontabschedule', 'label': 'Cron интервалы'},
    ]},
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_RESULT_BACKEND = 'django-db'
CELERY_BROKER_URL = env('REDIS_URL', default='redis://localhost:6379')


STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
MEDIA_ROOT = ''

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

