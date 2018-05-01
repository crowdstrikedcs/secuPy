##Dixon Styres
##secuPy

#production model
from __future__ import division
from sklearn import neighbors
from sklearn.preprocessing import StandardScaler
import traceback
import numpy as np

class KNNModel():
    #test data, test labels, train data, train labels
    def __init__(self, trainData, trainLabel, testData, testLabel):
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
    def predict(self, log):
            try:
                #so we can standardize a single sample.
                log = self.scaler.transform(np.reshape(log, (1,-1)))
                #predict for one sample
                type = self.knnModel.predict(log)
                return type
            except:
                return [0]
