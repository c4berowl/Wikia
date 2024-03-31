import socket

# Creating the socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Host
host = '127.0.0.1'
port = 4444

# Biding to socket
server_socket.bind((host, port))

# Starting TCP listener

server_socket.listen(5)

while True:
	# Starting the connection
    client_socket, address = server_socket.accept()
    print(f"Connection received from {str(address)}")

    message = 'Thank you for connecting to the server' + "\r\n"

    client_socket.send(message.encode('ascii'))

    client_socket.close()
