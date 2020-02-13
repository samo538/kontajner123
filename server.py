import socket

addr = ('0.0.0.0', 12345)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(addr)

sock.recv(1518)
















sock.close()