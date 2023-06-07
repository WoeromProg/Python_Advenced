import logging
from logging_config_task4_5 import dict_config
from logging import config
#app
logger = logging.getLogger('utils_Logger')
logging.config.dictConfig(dict_config)

logger.debug('Тест')
logger.info("Test")


def input_number():
    while True:
        try:
            number = float(input("> "))
            return number
        except ValueError:
            logger.warning('Пожалуйста, введите число: ')


def operations():
    while True:
        try:
            choice = int(input("> "))
            if choice not in [1, 2, 3, 4]:
                raise ValueError
            return choice
        except ValueError:
            logger.warning("Пожалуйста, выберите номер операции (от 1 до 4).")


def divide(x, y):
    if y == 0:
        logger.error('На ноль делить нельзя!')
        raise ZeroDivisionError("На ноль делить нельзя!")
    else:
        return x / y
