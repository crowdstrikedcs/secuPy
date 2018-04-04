##Dixon Styres
##secuPy

#Load in data, train model, listen for traffic and classify it.

import loader
import model
from socket import *

class TCPListen():
    def __init__(self, trainData, trainLabel, testData, testLabel,l1):
        self.m1 = model.KNNModel(trainData, trainLabel, testData, testLabel)
        self.l1 = l1
        self.m1.run()
        self.hostname = "student.cs.appstate.edu"
        self.port = 15015
    def listen(self):
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((self.hostname, self.port))

        #Input loop
        while 1:
            # Read line from server
            log = clientSocket.recv(1024)
            print 'FROM SERVER:', log
            #send sentence to classifier
            log = self.l1.format(log)
            type = self.m1.predict(log)
            print(type)
            #Check if we are done
            if(log == 'QUIT'):
                print "Connection Terminated"
                break

        # Close the socket
        clientSocket.close()

if __name__ == "__main__":
    l1 = loader.Loader("flowdata.binetflow")
    data = l1.load()
    trainData = data[0]
    trainLabel = data[1]
    testData = data[2]
    testLabel = data[3]
    listener = TCPListen(trainData, trainLabel, testData, testLabel,l1)
    listener.listen()
