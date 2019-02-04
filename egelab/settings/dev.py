from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'x-$pcy_dx+9)74_7v_g#sae^e)%vrg4v+jrw1^fhl+qyf!-vf1'

ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

WAGTAIL_CACHE = False

try:
    from .local_settings import *
except ImportError:
    pass
