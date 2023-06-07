import logging
import string

class ASCIIFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        if isinstance(record.msg, str):
            return all(char in string.printable for char in record.msg)
        return True