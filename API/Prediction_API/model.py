from sklearn import svm
import numpy as np
import pandas as pd
import json
from GetData import getArray


#Constants:
test_cases=0.75

data=getArray()
data_array=data.astype(float).values.tolist()

clf=svm.SVC(C=100,gamma=0.001)

xtrain=data_array[:-int((1-test_cases)*len(data_array))]
xtest=data_array[-int((1-test_cases)*len(data_array)):]

train=[i[:-1] for i in xtrain]
predtrain=[i[-1] for i in xtrain]

clf.fit(train,predtrain)

print(len(xtrain),len(xtest))

# for i in data_array

test=[i[:-1] for i in xtest]
predtest=[i[-1] for i in xtest]

accuracy=0

def get_prediction(input):
    return clf.predict([input])[0]


