import sys
from socket import *

PORT = 9000
BUFSIZE = 1000

def main(argv):
	# TO DO Your Code
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    sentence = raw_input("Input l or u")
    clientSocket.sendto(message, ('10.0.0.1', PORT))

    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print modifiedMessage

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
