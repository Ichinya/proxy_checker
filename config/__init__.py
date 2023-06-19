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
list_site = [
    'http://icanhazip.com',
    'http://ifconfig.me/ip',
    'http://azenv.net/',
    'http://ip-api.com/json/?fields=8217',
]


def site_check_ip():
    return random.choice(list_site)


TIMEOUT = int(os.getenv('TIMEOUT') or 3)

__all__ = ['site_check_ip', 'LOG_FILE', 'LOG_LEVEL_FILE', 'LOG_LEVEL_OUT', 'TIMEOUT']
