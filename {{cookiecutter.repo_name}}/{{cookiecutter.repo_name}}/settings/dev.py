from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': normpath(join(BASE_DIR, 'db.sqlite')),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    },
}

# logging
LOGGING['handlers'].update({
    'console': {
        'level': 'INFO',
        'class': 'logging.StreamHandler',
    }
}
)
LOGGING['loggers'].update({
    '': {
        'handlers': ['console'],
        'level': 'DEBUG',
        'propagate': True
    }
}
)

# debug-toolbar
INSTALLED_APPS += (
    'debug_toolbar',
)
MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)
INTERNAL_IPS = ('127.0.0.1', '10.0.2.2',)
DEBUG_TOOLBAR_CONFIG = {
    'DISABLE_PANELS': [
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ],
    'SHOW_TEMPLATE_CONTEXT': True,
}

# devserver
INSTALLED_APPS += (
    'devserver',
)
MIDDLEWARE_CLASSES += (
    'devserver.middleware.DevServerMiddleware',
)
DEVSERVER_MODULES = (
    'devserver.modules.sql.SQLRealTimeModule',
    'devserver.modules.sql.SQLSummaryModule',
    'devserver.modules.profile.ProfileSummaryModule',
    'devserver.modules.ajax.AjaxDumpModule',
    'devserver.modules.profile.MemoryUseModule',
    'devserver.modules.cache.CacheSummaryModule',
)
DEVSERVER_TRUNCATE_SQL = False
DEVSERVER_ARGS = ['--werkzeug', '--dozer']