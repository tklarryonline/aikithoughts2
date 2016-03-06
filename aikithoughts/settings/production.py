from .base import *

DEBUG = False

# Settings for Deployment to Heroku
# https://devcenter.heroku.com/articles/getting-started-with-python
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']


# Django-libsass & Django-Compressor
# https://github.com/torchbox/django-libsass
# https://django-compressor.readthedocs.org/en/latest/quickstart/

LIBSASS_OUTPUT_STYLE = 'compressed'

COMPRESS_OFFLINE = True
