import socket
from ethernet import Ethernet
from arp import ARP

BUFFER_SIZE = 65535

ARP_PROTO_CODE = 0x806
IPV4_PROTO_CODE = 0x800
IPV6_PROTO_CODE = 0x86DD

# Contadores
total = arp = ipv4 = ipv6 = icmp = icmpv6 = udp = tcp = 0


def main():
    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    while True:
        raw_data, addr = conn.recvfrom(BUFFER_SIZE)
        eth = Ethernet(raw_data)
        raw_data = raw_data[-14:]
        print eth

        if eth.proto == ARP_PROTO_CODE:
            arp = ARP(raw_data)
            print arp

