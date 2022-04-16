
from flask import Flask, render_template,request
import pickle
import numpy as np
#from sklearn.ensemble.forest import RandomForestClassifier

app= Flask(__name__)


svc_model = pickle.load(open('svc_trained_model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('Home.html')


@app.route('/predict', methods=['POST'])
def predict():
   
   
   inputs = []
   inputs.append(request.form['age'])
   inputs.append(request.form['trestbps'])    
   inputs.append(request.form['chol'])
   inputs.append(request.form['fbs'])
   
   age = request.form['age']
   trestbps = request.form['trestbps'] 
   chol = request.form['chol']
   fbs = request.form['fbs']
   

   
   
   final_inputs = [np.array(inputs)]
   prediction = svc_model.predict(final_inputs)
    #unseen_feature_vectors = request.form.values()
   
   if prediction[0] == 1:
        categorical_array = "Heart Disease Diagnosed"
   if prediction[0] == 0:
        categorical_array = "No Heart Disease Diagnosed"
    
   result= categorical_array
       
   return render_template('Home.html', prediction_text1=result, age1 = age, trestbps1=trestbps, chol1=chol, fbs1=fbs)



if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)