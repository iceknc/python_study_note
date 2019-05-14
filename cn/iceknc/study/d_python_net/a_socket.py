"""
linux 查看ip   ipconfig
window查看ip   ipconfig/all

socket
    import socket
    socket.socket(AddressFamily, Type)
        Address Family：可以选择 AF_INET（用于 Internet 进程间通信）
        或者 AF_UNIX（用于同一台机器进程间通信）,实际工作中常用AF_INET
        Type：套接字类型，可以是 SOCK_STREAM（流式套接字，主要用于 TCP 协议）
        或者 SOCK_DGRAM（数据报套接字，主要用于 UDP 协议）

    tcp套接字 socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    udp套接字 socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
"""
import socket

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tcp.close()
udp.close()