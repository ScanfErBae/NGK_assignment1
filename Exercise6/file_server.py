import sys
import socket
from lib import Lib
from socket import *
import math

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
        file = Lib.readTextTCP(connectionSocket)
        filename = Lib.extractFilename(file)
        #f = open(filename, "rb")
        size = str(Lib.check_File_Exists(filename))
        Lib.writeTextTCP(size, connectionSocket)
        filesize = int(size)
        chunks = int(math.ceil(filesize/BUFSIZE))
        with open(filename, 'rb') as f:
            dataToSend = str(f.read(BUFSIZE))
            Lib.writeTextTCP(dataToSend, connectionSocket)
        #for i in range (0, chunks):
           # dataToSend = unicode(f.read(BUFSIZE), "UTF-8")
         #   Lib.writeTextTCP(dataToSend, connectionSocket)
        connectionSocket.close()
        f.close()
    serverSocket.close()
                   

def sendFile(fileName,  fileSize,  conn):
    pass
	# TO DO Your Code
    
if __name__ == "__main__":
    main(sys.argv[1:])
