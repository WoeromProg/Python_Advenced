from logging.handlers import TimedRotatingFileHandler
from ASCll_task7 import ASCIIFilter
from task3HandlerLevels import task3HandlerLevels
#config_JSON
dict_config = {
    "version": 1,
    "filters": {
        "ASCIIFilter": {
            "()": ASCIIFilter,
        }
    },
    "disable_existing_loggers": False,
    "formatters": {
        "base": {
            "format": "%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s"
        }
    },

    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "base",
            "stream": "ext://sys.stdout"
        },
        "file": {
            #"class": "logging.FileHandler",
            "()": task3HandlerLevels,
            "level": "DEBUG",
            "formatter": "base",
            "mode": "a"
        },
        "rotating": {
            "()": "logging.handlers.TimedRotatingFileHandler",
            "filename": 'utils.log',
            "when": "h",
            "interval": 10,
            "backupCount": 5,
            "level": "INFO",
            "filters": ['ASCIIFilter'],
            "formatter": "base"
        }
    },
    "loggers": {
        "app_Logger": {
            "level": "DEBUG",
            "handlers": ["console", "file"]
            # "propagate": False,
        },
        "utils_Logger": {
            "level": "INFO",
            "handlers": ['rotating']
        },
        "unitsFileLogger": {
                "level": "INFO",
                "handlers": ['rotating']
            },
        "httpLogger": {
                "level": "DEBUG",
                "handlers": ['http_handler']
            }
    }

    # "filters": {},
    # "root" {} # == "":{}
}
