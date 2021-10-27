from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import pickle

app = Flask(__name__)  # initializing a flask app


@app.route('/', methods=['GET'])  # route to display homepage
@cross_origin()
def homepage():
    return render_template('index.html')


@app.route('/predict', methods=['POST', 'GET'])  # to show predictions in web ui
@cross_origin()
def index():
    if request.method == "POST":
        try:
            # reading the inputs given by the user
            pregnancies = float(request.form['pregnancies'])
            glucose = float(request.form['glucose'])
            bloodpressure = float(request.form['bloodpressure'])
            skinthickness = float(request.form['skinthickness'])
            insulin = float(request.form['insulin'])
            bmi = float(request.form['bmi'])
            diabetespedigreefunction = float(request.form['diabetespedigreefunction'])
            age = float(request.form['age'])

            filename = "diabetes.pickle"
            loaded_model = pickle.load(open(filename, 'rb'))
            prediction = loaded_model.predict(
                [[pregnancies, glucose, bloodpressure, skinthickness, insulin, bmi, diabetespedigreefunction, age]])
            print('prediction is ', prediction)
            if prediction == 1:
                pre = "Yes"
            else:
                pre = "No"

            return render_template('results.html', prediction=pre)
        except Exception as e:
            print('The Exception Message is ', e)
            return "Something is Wrong !!!"
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)

