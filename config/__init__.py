import logging
import os
import random

from dotenv import load_dotenv

# Грузим и устанавливаем первоначальные настройки
load_dotenv()

# Параметры логгера
LOG_LEVEL_OUT = int(os.getenv('LOG_LEVEL_OUT') or logging.INFO)
LOG_LEVEL_FILE = int(os.getenv('LOG_LEVEL_FILE') or logging.WARNING)
LOG_FILE = str(os.getenv('LOG_FILE') or 'log_warning.log')

# Очереди
AMQP_URL = str(os.environ['AMQP_URL'] or os.getenv('AMQP_URL') or '')

# Адрес для проверки ip. Используем несколько разных сайтов, чтобы уменьшить количество запросов на каждый
list_site = ['http://icanhazip.com', 'http://ifconfig.me/ip']
SITE_CHECK_IP = random.choice(list_site)

__all__ = ['SITE_CHECK_IP', 'LOG_FILE', 'LOG_LEVEL_FILE', 'LOG_LEVEL_OUT']
