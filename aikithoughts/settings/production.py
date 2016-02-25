from aikithoughts.settings import *

DEBUG = False

# Settings for Deployment to Heroku
# https://devcenter.heroku.com/articles/getting-started-with-python
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']
