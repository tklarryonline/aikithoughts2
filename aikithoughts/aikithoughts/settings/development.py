from .base import *

DEBUG = True

ALLOWED_HOSTS = []


# Configures Whitenoise to serve Sass
# http://whitenoise.evans.io/en/latest/django.html

WHITENOISE_USE_FINDERS = True
WHITENOISE_AUTOREFRESH = True
