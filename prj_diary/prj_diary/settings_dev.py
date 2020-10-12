from pathlib import Path
import os
from .settings_common import *

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8vq#$9nr@9)#y(h4tsu$@*^fm927@^0d$p8t926$z8u_i$*3$d'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  #ターミナルに送信