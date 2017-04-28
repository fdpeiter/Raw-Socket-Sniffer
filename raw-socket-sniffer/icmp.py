import binascii
from tools import *


class ICMP:

    def __init__(self, hex_data):
        self.type = binascii.hexlify(hex_data[0:1])
        self.code = binascii.hexlify(hex_data[1:2])
        self.checksum = binascii.hexlify(hex_data[2:4])
        self.message = binascii.hexlify(hex_data[4:8])


    def __str__(self):
        answer = ("-"*45)
        answer += ("\nICMP Header")
        answer += ("\n\t|Tipo          : " + self.type)
        answer += ("\n\t|Codigo        : " + self.code)
        answer += ("\n\t|Checksum      : " + self.checksum)
        answer += ("\n\t|ICMP Message  : " + self.message)
        answer += ("-" * 45)
        return answer