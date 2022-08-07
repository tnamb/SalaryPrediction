import pickle
lr = pickle.load(open("LR_2022_01.pkl", "rb"))

import numpy as np
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/prediction", methods = ['POST'])
def predict():
    pred_sal = lr.predict([[int(x) for x in request.form.values()]])
    return render_template("index.html", prediction_text = "Your salary is" + str(pred_sal[0]))

app.run(debug = True, use_reloader = False)