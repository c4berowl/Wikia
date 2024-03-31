import socket

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = '127.0.0.1'

port = 4444

client_socket.connect((host, port))

message = client_socket.recv(1024)

client_socket.close()

print(message.decode('ascii'))
