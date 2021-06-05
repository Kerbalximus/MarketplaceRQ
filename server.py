import socket
import json

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()

print ('connected:', addr)


data = conn.recv(1024)


    
conn.send(b"DATA find in hosting RQ")

conn.close()

data.decode()
print(data)
data_json = json.loads(data)

with open(f"./{data_json['name']}", "a") as python_file:
    python_file.write(data_json['data'])

print(f"OK, create mode {data_json['name']}")