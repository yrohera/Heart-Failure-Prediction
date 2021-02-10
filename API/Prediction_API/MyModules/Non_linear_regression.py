from Linear_regression import multi_regression,get_prediction
import numpy as np 
import math

def get_output(X,Y,predict,threshold=0.5):  #Sigmod function....
    Y_pred=get_prediction(X,Y,predict)
    deno=1+math.exp(-1*Y_pred[0])
    res=1/deno
    if res>=threshold:
        return 1,res
    else:
        return 0,res
def get_accuracy(X,Y,X_test,thresh=0.5):
    count=0
    for i in X_test:
        if int(i[-1])==get_output(X,Y,i[:-1],thresh)[0]:
            count+=1
    return count/len(X_test)


