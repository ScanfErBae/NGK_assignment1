import sys
from socket import *
from lib import Lib

PORT = 9000
BUFSIZE = 1000

def main(argv):
	# TO DO Your Code
    clientSocket = socket(socket.AF_INET, SOCK_STREAM)
    clientSocket.connect(('10.0.0.1', PORT))
    sentence = raw_input("Input lowercase sentence:")
    writeTextTCP(sentence, clientSocket)
    filelength = readTextTCP(clientSocket)
    print "fil length er, {}" .format(filelength)

    chunks = math.ceil(fileSize/BUFSIZE)
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
