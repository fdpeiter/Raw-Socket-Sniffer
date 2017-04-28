import binascii


class ARP:

    def __init__(self, hex_data):
        self.opcode = binascii.hexlify(hex_data[6:8])
        src_mac_raw = binascii.hexlify(hex_data[8:14])
        src_addr_raw = binascii.hexlify(hex_data[14:18])
        dst_mac_raw = binascii.hexlify(hex_data[18:24])
        dst_addr_raw = binascii.hexlify(hex_data[24:28])
        self.dst_mac = ':'.join([dst_mac_raw[i:i+2] for i in range(0, len(dst_mac_raw), 2)])
        self.src_mac = ':'.join([src_mac_raw[i:i+2] for i in range(0, len(src_mac_raw), 2)])
        self.src_add = self.format_ip(src_addr_raw)
        self.dst_add = self.format_ip(dst_addr_raw)
        hex_data = hex_data[-14:]

    def format_ip(self, hex_addr):
        octets = [hex_addr[i:i + 2] for i in range(0, len(hex_addr), 2)]
        ip = [int(i, 16) for i in reversed(octets)]
        return '.'.join(str(i) for i in ip)

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