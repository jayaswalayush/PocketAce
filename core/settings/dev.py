from .base import *

DEBUG = True

DATABASES = {

    'default': {
        "ENGINE": 'django.db.backends.mysql',
        'NAME': 'loco',
        'USER': 'loco',
        'PASSWORD': 'loco',
        'PORT': '3306',
        'HOST': 'localhost'
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': "[%(asctime)s] %(threadName)s %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'logfile': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': "V:/Logs/loco.log",
            'maxBytes': 1024 * 1024 * 5,
            'formatter': 'standard',
        },
    },
    'loggers': {
        'dcs': {
            'level': 'INFO',
            'handlers': ['logfile'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['logfile'],
            'level': 'INFO',
            'propagate': False
        },
    },
    "root": {
        "level": "INFO",
        'handlers': ['logfile'],
    }
}