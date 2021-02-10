import numpy as np 
import matplotlib.pyplot as plt 

def eucledian_distance(*args):
    arr=[c for c in args]
    dim=len(arr[0])
    dist=0
    for i in range(dim):
        dist+=(arr[0][i]-arr[1][i])**2
    return dist**0.5
def knn(dict,cluster_high,cluster_low,k_num,predict):
    dist=[]
    dict.setdefault('predict',predict)
    predict=dict['predict']
    dict.setdefault('k',k_num)
    k=dict['k']
    dict.popitem()
    predict=dict['predict']
    dict.popitem()
    array=[]
    clusters=len(dict)
    for i in dict:
        for j in dict[i]:
            array.append([eucledian_distance(j,predict),int(i)])
    array.sort(key=lambda array:array[0])
    count,s,max_index=0,0,k
    res,max=0,0
    new_dict={}
    for i in range(cluster_low,cluster_high+1):
        new_dict.setdefault(i,[])
    for i in range(k):
        new_dict[array[i][1]].append(array[i][0])
    for i in new_dict:
        if len(new_dict[i])>max:
            max=len(new_dict[i])
            res=i
    return res,array
def get_accuracy(Y_test,cluster_high,cluster_low,dict,k_num):
    count=0
    for i in Y_test:
        predict=knn(dict,cluster_high,cluster_low,k_num,i[:-1])[0]
        if predict==i[-1]:
            count+=1
    return count/len(Y_test),count

def print_predictions(Y_test,cluster_high,cluster_low,dict,k_num):
    count=0
    for i in Y_test:
        predict=knn(dict,cluster_high,cluster_low,k_num,i[:-1])[0]
        print("-----------------")
        print("Original" ,i[-1])
        print("Predicted: ",predict)
    print("###########")
    print("Accuracy: ",get_accuracy(Y_test,cluster_high,cluster_low,dict,k_num)[0])