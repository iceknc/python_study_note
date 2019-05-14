import socket
import chardet


def main():
    # 1 创建套接字
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2 获取服务器 ip port
    #dest_ip = input("请输入下载服务器ip:")
    #dest_port = int(input("请输入下载服务器port:"))

    # 3 连接服务器
    tcp.connect(("192.168.31.209", 8089))

    # 4 获取下载文件名
    #dest_file_name = input("请输入下载的文件名字:")
    dest_file_name = "download"

    # 5 将文件名发送到服务器
    tcp.send(dest_file_name.encode("utf-8"))

    # 6 接收文件数据
    recv = tcp.recv(1024)
    decode = recv.decode("gbk").encode("utf-8")
    print(chardet.detect(decode))

    # 7 保存接收到的数据
    with open("recv_" + dest_file_name, "wb") as  f:
        f.write(decode)

    # 8 关闭连接
    tcp.close()


if __name__ == '__main__':
    main()
