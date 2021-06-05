import socket
import json

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()

print ('connected:', addr)

while True:
    data = conn.recv(102400)
    if not data:
        break

    
    conn.send(b"DATA find in hosting RQ")

conn.close()

data = data.decode()
data_json = json.load(data)

with open(f"./python-data/{data_json['name']}", "w") as python_file:
    python_file.write(data_json['data'])

print(f"OK, create mode {data_json['name']}")