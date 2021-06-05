
import socket

sock = socket.socket()
sock.connect(('194.87.94.86', 9090))
sock.send('hello, world!')

data = sock.recv(1024)
sock.close()

print (data)