import socket
def main():
    host="127.0.0.1"
    port=83
    server=('127.0.0.1',82)
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((host,port))
    message="hello"
    while message !='q':
        s.sendto(message,server)
        data,addr=s.recvfrom(1024)
        print("recevied from server"+str(data))
        message=input('->')
    s.close()
if __name__=="__main__":
    main()
    
                      
    
