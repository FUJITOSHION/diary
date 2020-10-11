from pathlib import Path
import os
from django.contrib.messages import constants as messages

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8vq#$9nr@9)#y(h4tsu$@*^fm927@^0d$p8t926$z8u_i$*3$d'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app_diary.apps.AppDiaryConfig',
    'accounts.apps.AccountsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'prj_diary.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'prj_diary.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'private_diary',
        'USER': os.environ.get('DB_USER'),
        'PASSWARD': os.environ.get('DB_PASSWARD'),
        'HOST':'',
        'PORT':'',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS =(
    os.path.join(BASE_DIR, 'static'),
)
# # ロギング設定
# LOGGING = {
#     'version':1,
#     'disable_existing_loggers':False,
    
#     'loggers':{
#         'django':{
#             'handlers':['console'],
#             'level':'INFO',
#         },
#         'diary':{
#             'handlers':['console'],
#             'level':'DEBUG',
#         },
#     },
#     # ハンドラの設定
#     'handlers':{
#         'console':{
#             'level':'DEBUG',
#             'class':'logging.StreamHandler',
#             'formatter':'dev'
#         },
#     },

#     #　フォーマッタの設定
#     'formatters':{
#         'dev':{
#             'format':'\t'.join([
#                 '%(asctime)s',
#                 '[%(levelname)s]',
#                 '%(pathname)s(Line:%(lineno)d)',
#                 '%s(message)s'
#             ])
#         },
#     }
# }

MESSAGE_TAGS = {
    messages.ERROR:'alert alert-danger',
    messages.WARNING:'alert alert-warning',
    messages.SUCCESS:'alert alert-success',
    messages.INFO:'alert alert-info',
}