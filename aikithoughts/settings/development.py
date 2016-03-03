from .base import *

DEBUG = True

ALLOWED_HOSTS = []


# Django Sass Processor
# https://github.com/jrief/django-sass-processor

# Sets coding style of compiled result
SASS_OUTPUT_STYLE = 'nested'


# Configures Whitenoise to serve Sass
# http://whitenoise.evans.io/en/latest/django.html

WHITENOISE_USE_FINDERS = True
WHITENOISE_AUTOREFRESH = True
