import socket
s=socket.socket()
#ip=socket.gethostname()
#print(ip)
server='127.0.0.1'
port=89
s.connect((server,port))
while (True):
 print(s.recv(1024))
s.close()
