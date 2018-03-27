##Dixon Styres
##secuPy

#train and test our models

import sklearn

class KNNModel(threading.Thread):
    """Threaded K Nearest Neighbours Model"""
    def __init__(self, X, Y, XT, YT, accLabel=None):
        threading.Thread.__init__(self)
        self.X = X
        self.Y = Y
        self.XT=XT
        self.YT=YT
        self.accLabel= accLabel

    def run(self):
        X = np.zeros(self.X.shape)
        Y = np.zeros(self.Y.shape)
        XT = np.zeros(self.XT.shape)
        YT = np.zeros(self.YT.shape)
        np.copyto(X, self.X)
        np.copyto(Y, self.Y)
        np.copyto(XT, self.XT)
        np.copyto(YT, self.YT)
        for i in range(8):
            X[:, i] = (X[:, i] - X[:, i].mean()) / (X[:, i].std())
        for i in range(8):
            XT[:, i] = (XT[:, i] - XT[:, i].mean()) / (XT[:, i].std())
        knnModel = KNeighborsClassifier()
        knnModel.fit(X, Y)
        sd = knnModel.predict(XT)
        print(YT)
        acc = (sum(sd == YT) / len(YT) * 100)
        print("Accuracy of KNN Model: %.2f" % acc+' %')
        print('=' * 100)
        if self.accLabel: self.accLabel.set("Accuracy of KNN Model: %.2f" % (acc)+' %')
