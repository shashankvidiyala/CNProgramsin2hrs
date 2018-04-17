from socket import *
arpdct={"192.168.2.1":"ec-1a-59-16-be-7d","224.0.0.252":"01-00-5e-00-00-16"}
skt=socket(AF_INET,SOCK_STREAM)
skt.bind(("localhost",1997))
skt.listen(5)
while True:
    con,addr =skt.accept()
    tmp=con.recv(1024)
    print(tmp)
    if not tmp:
        con.close()
        break
    tmp=str(tmp.decode()).strip()
    print(tmp)
    if tmp in arpdct:
        con.send(str.encode(arpdct[tmp]))
    else:
        con.send(b"Not Found")
    con.close()
skt.close()

