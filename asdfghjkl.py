import socket
s=socket.socket()
server='127.0.0.1'
port=89
s.connect((server,port))
msg=s.recv(1024)
s.close()
print(msg.decode('ascii'))
