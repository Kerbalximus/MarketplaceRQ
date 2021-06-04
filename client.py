
import socket

sock = socket.socket()
sock.connect(('46.191.225.94', 9090))
sock.send('hello, world!')

data = sock.recv(1024)
sock.close()

print (data)