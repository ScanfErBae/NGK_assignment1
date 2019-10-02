import sys
import socket
from socket import *
from lib import Lib

HOST = ''
PORT = 9000
BUFSIZE = 1000

def main(argv):
	# TO DO Your Code
    serverSocket = socket(AF_INET,SOCK_DGRAM)
    serverSocket.bind((HOST, PORT))
    print 'The server is ready to receive'
    while 1:
        message, clientAddress = serverSocket.recvfrom(2048)
        print message
        
        if message in ('u', 'U'):
            with open('/proc/uptime', "rb") as f:
                data = f.read()
                serverSocket.sendto(data, clientAddress)
            f.close()
        if message in ('l', 'L'):
            with open('/proc/loadavg', "rb") as f:
                data = f.read()
                serverSocket.sendto(data, clientAddress)
            f.close()        
    serverSocket.close()
                   

    
if __name__ == "__main__":
    main(sys.argv[1:])
