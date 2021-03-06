from settings import *

ENVIRONMENT = 'PROD'

ALLOWED_HOSTS = [
    '{{ project_name }}.herokuapp.com',
]

DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}

STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_STORAGE_BUCKET_NAME = '{{ project_name }}'
AWS_S3_FILE_OVERWRITE = True
AWS_QUERYSTRING_AUTH = False
AWS_HEADERS = {
    'Cache-Control': 'public, max-age=%s' % (30 * 24 * 60 * 60),
}
COMPRESS_STORAGE = STATICFILES_STORAGE

STATIC_URL = 'https://s3.amazonaws.com/{{ project_name }}/'
MEDIA_URL = 'https://s3.amazonaws.com/{{ project_name }}/'

# AWS Information
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
