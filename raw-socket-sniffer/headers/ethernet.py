import binascii


class Ethernet:

    def __init__(self, data):
        self.src_mac = self.format_mac(binascii.hexlify(data[0:6]).decode())
        self.dst_mac = self.format_mac(binascii.hexlify(data[6:12]).decode())
        self.type = binascii.hexlify(data[12:14]).decode()

    def __str__(self):
        return "Src Mac: {} ---- Dst Mac: {} ---- Type {}".format(self.src_mac, self.dst_mac, self.type)

    # Referencia: http://stackoverflow.com/questions/11006702/elegant-format-for-a-mac-address-in-python-3-2
    def format_mac(self, raw_mac):
        return ':'.join(raw_mac[i:i + 2] for i in range(0, 12, 2))