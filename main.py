from checker import check_proxy
from config import Logger

logger = Logger.get_logger(__name__)


def main():
    check_proxy('socks5://72.195.114.169:4145')


if __name__ == '__main__':
    main()
