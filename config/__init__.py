import logging

import os

from dotenv import load_dotenv
from fake_useragent import UserAgent

load_dotenv()
LOG_LEVEL_OUT = int(os.getenv('LOG_LEVEL_OUT')) or logging.INFO
LOG_LEVEL_FILE = int(os.getenv('LOG_LEVEL_FILE')) or logging.WARNING

LOG_FILE = str(os.getenv('LOG_FILE') or 'log_warning.log')

from config.logger import Logger

__all__ = [Logger]
