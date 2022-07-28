import urllib.error

from checker.my_ip import get_my_ip, get_my_ip_with_proxy
from config import Logger

logger = Logger.get_logger(__name__)


def check_proxy(proxy):
    current_ip = get_my_ip()
    return is_work_proxy(current_ip, proxy)


def is_work_proxy(current_ip, proxy):
    logger.info(f'check proxy={proxy}')
    try:
        logger.info(f'current ip without proxy: {current_ip}')

        ext_ip = get_my_ip_with_proxy(proxy)
        logger.info(f'current ip with proxy: {ext_ip}')

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


__all__ = ['check_proxy']
