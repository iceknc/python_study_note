"""
发送的数据必须是byte
"""

import socket


def main():
    # 创建套接字
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定一个本地信息 端口一般不写
    local_addr = ('', 7788)
    udp.bind(local_addr)

    while True:
        data = input("请输入你要发送的数据:")
        if data == "exit":
            break
        udp.sendto(data.encode("utf-8"), ('192.168.31.209', 8088))
        udp.close()


if __name__ == '__main__':
    main()
