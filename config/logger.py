import logging

_log_format = "%(asctime)s [%(levelname)s] %(filename)s:%(name)s.%(funcName)s(%(lineno)d): %(message)s"


class Logger:
    @staticmethod
    def get_file_handler():
        file_handler = logging.FileHandler("log_warning.log")
        file_handler.setLevel(logging.WARNING)
        file_handler.setFormatter(logging.Formatter(_log_format))
        return file_handler

    @staticmethod
    def get_stream_handler():
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        stream_handler.setFormatter(logging.Formatter(_log_format))
        return stream_handler

    @staticmethod
    def get_logger(name):
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)
        logger.addHandler(Logger.get_file_handler())
        logger.addHandler(Logger.get_stream_handler())
        return logger


[__all__] = [Logger]
