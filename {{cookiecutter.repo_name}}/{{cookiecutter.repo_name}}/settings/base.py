# Django settings for kupler project.
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS

from os.path import abspath, dirname, join, normpath

# Absolute filesystem path to the top-level project folder
BASE_DIR = dirname(dirname(abspath(__file__)))

ADMINS = (
    ('{{cookiecutter.author_name}}', '{{cookiecutter.email}}'),
)

MANAGERS = ADMINS

# Hosts/domain names that are valid for this site; required if DEBUG is False
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Warsaw'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'pl'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

LANGUAGES = (
    ('en', 'English'),
    ('pl', 'Polski'),
)

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/{{cookiecutter.domain_name}}/media/"
MEDIA_ROOT = normpath(join(BASE_DIR, 'media'))

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://{{cookiecutter.domain_name}}/media/", "http://media.{{cookiecutter.domain_name}}.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/{{cookiecutter.domain_name}}/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://{{cookiecutter.domain_name}}/static/", "http://static.{{cookiecutter.domain_name}}/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    normpath(join(BASE_DIR, 'static')),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'compressor.finders.CompressorFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 't#+=f-led!+$5+tp-x%xoh6qi5r7g0gu$1+^w%kji^(luf8@=0'

TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.request',
)

TEMPLATE_DIRS = (
    normpath(join(BASE_DIR, 'templates')),
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'wsgi.application'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.formtools',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.humanize',

    'crispy_forms',
    'compressor',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

MIGRATION_MODULES = {
    'sites': 'contrib.sites.migrations'
}

# Mail settings
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Sluglifier
AUTOSLUG_SLUGIFY_FUNCTION = 'slugify.slugify'

# crispy-forms
CRISPY_TEMPLATE_PACK = 'bootstrap3'

# django-compressor
COMPRESS_ENABLED = True
COMPRESS_OUTPUT_DIR = 'cache'
COMPRESS_PRECOMPILERS = (
    ('text/less', 'lessc {infile} {outfile}'),
)