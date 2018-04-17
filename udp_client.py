from socket import *
sk=socket(AF_INET,SOCK_DGRAM)
sk.sendto(b"hello",('localhost',1997))
print( sk.recvfrom(1024))
sk.close()