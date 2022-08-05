import re

import requests

from config import SITE_CHECK_IP
from utils.Logger import Logger

logger = Logger.get_logger(__name__)


def get_my_ip():
    logger.info('Use site for check ip: ' + SITE_CHECK_IP)
    ext_ip = requests.get(SITE_CHECK_IP)
    return find_ip(ext_ip)


def get_my_ip_with_proxy(proxy):
    proxies = {
        "http": proxy,
        "https": proxy,
    }
    ext_ip = requests.get(SITE_CHECK_IP, proxies=proxies)
    return find_ip(ext_ip)


def find_ip(text):
    if isinstance(text, bytes):
        return text.decode('utf8')
    resp = text.text
    if len(resp) <= 15:
        return resp

    regex = r"ADDR.*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
    matches = re.findall(regex, resp)
    if len(matches[0]) <= 15:
        return matches[0]


__all__ = ['get_my_ip', 'get_my_ip_with_proxy']
