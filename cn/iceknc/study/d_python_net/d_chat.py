import socket

def msg_send(udp):
    ip = input("请输入目标ip:")
    port = input("请输入目标端口:")
    msg = input("请输入消息:")

    addr = (str(ip), int(port))

    udp.sendto(msg.encode("utf-8"), addr)

def msg_recv(udp):
    data = udp.recvfrom(1024)
    print("%s : %s" % (str(data[1]), data[0].decode("utf-8")))

def main():
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp.bind(('', 7788))

    while True:
        # 3. 选择功能
        print("=" * 30)
        print("1:发送消息")
        print("2:接收消息")
        print("=" * 30)
        op_num = input("请输入要操作的功能序号:")

        # 4. 根据选择调用相应的函数
        if op_num == "1":
            msg_send(udp)
        elif op_num == "2":
            msg_recv(udp)
        else:
            print("输入有误，请重新输入...")

if __name__ == '__main__':
    main()




