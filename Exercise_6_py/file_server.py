import sys
import socket
import os
import math
from lib import Lib


HOST = ''
PORT = 9000
BUFSIZE = 1000

def main(argv):
	serverSocket = socket(AF_INET,SOCK_STREAM)
    serverSocket.bind((HOST,PORT))
    serverSocket.listen(1)
    print 'The server is ready to receive'
    while 1:
        connectionSocket, addr = serverSocket.accept()
        sentence = conectionSocket.recv(1000)
        statinfo = os.stat(sentence)
        fileSize = statinfo.st_size
        connectionSocket.send(fileSize)
        sendFile(sentence, fileSize, connectionSocket)
        connectionSocket.close()

def sendFile(fileName,  fileSize,  conn):
	# TO DO Your Code
    f = open(fileName, 'rb')
    
    connectionSocket.send(f)
    chunks = math.ceil(fileSize/1000)
    for i in range(0,chunks)
        content = clientSocket.recv(1000)
        container.write(content)
        print 'Received a package'

    
    
if __name__ == "__main__":
   main(sys.argv[1:])
