# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/5/15
# @Desc  : 

import socket
import re

# 用来存储所有的新链接的socket
g_socket_list = list()

class WSGIServer(object):
    def __init__(self, server_addr):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置当服务器先close 即服务器端4次挥手之后资源能够立即释放，
        # 这样就保证了，下次运行程序时 可以立即绑定端口
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind(server_addr)
        self.server.listen(128)
        self.server.setblocking(False)

    def server_forever(self):
        while True:
            try:
                client = self.server.accept()
            except Exception as e:
                # print("静待客户端到来")
                # print(str(e))
                pass
            else:
                print("一个新的客户端到来:%s" % str(client))
                # 设置为非堵塞
                client[0].setblocking(False)
                g_socket_list.append(client)

            for client_socket, client_addr in g_socket_list:
                try:
                    recvData = client_socket.recv(1024)
                    if recvData:
                        self.handle_client(client_socket)
                    else:
                        print('[%s]客户端已经关闭' % str(client_addr))
                        client_socket.close()
                        g_socket_list.remove((client_socket, client_addr))
                except Exception as e:
                    # print(str(e))
                    pass

    def handle_client(self, socket):
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

def main():
    server = WSGIServer(SERVER_ADDR)
    server.server_forever()

# 设定服务器的端口
SERVER_ADDR = (HOST, PORT) = "", 8888

DOCUMENTS_ROOT = "./html"

if __name__ == "__main__":
    main()
