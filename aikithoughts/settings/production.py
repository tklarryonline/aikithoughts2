from .base import *

DEBUG = False

# Settings for Deployment to Heroku
# https://devcenter.heroku.com/articles/getting-started-with-python
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']


# Django-libsass
# https://github.com/torchbox/django-libsass

LIBSASS_OUTPUT_STYLE = 'compressed'
