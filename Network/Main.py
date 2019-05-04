import socket, sys
import struct

host = socket.gethostbyname(socket.gethostname())
port = 80
conn = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
conn.bind(('localhost', 0))
buffer = 2**16

while True:
    packet = conn.recvfrom(buffer)
    ipHeader = packet[0:20]
    iph = struct.unpack("!BBHHHBBH4s4s", ipHeader)

    version_ihl = iph[0]
    version = version_ihl
    ihl = version_ihl

    ttl = iph[5]
    protocol = iph[6]
    s_addr = socket.inet_ntoa(iph[8]);
    d_addr = socket.inet_ntoa(iph[9]);

    print('Version : ' + str(version) + ' IP Header Length : ' + str(ihl) + ' TTL : ' + str(ttl) + ' Protocol : ' + str(
        protocol) + ' Source Address : ' + str(s_addr) + ' Destination Address : ' + str(d_addr))







print('Done')