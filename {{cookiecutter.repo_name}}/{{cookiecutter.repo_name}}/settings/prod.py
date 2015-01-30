from .base import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

# database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    },
}

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)

# static & media
MEDIA_URL = 'http://{{cookiecutter.domain_name}}/media/'
MEDIA_ROOT = normpath(join(BASE_DIR, '..', 'public', 'media'))
STATIC_ROOT = normpath(join(BASE_DIR, '..', 'public', 'static'))
STATIC_URL = 'http://{{cookiecutter.domain_name}}/static/'

# Mail
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_HOST_USER = 'user@{{cookiecutter.domain_name}}'
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = '587'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = '{{cookiecutter.project_name}} <noreply@{{cookiecutter.domain_name}}>'
SERVER_EMAIL = 'server@{{cookiecutter.domain_name}}'