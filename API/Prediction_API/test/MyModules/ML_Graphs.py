import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np
from KNN import knn,get_accuracy,print_predictions
from split_data import split_data,get_dict
from matplotlib import style

style.use('ggplot')

def get_heatmap(data,size):
    data_corr=data.corr()
    corr_values=data_corr.values
    fig=plt.figure(figsize=(size[0],size[1]))
    ax=fig.add_subplot(111)
    heatmap=plt.pcolor(corr_values,cmap=plt.cm.RdYlGn)
    ax.set_xticks(np.arange(data_corr.shape[0])+0.5)
    ax.set_yticks(np.arange(data_corr.shape[1])+0.5)
    ax.set_xticklabels(data_corr.columns)
    ax.set_yticklabels(data_corr.index)
    ax.invert_yaxis()
    ax.xaxis.tick_top()
    plt.xticks(rotation=90)
    fig.colorbar(heatmap)
    heatmap.set_clim(-1,1)
    plt.show()
    return data_corr,corr_values

def columns_graph(data):
    for i in data.columns[:-1]:
        plt.scatter(data[i],data[data.columns[-1]])
        plt.title(i+" Vs "+data.columns[-1])
        plt.show()
    
def get_accuracy_graph_knn(X_test,high,low,main_dict,in_thresh=3,fi_thresh=99):
    max_acc=-np.inf
    x=[]
    y=[]
    for i in range(in_thresh,fi_thresh+1,2):
        acc=get_accuracy(X_test,high,low,main_dict,i)
        x.append(i)
        y.append(acc[0])
        max_acc_1=max_acc
        max_acc=max(max_acc,acc[0])
        if max_acc!=max_acc_1:
            k=i
    plt.plot(x,y)
    plt.xlabel('K')
    plt.ylabel("Accuracy")
    plt.show()
    print("Max Accuracy at: ",k)
    return k