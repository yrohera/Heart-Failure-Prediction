#For 2 Dimensional Only...
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

def get_coefficients(x,y,degree=2):
    Y=[[i] for i in y]
    X=[[x[j]**(i) for i in range(degree+1)] for j in range(np.size(x))]
    X_transpose=np.transpose(X)
    A=np.dot(X_transpose,X)
    A=np.linalg.inv(A)
    A=np.dot(A,X_transpose)
    A=np.dot(A,Y)
    return A
def get_prediction(x,y,predict,degree=2):
    A=get_coefficients(x,y,degree)
    predict=[[predict**(i) for i in range(degree+1)]]
    return np.dot(predict,A)
def get_coeff_of_determination(y_calc,y):
    y_mean=np.mean(y)
    SE=np.sum((y_calc-y)**2)
    SE_mean=np.sum((y-[np.mean(y) for i in range(np.size(y))])**2)
    return 1-SE/SE_mean


