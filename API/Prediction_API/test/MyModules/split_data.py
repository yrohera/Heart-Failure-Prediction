import numpy as np 
import pandas as pd 
import os 
from collections import Counter 


def split_data(data,train_pct=0.8):
    values=data.values.astype(float).tolist()
    X_train=values[:-int((1-train_pct)*len(values))]
    Y_train=values[-int((1-train_pct)*len(values)):-1]
    return X_train,Y_train,data[data.columns[-1]].max(),data[data.columns[-1]].min()

def get_dict(X_train,clusters_high,cluster_low):
    dict_train={}
    for i in range(cluster_low,clusters_high+1):
        dict_train.setdefault(i,[])
    for i in X_train:
        dict_train[i[-1]].append(i[:-1])
    return dict_train

def convert_to_number(data,cols):
    dict={}
    for i in cols:
        for j in data[i]:
            try:
                dict[j]+=1
            except:
                dict.setdefault(j,1)
    return dict

def get_proper_dict(data):
    data_pts=data.astype(float).values.tolist()
    dict={}
    for i in data[data.columns[-1]]:
        dict.setdefault(i,[])
    for i in data_pts:
        dict[i[-1]].append(i[:-1])
    return dict

def convert_2_numbers(data):
    for i in data.columns:
        if data[i].dtypes!='int64' and data[i].dtypes!='float64':
            dict=Counter(data[i])
            for count,j in enumerate(dict):
                data[i].replace(j,count,inplace=True)

def div_data(data,percentage=80):
    return data.head(int(data.shape[0]*(percentage/100)))

def Get_X_Y(data):
    X=[[data[i][j] for i in data.columns[:-1]] for j in range(data.shape[0])]
    Y=[[i] for i in data[data.columns[-1]]]
    return X,Y




