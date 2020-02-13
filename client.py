#192.168.5.233
import socket
from io import StringIO

#ip = input("ip: ")
pack = ('192.168.5.145',12345)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    




message = input("zadaj správu": )
max_data_len = int(input("zadaj dlžku správy: ")) 

while True:
    string_file = StringIO(message)
    if  len(message) > max_data_len:
        chunk = string_file.read(max_data_len)
        sock.sendto(chunk.encode("utf-8"),pack)
    else:
        sock.sendto(message.encode("utf-8"),pack)
        break
    if chunk <= max_data_len:
       break
        
    
    
