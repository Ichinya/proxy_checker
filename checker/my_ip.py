import http.client

import requests


def get_my_ip():
    conn = http.client.HTTPConnection("ifconfig.me")
    conn.request("GET", "/ip")
    ip = conn.getresponse().read()
    return ip.decode('utf-8')


def get_my_ip_with_proxy(proxy):
    proxies = {
        "http": proxy,
        "https": proxy,
    }
    ext_ip = requests.get('http://ifconfig.me/ip', proxies=proxies)
    return ext_ip.text


__all__ = ['get_my_ip', 'get_my_ip_with_proxy']
