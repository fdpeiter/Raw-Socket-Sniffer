import socket

def main():
    conn = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.ntohs(3))