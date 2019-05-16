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
                    request = client_socket.recv(1024).decode("utf-8", errors="ignore")
                    if request:
                        self.handle_client(client_socket, request)
                    else:
                        print('[%s]客户端已经关闭' % str(client_addr))
                        client_socket.close()
                        g_socket_list.remove((client_socket, client_addr))
                except Exception as e:
                    # print(str(e))
                    pass

    def handle_client(self, socket, request):
        if not request:
            return
        request_header_lines = request.splitlines()
        for i, line in enumerate(request_header_lines):
            print(i, line)

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
            response_body = "file not found, 请输入正确的url"
            # 404表示没有这个页面
            response_headers = "HTTP/1.1 404 not found\r\n"
            response_headers += "Content-Type: text/html; charset=utf-8\r\n"
            response_headers += "Content-Length: %d\r\n" % (len(response_body))
            response_headers += "\r\n"
        else:
            # 组织 内容(body)
            response_body = f.read()
            f.close()
            # 组织相应 头信息(header)
            response_headers = "HTTP/1.1 200 OK\r\n"  # 200表示找到这个资源
            response_headers += "Content-Length: %d\r\n" % (len(response_body))
            response_headers += "\r\n"  # 用一个空的行与body进行隔开
        finally:
            # 因为头信息在组织的时候，是按照字符串组织的，不能与以二进制打开文件读取的数据合并，
            socket.send(response_headers.encode('utf-8'))
            # 再发送body
            if isinstance(response_body, str):
                print(response_body)
                socket.send((response_headers + response_body).encode("utf-8"))
            else:
                socket.send(response_headers.encode('utf-8') + response_body)


def main():
    server = WSGIServer(SERVER_ADDR)
    server.server_forever()


# 设定服务器的端口
SERVER_ADDR = (HOST, PORT) = "", 8888

DOCUMENTS_ROOT = "./html"

if __name__ == "__main__":
    main()
