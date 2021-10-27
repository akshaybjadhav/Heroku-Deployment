from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import pickle

app = Flask(__name__) # initializing a flask app

@app.route('/',methods=['GET']) #route to display homepage
@cross_origin()
def homepage():
    return render_template('index.html')

@app.route('/predict',methods=['POST','GET']) #to show predictions in web ui
@cross_origin()
def index():
    if request.method == "POST":
        try:
            #reading the inputs given by the user
            gre_score = float(request.form['gre_score'])
            toefl_score = float(request.form['toefl_score'])
            university_rating = float(request.form['university_rating'])
            sop = float(request.form['sop'])
            lor = float(request.form['lor'])
            cgpa = float(request.form['cgpa'])
            is_research = request.form['research']
            if(is_research == 'yes'):
                research = 1
            else:
                research = 0
            filename = "admission_prediction_zcoer.pickle"
            loaded_model = pickle.load(open(filename,'rb'))
            prediction = loaded_model.predict([[gre_score,toefl_score,university_rating,sop,lor,cgpa,research]])
            print('prediction is ',prediction)

            return render_template('results.html',prediction = round(10*prediction[0]))
        except Exception as e:
            print('The Exception Message is ',e)
            return "Something is Wrong !!!"
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
    
