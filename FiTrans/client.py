# Libraries
import time as t
import socket as s

# Global variables
IP_FOR_TCP = 'localhost'
PORT_FOR_TCP = 9000
BUFF_SIZE = 2048

# setting for the client and printing info for user
tcp_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
tcp_socket.bind((IP_FOR_TCP, PORT_FOR_TCP))
print(f'Successful connection: {IP_FOR_TCP}:{PORT_FOR_TCP}')
print(tcp_socket.recv(1024).decode(), '\n')

# requesting files from server 
# connecting to server for file
requested_files = input('Request file: ')
tcp_socket.send(requested_files.encode())

# creates a new string called "file_received" by concatenating several other strings together.
# the two strings obtained above are concatenated together with the string "jpeg" to create the 
# final string "file_received", which likely represents the name of a new file that has been received.
file_recived = requested_files.split('.')[0]+str(t.time()).split('.')[0]+'jpeg'

# looping through the recieved file and opening it
with open(file_recived, 'wb') as file:
    print('Created File - SUCCESSFULLY')
    while True:
        recv_data = tcp_socket.recv(BUFF_SIZE)
        if (not recv_data):
            file.close()
            print(f'FILE: {file} - CLOSED')
            break
        file.write()

# printing message to user
print('FILE Downloaded - SUCCESSFULLY')
tcp_socket.close()