"""
tcp 服务器流程
    1. socket创建一个套接字
    2. bind绑定ip和port
    3. listen使套接字变为可以被动链接
    4. accept等待客户端的链接
    5. recv/send接收发送数据
"""
import socket


def main():
    # socket创建一个套接字
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # bind绑定ip和port
    addr = ("", 8989)
    tcp.bind(addr)

    # listen使套接字变为可以被动链接
    tcp.listen(128)

    # 循环目的，调用多次accept，从而为多个客户端服务
    while True:
        # accept等待客户端的链接
        client_socket, client_addr = tcp.accept()
        print(client_addr)

        # 循环目的，为同一个客户端 服务多次
        while True:
            # 接收客户端发送的数据
            recv_data = client_socket.recv(1024)
            print(recv_data.decode("gbk"))

            # 如果recv解堵塞，那么有两种方式：客户端发送过来的数据，客户端clsoe导致
            if recv_data:
                # 回复一段数据给客户端
                 client_socket.send("服务器回复的内容 gbk".encode("gbk"))
            else:
                print(str(client_addr) + " 断开连接")
                break

        # 断开连接
        client_socket.close()

    tcp.close()


if __name__ == '__main__':
    main()
