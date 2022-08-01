import argparse
import json
from enum import Enum

from checker import check_proxy, check_list_proxy
from mq import run_mq
from utils.Logger import Logger

logger = Logger.get_logger(__name__)


class RunMod(Enum):
    MQ = 'mq'
    FILE = 'file'
    LIST = 'list'
    PROXY = 'proxy'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Параметры запуска")
    parser.add_argument("--action", "-a", type=RunMod, choices=RunMod, default=RunMod.PROXY,
                        help='''
                        Режимы: 
                        mq - подключение к MQ, 
                        list - проверяет из списка переданных, 
                        proxy - проверка только одного прокси, 
                        file - проверка файла
                        ''')
    parser.add_argument("--list", '-l', help='Список через запятую')
    parser.add_argument("proxy", type=str, help='Прокси который нужно проверить в режиме proxy', nargs='?', default='')

    args = parser.parse_args()
    # print(args)
    # exit()
    if args.action == RunMod.PROXY:
        is_good_proxy = check_proxy(args.proxy)
        result = {'result': is_good_proxy, 'proxy': args.proxy}
        print(json.dumps(result))
        exit()
    if args.action == RunMod.LIST:
        print(json.dumps(check_list_proxy(args.list.split(','))))
        exit()
    if args.action == RunMod.MQ:
        run_mq()
        exit()
