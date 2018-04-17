from socket import *

sk=socket(AF_INET,SOCK_STREAM)
addr="localhost"
port=1997
sk.connect((addr,port))
sk.send(b"Hi")
print(sk.recv(1024))
sk.close()