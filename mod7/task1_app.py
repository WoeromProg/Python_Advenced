import logging
#app
from task1_utils import *
from logging_config_task4_5 import dict_config
from logging import config

logging.config.dictConfig(dict_config)
logger = logging.getLogger('app_Logger')


def calc():
    logger.info("Введите два числа:")
    num1, num2 = input_number(), input_number()
    logger.debug("Ввели два числа")

    logger.info("Выберите операцию: 1 = Сложение, 2 = Вычитание, 3 = Умножение, 4 = Деление")
    operation = operations()

    if operation == 1:
        result = num1 + num2
    if operation == 2:
        result = num1 - num2
    if operation == 3:
        result = num1 * num2
    if operation == 4:
        result = divide(num1, num2)

    logger.debug('Подсчет закончен')

    logger.info(f'Результат: {result}')


if __name__ == '__main__':

    calc()
