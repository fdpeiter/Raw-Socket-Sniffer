import socket
from ethernet import Ethernet
from arp import ARP

BUFFER_SIZE = 65535

ARP_PROTO_CODE = 0x806
IPV4_PROTO_CODE = 0x800
IPV6_PROTO_CODE = 0x86DD

def main():
    # Contadores
    total_count = arp_count = ipv4_count = ipv6_count = icmp_count = icmpv6_count = udp_count = tcp_count = 0
    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    while True:
        raw_data, addr = conn.recvfrom(BUFFER_SIZE)
        eth = Ethernet(raw_data)
        raw_data = raw_data[-14:]
        print eth

        if eth.proto == ARP_PROTO_CODE:
            arp_count += 1
            arp = ARP(raw_data)
            print arp

