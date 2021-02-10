
from flask import Flask,render_template,request,jsonify
from flask_cors import CORS
import json
from model import get_prediction
from GetData import dataUpdate,getData

app=Flask(__name__)
CORS(app)

@app.route('/predict',methods=['GET','POST'])
def predict():
    file=open('API/Prediction_API/sample.json')
    json_data=json.loads(file.read())
    for i in json_data:
        json_data[i]=request.args.get(i)
    array=[]
    for i in json_data:
        array.append(float(json_data[i]))
    predict=get_prediction(array)
    prediction={"prediction":predict}
    json_data.setdefault('target',str(int(predict)))
    getData(json_data,{})
    return jsonify(prediction)

if __name__=="__main__":
    app.run(debug=True)


