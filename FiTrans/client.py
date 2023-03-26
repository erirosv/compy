# Libraries
import socket

# Global variables
IP_FOR_TCP = 'localhost'
PORT_FOR_TCP = 9000
BUFF_SIZE = 2048

# setting for the client and printing info for user
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.bind((IP_FOR_TCP, PORT_FOR_TCP))
print(f'Successful connection: {IP_FOR_TCP}:{PORT_FOR_TCP}')
print(tcp_socket.recv(1024).decode(), '\n')

