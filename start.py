##Dixon Styres
##secuPy

#Load in data, train model, listen for traffic and classify it.

import loader
import model

class TCPListen():
    def __init__(self, trainData, trainLabel, testData, testLabel):
        m1 = model.KNNModel(trainData, trainLabel, testData, testLabel)
        m1.run()

if __name__ == "__main__":
    l1 = loader.Loader("flowdata.binetflow")
    data = l1.load()
    trainData = data[0]
    trainLabel = data[1]
    testData = data[2]
    testLabel = data[3]
    TCPListen(trainData, trainLabel, testData, testLabel)
