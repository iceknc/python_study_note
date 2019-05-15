# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/5/15
# @Desc  : 

import socket
import re

# 用来存储所有的新链接的socket
g_socket_list = list()


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置当服务器先close 即服务器端4次挥手之后资源能够立即释放，
    # 这样就保证了，下次运行程序时 可以立即绑定端口
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("", 8899))
    server.listen(128)

    # 将套接字设置为非堵塞
    # 设置为非堵塞后，如果accept时，恰巧没有客户端connect，那么accept会
    # 产生一个异常，所以需要try来进行处理
    server.setblocking(False)

    while True:
        try:
            client = server.accept()
        except Exception as e:
            print("静待客户端到来")
            print(str(e))
        else:
            print("一个新的客户端到来:%s" % str(client))
            # 设置为非堵塞
            client[0].setblocking(False)
            g_socket_list.append(client)

        for client_socket, client_addr in g_socket_list:
            try:
                recvData = client_socket.recv(1024)
                if recvData:
                    print('recv[%s]:%s' % (str(client_addr), recvData))
                else:
                    print('[%s]客户端已经关闭' % str(client_addr))
                    client_socket.close()
                    g_socket_list.remove((client_socket, client_addr))
            except Exception as e:
                print(str(e))


if __name__ == "__main__":
    main()
