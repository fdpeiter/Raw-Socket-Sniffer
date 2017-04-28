import binascii


class Ethernet:

    def __init__(self, hex_data):
        dst_mac_raw = binascii.hexlify(hex_data[0:6])
        src_mac_raw = binascii.hexlify(hex_data[6:12])
        self.dst_mac = ':'.join([dst_mac_raw[i:i+2] for i in range(0, len(dst_mac_raw), 2)])
        self.src_mac = ':'.join([src_mac_raw[i:i+2] for i in range(0, len(src_mac_raw), 2)])
        self.proto = '0x' + binascii.hexlify(hex_data[12:13]).upper()

    def __str__(self):
        answer = ("-"*45)
        answer += ("\nEthernet Header")
        answer += ("\n\t|MAC de Origem  : " + self.src_mac)
        answer += ("\n\t|MAC de Destino : " + self.dst_mac)
        answer += ("\n\t|Protocolo      : " + self.proto)
        answer += ("-" * 45)
        return answer