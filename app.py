import pickle
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd

app = Flask(__name__)
## carrega o modelo
regmodel=pickle.load(open('regmodel.pkl','rb'))
scalar=pickle.load(open('scaler.pkl', 'rb'))

# route note (root)
@app.route('/')
def home():
    return render_template('home.html') #essa linha olha para a pasta template

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data=request.json['data'] #data é soh o nome dos dados que serão enviados, nao tem relação com as variaveis do modelo
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))
    new_data=scalar.transform(np.array(list(data.values())).reshape(1,-1))
    output=regmodel.predict(new_data)
    print(output[0])
    return jsonify(output[0])

if __name__=="__main__": #isso faz o app rodar
    app.run(debug=True)
