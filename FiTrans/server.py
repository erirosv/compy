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
        # open file and read folder
        file = open(f'{self.path}{self.f_name}', 'rb')

        # loop through the file until the 

# Run the program