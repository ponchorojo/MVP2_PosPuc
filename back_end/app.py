from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np
import os

app = Flask(__name__)
CORS(app)

# Carrega o modelo treinado
modelo_path = os.path.join(os.path.dirname(__file__), 'modelo', 'modelo_treinado.pkl')
modelo = joblib.load(modelo_path)

@app.route("/prever", methods=["POST"])
def prever():
    dados = request.get_json()
    entrada = np.array([list(dados.values())])
    predicao = modelo.predict(entrada)
    return jsonify({"resultado": "Aprovado" if predicao[0] == 1 else "Recusado"})

if __name__ == "__main__":
    app.run(debug=True)
