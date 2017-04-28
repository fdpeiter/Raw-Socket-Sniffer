import binascii
from tools import *

ports = {
    21:"ftp",
    22:"ssh",
    23:"telnet",
    25:"smtp",
    80:"http",
    443:"https"
}

class TCP:

    def __init__(self, hex_data):
        self.src_port = binascii.hexlify(hex_data[0:2])
        self.dst_port = binascii.hexlify(hex_data[2:4])

    def format_port(self, port):
        try:
            return ports[port]
        except:
            return port

    def __str__(self):
        answer = ("-"*45)
        answer += ("\nTCP Header")
        answer += ("\n\t|Porta de Origem  : " + self.format_port(self.src_port))
        answer += ("\n\t|Porta de Destino : " + self.format_port(self.dst_port))
        answer += ("-" * 45)
        return answer