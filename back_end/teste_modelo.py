import os
import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def test_model_metrics():
    # Caminhos seguros relativos ao próprio arquivo teste_modelo.py
    base_dir = os.path.dirname(__file__)
    modelo_path = os.path.join(base_dir, "modelo", "modelo_treinado.pkl")
    dados_path = os.path.join(base_dir, "modelo", "dados_teste.csv")

    # Carregar modelo e dados de teste
    modelo = joblib.load(modelo_path)
    dados = pd.read_csv(dados_path)

    X = dados.drop("Loan_Status", axis=1)
    y = dados["Loan_Status"]
    y_pred = modelo.predict(X)

    acc = accuracy_score(y, y_pred)
    precision = precision_score(y, y_pred)
    recall = recall_score(y, y_pred)
    f1 = f1_score(y, y_pred)

    print(f"Acurácia: {acc:.2f}")
    print(f"Precisão: {precision:.2f}")
    print(f"Recall: {recall:.2f}")
    print(f"F1-score: {f1:.2f}")

    assert acc >= 0.70, "Acurácia abaixo do mínimo"
    assert precision >= 0.70, "Precisão abaixo do mínimo"
    assert recall >= 0.70, "Recall abaixo do mínimo"
    assert f1 >= 0.70, "F1-score abaixo do mínimo"