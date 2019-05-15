# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/5/15
# @Desc  : 

import socket
import re


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置当服务器先close 即服务器端4次挥手之后资源能够立即释放，
    # 这样就保证了，下次运行程序时 可以立即绑定端口
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("", 8899))
    server.listen(128)
    while True:
        client_socket, client_addr = server.accept()
        handle_client(client_socket)


def handle_client(socket):
    recv_data = socket.recv(1024).decode("utf-8", errors="ignore")
    if not recv_data:
        return
    request_header_lines = recv_data.splitlines()
    for line in request_header_lines:
        print(line)

    http_request_line = request_header_lines[0]
    get_file_name = re.match("[^/]+(/[^ ]*)", http_request_line).group(1)
    print("file name is %s" % get_file_name)

    # 如果没有指定访问哪个页面。例如index.html
    # GET / HTTP/1.1
    if get_file_name == "/":
        get_file_name = DOCUMENTS_ROOT + "/index.html"
    else:
        get_file_name = DOCUMENTS_ROOT + get_file_name

    try:
        f = open(get_file_name, "rb")
    except IOError:
        # 404表示没有这个页面
        response_headers = "HTTP/1.1 404 not found\r\n"
        response_headers += "\r\n"
        response_body = "====sorry ,file not found===="
    else:
        # 组织相应 头信息(header)
        response_headers = "HTTP/1.1 200 OK\r\n"  # 200表示找到这个资源
        response_headers += "\r\n"  # 用一个空的行与body进行隔开
        # 组织 内容(body)
        response_body = f.read()
    finally:
        # 因为头信息在组织的时候，是按照字符串组织的，不能与以二进制打开文件读取的数据合并，因此分开发送
        # 先发送response的头信息
        socket.send(response_headers.encode('utf-8'))
        # 再发送body
        if isinstance(response_body, str):
            print(response_body)
            socket.send(response_body.encode("utf-8"))
        else:
            socket.send(response_body)
        socket.close()


DOCUMENTS_ROOT = "./html"

if __name__ == "__main__":
    main()
