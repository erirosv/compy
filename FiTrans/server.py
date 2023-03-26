# Libraries
import socket
from threading import Thread

# Global variables
IP_FOR_TCP = 'localhost'
PORT_FOR_TCP = 9000
BUFF_SIZE = 2048

# Class ClientAccess
class ClientAccess(Thread):

    # A simple constructor which populate a few parameterser whenever the 
    # the class in initialized. Within the class are the 'Thread' class called
    # as a super class.
    def __init__(slef, ip_addr, port, socket, f_name, path=''):
        Thread.__init__(self)
        self.ip_addr = ip_addr
        self.port = port
        self.socket = socket
        self.f_name = f_name
        self.path = path

    def execute(self):
        # open file and print out the path and file-name
        file = open(f'{self.path}{self.f_name}', 'rb')

        # loop through the file until EOF
        while True:
            # reading a line within the file and then read the specific line
            line = file.read(BUFF_SIZE)
            while(line):
                self.sock.send(line)
                line = file.read(BUFF_SIZE)
            if not line:
                file.close()
                self.sock.close()
                break
        print(f'{self.ip_addr}:{self.port} [+] File Recieved: {self.f_name}')

#  *** Run the program *** 

# setting for the server
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.bind((IP_FOR_TCP, PORT_FOR_TCP))
threads = []

# show message
print('[ + ] Server Status: Ready...')
while True:
    tcp_socket.listen(3) # Experiment to get the correct setting
    
    # accepted connecntion from client to server
    (connection ,(ip_addr, port)) = tcp_socket.accept()
    # printing info to user screen
    print(f'Successful connection: {ip_addr}:{port}')
    print(f'File requested: {ip_addr}:{port} ', end='')

    # Sending the files (in byte foramt)
    connection.send(b'Options: ')
    request_client_file_name = connection.recv(1024).decode()
    print(request_client_file_name)

    # create new client on a new thread by calling the class
    thread = ClientAccess(ip_addr, port, connection, filename=request_client_file_name, path='images/')
    thread.start()
    thread.append(thread)

# This part does remove the thread when it has completed its task
for thread in threads:
    thread.join()
