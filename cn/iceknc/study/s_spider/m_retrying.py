# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/7/24
# @Desc  : 
import requests
from retrying import retry


@retry(stop_max_attempt_number=3)
def _parse_url(url, method, headers, data, proxies):
    print("-" * 10)
    if method == "POST":
        response = requests.post(url, headers=headers, data=data, proxies=proxies)
    else:
        response = requests.get(url, headers=headers, data=data, proxies=proxies)
    assert response.status_code == 200
    return response.content.decode()


def parse_url(url, method="GET", headers={}, data=None, proxies={}):
    try:
        html_str = _parse_url(url, method, headers, data, proxies)
    except:
        html_str = None
    return html_str


def main():
    url = parse_url("www.baidu.com")
    print(url)


if __name__ == "__main__":
    main()
