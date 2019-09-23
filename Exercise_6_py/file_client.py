import sys
import math
from socket import *
from lib import Lib

PORT = 9000
BUFSIZE = 1000

def main(argv):
	clientSocket = socket(socket.AF_INET, SOCK_STREAM)
    clientSocket.connect((10.0.0.1, PORT))
    sentence = raw_input('Input lowercase sentece:')
    clientSocket.send(sentence)
    fileSize = clientSocket.recv(1000)
    container = open('image.jpeg', 'wb')
    print 'Sending'
    
    
    chunks = math.ceil(fileSize/1000)
    for i in range(0,chunks)
        content = clientSocket.recv(1000)
        container.write(content)
        print 'Received a package'

   print 'Done downloading'
   container.close
   clientSocket.close()
    
    
    
def receiveFile(fileName,  conn):
	# TO DO Your Code

if __name__ == "__main__":
   main(sys.argv[1:])

