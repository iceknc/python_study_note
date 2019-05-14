# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/5/14
# @Desc  : 

from gevent import monkey
import gevent
import urllib.request

monkey.patch_all()


def download(url):
    print("Get --> %s" % url)
    resp = urllib.request.urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data), url))


def main():
    gevent.joinall([
        gevent.spawn(download,"https://www.baidu.com"),
        gevent.spawn(download,"https://www.qq.com"),
        gevent.spawn(download,"https://www.taobao.com"),
        gevent.spawn(download,"https://www.jd.com"),
    ])


if __name__ == "__main__":
    main()
