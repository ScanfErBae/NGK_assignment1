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
    serverSocket.bind(('', PORT))
    print 'The server is ready to receive'
    
    while 1:
        message, clientAddress = serverSocket.recvfrom(2048)
        print message
        if message in ('u', 'U'):
            serverSocket.sendto ('/proc/uptime', ('', PORT))
            with open('/proc/uptime', "rb") as f:
                serverSocket.sendto(f.read(), ('', PORT))
            f.close()
                
                
            #filename = Lib.extractFilename('/proc/uptime')
            #size = str(Lib.check_File_Exists(filename))
            #sendFile(filename, size, serverSocket)
        if message in ('l', 'L'):
            serverSocket.sendto ('/proc/loadavg', ('', PORT))
            with open('/proc/loadavg', "rb") as f:
                serverSocket.sendto(f.read(), ('', PORT))
            f.close()
            
            #filename = Lib.extractFilename('/proc/loadavg')
            #size = str(Lib.check_File_Exists(filename))
            #sendFile1(filename, size, serverSocket)
        
    serverSocket.close()
                   

    
if __name__ == "__main__":
    main(sys.argv[1:])
