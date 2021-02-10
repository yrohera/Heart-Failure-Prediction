import pandas as pd 
import numpy as np 
from collections import Counter
import math
from split_data import split_data

def get_coefficients(data):
    dict={}
    k=0
    Count=Counter(data[data.columns[-1]])
    for i in data[data.columns[-1]]:
        dict.setdefault(i,[])
    for i in dict:
        for k in range(data.shape[1]-1):
            const=data[data.columns[k]][data[data.columns[-1]]==i]
            dict[i].append([const.mean(),const.std()])
        dict[i].append(Count[i]/data.shape[0])
    return dict

def eval(*args):
    input=[c for c in args]
    a=np.e**(-((input[0]-input[1][0])/input[1][1])**2*0.5)
    b=1/(input[1][1]*(2*np.pi)**0.5)
    return a*b

def get_prediction(data,predict):
    dict=get_coefficients(data)
    max=-np.inf
    for i in dict:
        sum=math.log(dict[i][-1])
        for count,j in enumerate(dict[i][:-1]):
            sum+=math.log(eval(float(predict[count]),j))
        if sum>=max:
            max=sum
            res=i
    return res

def get_accuracy(data,X_test):
    count=0
    for i in X_test:
        if get_prediction(data,i[:-1])==i[-1]:
            count+=1
    return count/len(X_test)

def print_predictions(data,X_test):
    for i in X_test:
        prediction=get_prediction(data,i[:-1])
        print("-----------")
        print("Original: ",i[-1])
        print("Prediction: ",prediction)
    print("############")
    print("Accuracy :",get_accuracy(data,X_test))
