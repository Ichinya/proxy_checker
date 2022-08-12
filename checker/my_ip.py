import ipaddress
import json
import re

import requests
from FakeAgent import Fake_Agent
from config import SITE_CHECK_IP, TIMEOUT
from utils.Logger import Logger

fa = Fake_Agent()

logger = Logger.get_logger(__name__)


def headers():  # Socket headers send metod...

    return {
        "Host": "httpbin.org",
        "User-Agent": fa.random().strip(),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Cache-Control": "max-age=0",
    }


def get_my_ip():
    logger.info('Use site for check ip: ' + SITE_CHECK_IP)
    s = requests.Session()
    ext_ip = s.get(SITE_CHECK_IP, timeout=TIMEOUT, headers=headers())
    return find_ip(ext_ip)


def get_my_ip_with_proxy(proxy):
    proxies = {
        "http": proxy,
        "https": proxy,
    }
    s = requests.Session()
    ext_ip = s.get(SITE_CHECK_IP, proxies=proxies, timeout=TIMEOUT, headers=headers())
    return find_ip(ext_ip)


def find_ip(text):
    if isinstance(text, bytes):
        return text.decode('utf8')
    resp = text.text
    try:
        if ipaddress.ip_address(resp):
            return resp
    except Exception as ex:
        logger.debug(str(ex))

    try:
        resp_dict = json.loads(resp)
        ip = resp_dict.get('query')
        if ipaddress.ip_address(ip):
            return ip
    except Exception as ex:
        logger.debug(str(ex))

    regex = r"ADDR.*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
    matches = re.findall(regex, resp)
    try:
        if ipaddress.ip_address(matches[0]):
            return matches[0]
    except Exception as ex:
        logger.debug(str(ex))


__all__ = ['get_my_ip', 'get_my_ip_with_proxy']
