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
    receiveFile(sentence, clientSocket)
    clientSocket.close()
    
    

    
def receiveFile(fileName,  conn):
    Lib.writeTextTCP(fileName, conn)
    filelength = int(float(Lib.readTextTCP(conn)))
    print "fil length er {}" .format(filelength)

    chunks = int((filelength//BUFSIZE)+1)
    f = open("billede.jpg", "wb")
    for i in range(0, chunks):
        content = conn.recv(BUFSIZE)
        f.write(content)
        print 'Received a package'

    print 'Done downloading'
    f.close


if __name__ == "__main__":
    main(sys.argv[1:])
