import pickle
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd

app = Flask(__name__)
## carrega o modelo
regmodel=pickle.load(open('regmodel.pkl','rb'))

# route note (root)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data=request.json['data'] #data é soh o nome dos dados que serão enviados, nao tem relação com as variaveis do modelo
    print(data)
