import time
import urllib.error

from checker.my_ip import get_my_ip, get_my_ip_with_proxy
from utils.Logger import Logger

logger = Logger.get_logger(__name__)

count = 0
while True:
    time.sleep(count)
    my_ip = get_my_ip()
    logger.info(f'my ip: {my_ip}')
    if my_ip:
        break
    count += 1
    if count > 100:
        logger.error('Ошибка определения ip адреса')
        raise Exception('Не удалось подключиться ни к одному серверу для проверки ip адреса')


def check_proxy(proxy):
    current_ip = get_my_ip()
    return is_work_proxy(current_ip, proxy)


def check_proxy_without_request_ip(proxy):
    return is_work_proxy(my_ip, proxy)


def check_list_proxy(list_proxy):
    current_ip = get_my_ip()
    result_work = {}
    for proxy in list_proxy:
        result_work.setdefault(proxy, is_work_proxy(current_ip, proxy))
    return result_work


def is_work_proxy(current_ip, proxy):
    logger.info(f'check proxy={proxy}')
    try:
        logger.debug(f'current ip without proxy: {current_ip}')

        ext_ip = get_my_ip_with_proxy(proxy)
        logger.debug(f'current ip with proxy: {ext_ip}')

        if current_ip == ext_ip:
            raise Exception('No proxy was used')
    except urllib.error.HTTPError as e:
        logger.error('Error code: ' + str(e.code))
        logger.info('Proxy BAD')
        return e.code
    except Exception as detail:
        logger.error("ERROR: " + str(detail))
        logger.info('Proxy BAD')
        return False
    logger.info('Proxy work')
    return True


__all__ = ['check_proxy', 'check_list_proxy', 'check_proxy_without_request_ip']
