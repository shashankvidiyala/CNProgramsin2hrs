from socket import *
sk=socket(AF_INET,SOCK_DGRAM)
sk.bind(('localhost',1997))
data,addr=sk.recvfrom(1024)
print (addr)
print(data)
sk.sendto(data,addr)
sk.close()
