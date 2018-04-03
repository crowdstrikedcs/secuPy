##Dixon Styres
##secuPy

#production model
from __future__ import division
from sklearn import neighbors
from sklearn import preprocessing
import threading

class KNNModel():
    #test data, test labels, train data, train labels
    def __init__(self, trainData, trainLabel, testData, testLabel):
        #threading.Thread.__init__(self)
        self.trainData = trainData
        self.trainLabel = trainLabel
        self.testData = testData
        self.testLabel = testLabel
        self.knnModel = neighbors.KNeighborsClassifier()

    def run(self):
        #standardize features using z score
        self.trainData = preprocessing.scale(self.trainData)
        self.testData = preprocessing.scale(self.testData)

        #startup and fit model, default k
        self.knnModel.fit(self.trainData, self.trainLabel)
        print("Model Ready")

        #sd = self.knnModel.predict(self.testData)
        #acc = ((sum(sd == self.testLabel) / len(self.testLabel))*100)
        #print("Accuracy of Model: %.2f" % acc+' %')
