import socket

hostName='localhost'
port=8080

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((hostName,port))

msg = s.recv(1024)

while msg:
    print('Received: ' + msg.decode())
    msg = s.recv(1024)