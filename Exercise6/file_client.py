import sys
from socket import *
from lib import Lib
import math

PORT = 9000
BUFSIZE = 1000

def main(argv):
	# TO DO Your Code
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect(('10.0.0.1', PORT))
    sentence = raw_input("Input lowercase sentence:")
    Lib.writeTextTCP(sentence, clientSocket)
    filelength = Lib.readTextTCP(clientSocket)
    print "fil length er, {}" .format(filelength)

    chunks = math.ceil(filelength/BUFSIZE)
    for i in range(chunks):
        content = clientSocket.recv(BUFSIZE)
        
        container.write(content)
        print 'Received a package'

    print 'Done downloading'
    container.close
    clientSocket.close()
    
    

    
def receiveFile(fileName,  conn):
    pass
	# TO DO Your Code


if __name__ == "__main__":
    main(sys.argv[1:])
