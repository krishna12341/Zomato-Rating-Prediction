import numpy as np
from flask import Flask, request, render_template
import pickle
app = Flask(__name__,template_folder='Template',static_folder='static')
ext_model=pickle.load(open('zomato.pkl','rb'))
@app.route('/')
def home():
   return render_template('index.html')
# Prediction function
def valuepredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1,8)
    loaded_model= pickle.load(open('zomato.pkl','rb'))
    result1=loaded_model.predict(to_predict)
    return result1[0]
# output page and Logic
@app.route('/result',methods=['POST'])
def result():
    if request.method== 'POST':
     to_predict_list= request.form.to_dict()
     to_predict_list=list(to_predict_list.values())
     to_predict_list=list(map(int,to_predict_list))
     result1 = valuepredictor(to_predict_list)
     return render_template("result.html", prediction=result1)
     return render_template("result.html")








print(__name__)
if __name__ == "__main__":
    app.run(debug=True,port=8002)
    app.config['TEMPLATE_AUTO_RELOAD']=True
