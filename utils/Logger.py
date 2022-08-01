import logging

from config import LOG_FILE, LOG_LEVEL_FILE, LOG_LEVEL_OUT

_log_format = "%(asctime)s [%(levelname)s] %(name)s - (%(filename)s).%(funcName)s(%(lineno)d): %(message)s"


class Logger:
    @staticmethod
    def get_file_handler():
        file_handler = logging.FileHandler(LOG_FILE, encoding='utf-8')
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
        log_adapter = logging.getLogger(name)
        log_adapter.setLevel(LOG_LEVEL_OUT)
        log_adapter.addHandler(Logger.get_file_handler())
        log_adapter.addHandler(Logger.get_stream_handler())
        return log_adapter


__all__ = ['Logger']
