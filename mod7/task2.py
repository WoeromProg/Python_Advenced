import logging
import sys
from task3HandlerLevels import task3HandlerLevels

def logging_config():
    log_format = '%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s'
    formatter = logging.Formatter(log_format)
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)

    custom_file_handler = task3HandlerLevels()
    custom_file_handler.setFormatter(formatter)

    logging.basicConfig(level=logging.INFO,
                        handlers=[stream_handler, custom_file_handler])