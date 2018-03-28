##Dixon Styres
##secuPy

#train and test our models
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
        for i in range(8):
            self.trainData[:, i] = (self.trainData[:, i] - self.trainData[:, i].mean()) / (self.trainData[:, i].std())
        for i in range(8):
            self.testData[:, i] = (self.testData[:, i] - self.testData[:, i].mean()) / (self.testData[:, i].std())
        knnModel = KNeighborsClassifier()
        knnModel.fit(X, Y)
        sd = knnModel.predict(XT)
        print(YT)
        acc = (sum(sd == YT) / len(YT) * 100)
        print("Accuracy of KNN Model: %.2f" % acc+' %')
        print('=' * 100)
