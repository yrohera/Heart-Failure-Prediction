import requests
import json
import pandas as pd

#Getting the API key

#Url:

#Param1 and Param2 should be dictionary
def getData(param1,param2):
    api_key=open('API/api.json')
    json_res=json.loads(api_key.read())
    apiKey=json_res['API']
    url1="http://localhost:3000/dws_data/"+apiKey
    url2="http://localhost:3000/ds_data/"+apiKey
    if len(param1)>=1:
        url1+="?"
        for count,i in enumerate(param1):
            url1+=i+"="+param1[i]
            if count!=len(param1)-1:
                url1+="&" 
    if len(param2)>=1:
        url2+="?"
        for count,i in enumerate(param2):
            url2+=i+"="+param2[i]
            if count!=13:
                url2+="," 
    dws=requests.get(url1)
    # ds=requests.get(url2)
    dwsData=dws.json()
    # dsData=ds.json()

format={
  "age":[],
  "sex":[],
  "cp":[],
  "trestbps":[],
  "chol":[],
  "fbs":[],
  "restecg":[],
  "thalach":[],
  "exang":[],
  "oldpeak":[],
  "slope":[],
  "ca":[],
  "thal":[],
  "target":[]
}

data_dws=open('data/JSON/dws.json')


def getArray():
    for i in json.loads(data_dws.read()):
        for j in i:
            format[str(j)].append(i[str(j)])
    data=pd.DataFrame(format)
    return data

api_key=open('API/api.json')
json_res=json.loads(api_key.read())
apiKey=json_res['API']

def dataUpdate(data):
    api_key=open('API/api.json')
    json_res=json.loads(api_key.read())
    apiKey=json_res['API']
    for i in json.loads(data_dws.read()):
        if i[:-1]==data:
            print("The Data is already present")
            return 
    getData(data,{})    
    print("The database has been updated successfully!!!")

getData({},{})
