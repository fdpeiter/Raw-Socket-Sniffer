import socket
from headers.ethernet import Ethernet

def main():
    conn = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
    while True:
        raw_data, addr = conn.recvfrom(65535)
        ethernet_header = Ethernet(raw_data[:14])
        print(ethernet_header)

if __name__ == "__main__":
    exit(main())
