# -*- coding: utf-8 -*-
def format_ip(hex_value):
    octets = [hex_value[i:i + 2] for i in range(0, len(hex_value), 2)]
    ip = [int(i, 16) for i in reversed(octets)]
    return '.'.join(str(i) for i in ip)

def format_mac(hex_value):
    return ':'.join([hex_value[i:i + 2] for i in range(0, len(hex_value), 2)])