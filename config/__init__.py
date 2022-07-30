import logging
import os

from dotenv import load_dotenv

# Грузим и устанавливаем первоначальные настройки
load_dotenv()

# Параметры логгера
LOG_LEVEL_OUT = int(os.getenv('LOG_LEVEL_OUT') or logging.INFO)
LOG_LEVEL_FILE = int(os.getenv('LOG_LEVEL_FILE') or logging.WARNING)
LOG_FILE = str(os.getenv('LOG_FILE') or 'log_warning.log')

# Очереди
AMQP_URL = str(os.environ['AMQP_URL'] or os.getenv('AMQP_URL') or '')

# Подключаем внутренние файлы
from config.logger import Logger

__all__ = [Logger]
