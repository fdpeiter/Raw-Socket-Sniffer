import binascii


class IPv4:

    def __init__(self, hex_data):
        self.identification = binascii.hexlify(hex_data[4:6])
        self.ttl = binascii.hexlify(hex_data[6:7])
        self.protocol = binascii.hexlify(hex_data[7:8])
        self.src_address = format_ip(hex_data[12:16])
        self.dst_address = format_ip(hex_data[16:20])

    def __str__(self):
        answer = ("-" * 45)
        answer += ("\nIPv4 Header")
        answer += ("\n\t|Identification  : " + self.identification)
        answer += ("\n\t|TTL             : " + self.ttl)
        answer += ("\n\t|Protocolo       : " + self.protocol)
        answer += ("\n\t|Addr de Origem  : " + self.src_address)
        answer += ("\n\t|Addr de Destino : " + self.dst_address)
        answer += ("-" * 45)
        return answer