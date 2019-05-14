"""
tcp 通讯流程
    1.创建链接
    2.数据传输
    3.终止链接

tcp严格区分客户端与服务器端
"""

import socket

def main():
    #1 创建tcp套接字
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #2 连接服务器
    server_addr = ('192.168.31.209', 8089)
    tcp.connect(server_addr)

    #3 发送数据
    tcp.send("大兄弟你好 gbk".encode("gbk"))

    #4 关闭连接
    tcp.close()

if __name__ == '__main__':
    main()