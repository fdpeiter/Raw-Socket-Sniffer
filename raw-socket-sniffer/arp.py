import binascii
from tools import *


class ARP:

    def __init__(self, hex_data):
        self.opcode = binascii.hexlify(hex_data[6:8])
        src_mac_raw = binascii.hexlify(hex_data[8:14])
        src_addr_raw = binascii.hexlify(hex_data[14:18])
        dst_mac_raw = binascii.hexlify(hex_data[18:24])
        dst_addr_raw = binascii.hexlify(hex_data[24:28])
        self.dst_mac = format_mac(dst_mac_raw)
        self.src_mac = format_mac(src_mac_raw)
        self.src_add = format_ip(src_addr_raw)
        self.dst_add = format_ip(dst_addr_raw)


    def __str__(self):
        answer = ("-"*45)
        answer += ("\nARP Header")
        answer += ("\n\t|OPCode          : " + self.opcode)
        answer += ("\n\t|MAC de Origem   : " + self.src_mac)
        answer += ("\n\t|Addr de Origem  : " + self.src_add)
        answer += ("\n\t|MAC de Destino  : " + self.dst_mac)
        answer += ("\n\t|Addr de Destino : " + self.dst_add)
        answer += ("-" * 45)
        return answer