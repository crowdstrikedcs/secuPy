##Dixon Styres
##secuPy

#running model

import sklearn

class KNNModel(threading.Thread):
    #test data, test labels, train data, train labels
    def __init__(self, trainData, trainLabel, testData, testLabel):
        threading.Thread.__init__(self)
        self.trainData = trainData
        self.trainLabel = trainLabel
        self.testData = testData
        self.testLabel = testLabel

    def run(self):
        #standardize features using z score
        trainData = sklearn.preprocessing.scale(trainData)
        testData = sklearn.preprocessing.scale(testData)
        #startup and fit model, default k
        knnModel = KNeighborsClassifier()
        knnModel.fit(X, Y)
        #predict test data
        sd = knnModel.predict(XT)
        #calcuate accuracy
        #where predicted = actual / total test traffic
        acc = (sum(sd == YT) / len(YT) * 100)
        print("Accuracy of KNN Model: %.2f" % acc+' %')
        print('=' * 100)
