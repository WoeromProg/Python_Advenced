import getpass
import hashlib
import logging
import os
import re

logger = logging.getLogger("password_checker ")


def read_book(filename):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    BOOK_FILE = os.path.join(BASE_DIR, filename)
    with open(BOOK_FILE) as book:
        words = book.read()
        words = re.findall('[a-z]+', words, flags=re.IGNORECASE)
    return words


file = read_book('ENRUS.TXT')


def is_strong_password(password: str):
    for e in file:
        if e in password.lower() and len(e) > 3:
            return False
        return True


def input_and_check_password():
    password: str = getpass.getpass()
    if not password:
        logger.warning("Вы ввели пустой пароль.")
        return False
    try:
        hasher = hashlib.md5()
        hasher.update(password.encode("latin-1"))
        if not is_strong_password(password):
            logger.warning("Password have eng words")
        if hasher.hexdigest() == "098f6bcd4621d373cade4e832627b4f6":
            return True
    except ValueError as ex:
        logger.error("Вы ввели некорректный символ" + str(ex))
    return False


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filename='skillbox_json_messages.log',
                        format='{"time": "%(asctime)s", "level": "%(levelname)s", "message": %(message)s}',
                        datefmt='%H:%M:%S')
    logger.info("Вы пытаетесь аутентифицироваться")
    count_number: int = 3
    logger.info(f'У вас есть {count_number} попыток')
    while count_number > 0:
        if input_and_check_password():
            exit(0)
        count_number -= 1

    logger.error('Пользователь трижды ввел неправильный пароль!')
    exit(1)
