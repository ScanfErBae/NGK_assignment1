import sys
from socket import *

PORT = 9000
BUFSIZE = 1000

def main(argv):
	# TO DO Your Code
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    while 1:
            
        sentence = raw_input("Input l or u:")
        clientSocket.sendto(sentence, ('10.0.0.1', PORT))
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        print modifiedMessage

    clientSocket.close()

if __name__ == "__main__":
    main(sys.argv[1:])
