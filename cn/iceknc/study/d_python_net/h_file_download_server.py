import socket


def main():
    # socket创建一个套接字
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # bind绑定ip和port
    addr = ("", 8989)
    tcp.bind(addr)

    # listen使套接字变为可以被动链接
    tcp.listen(128)

    while True:
        # accept等待客户端的链接
        client_socket, client_addr = tcp.accept()
        print(client_addr)

        # 接收客户端发送的数据
        recv_data = client_socket.recv(1024)
        print(recv_data.decode("gbk"))

        file_content = None
        try:
            f = open("./recv_download", "rb")
            file_content = f.read()
            f.close()
        except Exception as ret:
            print(ret)

        if file_content:
            client_socket.send(file_content.decode("utf-8").encode("gbk"))

        # 断开连接
        client_socket.close()

    tcp.close()


if __name__ == '__main__':
    main()
