import logging.config
from logging_config import dict_config

logging.config.dictConfig(dict_config)
"""#root_logger = logging.getLogger()
#logging.basicConfig()


#module_logger = logging.getLogger('module_logger')
module_logger.propagate = False #Отключает отправления вверх по иерархии

formatter = logging.Formatter(fmt="%(levelname)s | %(name)s | %(message)s")

file_handler = logging.FileHandler('applog.log', mode='w') #mode = 'a'
file_handler.setFormatter(formatter)
module_logger.addHandler(file_handler)

custom_handler = logging.StreamHandler()
custom_handler.setFormatter(formatter)
module_logger.addHandler(custom_handler)

submodule_logger = logging.getLogger('module_logger.submodule_logger')
submodule_logger.setLevel('DEBUG')
#Handler "DEBUG | module_logger.submodule_logger | Hi there!"




#Write to file


"""
submodule_logger = logging.getLogger('module_logger.submodule_logger')
submodule_logger.setLevel('DEBUG')

def main():
    submodule_logger.debug("Hi there!")
    """print("root_logger")
    print(root_logger.handlers)
    print("submodule_logger")
    print(submodule_logger.handlers)
    print("module_logger")
    print(module_logger.handlers)

    submodule_logger.debug('Hi there!')"""


if __name__ == '__main__':
    main()
