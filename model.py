##Dixon Styres
##secuPy

#production model
from __future__ import division
from sklearn import neighbors
from sklearn.preprocessing import StandardScaler
import threading
import traceback
import numpy as np

class KNNModel():
    #test data, test labels, train data, train labels
    def __init__(self, trainData, trainLabel, testData, testLabel):
        #threading.Thread.__init__(self)
        self.trainData = trainData
        self.trainLabel = trainLabel
        self.testData = testData
        self.testLabel = testLabel
        self.knnModel = neighbors.KNeighborsClassifier()
        self.scaler = StandardScaler()
    def run(self):
        #standardize features using z score
        self.trainData = self.scaler.fit_transform(self.trainData)
        self.testData = self.scaler.transform(self.testData)
        #startup and fit model, default k
        self.knnModel.fit(self.trainData, self.trainLabel)
        print("Model Ready")
        sd = self.knnModel.predict(self.testData)
        acc = ((sum(sd == self.testLabel) / len(self.testLabel))*100)
        print("Accuracy of Model: %.2f" % acc+' %')
    def predict(self, log):
            try:
                log = self.scaler.transform(np.reshape(log, (1,-1)))
                type = self.knnModel.predict(log)
                return type
            except:
                traceback.print_exc()
                return [0]
