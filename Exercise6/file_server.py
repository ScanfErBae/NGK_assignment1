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
        size = str(Lib.check_File_Exists(filename))
        sendFile(filename, size, connectionSocket)
        
    serverSocket.close()
                   

def sendFile(fileName,  fileSize,  conn):
    Lib.writeTextTCP(fileSize, conn)
    with open(fileName, "rb") as f:
        conn.send(f.read())
    conn.close()
    f.close()
    
if __name__ == "__main__":
    main(sys.argv[1:])
