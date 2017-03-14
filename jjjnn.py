import socket
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip=socket.gethostname("www.google.com")
print(ip)
port=82
address=(ip,port)
print(address)
client.connect(address)
client.send("https://www.google.co.in/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8")
client.recv(1024)
