import http.client

import requests

from config import SITE_CHECK_IP
from utils.Logger import Logger
from utils.strip_scheme import strip_scheme

logger = Logger.get_logger(__name__)


def get_my_ip():
    logger.info('Use site for check ip: ' + SITE_CHECK_IP)
    conn = http.client.HTTPConnection(strip_scheme(SITE_CHECK_IP))
    conn.request("GET", "/ip")
    ip = conn.getresponse().read()
    return ip.decode('utf-8')


def get_my_ip_with_proxy(proxy):
    proxies = {
        "http": proxy,
        "https": proxy,
    }
    ext_ip = requests.get(SITE_CHECK_IP, proxies=proxies)
    return ext_ip.text


__all__ = ['get_my_ip', 'get_my_ip_with_proxy']
