##TCPServer.py
##Dixon Styres
##secuPy

#TCPServer creates a simple client server model with threading and returns to the client
#logs, one line at a time from an input Argus Logfile

from socket import *
import sys
import multiprocessing
import time

port = 15015
fileName = ""

# Create welcoming socket using the given port
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((gethostname(), port))
serverSocket.listen(1)

print 'Listening on port', port, '...'

# While loop to handle clients making requests
def worker():
    try:
        file = open(fileName, 'r')
        print("File opened successfully, reading...")
    except:
        print("Unable to load file")
        print("Usage: python loader.py 'filepath'")
        exit()
    while 1:
        # Write output line to socket
        for x in range(0,port):
            serverSentence = file.readline().rstrip()
            connectionSocket.send(serverSentence)
            time.sleep(1)
        serverSentence = "QUIT"
        connectionSocket.send(serverSentence)
        print 'Transfer End'
        connectionSocket.close()
        break
    return

if __name__ == "__main__":
    try:
        fileName = str(sys.argv[1])
    except:
        print("Usage: python server.py 'filename'")
        exit()
    while 1:
        # Waits for some client to connect and creates new socket
        # for connection
        connectionSocket, addr = serverSocket.accept()
        print 'Client Made Connection'
        #start a new thread for the client
        p = multiprocessing.Process(target=worker)
        p.start()
