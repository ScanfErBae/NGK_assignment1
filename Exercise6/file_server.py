import sys
import socket
from lib import Lib
from socket import *
HOST = ''
PORT = 9000
BUFSIZE = 1000

def main(argv):
	# TO DO Your Code
    serverSocket = socket(AF_INET,SOCK_STREAM)
    serverSocket.bind(('', PORT))
    serverSocket.listen(1)
    print 'The server is ready to receive'
    
    while 1:
        connectionSocket, addr = serverSocket.accept()
        file = readTextTCP(connectionSocket)
        size = check_File_Exists(file)
        writeTextTCP(size, connectionSocket)
        connectionSocket.close()
    
    


def sendFile(fileName,  fileSize,  conn):
    pass
	# TO DO Your Code
    
if __name__ == "__main__":
    main(sys.argv[1:])
