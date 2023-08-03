

from pathlib import Path
from corsheaders.defaults import default_headers, default_methods
import os
import environ
print(os.environ.get('PORT'))
PORT = int(os.environ.get('PORT', 5000))


env = environ.Env(
    DEBUG=(bool, False)
)

environ.Env.read_env()

LOCAL_DEV = env('LOCAL_DEV')
DEBUG = env('DEBUG')
SECRET_KEY = env('SECRET_KEY')

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'drf_yasg',
    # apps dependesis
    'core',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'django_cron',
    # apps project
    'app.meet',
    'app.professionals',
    'app.customUser',
    'app.services',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # cors middleware
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_WHITELIST = (
    "*"
)

CORS_ALLOW_ALL_ORIGINS = False

CORS_ALLOWED_ORIGINS = [
    'http://*',
    'https://*'
    # Agrega otros dominios permitidos si es necesario
]

CORS_ALLOW_METHODS = list(default_methods) + ['*'
                                              ]

CORS_ALLOW_HEADERS = list(default_headers) + [
    'contenttype',
]

CORS_ALLOW_CREDENTIALS = True
ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'template')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
if (DEBUG and LOCAL_DEV):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',

            # 'ENGINE': 'django.db.backends.postgresql',
            # 'NAME': env('PGDATABASE'),
            # 'USER': env('PGUSER'),
            # 'PASSWORD': env('PGPASSWORD'),
            # #'HOST': env('PGHOST'),
            # 'PORT': env('PGPORT'),
            # 'ATOMIC_REQUESTS': False,
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': env('PGDATABASE'),
            'USER': env('PGUSER'),
            'PASSWORD': env('PGPASSWORD'),
            # 'HOST': env('PGHOST'),
            'PORT': env('PGPORT'),
            'ATOMIC_REQUESTS': False,
        }
    }


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/


STATIC_URL = '/static/'

STATIC_DIRS = [
    os.path.join(BASE_DIR, 'static'),

]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [

    os.path.join(BASE_DIR, 'staticfiles'),
]


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

RESR_FRAMEWORK = {
    'DEFAULT_PERMISSiON_CLASS': [
        'rest_framework_permissions.allowAny'
    ]
}

AUTH_USER_MODEL = 'customUser.CustomUser'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')


CRON_CLASSES = [
    'app.meet.cron.VerificarMeetCronJob',
]
