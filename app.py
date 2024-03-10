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

@app.route('/predict', methods=['POST'])
def predict():
    data=[float(x) for x in request.form.values()] #for para pegar(request) valores de um form html. 
    final_input=scalar.transform(np.array(data).reshape(1,-1)) #passa o scaler nos dados e transforma em np.array(eh como o modelo aceita dados)
    print(final_input)
    output=regmodel.predict(final_input)[0] #vai retornar soh uma linha (pq soh estou enviando uma linha) e preciso q apareça na tela
    return render_template("home.html", prediction_text="O valor estimado foi $ {:.2f}".format(output))
                                        #prediction_text é um placeholder

if __name__=="__main__": #isso faz o app rodar
    app.run(debug=True)
