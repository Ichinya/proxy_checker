import logging

from config import *

_log_format = "%(asctime)s [%(levelname)s] %(name)s - (%(filename)s).%(funcName)s(%(lineno)d): %(message)s"


class Logger:
    @staticmethod
    def get_file_handler():
        file_handler = logging.FileHandler(LOG_FILE)
        file_handler.setLevel(LOG_LEVEL_FILE)
        file_handler.setFormatter(logging.Formatter(_log_format))
        return file_handler

    @staticmethod
    def get_stream_handler():
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(LOG_LEVEL_OUT)
        stream_handler.setFormatter(logging.Formatter(_log_format))
        return stream_handler

    @staticmethod
    def get_logger(name):
        logger = logging.getLogger(name)
        logger.setLevel(LOG_LEVEL_OUT)
        logger.addHandler(Logger.get_file_handler())
        logger.addHandler(Logger.get_stream_handler())
        return logger


[__all__] = [Logger]
