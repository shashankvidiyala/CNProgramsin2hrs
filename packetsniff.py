from socket import *
from struct import *

skt=socket(AF_INET,SOCK_RAW,IPPROTO_TCP)

while True:
    packet=skt.recvfrom(65565)
    packet=packet[0]
    ip_header=packet[0:20]
    iph=unpack("!BBHHHBBH4s4s",ip_header)
    version_ihl=iph[0]
    version=version_ihl>>4
    ihl=version_ihl&0xF
    iph_length=ihl*4
    ttl=iph[5]
    protocol=iph[6]
    src_add=iph[8]
    dest_add=iph[9]
    print(ttl,protocol,src_add,dest_add)
    tcp_header=packet[iph_length:iph_length+20]
    tcph=unpack("!HHLLBBHHH",tcp_header)
    src_port=tcp[0]
    dst_port=tcp[1]
    seq=tcp[2]
    ack=tcp[3]
    reser=tcp[4]
    tcp_header_length=reser>>4
    print(src_port,dst_port,ack,reser)
    h_size=iph_length+tcp_header_length*4
    print(packet[h_size:])

