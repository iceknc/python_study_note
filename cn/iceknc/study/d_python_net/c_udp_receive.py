import socket


def main():
    # 创建套接字
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定一个本地信息 端口一般不写
    local_addr = ('', 7788)
    udp.bind(local_addr)
    while True:
        # 接收数据
        recv_data = udp.recvfrom(1024)
        # recv_data这个变量存储的是一个元组(接受到的数据，(发送方的ip, port))
        recv_msg = recv_data[0]
        recv_addr = recv_data[1]
        print("%s : %s" % (str(recv_addr), recv_msg.decode("gbk")))
        if recv_msg.decode("gbk") == "exit":
            print("接收到退出指令")
            break
    udp.close()


if __name__ == '__main__':
    main()
