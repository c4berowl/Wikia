# Simple python script to check open ports

import socket

socket_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket_s.settimeout(5)

host = input("Please enter the IP you want to scan: ")
port = int(input("Please enter the port you want to scan: "))

def portScanner(port):
    if socket_s.connect_ex((host, port)):
        print("The port is closed")
    else:
        print("The port is open")

portScanner(port)
