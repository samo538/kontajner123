#192.168.5.233
import socket
pack = ('192.168.5.145',12345)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)





sock.sendto("hello".encode("utf-8"),pack)


