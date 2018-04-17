from socket import *
skt=socket(AF_INET,SOCK_STREAM)
skt.bind(("localhost",1997))
skt.listen(1)
con,add=skt.accept()

print (add)
tmp=con.recv(1024)
con.send(tmp)
con.close()
skt.close()

