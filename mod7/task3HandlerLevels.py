import logging

class task3HandlerLevels(logging.Handler):
    def __int__(self, mode='w'):
        super().__init__()
        self.mode = mode

    def emit(self, record: logging.LogRecord) -> None:
        message = self.format(record)
        with open(f'logs/app_{record.levelname}.log', mode=self.mode) as f:
            f.write(message + '\n')
