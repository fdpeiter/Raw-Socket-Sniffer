import socket
from collections import Counter
from ethernet import Ethernet
from arp import ARP
from ipv4 import IPv4
from icmp import ICMP
from tcp import TCP
from udp import UDP

BUFFER_SIZE = 65535

ARP_PROTO_CODE = 0x806
IPV4_PROTO_CODE = 0x800
IPV6_PROTO_CODE = 0x86DD

def main():
    # Contadores
    total_count = arp_count = ipv4_count = ipv6_count = icmp_count = icmpv6_count = udp_count = tcp_count = 0
    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    src_ips_count = []
    dst_ips_count = []
    tcp_protocols_count = []
    udp_protocols_count = []
    while True:
        raw_data, addr = conn.recvfrom(BUFFER_SIZE)
        total_count += 1
        eth = Ethernet(raw_data)
        raw_data = raw_data[-14:]
        print(eth)
        if eth.proto == ARP_PROTO_CODE:
            arp_count += 1
            arp = ARP(raw_data)
            print(arp)
            if(arp.src_add != '0.0.0.0'):
                src_ips_count.append(arp.src_add)
            if(arp.dst_add != '0.0.0.0'):
                dst_ips_count.append(arp.dst_add)
        elif eth.proto == IPV4_PROTO_CODE:
            ipv4_count += 1
            ipv4 = IPv4(raw_data)
            print(ipv4)
            src_ips_count.append(ipv4.src_address)
            dst_ips_count.append(ipv4.dst_address)
            raw_data = raw_data[-20:]
            if ipv4.protocol == 1:
                icmp_count += 1
                icmp = ICMP(raw_data)
                print(icmp)
            if ipv4.protocol == 6:
                tcp_count += 1
                tcp = TCP(raw_data)
                print(tcp)
                tcp_protocols_count.append(tcp.src_port)
                tcp_protocols_count.append(tcp.dst_port)
            if ipv4.protocol == 17:
                udp_count += 1
                udp = UDP(raw_data)
                print(udp)
                udp_protocols_count.append(udp.src_port)
                udp_protocols_count.append(udp.dst_port)
        elif eth.proto == IPV6_PROTO_CODE:
            ipv6_count += 1
    print("ARP: {0:.0f}% IPv4: {0:.0f}% IPv6: {0:.0f}% ICMP: {0:.0f}% "
          "ICMPv6: {0:.0f}% UDP: {0:.0f}% TCP: {0:.0f}%\n".format(arp_count/total_count,ipv4_count/total_count,
                                                                ipv6_count/total_count,icmp_count/total_count,
                                                                icmpv6_count/total_count,udp_count/total_count,
                                                                tcp_count/total_count))
    src_addr_counter = Counter(src_ips_count).most_common(1)[0][0]
    dst_addr_counter = Counter(dst_ips_count).most_common(1)[0][0]
    tcp_protocols_counter = Counter(tcp_protocols_count).most_common(1)[0][0]
    udp_protocols_count = Counter(udp_protocols_count).most_common(1)[0][0]
    print("IP de Origem com mais conexoes: %s\n", src_addr_counter)
    print("IP de Destino com mais conexoes: %s\n", dst_addr_counter)
    print("TCP Protocol com mais conexoes: %s\n", tcp_protocols_counter)
    print("UDP Protocol com mais conexoes: %s\n", udp_protocols_count)

