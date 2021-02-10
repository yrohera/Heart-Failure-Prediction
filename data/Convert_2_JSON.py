import json
import pandas as pd 
import os

def get_json_array(data):
    array=[]
    temp={}
    for i in range(data.shape[0]):
        for j in data.columns:
            temp.setdefault(str(j),str(data[j][i]))
        array.append(temp)
        temp={}

    return array

def store_as_json(data,name,command):
    temp=get_json_array(data)
    filePath="./JSON/"+name+".json"
    json_string=json.dumps(temp)
    f=open(filePath,command)
    f.write(json_string)
    print("Data Constructed Successfully!!!")

dws=pd.read_csv('DataSet/heart.csv')
ds=pd.read_csv('DataSet/heart_failure_clinical_records_dataset.csv')

# Converting Data to the array of JSON
store_as_json(dws,"dws","w")
store_as_json(ds,"ds","w")