#Will also cover Multiple regression
import numpy as np 

def get_coefficients(x,y):  #Can also be solved using Multi regression....
    x_mean=np.mean(x)
    y_mean=np.mean(y)
    N=np.size(x)
    a=np.sum(x*y)-N*x_mean*y_mean
    b=np.sum(x*x)-N*x_mean*x_mean
    slope=a/b
    inter=y_mean-slope*x_mean
    return slope,inter
def predict(x,y):
    slope,inter=get_coefficients(x,y)
    y=slope*x+inter
    return list(y)
def coeff_of_determination(y_cal,y):  #Also known as R^2
    y_mean=np.mean(y)
    SE=np.sum((y-y_cal)**2)
    SE_mean=np.sum((y-y_mean)**2)
    return 1-SE/SE_mean

def multi_regression(X,Y):
    X_trans=np.transpose(X)
    A=np.dot(X_trans,X)
    A=np.linalg.inv(A)
    A=np.dot(A,X_trans)
    A=np.dot(A,Y)
    return A
def get_prediction(X,Y,predict):
    A=multi_regression(X,Y)
    return np.dot(predict,A)
def coeff_of_determination_mr(Y_cal,y_act):
    SE=np.sum((Y_cal-y_act)**2)
    SE_mean=np.sum((y_act-np.mean(y_act))**2)
    return 1-SE/SE_mean



