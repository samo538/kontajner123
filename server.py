import socket

addr = ('0.0.0.0', 12345)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(addr)

while True:
    client_add = sock.recvfrom(1518)
    message = client_add[0]
    client = client_add[1]
    print(message)
    print(client)












sock.close()
