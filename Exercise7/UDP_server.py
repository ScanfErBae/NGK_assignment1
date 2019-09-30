import sys
import socket
from lib import Lib
from socket import *

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
        if message == ('u'or 'U')
            filename = Lib.extractFilename('/proc/uptime')
            size = str(Lib.check_File_Exists(filename))
            sendFile(filename, size, serverSocket)
        else if message == ('l' or 'L')
            filename = Lib.extractFilename('/proc/loadavg')
            size = str(Lib.check_File_Exists(filename))
            sendFile(filename, size, serverSocket)
        else 
            break
        
    serverSocket.close()
                   

def sendFile(fileName,  fileSize,  conn):
    Lib.writeTextTCP(fileSize, conn)
    with open(fileName, "rb") as f:
        conn.send(f.read())
    conn.close()
    f.close()
    
if __name__ == "__main__":
    main(sys.argv[1:])
