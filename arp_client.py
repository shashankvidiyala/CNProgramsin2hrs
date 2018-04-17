from socket import *
sk=socket(AF_INET,SOCK_STREAM)

sk.connect(('localhost',1997))

while True:
    ip=input("Enter ip address")
    if not ip:
        break
    sk.send(str.encode(ip))
    print(sk.recv(1024).decode())